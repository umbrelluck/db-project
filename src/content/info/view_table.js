import React from 'react'
import GO from '../GO'
import axios from 'axios'

import Result from '../result'
import { Route } from 'react-router-dom'

export default class ViewTable extends React.Component {
    // TODO register
    constructor() {
        super()
        this.lst = []
        this.state = {
            info: []
        }
    }

    async register(list, table_name) {
        console.log(list, table_name);
        const response = await axios.get("/get_whole_table", {
            params: {
                table_name: table_name
            }
        });
        console.log("response = ", response)
        // this.lst.push(response.data.result);
        this.setState(state => ({
            info: response.data.result
        }))
    }

    handler = () => {
        var select = document.getElementById('tables');
        var table = select.options[select.selectedIndex].value
        console.log(this.lst, table);
        console.log("index", select.selectedIndex)
        this.register(this.lst, table);
    }

    render() {
        // var url = this.props.match.url.substring(0, this.props.match.url.length - 3);
        var url = this.props.match.url;
        return (
            (this.state.info.length !== 0) ? <div className="data_input">
                <select id="tables">
                    <optgroup label="Головні таблиці">
                        <option value="human">Human</option>
                        <option value="alien">Alien</option>
                        <option value="ship">Ship</option>
                        <option value="experiment">Experiment</option>
                        <option value="excursion">Excursion</option>
                        <option value="murder">Murder</option>
                    </optgroup>
                    <optgroup label="Допоміжні таблиці">
                        <option value="human_passenger">Human passenger</option>
                        <option value="alien_passenger">Alien passenger</option>
                        <option value="on_boarding">On boarding</option>
                        <option value="experiment_alien">Experiment alien</option>
                        <option value="excursion_human">Excursion human</option>
                    </optgroup>
                </select>
                <GO fun={this.handler} url={url}></GO>
                <Route path={this.props.match.url + '/result'} render={() => (<Result info={this.state.info} />)} />
            </div> :
                <div className="data_input">
                    <select id="tables">
                        <optgroup label="Головні таблиці">
                            <option value="human">Human</option>
                            <option value="alien">Alien</option>
                            <option value="ship">Ship</option>
                            <option value="experiment">Experiment</option>
                            <option value="excursion">Excursion</option>
                            <option value="murder">Murder</option>
                        </optgroup>
                        <optgroup label="Допоміжні таблиці">
                            <option value="human_passanger">Human passanger</option>
                            <option value="alien_passanger">Alien passanger</option>
                            <option value="on_boarding">On boarding</option>
                            <option value="experiment_alien">Experiment alien</option>
                            <option value="excursion_human">Excursion human</option>
                        </optgroup>
                    </select>
                    <GO fun={this.handler} url={url}></GO>
                </div>
        )
    }
};