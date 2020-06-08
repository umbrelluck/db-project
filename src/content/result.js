import React from 'react'

export default class Result extends React.Component {
    render() {
        return (
            (this.props.info.length != 0) ? <div className="result">
                <p>{this.props.info.join(", ")}</p>
            </div>
                : <div className="result">
                    <p>Getting result... Please press "GO" button in a second...</p>
                </div>
        )
    }
}