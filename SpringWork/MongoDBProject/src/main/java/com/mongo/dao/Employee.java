package com.mongo.dao;

import java.util.Date;

public class Employee {
	private Double empno;
	private String ename;
	private String job;
	private Date hiredate;
	private Double deptno;
	public Double getDeptno() {
		return deptno;
	}
	public void setDeptno(Double deptno) {
		this.deptno = deptno;
	}
	public Double getEmpno() {
		return empno;
	}
	public void setEmpno(Double empno) {
		this.empno = empno;
	}
	public String getEname() {
		return ename;
	}
	public void setEname(String ename) {
		this.ename = ename;
	}
	public String getJob() {
		return job;
	}
	public void setJob(String job) {
		this.job = job;
	}
	public Date getHiredate() {
		return hiredate;
	}
	public void setHiredate(Date hiredate) {
		this.hiredate = hiredate;
	}
	
	

}
