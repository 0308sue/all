import Form from "./components/Form";
import TodoItemList from "./components/TodoItemList";

const { Component } = require("react");


class App extends Component {
  id = 3;
  state = {
    input: '',
    todos: [
      { id: 0, text: '치킨먹기', checked: false },
      { id: 1, text: '치킨먹기2', checked: true },
      { id: 2, text: '치킨먹기3', checked: false }
    ]
  }

  handleChange = e => {
    this.setState({
      input: e.target.value
    })
  }

  handelToggle = (id) => {
    const { todos } = this.state

    const index = todos.findIndex(todo => todo.id === id)
    const selected = todos[index]

    const nextTodos = [...todos]
    nextTodos[index] = {
      ...selected,
      checked: !selected.checked
    }
    this.setState({
      todos: nextTodos
    })
  }

  handleCreate = () => {
    const { input, todos } = this.state
    this.setState({
      input: '',
      todos: todos.concat({
        id: this.id++,
        text: input,
        checked: false
      })
    })
  }

  handleKeyPress = e => {
    if (e.key == 'Enter') {
      this.handleCreate()
    }
  }
  handleRemove = id => {
    console.log("id : " + id)
    const { todos } = this.state
    const nextTodos = todos.filter(todo => todo.id !== id)

    this.setState({
      todos: nextTodos
    })
  }

  render() {
    return (
      <div className="todo-list">
        <h3>오늘의 할일</h3>
        <Form value={this.state.input}
          onKeyPress={this.handleKeyPress}
          onChange={this.handleChange}
          onCreate={this.handleCreate}
        />
        <TodoItemList todos={this.state.todos}
          onRemove={this.handleRemove}
          onToggle={this.handelToggle} />
      </div>
    )
  }
}

export default App;