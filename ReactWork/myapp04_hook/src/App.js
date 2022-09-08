import logo from './logo.svg';
import './App.css';
import InputSample from './InputSample';
import InputTest from './InputTest';
import Say from './Say';
import Counter from './Counter';
import Parent from './Parent';

function App() {
  return (
    <div>
      <InputSample /> <hr />
      <InputTest /><hr />
      <Say /><hr />
      <Counter /><hr />
      <Parent />
    </div>
  );
}

export default App;
