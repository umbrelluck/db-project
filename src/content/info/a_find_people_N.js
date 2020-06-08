import React from 'react'
import GO from '../GO'
import axios from 'axios'

import Result from '../result'
import { Route } from 'react-router-dom'

export default class AFindNPeople extends React.Component {
    constructor(props) {
        super(props);
        this.lst = []
    }

    async register(list, alien, number, st_date, end_date) {
        console.log(list, alien, number, st_date, end_date);
        const response = await axios.get('/get_select_alien_kidnapping', {
            params: {
                alien_name: alien,
                n_times: number,
                date_from: st_date,
                date_to: end_date
            }
        });
        console.log("response = ", response)
        this.lst.push(response.data.result);
    }

    handler = () => {
        var res = []
        var cnt = 0
        for (var elem of document.getElementsByTagName('input')) {
            console.log(elem)
            if (cnt !== 1)
                res.push(elem.value)
            else
                res.push(Number(elem.value))
            cnt++;
        }
        console.log(this.lst, res);
        this.register(this.lst, res[0], res[1], res[2], res[3]);
    }


    render() {
        if (this.lst.length > 1)
            this.lst = this.lst.splice(1, 2)
        // var url = this.props.match.url.substring(0, this.props.match.url.length - 3);
        var url = this.props.match.url;
        return (
            <div className="data_input">
                <input placeholder="Alien"></input>
                <input placeholder='Number'></input>
                <input placeholder='Start date (mnth-day-year)'></input>
                <input placeholder='End date (mnth-day-year)'></input>
                <GO fun={this.handler} url={url}></GO>
                <Route path={this.props.match.url + '/result'} render={() => (<Result info={this.lst} />)} />
            </div>
        )
    }
};