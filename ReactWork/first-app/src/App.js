import Device from './Device';
import Counter from './Counter';
import Food from './Food';
import Movie from './Movie';
import Counter2 from './Counter2';
import MyDevice from './MyDevice';
import MyDevice1 from './MyDevice1';

function App() {

  const mydataApp = {
    "myDeviceData": [
      {
        name: "갤럭시1",
        RAM: 16,
        HomeButton: true,
        TouchID: "NO",
        FaceID: "yes"
      },
      {
        name: "갤럭시2",
        RAM: 32,
        HomeButton: true,
        TouchID: "NO",
        FaceID: "yes"
      },
      {
        name: "갤럭시3",
        RAM: 64,
        HomeButton: false,
        TouchID: "NO",
        FaceID: "yes"
      }
    ]
  }
  return (
    <div className="App">
      <h1>안녕</h1>
      <h2>안녕</h2>
      <Device />
      <Counter />
      <Food />
      <Movie title="영화1" />
      <Movie title="영화2" />
      <Movie title="영화3" />
      <Movie title="영화4" />
      <hr />
      <h3>Count2 클래스 화살표 함수</h3>
      <Counter2 />
      <hr />
      <h4>MyDevice 클래스</h4>
      <MyDevice mydata={mydataApp} />
      <h4>MyDevice1 클래스</h4>
      <MyDevice1 mydata={mydataApp.myDeviceData} />
    </div>
  );
}

export default App;
