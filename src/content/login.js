import React from 'react'
import { NavLink, withRouter } from 'react-router-dom'

export default class Login extends React.Component {
    render() {
        return (
            <div id='login'>
                <NavLink exact to='/alien'>
                    <button className='alien-b'>Alien</button>
                </NavLink>

                <NavLink exact to='/human'>
                    <button className="human-b">Human</button>
                </NavLink>
            </div>
        )
    }
}