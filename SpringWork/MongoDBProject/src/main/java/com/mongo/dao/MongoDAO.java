package com.mongo.dao;

import java.util.ArrayList;

import org.bson.Document;

import com.mongodb.BasicDBObject;
import com.mongodb.MongoClient;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;

public class MongoDAO {
	private static MongoDAO dao = new MongoDAO();
	
	public static MongoDAO getInstance() {
		return dao;
	}

	public void insert(Employee emp) {
		MongoClient mongoClient = new MongoClient("localhost", 27017);
		MongoDatabase db = mongoClient.getDatabase("testDB");	 
	    MongoCollection<Document> collections = db.getCollection("employees");
	    Document doc = new Document("empno",emp.getEmpno())
	    		.append("ename", emp.getEname())
	    		.append("job", emp.getJob())
	    		.append("hiredate", emp.getHiredate())
	    		.append("deptno", emp.getDeptno());
	    collections.insertOne(doc);
	    mongoClient.close();
	}
	
	public ArrayList<Employee> list(){
		MongoClient mongoClient = new MongoClient("localhost", 27017);
		MongoDatabase db = mongoClient.getDatabase("testDB");	  
	    MongoCollection<Document> collections = db.getCollection("employees");
	    FindIterable<Document>iterable = collections.find();
		MongoCursor<Document> cursor=iterable.iterator();
		ArrayList<Employee> lists =  new ArrayList<>();
		while(cursor.hasNext()) {
			Document doc = cursor.next();
			Employee emp = new Employee();
			emp.setEmpno(doc.getDouble("empno"));
			emp.setEname(doc.getString("ename"));
			emp.setDeptno(doc.getDouble("deptno"));
			emp.setJob(doc.getString("job"));
			emp.setHiredate(doc.getDate("hireDate"));
			lists.add(emp);
		}
		return lists;
	}
	
	public void delete(Double empno) {
		MongoClient mongoClient = new MongoClient("localhost", 27017);
		MongoDatabase db = mongoClient.getDatabase("testDB");	  
	    MongoCollection<Document> collections = db.getCollection("employees");
	    BasicDBObject inQuery = new BasicDBObject();
	    inQuery.put("empno", empno);
	    collections.deleteOne(inQuery);
	    mongoClient.close();
	}
	
	public void update(Employee emp) {
		MongoClient mongoClient = new MongoClient("localhost", 27017);
		MongoDatabase db = mongoClient.getDatabase("testDB");	 
	    MongoCollection<Document> collections = db.getCollection("employees");
	    BasicDBObject inQuery = new BasicDBObject();
	    inQuery.put("empno", emp.getEmpno());
	    
	    BasicDBObject obj = new BasicDBObject()
	    		.append("ename", emp.getEname())
	    		.append("job", emp.getJob())
	    		.append("deptno", emp.getDeptno());
	    
	    BasicDBObject newDoc = new BasicDBObject()
	    		.append("$set",obj);
	    
	    collections.updateOne(inQuery,newDoc);
	    mongoClient.close();
	}
	public Employee findOne(Double empno) {
		MongoClient mongoClient = new MongoClient("localhost", 27017);
		MongoDatabase db = mongoClient.getDatabase("testDB");	  
	    MongoCollection<Document> collections = db.getCollection("employees");
	    BasicDBObject inQuery = new BasicDBObject();
	    inQuery.put("empno", empno);
	    FindIterable<Document>iterable = collections.find(inQuery);
		MongoCursor<Document> cursor=iterable.iterator();
		Employee emp = null;
		if(cursor.hasNext()) {
			Document doc = cursor.next();
			emp = new Employee();
			emp.setEmpno(doc.getDouble("empno"));
			emp.setEname(doc.getString("ename"));
			emp.setDeptno(doc.getDouble("deptno"));
			emp.setJob(doc.getString("job"));
			emp.setHiredate(doc.getDate("hireDate"));
		}
		mongoClient.close();
		return emp;
	}
}
