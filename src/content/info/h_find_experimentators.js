import React from 'react'
import GO from '../GO'

import Result from '../result'
import { Route } from 'react-router-dom'

export default class HFindExp extends React.Component {

    handler() {
        console.log("Handler for finding experimentators")
    }
    render() {
        // var url = this.props.match.url.substring(0, this.props.match.url.length - 3);
        var url = this.props.match.url;
        return (
            <div className="data_input">
                <input placeholder="Human"></input>
                <input placeholder="Time"></input>
                <input placeholder="Number"></input>
                <GO fun={this.handler} url={url}></GO>
                <Route path={this.props.match.url + '/result'} render={() => (<Result />)} />
            </div>
        )
    }
};