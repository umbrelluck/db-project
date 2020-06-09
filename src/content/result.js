import React from 'react'

export default class Result extends React.Component {

    render() {
        var text = (<p>No data found on your query</p>)
        try {
            if (this.props.info.length !== 0)
                if (this.props.info[0].length !== 0) {
                    text = this.props.info.map((item, id) => (<p key={id}>{item.join(", ")}</p>))
                    // text = this.props.info.map(item => item.join(", "))
                    // text = text.map(item => "<p>"+item+"</p>")
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
            (this.props.info.length !== 0) ? <div className="result">
                {text}
            </div>
                : <div className="result">
                    <p>Getting info on your query...<br /> Please press "GO" button in a second...</p>
                </div>
        )
    }
}