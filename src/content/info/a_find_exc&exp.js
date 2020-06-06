import React from 'react'
import GO from '../GO'

import Result from '../result'
import { Route } from 'react-router-dom'

export default class AEcxAndExp extends React.Component {

    handler() {
        console.log("Handler for common exp and exc")
    }
    render() {
        // var url = this.props.match.url.substring(0, this.props.match.url.length - 3);
        var url = this.props.match.url;
        return (
            <div className="data_input">
                <input placeholder="Alien"></input>
                <input placeholder='Human'></input>
                <input placeholder='Time'></input>
                <GO fun={this.handler} url={url}></GO>
                <Route path={this.props.match.url + '/result'} component={Result} />
            </div>
        )
    }
};