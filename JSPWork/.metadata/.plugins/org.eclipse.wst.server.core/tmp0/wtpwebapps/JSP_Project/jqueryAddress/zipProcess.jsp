<%@page import="org.json.simple.JSONObject"%>
<%@page import="com.jqueryAddress.ZipcodeVO"%>
<%@page import="org.json.simple.JSONArray"%>
<%@page import="java.util.ArrayList"%>
<%@page import="com.jqueryAddress.JAddressDAOImpl"%>
<%@page import="com.jqueryAddress.JAddressDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8");%>

<% 
String dong = request.getParameter("dong");
//String dong = "부전동";
JAddressDAO dao = JAddressDAOImpl.getInstance();
ArrayList<ZipcodeVO> zarr = dao.getZipcode(dong);

JSONArray jsonarr = new JSONArray();
for(ZipcodeVO z:zarr){
	JSONObject obj = new JSONObject();
	obj.put("zipcode",z.getZipcode());
	obj.put("sido",z.getSido());
	obj.put("gugun",z.getGugun());
	obj.put("dong",z.getDong());
	obj.put("bunji",z.getBunji());
	jsonarr.add(obj);
}
out.println(jsonarr.toString());
%>