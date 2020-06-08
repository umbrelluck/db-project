import React from 'react'
import GO from '../GO'
import axios from 'axios'

import Result from '../result'
import { Route } from 'react-router-dom'

export default class Atransport extends React.Component {
    constructor(props) {
        super(props);
        this.lst = []
        this.state = {
            info: []
        }
    }

    async register(list, date, id_ship_from, id_ship_to, id_human, id_alien) {
        console.log(list, date, id_ship_from, id_ship_to, id_human, id_alien);
        const response = await axios.get('/get_alien_transports_human', {
            params: {
                date: date,
                id_ship_from: id_ship_from,
                id_ship_to: id_ship_to,
                id_human: id_human,
                id_alien: id_alien
            }
        });
        console.log("response = ", response)
        // this.lst.push(response.data.result);
        this.setState((state) => ({
            info: response.data.result
        }))
    }

    handler = () => {
        var res = []
        var cnt = 0
        for (var elem of document.getElementsByTagName('input')) {
            console.log(elem)
            if (cnt === 0)
                res.push(elem.value)
            else
                res.push(Number(elem.value))
            cnt++;
        }
        console.log(this.lst, res);
        this.register(this.lst, res[0], res[1], res[2], res[3], res[4]);
    }

    render() {
        // var url = this.props.match.url.substring(0, this.props.match.url.length - 3);
        var url = this.props.match.url;
        return (
            (this.state.info.length !== 0) ? <div className="data_input">
                <input placeholder="Cur. date(mnth-day-year)"></input>
                <input placeholder="Ship from ID"></input>
                <input placeholder="Ship to ID"></input>
                <input placeholder="Human ID"></input>
                <input placeholder="Alien ID"></input>
                <GO fun={this.handler} url={url}></GO>
                <Route path={this.props.match.url + '/result'} render={() => (<Result info={this.state.info} />)} />
            </div> : <div className="data_input">
                    <input placeholder="Cur. date(mnth-day-year)"></input>
                    <input placeholder="Ship from ID"></input>
                    <input placeholder="Ship to ID"></input>
                    <input placeholder="Human ID"></input>
                    <input placeholder="Alien ID"></input>
                    <GO fun={this.handler} url={url}></GO>
                </div>
        )
    }
};