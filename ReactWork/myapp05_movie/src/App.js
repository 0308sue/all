import { BrowserRouter, HashRouter, Route, Switch } from "react-router-dom"
import Navigation from "./components/Navigation";
import Home from "./routers/Home";
import MovieView from "./routers/MovieView";
import './App.css';
import About from "./routers/About";


function App() {
    return (
        <BrowserRouter>
            <Navigation />
            <Switch>
                <Route path="/" exact={true}
                    component={Home} ></Route>
                <Route path="/movie-view"
                    component={MovieView} ></Route>
                <Route path="/about"
                    component={About} ></Route>
            </Switch>
        </BrowserRouter>
    )
}

export default App;