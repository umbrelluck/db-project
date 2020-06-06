import React from 'react'
import { NavLink } from 'react-router-dom'

var GO = ({ url, fun }) => (
    <NavLink to={url + '/result'}>
        <button className="go" onClick={fun}>GO</button>
    </NavLink>
)
export default GO;