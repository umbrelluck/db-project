import React from 'react'
import { Route } from 'react-router-dom'
import axios from 'axios'

import Result from '../../result'
import GO from '../../GO'

export default class Excursion extends React.Component {
    constructor() {
        super()
        this.state = {
            info: []
        }
    }

    async register(id_excursion, id_human) {
        console.log(id_excursion, id_human);
        const response = await axios.get('/get_add_human_to_excursion', {
            params: {
                id_excursion: id_excursion,
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
        var fl = true
        for (var elem of document.getElementsByTagName('input')) {
            console.log(elem)
            if (elem.value === "") {
                fl = false
                break
            }
            res.push(Number(elem.value))
        }
        console.log(res);
        if (fl)
            this.register(res[0], res[1]);
        else
            this.setState(state => ({
                info: new Array(new Array("Invalid input"))
            }))
    }


    render() {
        var url = this.props.url;
        var text = (<p>No data found on your query</p>)
        try {
            if (this.props.info.length !== 0)
                if (this.props.info[0].length !== 0) {
                    text = this.props.info.map((item, id) => (<p key={id}>{item.join(", ")}</p>))
                }
            console.log("text is ", text)
        } catch {
            if (this.props.info.length === 0)
                text = (<p>Can not connect to database server<br />142.93.163.88 seems to be down</p>)
            else
                text = (<p>{this.props.info}</p>)
            console.log("error: ", this.props.info)
        }
        return (
            (this.props.info.length !== 0) ?
                (this.state.info.length !== 0) ?
                    (this.info !== "Invalid input") ?
                        <div className="result">
                            {text}
                            <p>Now, add a human</p>
                            <input placeholder="Excursion ID"></input>
                            <input placeholder="Human ID"></input>
                            <GO fun={this.handler} url={url}></GO>
                            <Route path={url + '/result'} render={() => (<Result info={this.state.info} />)} />
                        </div>
                        : <div className="result">
                            {text}
                        </div>
                    : (this.info !== "Invalid input") ?
                        <div className="result">
                            {text}
                            <p>Now, add a human</p>
                            <input placeholder="Excursion ID"></input>
                            <input placeholder="Human ID"></input>
                            <GO fun={this.handler} url={url}></GO>
                        </div>
                        : <div className="result">
                            {text}
                        </div>

                : <div className="result">
                    <p>Getting info on your query...<br /> Please press "GO" button in a second...</p>
                </div>
        )
    }
}