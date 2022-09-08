import logo from './logo.svg';
import './App.css';
import BoardForm from './BoardForm';
import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {

  const [listContent, setListContent] = useState([]);

  const [formContent, setFormContent] = useState({
    title: '',
    content: ''
  })

  useEffect(() => {
    listBoard()
  }, [])

  const getValue = (e) => {
    setFormContent({
      ...formContent,
      [e.target.name]: e.target.value
    })
  }

  const submitBoard = () => {
    axios.post('/api/insert', {
      title: formContent.title,
      content: formContent.content
    }).then(() => {
      alert("등록완료")
      listBoard()
    })
  }
  const listBoard = () => {
    axios.get('/api/list').then((resp) => {
      console.log(resp.data)
      setListContent(resp.data)
    })
  }



  return (
    <div>
      <h1>Simple Board</h1>
      <hr />
      <input type="text" name="title" placeholder="제목" onChange={getValue}></input><br />
      <textarea name="content" cols={50} rows="10" onChange={getValue} ></textarea><br />
      <button onClick={submitBoard}>입력</button>
      {/* <button onClick={listBoard}>전체보기</button> */}
      <hr />
      <div>
        {
          listContent.map((board, index) => (
            <p key={index}>
              번호: {board.num} <br />
              제목: {board.title}<br />
              내용: {board.content}<br />
            </p>
          ))
        }
      </div>
    </div>
  );
}

export default App;
