import React, { Component } from 'react';
import Movie from '../components/Movie';
import './Home.css';

class Home extends Component {
    state = {
        isLoading: true
    }

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
        this.getMovies()
    }

    render() {
        const { isLoading, movies } = this.state
        return (
            <section className='container'>
                {isLoading ?
                    (<div className='loader'>
                        <span className='loader__text'>isLoading</span>
                    </div>) : (
                        <div className='movies'>
                            {
                                movies.map((movie) => {
                                    return (
                                        <Movie key={movie.id}
                                            id={movie.id}
                                            year={movie.year}
                                            title={movie.title}
                                            summary={movie.summary}
                                            poster={movie.medium_cover_image}
                                            genres={movie.genres}
                                        />
                                    )
                                })
                            }
                        </div>
                    )
                }
            </section>
        )
    }
}

export default Home;