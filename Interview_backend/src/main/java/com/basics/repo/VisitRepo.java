package com.basics.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.basics.model.BlogUserId;
import com.basics.model.Visiting;

@Repository
public interface VisitRepo extends JpaRepository<Visiting, BlogUserId>{

}
