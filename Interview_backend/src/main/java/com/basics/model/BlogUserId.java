package com.basics.model;

import jakarta.persistence.Column;
import jakarta.persistence.Embeddable;;

@Embeddable
public class BlogUserId {

    @Column(name = "blog_id")
    private int blogId;

    @Column(name = "user_id")
    private int userId;

	public int getBlogId() {
		return blogId;
	}

	public void setBlogId(int blogId) {
		this.blogId = blogId;
	}

	public int getUserId() {
		return userId;
	}

	public void setUserId(int userId) {
		this.userId = userId;
	}

	public BlogUserId(int blogId, int userId) {
		super();
		this.blogId = blogId;
		this.userId = userId;
	}

	public BlogUserId() {
		
	}
}
