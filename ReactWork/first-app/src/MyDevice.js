import Device from "./Device";

const MyDevice = ({ mydata }) => {
    return (
        <div>
            <h4>MyDevice test</h4>
            {
                mydata.myDeviceData.map((device, index) => {
                    return (
                        <div key={index}>
                            키 :{index}<br />
                            이름 : {device.name}<br />
                            램 : {device.RAM}<br />
                            홈버튼 : {(device.HomeButton === true) ? '있음' : '없음'}<br />
                        </div>
                    )
                })
            }
        </div>
    )
}

export default MyDevice;