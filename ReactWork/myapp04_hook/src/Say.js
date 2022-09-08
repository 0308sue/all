import { useState } from "react";

const Say = () => {
    const [message, setMessage] = useState('안녕')
    const [color, setColor] = useState('black')

    const onClickEnter = () => {
        setMessage('반갑습니다')
        setColor('blue')
    }
    const onClickOut = (e) => {
        setMessage('안녕히가세요')
        setColor('green')
    }

    const changeColor = (color) => {
        setColor(color)
    }

    const clickColor = () => {
        setColor('pink')
    }
    return (
        <div>
            <button onClick={onClickEnter}>입장</button>
            <button onClick={onClickOut}>퇴장</button>
            <h1 style={{ color }}> {message} </h1>
            <button onClick={() => changeColor('red')}>빨간색</button>
            <button onClick={() => changeColor('green')}>초록색</button>
            <button onClick={() => changeColor('blue')}>파란색</button>
            <button onClick={clickColor}>분홍색</button>
        </div>
    )
}
export default Say;
