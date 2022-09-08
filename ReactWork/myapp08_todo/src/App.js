import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'
import { useEffect, useState } from 'react';
import { Container } from 'react-bootstrap';
import './App.css';
import TodoForm from './TodoForm';
import TodoList from './TodoList';

function App() {

  const [listContent, setListContent] = useState([]);

  useEffect(() => {
    listTodo()
  }, [])

  const listTodo = () => {
    axios.get("/todo/list").then((resp) => {
      setListContent(resp.data)
    })
  }

  const deleteTodo = (num) => {
    axios.delete("todo/delete/" + num).then(() => {
      alert("삭제 성공")
      setListContent(listContent.filter(todo => todo.num !== num))
    })
  }

  return (
    <Container>
      <h1>TO DO 송수민</h1>
      <TodoForm listTodo={listTodo} />
      <TodoList lists={listContent} deleteTodo={deleteTodo} />
    </Container>
  );
}

export default App;
