package com.address;

public class ZipCode {
private String Zipcode;
private String sido;
private String gugun;
private String dong;
private String bunji;
private int seq;
public String getZipcode() {
	return Zipcode;
}
public void setZipcode(String zipcode) {
	Zipcode = zipcode;
}
public String getSido() {
	return sido;
}
public void setSido(String sudo) {
	this.sido = sudo;
}
public String getGugun() {
	return gugun==null?"":gugun;
}
public void setGugun(String gugun) {
	this.gugun = gugun;
}
public String getDong() {
	return dong;
}
public void setDong(String dong) {
	this.dong = dong;
}
public String getBunji() {
	return bunji ==null?"":bunji;
}
public void setBunji(String bunji) {
	this.bunji = bunji;
}
public int getSeq() {
	return seq;
}
public void setSeq(int seq) {
	this.seq = seq;
}


}
