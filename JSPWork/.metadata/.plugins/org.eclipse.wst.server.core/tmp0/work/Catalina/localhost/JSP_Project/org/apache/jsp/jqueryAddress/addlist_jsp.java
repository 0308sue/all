/*
 * Generated by the Jasper component of Apache Tomcat
 * Version: Apache Tomcat/9.0.62
 * Generated at: 2022-04-12 02:30:17 UTC
 * Note: The last modified time of this file was set to
 *       the last modified time of the source file after
 *       generation to assist with modification tracking.
 */
package org.apache.jsp.jqueryAddress;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import com.jqueryAddress.JAddressDAOImpl;
import com.jqueryAddress.JAddressDAO;
import java.util.ArrayList;
import com.jqueryAddress.AddressVO;

public final class addlist_jsp extends org.apache.jasper.runtime.HttpJspBase
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
    _jspx_imports_classes.add("com.jqueryAddress.AddressVO");
    _jspx_imports_classes.add("com.jqueryAddress.JAddressDAOImpl");
    _jspx_imports_classes.add("com.jqueryAddress.JAddressDAO");
    _jspx_imports_classes.add("java.util.ArrayList");
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
      out.write("\r\n");
      out.write("\r\n");
      out.write("<!DOCTYPE html>\r\n");
      out.write("<html>\r\n");
      out.write("<head>\r\n");
      out.write("<meta charset=\"UTF-8\">\r\n");
      out.write("<title>Insert title here</title>\r\n");
      out.write("<link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css\">\r\n");
      out.write("  <script src=\"https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.slim.min.js\"></script>\r\n");
      out.write("  <script src=\"https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js\"></script>\r\n");
      out.write("  <script src=\"https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js\"></script>\r\n");
      out.write("  <script src=\"https://code.jquery.com/jquery-3.6.0.min.js\"></script>\r\n");
      out.write("\r\n");

JAddressDAO dao = JAddressDAOImpl.getInstance();
ArrayList<AddressVO> jarr =  dao.list();
int count = dao.getCount();

      out.write(" \r\n");
      out.write("</head>\r\n");
      out.write("<script>\r\n");
      out.write("$(document).ready(function(){\r\n");
      out.write("	$(\"#btnSearch\").click(function () {\r\n");
      out.write("		$.ajax({\r\n");
      out.write("			type :\"get\",\r\n");
      out.write("			url : \"searchProcess.jsp\",\r\n");
      out.write("			data : {\r\n");
      out.write("				\"field\":$(\"#field\").val(),\r\n");
      out.write("				\"word\":$(\"#word\").val(),\r\n");
      out.write("			},\r\n");
      out.write("			success : function (resp) {\r\n");
      out.write("				var d = JSON.parse(resp);\r\n");
      out.write("				var str =\"\";\r\n");
      out.write("				$.each(d.jarrobj,function(key,val){\r\n");
      out.write("					str += \"<tr>\"\r\n");
      out.write("					str += \"<td>\"+val.num +\"</td>\"\r\n");
      out.write("					str += \"<td><a href='addrDetail.jsp?num=\"+val.num+\"'>\"+val.name +\"</a></td>\"\r\n");
      out.write("					str += \"<td>\"+val.addr +\"</td>\"\r\n");
      out.write("					str += \"<td>\"+val.tel +\"</td>\"\r\n");
      out.write("					str += \"</tr>\"\r\n");
      out.write("				})\r\n");
      out.write("				$(\"table tbody\").html(str);\r\n");
      out.write("				$(\"#cntSpan\").text(d.countObj.count);\r\n");
      out.write("			},\r\n");
      out.write("			error : function (e) {\r\n");
      out.write("				alert(\"error : \"+e);\r\n");
      out.write("			}\r\n");
      out.write("		})//aj\r\n");
      out.write("		\r\n");
      out.write("	})//bt\r\n");
      out.write("})//do\r\n");
      out.write("</script>\r\n");
      out.write("<body>\r\n");
      out.write("\r\n");
      out.write("<div class=\"container\">\r\n");
      out.write("<div align=\"right\">\r\n");
      out.write("<a href=\"insert.jsp\"> 추가하기\r\n");
      out.write("/<a href=\"addlist.jsp\"> 전체보기</a><br><br>\r\n");
      out.write("</div>\r\n");
      out.write("\r\n");
      out.write("<h2>Jquery Address 전체보기(<span id=\"cntSpan\">");
      out.print( count );
      out.write("</span>)</h2>\r\n");
      out.write("	<table class=\"table table-hover\">\r\n");
      out.write("	<thead>\r\n");
      out.write("		<tr>\r\n");
      out.write("			<th>번호</th>\r\n");
      out.write("			<th>이름</th>\r\n");
      out.write("			<th>주소</th>\r\n");
      out.write("			<th>전화번호</th>\r\n");
      out.write("		</tr>\r\n");
      out.write("	</thead>\r\n");
      out.write("	<tbody>	\r\n");
      out.write("	");

	for(AddressVO a:jarr){
		
      out.write("\r\n");
      out.write("\r\n");
      out.write("		<tr>\r\n");
      out.write("			<td>");
      out.print( a.getNum() );
      out.write("</td>\r\n");
      out.write("			<td><a href=\"addrDetail.jsp?num=");
      out.print( a.getNum() );
      out.write('"');
      out.write('>');
      out.write(' ');
      out.print( a.getName() );
      out.write("</a></td>\r\n");
      out.write("			<td>");
      out.print( a.getAddr() );
      out.write("</td>\r\n");
      out.write("			<td>");
      out.print( a.getTel() );
      out.write("</td>\r\n");
      out.write("		</tr>\r\n");
      out.write("		</tr>\r\n");
      out.write("		");

		}
		
      out.write("\r\n");
      out.write("	</tbody>\r\n");
      out.write("	</table>\r\n");
      out.write("	<select name=\"field\" id=\"field\">\r\n");
      out.write("	<option value=\"name\">이름</option>\r\n");
      out.write("	<option value=\"tel\">전화번호</option>\r\n");
      out.write("	</select>\r\n");
      out.write("	<input type=\"text\" name=\"word\" id=\"word\">\r\n");
      out.write("	<input type=\"button\" value=\"검색\" id=\"btnSearch\">\r\n");
      out.write("\r\n");
      out.write("</div>\r\n");
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