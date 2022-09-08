import axios from "axios";
import { useState } from "react";
import { Button, Container, Form } from "react-bootstrap"


const TodoForm = () => {

    const [todoContent, setTodoContent] = useState({
        title: '',
        content: ''
    })

    const getValue = (e) => {
        setTodoContent({
            ...todoContent,
            [e.target.name]: e.target.value
        })
    }

    const addTodo = () => {
        axios.post('/todo/insert', {
            title: todoContent.title,
            content: todoContent.content
        }).then(() => {
            alert("추가 완료")
            setTodoContent({
                title: '',
                content: ''
            })
        })
    }

    return (
        <Container className="mt-5" >
            <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                <Form.Label>제목</Form.Label>
                <Form.Control type="text" name="title" placeholder="title" onChange={getValue} value={todoContent.title} />
            </Form.Group>
            <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                <Form.Label>내용</Form.Label>
                <Form.Control as="textarea" name="content" rows={3} placeholder="content" onChange={getValue} value={todoContent.content} />
            </Form.Group>
            <Button variant="outline-primary" onClick={addTodo} >전송</Button><br /><br /><br />
        </Container>
    )
}

export default TodoForm;