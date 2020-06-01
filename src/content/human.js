import React from 'react'
import { NavLink, Route } from 'react-router-dom'
import Result from './result'

export default class Human extends React.Component {
    render() {
        // console.log(this.props.match)
        return (
            <div id="human">
                <p>Human section</p>
                <NavLink to={this.props.match.url + '/result'}>
                    <button >GO</button>
                </NavLink>
                <Route path={this.props.match.url + '/result'} component={Result} />
            </div>
        )
    }
}