import React from 'react'
import GO from '../GO'
import axios from 'axios'

import Result from '../result'
import { Route } from 'react-router-dom'

export default class HStolenAndMurdered extends React.Component {
    constructor(props) {
        super(props);
        this.lst = []
    }

    async register(list, human) {
        console.log(list, human);
        const response = await axios.get('/get_select_human_revenge', {
            params: {
                human_id: human,
            }
        });
        console.log("response = ", response)
        this.lst.push(response.data.result);
    }

    handler = () => {
        var res = []
        for (var elem of document.getElementsByTagName('input')) {
            console.log(elem)
            res.push(Number(elem.value))
        }
        console.log(this.lst, res);
        this.register(this.lst, res[0]);
    }


    render() {
        if (this.lst.length > 1)
            this.lst = this.lst.splice(1, 2)
        // var url = this.props.match.url.substring(0, this.props.match.url.length - 3);
        var url = this.props.match.url;
        return (
            <div className="data_input">
                <input placeholder="Human ID"></input>
                <GO fun={this.handler} url={url}></GO>
                <Route path={this.props.match.url + '/result'} render={() => (<Result info={this.lst} />)} />
            </div>
        )
    }
};