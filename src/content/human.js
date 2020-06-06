import React from 'react'
import { NavLink, Route } from 'react-router-dom'

import Hescape from './events/h_escape'
import HKill from './events/h_kill'

import Result from './result'

export default class Human extends React.Component {
    render() {
        // console.log(this.props.match)
        return (
            <div id="human">
                <h3>Сектор двоногих</h3>
                <ul className='ul_events_info'>
                    <p>Доступна інформація</p>
                    <li><NavLink to={this.props.match.url + '/i1'}>Для людини H знайти усi кораблi, де вона побувала за вказаний перiод</NavLink></li>
                    <li><NavLink to={this.props.match.url + '/i2'}>Для людини H знайти усiх прибульцiв, якi викрадали її хоча б N разiв за вказаний перiод</NavLink></li>
                    <li><NavLink to={this.props.match.url + '/i3'}>Для людини H знайти усiх прибульцiв, яких вона вбила за вказаний перiод </NavLink></li>
                    <li><NavLink to={this.props.match.url + '/i4'}>Для людини H знайти усiх прибульцiв, якi викрадали її та були вбитi нею ж</NavLink></li >
                    <li><NavLink to={this.props.match.url + '/i5'}>Знайти усiх людей, яких викрадали хоча б N разiв за вказаний перiод (з дати F по дату T)</NavLink></li >
                    <li><NavLink to={this.props.match.url + '/i6'}>Для людини H та кожного експерименту, у якому вона брала участь, знайти скiльки разiв за вказаний перiод (з дати F по дату T) експеримент над нею проводили щонайменше N прибульцiв</NavLink></li >
                    <li><NavLink to={this.props.match.url + '/i7'}>Знайти сумарну кiлькiсть викрадень по мiсяцях</NavLink></li >
                </ul>

                <ul className='ul_events_info'>
                    <p>Доступні дії</p>
                    <li><NavLink to={this.props.match.url + '/e1'}>Втекти з космічного корабля</NavLink></li>
                    <li><NavLink to={this.props.match.url + '/e2'}>Вбити поневолювача</NavLink></li>
                </ul>

                {/* <NavLink to={this.props.match.url + '/result'}>
                    <button >GO</button>
                </NavLink> */}

                <Route path={this.props.match.url + '/e1'} component={Hescape} />
                <Route path={this.props.match.url + '/e2'} component={HKill} />

                {/* <Route path={this.props.match.url + '/result'} component={Result} /> */}
            </div >
        )
    }
}