import React, { Component } from 'react';
import axios from 'axios';


class App extends Component {

  state = {
    todos: []
  }

  // Ensure API call is made at correct time during the React lifecycle
  componentDidMount() {
    this.getTodos();
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
