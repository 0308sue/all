import { useState } from "react";
import { Button, Container, Form } from "react-bootstrap"
import axios from 'axios';

const TodoForm = ({ listTodo }) => {

    const [formContent, setFormContent] = useState({
        subject: '',
        name: '',
        summary: ''
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
                subject: formContent.subject,
                name: formContent.name,
                summary: formContent.summary
            })
        }).then((resp) => {
            alert("등록 성공!!!");
            listTodo();
            setFormContent({
                subject: '',
                name: '',
                summary: ''
            })
        })
    }
    // const submitTodo = () => {
    //     axios.post('/todo/insert', {
    //         subject: formContent.subject,
    //         name: formContent.name,
    //         summary: formContent.summary
    //     }).then((resp) => {
    //         alert(resp.data);
    //         listTodo();
    //         setFormContent({
    //             subject: '',
    //             name: '',
    //             summary: ''
    //         })
    //     })
    // }

    return (
        <Form>
            <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                <Form.Label>subject</Form.Label>
                <Form.Control type="text" name="subject" placeholder="subject" onChange={getValue} value={formContent.subject} />
            </Form.Group>
            <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                <Form.Label>name</Form.Label>
                <Form.Control type="text" name="name" placeholder="name" onChange={getValue} value={formContent.name} />
            </Form.Group>
            <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                <Form.Label>summary</Form.Label>
                <Form.Control as="textarea" name="summary" rows={3} onChange={getValue} value={formContent.summary} />
            </Form.Group>
            <Button variant="secondary" onClick={submitTodo}>전송</Button><br /><br /><br />
        </Form>
    )
}

export default TodoForm;