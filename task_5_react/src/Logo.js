import React, { Component } from 'react';
import './style.css';


class Logo extends Component {
  render() {
    return (
        <div className="container-fluid">
            <div className="row backgroundImage" >
                <img src={require("./imgs/logo.png")} className="center-block" alt="ACES logo"/>
            </div>
        </div>
    );
  }
}
export default Logo;