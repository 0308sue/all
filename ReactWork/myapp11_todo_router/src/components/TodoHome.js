import axios from "axios";
import { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import TodoForm from "./TodoForm";
import TodoList from "./TodoList";

function TodoHome({ loadTodos, handleDelete, handleUpdate, todos }) {
  return (
    <Container>
      <TodoForm loadTodos={loadTodos} />
      <TodoList todos={todos} onRemove={handleDelete} onUpdate={handleUpdate} />
    </Container>
  );
}

export default TodoHome;
