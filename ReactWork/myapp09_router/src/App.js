import 'bootstrap/dist/css/bootstrap.min.css'
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import './App.css';
import Navigation from './components/Navigation';
import TodoForm from './components/TodoForm';
import TodoHome from './components/TodoHome';
import TodoView from './components/TodoView';

function App() {

  return (
    <BrowserRouter>
      <Navigation />
      <Switch>
        <Route path="/" exact={true} component={TodoHome} />
        <Route path="/add" component={TodoForm} />
        <Route path="/view/:num" component={TodoView} />
      </Switch>
    </BrowserRouter>
  );
}

export default App;
