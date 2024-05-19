package com.basics.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.basics.model.Blog;

class Sentence {
	private String sentence;

	public Sentence(String sentence) {
		super();
		this.sentence = sentence;
	}

	public Sentence() {
//		super();
	}

	public String getSentence() {
		return sentence;
	}

	public void setSentence(String sentence) {
		this.sentence = sentence;
	} 
}

class User_id{
	private int user_id;
	
	public User_id(int user_id) {
		super();
		this.user_id = user_id;
	}
	
	public User_id() {
		
	}
	
	public int getuser_id() {
		return user_id;
	}
	
	public void setUser_id(int user_id) {
		this.user_id = user_id;
	}
}

@Service
public class FlaskService {

    @Autowired
    RestTemplate restTemplate;

    public List<Blog> callFlaskEndpoint(String sentence) {
    	Sentence ss = new Sentence(sentence);
        String flaskUrl = "http://localhost:5000/similar-blogs";
        HttpEntity<Sentence> requestEntity = new HttpEntity<>(ss);

        // Define the type reference for List<Blog>
        ParameterizedTypeReference<List<Blog>> responseType = new ParameterizedTypeReference<List<Blog>>() {};

        // Send a POST request to the Flask URL and deserialize the JSON response into a List<Blog>
        ResponseEntity<List<Blog>> responseEntity = restTemplate.exchange(
        		flaskUrl, 
        		HttpMethod.POST, 
        		requestEntity, 
        		responseType
        );

        // Extract the list of blogs from the response entity
        List<Blog> blogs = responseEntity.getBody();
        System.out.println(blogs.size());
        return blogs;
    }
    
    public List<Blog> first10Recommend(int uid){
    	User_id user_id  = new User_id(uid);
        String flaskUrl = "http://localhost:5000/recommend-blogs";
        HttpEntity<User_id> requestEntity = new HttpEntity<>(user_id);
        
        System.out.println(user_id);

     // Define the type reference for List<Blog>
        ParameterizedTypeReference<List<Blog>> responseType = new ParameterizedTypeReference<List<Blog>>() {};

        // Send a POST request to the Flask URL and deserialize the JSON response into a List<Blog>
        ResponseEntity<List<Blog>> responseEntity = restTemplate.exchange(
        		flaskUrl, 
        		HttpMethod.POST, 
        		requestEntity, 
        		responseType
        );
        
        List<Blog> blogs = responseEntity.getBody();
        System.out.println(blogs.size());
        return blogs;
    }
}
