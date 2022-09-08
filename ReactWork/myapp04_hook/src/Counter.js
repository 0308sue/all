import React, { Component, useState } from "react";

const Counter = () => {
    const [number, setNumber] = useState(0)

    const clickup = () => {
        setNumber(number + 1)
    }

    const clickdown = () => {
        setNumber(number - 1)
    }

    const change = (num) => {
        setNumber(number + num)
    }

    return (
        <div>
            <h1>{number}</h1>
            <button onClick={clickup} >+1</button>
            <button onClick={clickdown}>-1</button>
            <br />
            <button onClick={() => change(1)} >1증가</button>
            <button onClick={() => change(-1)}>1감소</button>
        </div>
    )
}
export default Counter;