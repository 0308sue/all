/*
 * Generated by the Jasper component of Apache Tomcat
 * Version: Apache Tomcat/9.0.62
 * Generated at: 2022-04-15 03:23:56 UTC
 * Note: The last modified time of this file was set to
 *       the last modified time of the source file after
 *       generation to assist with modification tracking.
 */
package org.apache.jsp.board;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import com.board.dto.BoardDTO;
import com.board.dao.BoardDAO;

public final class boardView_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent,
                 org.apache.jasper.runtime.JspSourceImports {

  private static final javax.servlet.jsp.JspFactory _jspxFactory =
          javax.servlet.jsp.JspFactory.getDefaultFactory();

  private static java.util.Map<java.lang.String,java.lang.Long> _jspx_dependants;

  private static final java.util.Set<java.lang.String> _jspx_imports_packages;

  private static final java.util.Set<java.lang.String> _jspx_imports_classes;

  static {
    _jspx_imports_packages = new java.util.HashSet<>();
    _jspx_imports_packages.add("javax.servlet");
    _jspx_imports_packages.add("javax.servlet.http");
    _jspx_imports_packages.add("javax.servlet.jsp");
    _jspx_imports_classes = new java.util.HashSet<>();
    _jspx_imports_classes.add("com.board.dto.BoardDTO");
    _jspx_imports_classes.add("com.board.dao.BoardDAO");
  }

  private volatile javax.el.ExpressionFactory _el_expressionfactory;
  private volatile org.apache.tomcat.InstanceManager _jsp_instancemanager;

  public java.util.Map<java.lang.String,java.lang.Long> getDependants() {
    return _jspx_dependants;
  }

  public java.util.Set<java.lang.String> getPackageImports() {
    return _jspx_imports_packages;
  }

  public java.util.Set<java.lang.String> getClassImports() {
    return _jspx_imports_classes;
  }

  public javax.el.ExpressionFactory _jsp_getExpressionFactory() {
    if (_el_expressionfactory == null) {
      synchronized (this) {
        if (_el_expressionfactory == null) {
          _el_expressionfactory = _jspxFactory.getJspApplicationContext(getServletConfig().getServletContext()).getExpressionFactory();
        }
      }
    }
    return _el_expressionfactory;
  }

  public org.apache.tomcat.InstanceManager _jsp_getInstanceManager() {
    if (_jsp_instancemanager == null) {
      synchronized (this) {
        if (_jsp_instancemanager == null) {
          _jsp_instancemanager = org.apache.jasper.runtime.InstanceManagerFactory.getInstanceManager(getServletConfig());
        }
      }
    }
    return _jsp_instancemanager;
  }

  public void _jspInit() {
  }

  public void _jspDestroy() {
  }

  public void _jspService(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response)
      throws java.io.IOException, javax.servlet.ServletException {

    if (!javax.servlet.DispatcherType.ERROR.equals(request.getDispatcherType())) {
      final java.lang.String _jspx_method = request.getMethod();
      if ("OPTIONS".equals(_jspx_method)) {
        response.setHeader("Allow","GET, HEAD, POST, OPTIONS");
        return;
      }
      if (!"GET".equals(_jspx_method) && !"POST".equals(_jspx_method) && !"HEAD".equals(_jspx_method)) {
        response.setHeader("Allow","GET, HEAD, POST, OPTIONS");
        response.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED, "JSP들은 오직 GET, POST 또는 HEAD 메소드만을 허용합니다. Jasper는 OPTIONS 메소드 또한 허용합니다.");
        return;
      }
    }

    final javax.servlet.jsp.PageContext pageContext;
    javax.servlet.http.HttpSession session = null;
    final javax.servlet.ServletContext application;
    final javax.servlet.ServletConfig config;
    javax.servlet.jsp.JspWriter out = null;
    final java.lang.Object page = this;
    javax.servlet.jsp.JspWriter _jspx_out = null;
    javax.servlet.jsp.PageContext _jspx_page_context = null;


    try {
      response.setContentType("text/html; charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;

      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("<!DOCTYPE html>\r\n");
      out.write("<html>\r\n");
      out.write("<head>\r\n");
      out.write("<meta charset=\"UTF-8\">\r\n");
      out.write("<title>Insert title here</title>\r\n");
      out.write("<script src=\"https://code.jquery.com/jquery-3.6.0.min.js\"></script>\r\n");
      out.write("\r\n");

request.setCharacterEncoding("utf-8");
int num = Integer.parseInt(request.getParameter("num"));
BoardDAO dao = BoardDAO.getInstance();
BoardDTO b =dao.findByNum(num);
int ref = b.getRef();
int re_step = b.getRe_step();
int re_level = b.getRe_level();

      out.write("\r\n");
      out.write("\r\n");
      out.write("<script >\r\n");
      out.write("function del() {\r\n");
      out.write("	if(confirm(\"정말 삭제할까요?\")){\r\n");
      out.write("		location.href=\"deletePro.jsp?num=");
      out.print(num);
      out.write("\";	\r\n");
      out.write("	}\r\n");
      out.write("	\r\n");
      out.write("}\r\n");
      out.write("\r\n");
      out.write("</script>\r\n");
      out.write("\r\n");
      out.write("</head>\r\n");
      out.write("<body>\r\n");
      out.write("<h2>글 내용 보기</h2>\r\n");
      out.write("<input type=\"hidden\" id=\"num\" value=\"");
      out.print(num);
      out.write("\">\r\n");
      out.write("<table border=\"1\">\r\n");
      out.write("	<tr>\r\n");
      out.write("		<th>글번호</th>\r\n");
      out.write("		<td>");
      out.print(b.getNum() );
      out.write("</td>\r\n");
      out.write("		<th>조회수</th>\r\n");
      out.write("		<td>");
      out.print(b.getReadcount() );
      out.write("</td>\r\n");
      out.write("	<tr>\r\n");
      out.write("		<th>작성자</th>\r\n");
      out.write("		<td>");
      out.print(b.getWriter() );
      out.write("</td>\r\n");
      out.write("		<th>작성일</th>\r\n");
      out.write("		<td>");
      out.print(b.getReg_date() );
      out.write("</td>\r\n");
      out.write("	</tr>\r\n");
      out.write("	<tr>\r\n");
      out.write("		<th>글제목</th>\r\n");
      out.write("		<td colspan=\"3\">");
      out.print(b.getSubject() );
      out.write("</td>\r\n");
      out.write("	</tr>\r\n");
      out.write("	<tr>\r\n");
      out.write("		<th>글내용</th>\r\n");
      out.write("		<td colspan=\"3\">");
      out.print(b.getContent() );
      out.write("</td>\r\n");
      out.write("	</tr>\r\n");
      out.write("	<tr>\r\n");
      out.write("		<td colspan=\"4\" >\r\n");
      out.write("		<input type=\"button\" value=\"글수정폼\" onclick=\"location.href='updateForm.jsp?num=");
      out.print(num);
      out.write("'\"> \r\n");
      out.write("		<input type=\"button\" value=\"글삭제\" onclick=\"del()\">\r\n");
      out.write("		<input type=\"button\" value=\"답글쓰기\" onclick=\"location.href='writeForm.jsp?num=");
      out.print(num);
      out.write("&ref=");
      out.print(ref);
      out.write("&re_step=");
      out.print(re_step);
      out.write("&re_level=");
      out.print(re_level);
      out.write("'\"> \r\n");
      out.write("		<input type=\"button\" value=\"글목록\" onclick=\"location.href='list.jsp'\"> \r\n");
      out.write("		</td>\r\n");
      out.write("	</tr>\r\n");
      out.write("	</table>\r\n");
      out.write("	<br><br><br><br><br>\r\n");
      out.write("	<div align=\"center\">\r\n");
      out.write("	<textarea rows=\"5\" cols=\"50\" id=\"msg\"></textarea>\r\n");
      out.write("	<input type=\"button\" value=\"comment Insert\" id=\"commentBtn\">\r\n");
      out.write("	</div>\r\n");
      out.write("	Comment(<span id=\"spanCnt\"></span>) <br>\r\n");
      out.write("	<div id=\"result\"></div>\r\n");
      out.write("	<script>\r\n");
      out.write("	var init = function(){\r\n");
      out.write("		$.getJSON(\"commentList.jsp\",{\"bnum\":$(\"#num\").val()},\r\n");
      out.write("				function(resp){\r\n");
      out.write("					// alert(resp);\r\n");
      out.write("					var str = \"<table>\"\r\n");
      out.write("					$.each(resp.main,function(key,val){\r\n");
      out.write("						str += \"<tr>\";\r\n");
      out.write("						str += \"<td>\"+ val.msg + \"</td>\"\r\n");
      out.write("						str += \"<td>\"+ val.userid + \"</td>\"\r\n");
      out.write("						str += \"<td>\"+ val.regdate + \"</td>\"\r\n");
      out.write("						str += \"</tr>\";\r\n");
      out.write("					})\r\n");
      out.write("					\r\n");
      out.write("					$(\"#result\").html(str);\r\n");
      out.write("					$(\"#spanCnt\").text(resp.count.count);\r\n");
      out.write("			\r\n");
      out.write("		})\r\n");
      out.write("	}\r\n");
      out.write("	\r\n");
      out.write("	$(\"#commentBtn\").on(\"click\",function(){\r\n");
      out.write("		if($(\"#msg\").val()==\"\"){\r\n");
      out.write("			alert(\"메세지를 입력하세요\")\r\n");
      out.write("			return;\r\n");
      out.write("		}\r\n");
      out.write("		$.ajax({\r\n");
      out.write("			type:\"get\",\r\n");
      out.write("			url:\"commentInsertPro.jsp\",\r\n");
      out.write("			data:{\"msg\" : $(\"#msg\").val(),\"bnum\" : $(\"#num\").val()},\r\n");
      out.write("			success:function(resp){\r\n");
      out.write("				//alert(resp);\r\n");
      out.write("				if(resp.trim()==1){\r\n");
      out.write("					alert(\"로그인 하세요\");\r\n");
      out.write("					location.href=\"../member/loginForm.jsp\";\r\n");
      out.write("				}else{\r\n");
      out.write("				init();\r\n");
      out.write("				$(\"#msg\").val(\"\");	\r\n");
      out.write("				}\r\n");
      out.write("			},\r\n");
      out.write("			error:function(e){\r\n");
      out.write("				alert(\"error:\"+e);\r\n");
      out.write("			}\r\n");
      out.write("		})\r\n");
      out.write("	})\r\n");
      out.write("	\r\n");
      out.write("	init();\r\n");
      out.write("	</script>\r\n");
      out.write("	<br>\r\n");
      out.write("</body>\r\n");
      out.write("</html>");
    } catch (java.lang.Throwable t) {
      if (!(t instanceof javax.servlet.jsp.SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          try {
            if (response.isCommitted()) {
              out.flush();
            } else {
              out.clearBuffer();
            }
          } catch (java.io.IOException e) {}
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}