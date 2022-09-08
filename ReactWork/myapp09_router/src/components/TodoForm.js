import { useState } from "react"
import { Button, Container, Form } from "react-bootstrap"

const TodoForm = () => {
    const [formContent, setFormContent] = useState({
        title: '',
        content: '',
    })

    const getValue = (e) => {
        setFormContent({
            ...formContent,
            [e.target.name]: e.target.value
        })
    }

    const submitTodo = () => {
        fetch('/todo/insert', {
            method: 'post',
            headers: {
                'Content-type': 'application/json'
            },
            body: JSON.stringify({
                title: formContent.title,
                content: formContent.content
            })
        }).then((resp) => {
            alert("등록 성공!!!");
            setFormContent({
                title: '',
                content: ''
            })
        })
    }
    return (
        <Container>
            <br></br>
            <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                <Form.Label>title</Form.Label>
                <Form.Control type="text" name="title" placeholder="title" onChange={getValue} value={formContent.title} />
            </Form.Group>
            <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                <Form.Label>content</Form.Label>
                <Form.Control as="textarea" name="content" rows={3} onChange={getValue} value={formContent.content} />
            </Form.Group>
            <Button variant="primary" onClick={submitTodo}>전송</Button><br /><br /><br />
        </Container>
    )
}

export default TodoForm;