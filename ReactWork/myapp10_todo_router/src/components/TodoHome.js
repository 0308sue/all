import { Button, Card, Col, Container, Form, Row } from "react-bootstrap";
import axios from 'axios';
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import TodoItem from "./TodoItem";

const TodoHome = () => {

    const [listContent, setListContent] = useState([]);
    const [word, setWord] = useState('');

    useEffect(() => {
        Contentlist()
    }, [])

    const Contentlist = () => {
        axios.get('/todo/list').then((resp) => {
            console.log(resp.data)
            setListContent(resp.data)
        })
    }

    const deletecontent = (num) => {
        axios.delete("todo/delete/" + num)
            .then(() => {
                alert("삭제성공")
                setListContent(listContent.filter(todo => todo.num !== num))
            })
    }

    const search = () => {
        axios.get("todo/search?word=" + word)
            .then((resp) => {
                setListContent(resp.data)
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
        <Container className="mt-5">
            <Row>
                {
                    listContent && listContent.map((todo, index) => (
                        <Col key={index}>
                            <TodoItem key={todo.num} todo={todo} deletecontent={deletecontent} ></TodoItem>
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

export default TodoHome;