import React from 'react'
import GO from '../GO'
import axios from 'axios'

import Result from '../result'
import { Route } from 'react-router-dom'

export default class HFindMurders extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            info: []
        }
        this.lst = []
    }

    async register(list, human, st_date, end_date) {
        console.log(list, human, st_date, end_date);
        const response = await axios.get('/get_select_human_murder', {
            params: {
                human_first_name: human,
                date_from: st_date,
                date_to: end_date
            }
        });
        console.log("response = ", response)
        // this.lst.push(response.data.result);
        this.setState((state) => ({
            info: response.data.result
        }))
    }

    handler = () => {
        var fl = true
        var res = []
        for (var elem of document.getElementsByTagName('input')) {
            console.log(elem)
            if (elem.value === "") {
                fl = false
                break
            }
            res.push(elem.value)
        }
        console.log(this.lst, res);
        if (fl)
            this.register(this.lst, res[0], res[1], res[2]);
        else
            this.setState(state => ({
                info: new Array(new Array("Invalid input"))
            }))
    }


    render() {
        // if (this.lst.length > 1)
        //     this.lst = this.lst.splice(1, 2)
        // var url = this.props.match.url.substring(0, this.props.match.url.length - 3);
        var url = this.props.match.url;
        return (
            (this.state.info.length !== 0) ? <div className="data_input">
                <input placeholder="Human"></input>
                <input placeholder='Start date (mnth-day-year)'></input>
                <input placeholder='End date (mnth-day-year)'></input>
                <GO fun={this.handler} url={url}></GO>
                <Route path={this.props.match.url + '/result'} render={() => (<Result info={this.state.info} />)} />
            </div> :
                <div className="data_input">
                    <input placeholder="Human"></input>
                    <input placeholder='Start date (mnth-day-year)'></input>
                    <input placeholder='End date (mnth-day-year)'></input>
                    <GO fun={this.handler} url={url}></GO>
                </div>
        )
    }
};