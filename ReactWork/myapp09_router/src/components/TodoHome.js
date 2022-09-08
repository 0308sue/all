import { Button, Card, Col, Container, Form, Row } from "react-bootstrap";
import axios from 'axios';
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

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
                            <Card style={{ width: '18rem' }}>
                                <Card.Body>
                                    <Card.Title>제목 : {todo.title}</Card.Title>
                                    <Card.Text>
                                        {todo.content}
                                    </Card.Text>
                                    <Link to={"/view/" + todo.num} >
                                        <Button variant="success">수정</Button>{' '}
                                    </Link>
                                    <Button variant="warning" onClick={() => deletecontent(todo.num)}>삭제</Button>
                                </Card.Body>
                            </Card>
                        </Col>
                    ))
                }
            </Row>
            <Row className="justify-content-md-center mt-5">
                <Col md="auto">
                    <Form.Control type="text" name="search" placeholder="Search" onChange={changeWord} onKeyDown={checkenter} />
                </Col>
                <Col xs lg="2">
                    <Button variant="light" onClick={search} >검색</Button>
                </Col>
            </Row>
        </Container>

    )
}

export default TodoHome;