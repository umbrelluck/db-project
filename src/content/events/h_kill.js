import React from 'react'
import GO from '../GO'
import axios from 'axios'

import Result from '../result'
import { Route } from 'react-router-dom'

export default class HKill extends React.Component {

    constructor(props) {
        super(props);
        this.lst = []
        this.state = {
            info: []
        }
    }

    async register(list, date, weapon, id_ship, id_human, id_alien) {
        console.log(list, date, weapon, id_ship, id_human, id_alien);
        const response = await axios.get('/get_human_kills_alien', {
            params: {
                date: date,
                weapon: weapon,
                id_ship: id_ship,
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
        var fl = true
        for (var elem of document.getElementsByTagName('input')) {
            console.log(elem)
            if (elem.value === "") {
                fl = false
                break
            }
            if (cnt < 2)
                res.push(elem.value)
            else
                res.push(Number(elem.value))
            cnt++;
        }
        console.log(this.lst, res);
        if (fl)
            this.register(this.lst, res[0], res[1], res[2], res[3], res[4]);
        else
            this.setState(state => ({
                info: new Array(new Array("Invalid input"))
            }))
    }

    render() {
        // var url = this.props.match.url.substring(0, this.props.match.url.length - 3);
        var url = this.props.match.url;
        return (
            (this.state.info.length !== 0) ? <div className="data_input">
                <input placeholder="Cur. date(mnth-day-year)"></input>
                <input placeholder="Weapon"></input>
                <input placeholder="Ship ID"></input>
                <input placeholder="Human ID"></input>
                <input placeholder="Alien ID"></input>
                <GO fun={this.handler} url={url}></GO>
                <Route path={this.props.match.url + '/result'} render={() => (<Result info={this.state.info} />)} />
            </div> : <div className="data_input">
                    <input placeholder="Cur. date(mnth-day-year)"></input>
                    <input placeholder="Weapon"></input>
                    <input placeholder="Ship ID"></input>
                    <input placeholder="Human ID"></input>
                    <input placeholder="Alien ID"></input>
                    <GO fun={this.handler} url={url}></GO>
                </div>
        )
    }
};