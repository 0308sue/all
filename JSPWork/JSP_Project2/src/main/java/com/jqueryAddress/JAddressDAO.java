package com.jqueryAddress;

import java.util.ArrayList;

public interface JAddressDAO {
	
	//�߰�
	public void insert(AddressVO avo);
	//��ü����
	public ArrayList<AddressVO>list();
	//�󼼺���
	public AddressVO findbyNum(int num);
	//����
	public int getCount();
	//�˻�����
	public int getCount(String field,String word);
	//�����ϱ�
	public void update(AddressVO avo);
	//����
	public void delete(int num);
	//�˻� ��ü����
	public ArrayList<AddressVO> searchlist(String field,String word);
	//�����ȣ �˻�
	public ArrayList<ZipcodeVO> getZipcode(String dong);
	
	
	
	
	

}
