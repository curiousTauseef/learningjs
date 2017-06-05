var React = require('react');


module.exports = React.createClass({
  _handleClick: function(){
    alert('You just obeyed me? :P');
  },
  render: function() {
    return (
      <html>
        <head>
          <title>{!this.props.title?'YO YO':this.props.title}</title>
          <link rel='stylesheet' href='/style.css' />
        </head>
        <body>
          <div>
            <h1> Hello World, by{this.props.title}</h1>
            <p>Bla bla bla</p>
            <button  onClick={this._handleClick}>Click karo abhi!</button>
          </div>
          <script src='/bundle.js'
          data-props={JSON.stringify(this.props)}
          id='props' />
        </body>
      </html>

    );
  }
});
