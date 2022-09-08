import axios from "axios";
import { useEffect, useState } from "react";
import { Button, Col, Container, Form, Row } from "react-bootstrap"
import TodoItem from "./TodoItem";

const TodoList = () => {

    const [listTodo, setListTodo] = useState([]);
    const [word, setWord] = useState('');

    useEffect(() => {
        todolist()
    }, [])

    const todolist = () => {
        axios.get('/todo/list').then((resp) => {
            setListTodo(resp.data)
        })
    }

    const tododelete = (num) => {
        axios.delete('todo/delete/' + num).then(() => {
            alert("삭제성공")
            setListTodo(listTodo.filter(todo => todo.num !== num))
        })
    }
    const search = () => {
        axios.get("todo/search?word=" + word)
            .then((resp) => {
                setListTodo(resp.data)
                setWord('')

            })
    }

    const changeWord = (e) => {
        setWord(e.target.value)
    }

    const checkenter = (e) => {
        if (e.key == "Enter") {
            search()
        }
    }

    return (
        <Container className="mt-5" >
            <Row>
                {
                    listTodo && listTodo.map((todo, index) => (
                        <Col key={index}>
                            <TodoItem key={todo.num} todo={todo} tododelete={tododelete} ></TodoItem>
                            <br />
                        </Col>
                    ))
                }
            </Row>
            <Row className="justify-content-md-center mt-5">
                <Col md="auto">
                    <Form.Control type="text" name="search" placeholder="Search" onChange={changeWord} onKeyDown={checkenter} value={word} />
                </Col>
                <Col xs lg="2">
                    <Button variant="light" onClick={search} >검색</Button>
                </Col>
            </Row>
        </Container>
    )
}

export default TodoList;