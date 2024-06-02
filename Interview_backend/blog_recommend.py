#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import nltk
import re
from nltk import corpus
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk import wsd
from nltk.corpus import wordnet as wn
import mysql.connector
from bs4 import BeautifulSoup

# nltk.download('omw-1.4')
# nltk.download('wordnet')
# nltk.download('wordnet2022')
# nltk.download('stopwords')


# In[4]:


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="itsa",
    database="finalyear"
)


# In[5]:


sql_query_1 = """
    SELECT * FROM blog;
"""


# In[6]:


blog_df = pd.read_sql(sql_query_1, connection)


# In[7]:


blog_df


# In[8]:


def clean_tags(tags):
    if isinstance(tags, str):  # Check if the value is a string
        # Split tags by '#', remove '#' from each tag, and strip leading/trailing whitespace
        cleaned_tags = [tag.strip('#').strip() for tag in tags.split()]
        return ', '.join(cleaned_tags)
    else:
        return ""

# Apply the function to create the new column
blog_df['cleaned_tags'] = blog_df['tags'].apply(clean_tags)


# In[9]:


sql_query_2 = """
    SELECT user_id, user_name FROM users;
"""


# In[10]:


author_df = pd.read_sql(sql_query_2, connection)


# In[12]:


sql_query_3 = """
    SELECT * FROM visiting;
"""


# In[13]:


ratings_df =pd.read_sql(sql_query_3, connection)


# In[14]:


ratings_df


# In[15]:


def html_to_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()


# In[16]:


blog_df['blog_new_text'] = blog_df['blog_text'].apply(html_to_text)


# In[17]:


lst_stopwords=corpus.stopwords.words('english')
def pre_process_text(text, flg_stemm=False, flg_lemm=True, lst_stopwords=None):
    text=str(text).lower()
    text=text.strip()
    text = re.sub(r'[^\w\s]', '', text)
    lst_text = text.split()
    if lst_stopwords is not None:
        lst_text=[word for word in lst_text if word not in lst_stopwords]
    if flg_lemm:
        lemmatizer = WordNetLemmatizer()
        lst_text = [lemmatizer.lemmatize(word) for word in lst_text]
    if flg_stemm:
        stemmer = PorterStemmer()
        lst_text = [stemmer.stem(word) for word in lst_text]
    text=" ".join(lst_text)
    return text


# In[18]:


def combine_columns(row):
    return row['blog_new_text'] + ' ' + row['cleaned_tags'] + ' ' + row['blog_title']

# Apply the function to create the new column
blog_df['combined_content'] = blog_df.apply(combine_columns, axis=1)


# In[19]:


blog_df['clean_blog_content'] = blog_df['combined_content'].apply(lambda x: pre_process_text(x,flg_stemm=False,flg_lemm=True,lst_stopwords=lst_stopwords))



# In[21]:


tfidf_vecotorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vecotorizer.fit_transform(blog_df['clean_blog_content'])
print(tfidf_matrix.shape)


# In[22]:


cosine_sim = cosine_similarity(tfidf_matrix)
print(cosine_sim)


# In[23]:


# Let us have the blogs rated by user with user id 12
user_rating = ratings_df[ratings_df['user_id']==3]

# consider blogs with ratings greater than or equal to 3.5 just for simplification
blogs_to_consider = user_rating[user_rating['rating']>=3]['blog_id']

# Now we need Id's of this blogs in form of a list
high_rated_blogs = blogs_to_consider.values


# In[25]:


rated_blogs = blog_df[blog_df['blog_id'].isin(high_rated_blogs)]


# In[28]:


def get_similar_blog(high_rated_blogs, top_n=10):
    """
    Args:
        high_rated_blogs: List of blog IDs of the blogs rated highly by the user.
        top_n: Number of top similar blogs to return (default is 10).
    Returns:
        recommended_blogs: List of blog IDs of the blogs that are to be recommended,
                           sorted by their similarity score in descending order.
    """
    recommended_blogs = []
    similarity_scores = []
    
    for blog_id in high_rated_blogs:
        # Find out the index value of the particular blog
        temp_id = blog_df[blog_df['blog_id'] == blog_id].index.values[0]
        
        # Get similarity scores for all blogs
        sim_scores = list(enumerate(cosine_sim[temp_id]))
        
        # Sort based on similarity scores in descending order
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        for idx, score in sim_scores:
            blog_id_at_idx = blog_df.iloc[idx]['blog_id']
            if blog_id_at_idx not in recommended_blogs and blog_id_at_idx not in high_rated_blogs:
                recommended_blogs.append(blog_id_at_idx)
                similarity_scores.append(score)
    
    # Combine the blog IDs and their similarity scores
    blog_similarity_pairs = list(zip(recommended_blogs, similarity_scores))
    
    # Sort by similarity score again to ensure global sorting
    blog_similarity_pairs = sorted(blog_similarity_pairs, key=lambda x: x[1], reverse=True)
    
    # Extract sorted blog IDs
    sorted_recommended_blogs = [blog_id for blog_id, score in blog_similarity_pairs[:top_n]]
    
    return sorted_recommended_blogs


# In[29]:
recommended_blogs=get_similar_blog(high_rated_blogs)

# In[35]:

def give_recomm_ids(user_id):
    # Let us have the blogs rated by user with user id 12
    user_rating = ratings_df[ratings_df['user_id']==user_id]

    # consider blogs with ratings greater than or equal to 3.5 just for simplification
    blogs_to_consider = user_rating[user_rating['rating']>=3]['blog_id']

    # Now we need Id's of this blogs in form of a list
    high_rated_blogs = blogs_to_consider.values

    similar_blog_ids =  get_similar_blog(high_rated_blogs) 

    if user_rating.empty:
        print("sfd")
        most_viewed_blogs = blog_df.nlargest(10, 'views')
        most_viewed_blog_ids = most_viewed_blogs['blog_id'].tolist()
        similar_blog_ids = most_viewed_blog_ids

    similar_blogs = []
    # df.drop(['cleaned_tags'],axis='columns',inplace=True) 
    for blog_id in similar_blog_ids:
        blog = blog_df[blog_df['blog_id'] == blog_id].iloc[0]  # Assuming 'blog_id' is the column name for blog IDs
        if not blog.empty:
            similar_blogs.append(blog)

    return similar_blogs