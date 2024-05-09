package com.basics.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.basics.model.User;
import com.basics.model.Visiting;
import com.basics.repo.UserRepo;
import com.basics.repo.VisitRepo;

@Service
public class UserService {

	@Autowired
	UserRepo userRepo;
	
	@Autowired
	VisitRepo visitRepo;
	
	public void addVisit(Visiting visit) {
		visitRepo.save(visit);
	}
	
	public void addUser(User user) {
		userRepo.save(user);
	}

	public User getUserByUserName(String userName) {
		return userRepo.findByUserName(userName);
		
	}

	public User getUserByUserId(Long userId) {
		return userRepo.findById(userId).get();
	}

}
