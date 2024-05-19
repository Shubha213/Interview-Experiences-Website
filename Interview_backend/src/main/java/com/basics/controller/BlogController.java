package com.basics.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.basics.model.Blog;
import com.basics.service.BlogService;
import com.basics.service.FlaskService;

@CrossOrigin(origins = "http://localhost:4200")
@RestController
@RequestMapping("/Blogapi")
public class BlogController {
	
	@Autowired
	BlogService blogService;
	
	@Autowired
	FlaskService flaskService;
	
	@GetMapping("/getAllBlogs")
	public List<Blog> getAllBlogs(){
		return blogService.getALlBlogs();
	}
	
	@PostMapping("/addblog")
	public boolean add(@RequestBody Blog blog) {
		System.out.println("poiuy");
		blogService.addBlog(blog);
		return true;
	}
	
	@GetMapping("getblogbyid/{blogid}")
	public Blog getBlogById(@PathVariable Long blogid) {
		return blogService.getBlogById(blogid);
	}
	
	@GetMapping("getblog/{userid}")
	public List<Blog> getUserBlogs(@PathVariable int userid){
		return blogService.getUserBlogs(userid);
	}
	
	@GetMapping("getblogbytag/{tags}")
	public List<Blog> getBlogsByTags(@PathVariable String tags){
		System.out.println(tags);
		return blogService.getBlogsByTags(tags);
	}
	
	@GetMapping("like/{blogId}")
	public void incLike(@PathVariable Long blogId) {
		blogService.incLike(blogId);
	}

	@GetMapping("dislike/{blogId}")
	public void disLike(@PathVariable Long blogId) {
		blogService.disLike(blogId);
	}
	
	@GetMapping("/byid/{page}/{userid}")
    public List<Blog> getBlogsByPage(@PathVariable int page, @PathVariable int userid) {
//		int userid = 3;
		System.out.println(page + " " + userid);
		if(page-1 == 0 && userid !=0) {
			System.out.println("in recom " + userid);
			return flaskService.first10Recommend(userid);			
		}

		return blogService.getBlogsByPage(page-1);
	}
	
	@GetMapping("/views/{blog_id}")
	public boolean updateViews(@PathVariable long blog_id) {
		return blogService.upadteViews(blog_id);
	}
	
    @PostMapping("/search-similar-blogs/{sentence}")
    public List<Blog> searchSimilarBlogs(@PathVariable String sentence) {
    	System.out.println("Searching");
        return flaskService.callFlaskEndpoint(sentence);
    }
    
}
