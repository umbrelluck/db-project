import React from 'react'
import GO from '../GO'

import Result from '../result'
import { Route } from 'react-router-dom'

export default class HKill extends React.Component {

    handler = () => {
        var res = []
        var cnt = 0
        for (var elem of document.getElementsByTagName('input')) {
            console.log(elem)
            if (cnt < 2)
                res.push(elem.value)
            else
                res.push(Number(elem.value))
            cnt++;
        }
        console.log(this.lst, res);
        this.register(res[0], res[1], res[2], res[3], res[4]);
    }

    render() {
        // var url = this.props.match.url.substring(0, this.props.match.url.length - 3);
        var url = this.props.match.url;
        return (
            <div className="data_input">
                <input placeholder="Current date"></input>
                <input placeholder="Weapon"></input>
                <input placeholder="Ship ID"></input>
                <input placeholder="Human ID"></input>
                <input placeholder="Alien ID"></input>
                <GO fun={this.handler} url={url}></GO>
                <Route path={this.props.match.url + '/result'} render={() => (<Result info={new Array(new Array("Data sent"))} />)} />
            </div>
        )
    }
};