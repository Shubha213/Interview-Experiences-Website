#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
from bs4 import BeautifulSoup


# In[2]:


nltk.download('punkt')
nltk.download('stopwords')


# In[3]:


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shubham@123",
    database="finalyear"
)


# In[4]:


sql_query = """
    SELECT * FROM blog;
"""


# In[5]:


df = pd.read_sql(sql_query, connection)


# In[13]:


df


# In[12]:


def clean_tags(tags):
    if isinstance(tags, str):  # Check if the value is a string
        # Split tags by '#', remove '#' from each tag, and strip leading/trailing whitespace
        cleaned_tags = [tag.strip('#').strip() for tag in tags.split()]
        return ', '.join(cleaned_tags)
    else:
        return ""

# Apply the function to create the new column
df['cleaned_tags'] = df['tags'].apply(clean_tags)


# In[7]:


# Assuming 'df' is your DataFrame and 'column_name' is the name of the column you want to access
blog_text= df['blog_text'];

# Creating an empty dictionary to store the mapping
blog_map = {}

# Iterating over the DataFrame rows
for index, row in df.iterrows():
    # Extracting values from the 'blog_id' and 'blog_text' columns
    blog_id = row['blog_id']
    soup = BeautifulSoup(row['blog_text'], 'html.parser')
    plain_text = soup.get_text()
    blog_text = plain_text
    
    # Adding the mapping to the dictionary
    blog_map[blog_id] = blog_text
    
    
# Creating an empty dictionary to store the mapping
title_map = {}

# Iterating over the DataFrame rows
for index, row in df.iterrows():
    # Extracting values from the 'blog_id' and 'blog_text' columns
    blog_id = row['blog_id']
    blog_title = row['blog_title']
    
    # Adding the mapping to the dictionary
    title_map[blog_id] = blog_title
    
    
# Creating an empty dictionary to store the mapping
tags_map = {}

# Iterating over the DataFrame rows
for index, row in df.iterrows():
    # Extracting values from the 'blog_id' and 'blog_text' columns
    blog_id = row['blog_id']
    tags = row['cleaned_tags']
    
    # Adding the mapping to the dictionary
    tags_map[blog_id] = tags
    


# In[ ]:





# In[8]:


# Function to preprocess text: remove stopwords and perform stemming
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    tokens = nltk.word_tokenize(text.lower())
    tokens = [stemmer.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)


# In[9]:


# Function to find blog IDs that have similar content to a given sentence after preprocessing
def find_similar_blog_ids(sentence, threshold=0):
    similar_blog_ids = []
    
    # Preprocess the query sentence
    processed_sentence = preprocess_text(sentence)
    
    # Combine titles, tags, and text into a single string for each blog ID and preprocess them
    combined_texts = {}
    for blog_id in title_map.keys():
        title = title_map[blog_id]
        tags = tags_map.get(blog_id, '')
        blog_text = blog_map.get(blog_id, '') 
        combined_texts[blog_id] = preprocess_text(f"{title} {tags} {blog_text}")
    
    # Compute TF-IDF vectors for the combined texts
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(combined_texts.values())
    
    # Compute TF-IDF vector for the query sentence
    query_vector = tfidf_vectorizer.transform([processed_sentence])

    # Compute cosine similarity between the query and each document
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    # Find blog IDs with similarity above the threshold
    for score, blog_id in zip(cosine_similarities, combined_texts.keys()):
        if score > threshold:
            similar_blog_ids.append(blog_id)
    
    return similar_blog_ids


# In[15]:


def find_similar_blogs(sentence, threshold=0):
    similar_blog_ids = find_similar_blog_ids(sentence, threshold)
    similar_blogs = []
    # df.drop(['cleaned_tags'],axis='columns',inplace=True) 
    for blog_id in similar_blog_ids:
        blog = df[df['blog_id'] == blog_id].iloc[0]  # Assuming 'blog_id' is the column name for blog IDs
        if not blog.empty:
            similar_blogs.append(blog)
    
    return similar_blogs


# In[ ]:




