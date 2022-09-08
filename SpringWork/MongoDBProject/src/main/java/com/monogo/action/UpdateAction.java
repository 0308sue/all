package com.monogo.action;

import java.io.IOException;
import java.util.Date;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.mongo.dao.Employee;
import com.mongo.dao.MongoDAO;

/**
 * Servlet implementation class UpdateAction
 */
@WebServlet("/update")
public class UpdateAction extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public UpdateAction() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		Double empno = Double.parseDouble(request.getParameter("empno"));
		MongoDAO dao = MongoDAO.getInstance();
		Employee emp = dao.findOne(empno);
		request.setAttribute("emp", emp);
		request.getRequestDispatcher("update.jsp").forward(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		Employee emp = new Employee();
		emp.setEmpno(Double.parseDouble(request.getParameter("empno")));
		emp.setEname(request.getParameter("ename"));
		emp.setJob(request.getParameter("job"));
		emp.setDeptno(Double.parseDouble(request.getParameter("deptno")));
		emp.setHiredate(new Date());
		MongoDAO dao = MongoDAO.getInstance();
		dao.update(emp);
		response.sendRedirect("list");
	}

}
