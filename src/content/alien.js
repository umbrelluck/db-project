import React from 'react'
import { NavLink, Route } from 'react-router-dom'

import Aexcursion from './events/a_excursion'
import Aexperiment from './events/a_experiment'
import Akidnap from './events/a_kidnap'
import Atransport from './events/a_transport'

import Result from './result'

export default class Alien extends React.Component {
    render() {
        return (
            <div id="alien">
                <h3>Сектор чужих</h3>
                <ul className='ul_events_info'>
                    <p>Доступна інформація</p>
                    <li><NavLink to={this.props.match.url + '/i1'}>Для прибульця A знайти усiх людей, яких вiн викрадав хоча б N разiв за вказаний перiод</NavLink></li>
                    <li><NavLink to={this.props.match.url + '/i2'}>Знайти усiх прибульцiв якi викрали щонайменше N рiзних людей за вказаний перiод</NavLink></li>
                    <li><NavLink to={this.props.match.url + '/i3'}>Знайти усi спiльнi екскурсiї та експерименти для прибульця A та людини H за вказаний період</NavLink></li>
                    <li><NavLink to={this.props.match.url + '/i4'}>Для прибульця A та кожної екскурсiї, яку вiн проводив, знайти скiльки разiв за вказаний перiод (з дати F по дату T) вiн проводив екскурсiю для щонайменше N людей</NavLink></li>
                    <li><NavLink to={this.props.match.url + '/i5'}>Вивести кораблi у порядку спадання сумарної кiлькостi еспериментiв, що були проведенi на кораблi за участi даного прибульця A протягом вказаного перiоду (з дати F по дату T)</NavLink></li>
                </ul>

                <ul className='ul_events_info'>
                    <p>Доступні дії</p>
                    <li><NavLink to={this.props.match.url + '/e1'}>Викрасти людину</NavLink></li>
                    <li><NavLink to={this.props.match.url + '/e2'}>Транспортувати людину на інший корабель</NavLink></li>
                    <li><NavLink to={this.props.match.url + '/e3'}>Провести експеримент</NavLink></li>
                    <li><NavLink to={this.props.match.url + '/e4'}>Провести екскурсію</NavLink></li>
                </ul>

                <Route path={this.props.match.url + '/e1'} component={Akidnap} />
                <Route path={this.props.match.url + '/e2'} component={Atransport} />
                <Route path={this.props.match.url + '/e3'} component={Aexperiment} />
                <Route path={this.props.match.url + '/e4'} component={Aexcursion} />

                {/* <NavLink to={this.props.match.url + '/result'}>
                    <button >GO</button>
                </NavLink> */}

                {/* <Route path={this.props.match.url + '/result'} component={Result} /> */}
            </div>
        )
    }
}