import logo from './logo.svg';
import './App.css';
import PhoneForm from './components/PhoneForm';
import PhoneList from './components/PhoneList';
import { Component } from 'react';

class App extends Component {
  id = 2;

  state = {
    information: [
      {
        id: 0,
        name: "홍길동",
        phone: "010-1111-1111"
      },
      {
        id: 1,
        name: "이순신",
        phone: "010-2222-2222"
      }
    ]
  }

  handleCreate = (data) => {
    console.log(data)
    const { information } = this.state
    this.setState({
      information: information.concat({ id: this.id++, ...data })
    })
  }

  handleRemove = (id) => {
    const { information } = this.state
    this.setState({
      information: information.filter(info => info.id !== id)
    })
  }

  render() {
    return (
      <div>
        <br />
        <PhoneForm onCreate={this.handleCreate} />
        <PhoneList data={this.state.information} onRemove={this.handleRemove} />
      </div>
    );
  }
}

export default App;
