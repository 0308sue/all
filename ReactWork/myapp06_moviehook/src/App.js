import logo from './logo.svg';
import { BrowserRouter, HashRouter, Route, Switch } from "react-router-dom"
import './App.css';
import Home from './routers/Home';
import Navigation from './components/Navigation';
import About from './routers/About';
import Detail from './routers/Detail';
import Index from './routers/Index';
import Detail2 from './routers/Detail2';

function App() {
  return (
    <BrowserRouter>
      <Navigation />
      <Switch>
        <Route path='/' exact={true} component={Home}></Route>
        <Route path='/index' component={Index}></Route>
        <Route path='/list' component={Home}></Route>
        <Route path='/about' component={About}></Route>
        <Route path='/detail' component={Detail}></Route>
        <Route path='/detail2' component={Detail2}></Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
