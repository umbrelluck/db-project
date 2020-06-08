import React from 'react'
import GO from '../GO'
import axios from 'axios'

import Result from '../result'
import { Route } from 'react-router-dom'

export default class HTotal extends React.Component {
    constructor(props) {
        super(props);
        this.lst = []
    }

    async register(list, year) {
        console.log(list, year);
        const response = await axios.get('http://localhost:5000/get_select_all_kidnappings', {
            params: {
                year: year
            }
        });
        console.log("response = ", response)
        this.lst.push(response.data.result);
    }

    handler = () => {
        var res = []
        for (var elem of document.getElementsByTagName('input')) {
            console.log(elem)
            res.push(elem.value)
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
                <input placeholder="Year"></input>
                <GO fun={this.handler} url={url}></GO>
                <Route path={this.props.match.url + '/result'} render={() => (<Result info={this.lst} />)} />
            </div>
        )
    }
};