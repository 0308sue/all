import logo from './logo.svg';
import './App.css';
import Greet from './Greet';
import Greet1 from './Greet1';
import Welcome from './Welcome';

function App() {
  let obj = {
    name: "test",
    age: 1
  }
  let { name, age } = obj
  console.log(name)

  const array = ['a', 'b', 'c', 'd']
  const [first, second, third, fourth] = array

  console.log(first)
  console.log(second)
  console.log(third)
  console.log(fourth)

  const deepObject = {
    state: {
      information: {
        title: "reactname",
        category: ['js', 'algorithm', 'java']
      }
    },
    age2: 1
  }

  const {
    state: {
      information: { title, category }
    },
    age2
  } = deepObject

  // const { title, category } = deepObject.state.information
  // const { age2 } = deepObject;

  // const extracted = {
  //   title,
  //   category,
  //   age2: age2
  // }
  // console.log(extracted)

  // const extracted1 = {
  //   title,
  //   category,
  //   age2
  // }
  // console.log(extracted1)

  return (
    <div>
      <Greet name="Diana" heroName="Wonder Woman" />
      <Greet1 name="Diana" heroName="Wonder Woman" />
      <Welcome name="Bruce" heroName="Batman" />
    </div>
  );
}

export default App;
