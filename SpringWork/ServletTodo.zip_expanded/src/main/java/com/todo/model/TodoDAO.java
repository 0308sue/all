package com.todo.model;

import java.util.ArrayList;

public interface TodoDAO {
	//�߰�
	public void insert(Todo todo);
	//��ü����
	public ArrayList<Todo> list();
	

}
