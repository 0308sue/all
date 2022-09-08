import { Component } from "react";

class Counter extends Component {
    constructor(props) {
        super(props);
        this.state = {
            count: 0
        }
        this.increaseCount = this.increaseCount.bind(this);
        this.decreaseCount = this.decreaseCount.bind(this);
    }
    increaseCount() {
        // this.setState(({ count }) => {return { count: count + 1 }})
        // return 생략
        this.setState(({ count }) => ({ count: count + 1 }))
    }
    decreaseCount() {
        // this.setState(({ count }) => {
        //     return { count: count - 1 }
        // })
        this.setState((st) => {
            console.log("st :" + st)
            return { count: st.count - 1 }
        })
    }
    render() {
        return (
            <div>
                <span>카운트 : {this.state.count}</span>
                <button onClick={this.increaseCount}>카운트 증가</button>
                <button onClick={this.decreaseCount}>카운트 감소</button>
            </div>
        )
    }
}
export default Counter;