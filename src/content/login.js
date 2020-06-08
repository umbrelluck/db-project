import React from 'react'
import { NavLink, Route } from 'react-router-dom'

import Info from './info'

export default class Login extends React.Component {
    render() {
        return (
            <div>
                <div id='login'>
                    <NavLink exact to='/alien'>
                        <button className='alien-b'>Alien</button>
                    </NavLink>

                    <NavLink exact to='/human'>
                        <button className="human-b">Human</button>
                    </NavLink>
                </div>

                <Route exact path='/' component={Info}></Route>
            </div>
        )
    }
}