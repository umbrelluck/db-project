import React from 'react';
import { Switch, Route, BrowserRouter } from 'react-router-dom'
import Login from './login'
import Alien from './alien'
import Human from './human'

export default class Content extends React.Component {
    render() {
        return (
            <div id="content">
                <Login />
                <Switch>
                    {/* <BrowserRouter> */}
                    <Route path='/alien' component={Alien} />
                    <Route path='/human' component={Human} />
                </Switch>
                {/* </BrowserRouter> */}
            </div >
        )
    }
}