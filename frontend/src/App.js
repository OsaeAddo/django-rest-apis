import React, { Component } from 'react';
import axios from 'axios';

const list = [
  {
    "id": 1,
    "title": "Study for Physics exam",
    "body": "prepare for upcoming physics exam"
  },
  {
      "id": 2,
      "title": "Call prospect",
      "body": "make a business call"
  },
  {
      "id": 3,
      "title": "Visit my bby girl",
      "body": "surprise my girl with a visit"
  }
]

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { list };
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
