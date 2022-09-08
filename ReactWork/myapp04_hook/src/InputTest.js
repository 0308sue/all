import React, { Component, useState } from "react";

class InputTest extends Component {
    state = {
        text: ''
    }

    textChange = (e) => {
        this.setState({ text: e.target.value })
    }

    onReset = () => {
        this.setState({
            text: ''
        })
    }

    render() {
        return (
            <div>
                <input name={this.state.text} onChange={this.textChange} />
                <button onClick={this.onReset} >초기화</button>
                <div>
                    <b>text : {this.state.text}</b>
                </div>
            </div>
        )
    }
}

// const InputTest = () => {
//     const [text, setText] = useState('')
//     const textChange = (e) => {
//         setText(e.target.value)
//     }

//     const onReset = () => {
//         setText('')
//     }

//     return (
// <div>
//     <input name={text} onChange={textChange} />
//     <button onClick={onReset} >초기화</button>
//     <div>
//         <b>text : {text}</b>
//     </div>
// </div>
//     )
// }
export default InputTest;