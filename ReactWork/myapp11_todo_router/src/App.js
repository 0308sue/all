import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Navigation from "./components/Navigation";
import TodoHome from "./components/TodoHome";
import TodoList from "./components/TodoList";
import TodoView from "./components/TodoView";

function App() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    loadTodos();
  }, []);

  // 모든 todo 가지고 온다
  const loadTodos = () => {
    axios.get("/todo/list").then((resp) => {
      setTodos(resp.data);
    });
  };

  const handleDelete = (num) => {
    axios.delete("/todo/delete/" + num).then(() => {
      alert("delete");
      setTodos(todos.filter((todo) => todo.num !== num));
    });
  };

  const handleUpdate = (searchTodos) => {
    setTodos(searchTodos);
  };

  return (
    <BrowserRouter>
      <Container className="mt-5">
        <Navigation />
      </Container>
      <Routes>
        <Route
          path="/"
          element={
            <TodoHome
              loadTodos={loadTodos}
              todos={todos}
              handleDelete={handleDelete}
              handleUpdate={handleUpdate}
            />
          }
        />
        <Route
          path="/list"
          element={
            <TodoList
              todos={todos}
              onRemove={handleDelete}
              onUpdate={handleUpdate}
            />
          }
        />
        <Route path="/view">
          <Route path=":num" element={<TodoView />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
