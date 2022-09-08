import 'bootstrap/dist/css/bootstrap.min.css'
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Admin from './components/Admin';
import Home from './components/Home';
import Login from './components/Login';
import Manager from './components/Manager';
import Navigation from './components/Navigation';
import Profile from './components/Profile';
import Register from './components/Register';
import User from './components/User';

function App() {
  return (
    <BrowserRouter>
      <Navigation />
      <div className="container mt-5">
        <Switch>
          <Route path={["/", "/home"]} exact component={Home} />
          <Route path="/register" component={Register} />
          <Route path="/profile" component={Profile} />
          <Route path="/login" component={Login} />
          <Route path="/user" component={User} />
          <Route path="/manager" component={Manager} />
          <Route path="/admin" component={Admin} />
        </Switch>
      </div>
    </BrowserRouter>
  );
}

export default App;
