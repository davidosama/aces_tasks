import React, { Component } from 'react';
import { Row, Col } from 'antd';
import 'antd/dist/antd.css';
import './style.css';
import Logo from './Logo.js';
import Navbar from './Navbar.js';


class App extends Component {
  render() {
    return (
      <div>
        <div className="height">
          <Logo/>
          <Navbar/>
        </div>
        <div className="height">
          <Row>
            <Col span={24}>
             <img src={require("./imgs/mainevent.png")} width="100%" alt="mainevent"/>
            </Col>
          </Row>
        </div>
        <div className="height">
          <Row>
            <Col span={12}><img src={require("./imgs/acg.png")} width="100%" alt="acg"/></Col>
            <Col span={12}><img src={require("./imgs/timeline.png")} width="100%" alt="timeline"/></Col>
          </Row>
        </div>
      </div>
    );
  }
}

export default App;
