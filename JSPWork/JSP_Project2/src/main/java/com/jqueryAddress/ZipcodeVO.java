package com.jqueryAddress;

public class ZipcodeVO {
	private String Zipcode;
	private String sido;
	private String gugun;
	private String dong;
	private String bunji;
	private int seq;
	public String getZipcode() {
		return Zipcode == null ? "" : Zipcode.trim();
	}
	public void setZipcode(String zipcode) {
		Zipcode = zipcode;
	}
	public String getSido() {
		return sido == null ? "" : sido.trim();
	}
	public void setSido(String sido) {
		this.sido = sido;
	}
	public String getGugun() {
		return gugun == null ? "" : gugun.trim();
	}
	public void setGugun(String gugun) {
		this.gugun = gugun;
	}
	public String getDong() {
		return dong == null ? "" : dong.trim();
	}
	public void setDong(String dong) {
		this.dong = dong;
	}
	public String getBunji() {
		return bunji == null ? "" : bunji.trim();
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
