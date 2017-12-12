import React, { Component } from 'react';
import { Menu } from 'antd';
import 'antd/dist/antd.css';


class Navbar extends Component {
  render() {
    return (
        <Menu mode="horizontal" selectedKeys="home">
            <Menu.Item key="home" className="center-block">Home</Menu.Item>
            <Menu.Item>Events</Menu.Item>
            <Menu.Item>Tracks</Menu.Item>
            <Menu.Item>Gallery</Menu.Item>
        </Menu>
    );
  }
}
export default Navbar;