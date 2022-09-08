import React, { useState } from "react";

const InputSample = () => {
    // const [name, setName] = useState('')
    // const [nickname, setNickname] = useState('')
    // const [phone, setPhone] = useState('')

    // const onChangeName = (e) => {
    //     setName(e.target.value)
    // }

    // const onChangeNickname = (e) => {
    //     setNickname(e.target.value)
    // }

    // const onChangePhone = (e) => {
    //     setPhone(e.target.value)
    // }

    // const onReset = (e) => {
    //     setName('')
    //     setNickname('')
    //     setPhone('')
    // }

    const [inputs, setInputs] = useState({
        name: '',
        nickname: '',
        phone: '',
    })
    const { name, nickname, phone } = inputs

    const onChange = (e) => {
        setInputs({
            ...inputs,
            [e.target.name]: e.target.value
        })
    }

    const onReset = () => {
        setInputs({
            name: '',
            nickname: '',
            phone: '',
        })
    }
    return (
        <div>
            <input name="name" placeholder="이름" value={name} onChange={onChange} />
            <input name="nickname" placeholder="닉네임" value={nickname} onChange={onChange} />
            <input name="phone" placeholder="전화번호" value={phone} onChange={onChange} />
            <button onClick={onReset}>초기화</button>
            <div>
                <b>소개 : </b>
                {name} / {nickname} /{phone}
            </div>
        </div>
    )
}
export default InputSample;