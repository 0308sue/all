import { Component } from "react";

class MyDevice1 extends Component {
    render() {
        const { mydata } = this.props
        return (
            <div>
                {
                    mydata.map((device, index) => {
                        return (
                            <div key={index}>
                                키 :{index}<br />
                                이름 : {device.name}<br />
                                램 : {device.RAM}<br />
                                홈버튼 : {(device.HomeButton === true) ? '있다' : '없다'}<hr />
                            </div>
                        )
                    })
                }
            </div>
        )
    }
}

export default MyDevice1;