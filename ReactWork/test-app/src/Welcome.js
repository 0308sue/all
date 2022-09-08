import { Component } from "react";

class Welcome extends Component {
    state = {
        state1: 'aaa',
        state2: 'bbb'
    }
    render() {
        const { name, heroName } = this.props;
        const { state1, state2 } = this.state;

        return (
            <h1>
                Welcome {name} ///// {heroName} <br />
                State {state1} ///// {state2}
            </h1>
        )
    }
}
export default Welcome;