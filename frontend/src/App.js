import React, { Component } from 'react';
import axios from 'axios';


class App extends Component {
  state = {
    todos: []
  }

  render() {
    return (
      <div>
        {this.state.list.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <p>{item.body}</p>
          </div>
        ))}
      </div>
    );
  }
}



export default App;
