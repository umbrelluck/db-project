import React from 'react'
import { NavLink, Route } from 'react-router-dom'
import Result from './result'

export default class Alien extends React.Component {
    render() {
        return (
            <div id="alien">
                <p>Alien section</p>
                <NavLink to={this.props.match.url + '/result'}>
                    <button >GO</button>
                </NavLink>
                <Route path={this.props.match.url + '/result'} component={Result} />
            </div>
        )
    }
}