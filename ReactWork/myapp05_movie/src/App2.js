import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  state = {
    isLoading: true
  }

  // getMovies = async () => {
  //   const {
  //     data: {
  //       data: { movies }
  //     }
  //   } = await axios.get('https://yts-proxy.now.sh/list_movies.json?sort_by=rating')
  //   this.setState({ movies, isLoading: false })
  // }

  getMovies = () => {
    fetch('https://yts-proxy.now.sh/list_movies.json?sort_by=rating')
      .then((res) => res.json())
      .catch(err => console.log(err))
      .then((res) => {
        console.log(res.data.movies)
        this.setState({ movies: res.data.movies, isLoading: false })
      })
  }

  componentDidMount() {
    //   setTimeout(() => {
    //     this.setState({ isLoading: false })
    //   }, 6000)
    // axios.get('https://yts-proxy.now.sh/list_movies.json')
    this.getMovies()
  }

  render() {
    const { isLoading, movies } = this.state
    return (
      <div>
        {isLoading ? 'isLoading...' :
          <div>
            {
              movies.map((movie, index) => {
                return (
                  <div key={index}>
                    {movie.title}
                  </div>
                )
              })
            }
          </div>
        }
      </div>
    )
  }
}

export default App;
