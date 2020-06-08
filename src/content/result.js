import React from 'react'

export default class Result extends React.Component {

    render() {
        var text = "No data found on your query"
        if (this.props.info.length !== 0)
            if (this.props.info[0].length !== 0)
                text = this.props.info.join(", ")
        return (
            (this.props.info.length !== 0) ? <div className="result">
                <p>{text}</p>
            </div>
                : <div className="result">
                    <p>Getting info on your query...<br /> Please press "GO" button in a second...</p>
                </div>
        )
    }
}