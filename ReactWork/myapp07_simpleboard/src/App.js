import logo from './logo.svg';
import './App.css';
import BoardForm from './BoardForm';
import BoardList from './BoardList';
import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {

  const [listContent, setListContent] = useState([]);

  useEffect(() => {
    listBoard()
  }, [])

  const listBoard = () => {
    axios.get('/api/list').then((resp) => {
      console.log(resp.data)
      setListContent(resp.data)
    })
  }

  const deleteBoard = (num) => {
    axios.delete("api/delete/" + num)
      .then(() => {
        alert("삭제성공")
        setListContent(listContent.filter(board => board.num !== num))
      })
  }
  return (
    <div>
      <h1>myapp07 Simple Board</h1>
      <BoardForm listBoard={listBoard} />
      <BoardList lists={listContent}
        deleteBoard={deleteBoard} />
    </div>
  );
}

export default App;
