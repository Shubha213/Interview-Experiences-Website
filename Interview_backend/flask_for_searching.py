from flask import Flask, request, jsonify
from search_blog import find_similar_blogs
from blog_recommend import give_recomm_ids

app = Flask(__name__)

@app.route('/similar-blogs', methods=['POST'])
def similar_blogs():
    data = request.json  # Assuming JSON data is sent from the client
    search_sentence = data['sentence']
    similar_blogs = find_similar_blogs(search_sentence)
    json_response = []
    for blog in similar_blogs:
        blog_dict = blog.to_dict()  # Convert Pandas Series to dictionary
        json_response.append(blog_dict)
    
    return jsonify(json_response)

@app.route('/recommend-blogs', methods=['POST'])
def recommend_blogs():
    data = request.json  # Assuming JSON data is sent from the client
    # print("printing " + data)
    # return data
    userId = data['user_id']
    similar_blogs = give_recomm_ids(userId)
    json_response = []
    for blog in similar_blogs:
        blog_dict = blog.to_dict()  # Convert Pandas Series to dictionary
        json_response.append(blog_dict)
    
    return jsonify(json_response)
    # return {}

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




