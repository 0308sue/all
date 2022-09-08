import { useEffect, useState } from "react";
import axios from 'axios';
import { Button, Container, Form } from "react-bootstrap";

const TodoView = (props) => {

    const [formContent, setFormContent] = useState({
        title: '',
        content: '',
    })

    const findByNum = (num) => {
        axios.get('/todo/get/' + num)
            .then((resp) => {
                console.log(resp.data)
                setFormContent(resp.data)
            })
    }
    useEffect(() => {
        let num = props.match.params.num
        console.log("num : " + num)
        findByNum(num)
    }, [])

    const getValue = (e) => {
        setFormContent({
            ...formContent,
            [e.target.name]: e.target.value
        })
    }

    const updateTodo = () => {
        fetch('/todo/update', {
            method: 'post',
            headers: {
                'Content-type': 'application/json'
            },
            body: JSON.stringify({
                num: formContent.num,
                title: formContent.title,
                content: formContent.content
            })
        }).then((resp) => {
            alert("수정 성공!!!");
            props.history.push('/')
        })
    }

    return (
        <Container>
            <br></br>
            <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                <Form.Label>title</Form.Label>
                <Form.Control type="text" name="title" value={formContent.title} onChange={getValue} />
            </Form.Group>
            <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                <Form.Label>content</Form.Label>
                <Form.Control as="textarea" name="content" rows={3} value={formContent.content} onChange={getValue} />
            </Form.Group>
            <Button variant="primary" onClick={updateTodo}>수정</Button><br /><br /><br />
        </Container>
    )
}

export default TodoView;