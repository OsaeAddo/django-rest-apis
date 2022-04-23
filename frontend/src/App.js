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


  // Make GET requests to the Todos API with axios
  getTodos() {
    axios
      .get('http://127.0.0.1:8000/api/todo/')

      .then(res => {
        this.setState({ todos: res.data }); //put the retrieved API data into the todos list
      })

      .catch(err => {
        console.log(err);
      })
  }

  render() {
    return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.body}</span>
          </div>
        ))}
      </div>
    );
  }
}



export default App;
