import React from 'react'
import GO from '../GO'
import axios from 'axios'

import Result from '../result'
import { Route } from 'react-router-dom'

export default class ViewTable extends React.Component {
    // TODO register

    async register(list, table) {
        console.log(list, table);
        // def human_escapes_from_the_ship(conn, date, id_ship_from, id_human):
        const response = await axios.get('/get_select_aliens_kidnapping', {
            params: {
                table: table
            }
        });
        console.log("response = ", response)
        this.lst.push(response.data.result);
    }

    handler = () => {
        var select = document.getElementById('tables');
        var table = select.options[select.selectedIndex].value
        console.log(this.lst, table);
        this.register(this.lst, table);
    }

    render() {
        // var url = this.props.match.url.substring(0, this.props.match.url.length - 3);
        var url = this.props.match.url;
        return (
            <div className="data_input">
                <select id="tables">
                    <option value="human">Human</option>
                    <option value="alien">Alien</option>
                    <option value="ship">Ship</option>
                    <option value="experiment">Experiment</option>
                    <option value="excursion">Excursion</option>
                </select>
                <GO fun={this.handler} url={url}></GO>
                <Route path={this.props.match.url + '/result'} render={() => (<Result info={new Array(new Array("Data sent"))} />)} />
            </div>
        )
    }
};