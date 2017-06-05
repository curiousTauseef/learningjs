var React = require('react');
var ReactDOM = require('react-dom');
var Component = require('./Component.jsx');

var element = document.getElementById('props');
var props = JSON.parse(element.getAttribute('data-props'));

ReactDOM.render(
  React.createElement(Component, props), document
);
