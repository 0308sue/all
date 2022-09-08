import React from 'react';
import { Link } from 'react-router-dom';
import './Movie.css';

function Movie({ id, year, title, summary, poster, genres }) {
    return (
        <div className='movie'>
            <Link to={{
                pathname: '/movie-view',
                state: { year, title, summary, poster, genres }
            }}>
                <img src={poster} alt={title} title={title} />
                <div className='movie__data'>
                    <h3 className='movie__tilte'>{title}</h3>
                    <h5 className='movie__tilte'>{title}</h5>
                    <ul className='movie__genres'>
                        {
                            genres.map((genre, index) => {
                                return (
                                    <li key={index}
                                        className="movie__genre">{genre}</li>
                                )
                            })
                        }
                    </ul>
                    <p className='movie__summary'>{summary.slice(0, 180)}...</p>
                </div>
            </Link>
        </div>
    )
}
export default Movie;