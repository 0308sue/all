package com.jqueryAddress;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

import com.address.Address;
import com.address.AddressDAO;

public class JAddressDAOImpl implements JAddressDAO{
	
	private static JAddressDAO instance;
	public static JAddressDAO getInstance() {
		if(instance == null) {
			instance = new JAddressDAOImpl();
		}
		return instance;
	}
	
	private Connection getConnection() throws Exception {
		Context initCtx = new InitialContext();
		Context envCtx =(Context)initCtx.lookup("java:comp/env");
		DataSource ds = (DataSource)envCtx.lookup("jdbc/jsp");
		return ds.getConnection();
		
	}
	private void closeConnection(Connection con, PreparedStatement ps, 
			Statement st, ResultSet rs) {
		try {
			if(con!=null) con.close();
			if(ps!=null) ps.close();
			if(st!=null) st.close();
			if(rs!=null) rs.close();
		}catch(SQLException e) {
			e.printStackTrace();
		}
		
	}

	@Override
	public void insert(AddressVO avo) {
		Connection con = null;
		PreparedStatement ps = null;
		try {
			con =getConnection();
			String sql = "insert into address values(address_seq.nextval,?,?,?,?)";
			ps=con.prepareStatement(sql);
			ps.setString(1, avo.getName());
			ps.setString(2, avo.getAddr());
			ps.setString(3, avo.getZipcode());
			ps.setString(4, avo.getTel());
			ps.executeUpdate();
			
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			closeConnection(con,ps,null, null);
		}
		
	}

	@Override
	public ArrayList<AddressVO> list() {
		Connection con = null;
		Statement st = null;
		ResultSet rs = null;
		ArrayList<AddressVO> jarr = new ArrayList<AddressVO>();
		try {
			con = getConnection();
			String sql = "select * from address order by num desc";
			st = con.createStatement();
			rs = st.executeQuery(sql);
			while(rs.next()) {
				AddressVO avo = new AddressVO();
				avo.setAddr(rs.getString("addr"));
				avo.setName(rs.getString("name"));
				avo.setNum(rs.getInt("num"));
				avo.setTel(rs.getString("tel"));
				avo.setZipcode(rs.getString("zipcode"));
				jarr.add(avo);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			closeConnection(con, null, st, rs);
		}
		
		return jarr;
	}

	@Override
	public AddressVO findbyNum(int num) {
		String sql="select * from address where num ="+num;
		AddressVO avo =null;
		try(Connection con = getConnection();){
			Statement st = con.createStatement();
			ResultSet rs = st.executeQuery(sql);
			if(rs.next()) {
				avo = new AddressVO();
				avo.setAddr(rs.getString("addr"));
				avo.setName(rs.getString("name"));
				avo.setNum(rs.getInt("num"));
				avo.setTel(rs.getString("tel"));
				avo.setZipcode(rs.getString("zipcode"));
			}
		}
		 catch (SQLException e) {
				e.printStackTrace();
			} catch (Exception e) {
				e.printStackTrace();
			}return avo;
//		Connection con = null;
//		Statement st = null;
//		ResultSet rs = null;
//		AddressVO avo =null;
//		
//			try {
//			con = getConnection();
//			String sql="select * from address where num ="+num;
//			st= con.createStatement();
//			rs = st.executeQuery(sql);
//			if(rs.next()) {
//				avo = new AddressVO();
//				avo.setAddr(rs.getString("addr"));
//				avo.setName(rs.getString("name"));
//				avo.setNum(rs.getInt("num"));
//				avo.setTel(rs.getString("tel"));
//				avo.setZipcode(rs.getString("zipcode"));
//			}
//		} catch (Exception e) {
//			e.printStackTrace();
//		}finally {
//			closeConnection(con,null,st,rs);
//		}
//			return avo;

		
	}

	@Override
	public int getCount() {
		Connection con = null;
		Statement st = null;
		ResultSet rs = null;
		int count = 0;
		try {
			con = getConnection();
			String sql ="select count(*) from address";
			st = con.createStatement();
			rs = st.executeQuery(sql);
			if(rs.next()) {
				count = rs.getInt(1);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			closeConnection(con, null, st, rs);
		}
		return count;
	}

	@Override
	public int getCount(String field, String word) {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public void update(AddressVO avo) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void delete(int num) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public ArrayList<AddressVO> searchlist(String field, String word) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public ArrayList<ZipcodeVO> getZipcode(String dong) {
		Connection con = null;
		Statement st = null;
		ResultSet rs = null;
		ArrayList<ZipcodeVO> zarr = new ArrayList<ZipcodeVO>();
		try {
			con = getConnection();
			String sql ="select * from zipcode where dong like '%"+dong+"%'";
			st = con.createStatement();
			rs = st.executeQuery(sql);
			while(rs.next()) {
				ZipcodeVO zip =new ZipcodeVO();
				zip.setBunji(rs.getString("bunji"));
				zip.setDong(rs.getString("dong"));
				zip.setGugun(rs.getString("gugun"));
				zip.setSido(rs.getString("sido"));
				zip.setZipcode(rs.getString("zipcode"));
				zarr.add(zip);
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally {
			closeConnection(con, null, st, rs);
		}
		return zarr;
	}

}
