import React from 'react'
import GO from '../GO'
import axios from 'axios'

import Result from '../result'
import { Route } from 'react-router-dom'

export default class Hescape extends React.Component {
    constructor(props) {
        super(props);
        this.lst = []
        this.state = {
            info: []
        }
    }

    async register(date, id_ship_from, id_human) {
        console.log(date, id_ship_from, id_human);
        // def human_escapes_from_the_ship(conn, date, id_ship_from, id_human):
        const response = await axios.get('/get_human_escapes_from_the_ship', {
            params: {
                date: date,
                id_ship_from: id_ship_from,
                id_human: id_human
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
        this.register(res[0], res[1], res[2]);
    }

    render() {
        // var url = this.props.match.url.substring(0, this.props.match.url.length - 3);
        var url = this.props.match.url;
        return (
            (this.state.info.length !== 0) ? <div className="data_input">
                <input placeholder="Cur. date(mnth-day-year)"></input>
                <input placeholder="From ship ID"></input>
                <input placeholder="Human ID"></input>
                <GO fun={this.handler} url={url}></GO>
                <Route path={this.props.match.url + '/result'} render={() => (<Result info={new Array(new Array("Data sent"))} />)} />
            </div> :
                <div className="data_input">
                    <input placeholder="Cur. date(mnth-day-year)"></input>
                    <input placeholder="From ship ID"></input>
                    <input placeholder="Human ID"></input>
                    <GO fun={this.handler} url={url}></GO>
                </div>
        )
    }
};