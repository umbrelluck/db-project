import React from 'react'
import GO from '../GO'

import Result from '../result'
import { Route } from 'react-router-dom'

export default class HKill extends React.Component {

    handler() {
        console.log("Handler for human kill")
    }
    render() {
        // var url = this.props.match.url.substring(0, this.props.match.url.length - 3);
        var url = this.props.match.url;
        return (
            <div className="data_input">
                <input placeholder="Human"></input>
                {/* <input></input> */}
                <GO fun={this.handler} url={url}></GO>
                <Route path={this.props.match.url + '/result'} render={() => (<Result />)} />
            </div>
        )
    }
};