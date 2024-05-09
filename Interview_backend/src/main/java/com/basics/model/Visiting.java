package com.basics.model;

import jakarta.persistence.EmbeddedId;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name = "visiting")
public class Visiting {
	

	@EmbeddedId
	private BlogUserId id;
	
	private float rating;

	public Visiting(BlogUserId id, float rating) {
		super();
		this.id = id;
		this.rating = rating;
	}

	public BlogUserId getId() {
		return id;
	}

	public void setId(BlogUserId id) {
		this.id = id;
	}

	public float getRating() {
		return rating;
	}

	public void setRating(float rating) {
		this.rating = rating;
	}

	public Visiting() {
	}
	
}
