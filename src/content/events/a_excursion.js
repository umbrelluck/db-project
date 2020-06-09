import React from 'react'
import { Route } from 'react-router-dom'
import axios from 'axios'

import GO from '../GO'
import Excursion from './helper/excusrion'


export default class Aexcursion extends React.Component {
    constructor() {
        super()
        this.state = {
            info: []
        }
    }

    async register(date, duration, price, id_alien, id_ship) {
        console.log(date, duration, price, id_alien, id_ship);
        const response = await axios.get('/get_excursion_set', {
            params: {
                date: date,
                duration: duration,
                price: price,
                id_alien: id_alien,
                id_ship: id_ship
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
            if (cnt === 0)
                res.push(elem.value)
            else
                res.push(Number(elem.value))
            cnt++;
        }
        console.log(res);
        if (fl)
            this.register(res[0], res[1], res[2], res[3], res[4]);
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
                <p>Set excursion</p>
                <input placeholder="Date (mnth-day-year)"></input>
                <input placeholder="Duration"></input>
                <input placeholder="Price"></input>
                <input placeholder="Alien ID"></input>
                <input placeholder="Ship ID"></input>
                {/* <input></input> */}
                <GO fun={this.handler} url={url}></GO>

                <Route path={this.props.match.url + '/result'} render={() => (<Excursion url={url + "/result"} info={this.state.info} />)} />
            </div> :
                <div className="data_input">
                    <p>Set excursion</p>
                    <input placeholder="Date (mnth-day-year)"></input>
                    <input placeholder="Duration"></input>
                    <input placeholder="Price"></input>
                    <input placeholder="Alien ID"></input>
                    <input placeholder="Ship ID"></input>
                    {/* <input></input> */}
                    <GO fun={this.handler} url={url}></GO>
                </div>

        )
    }
};