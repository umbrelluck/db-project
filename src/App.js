import React from 'react';
import { BrowserRouter } from 'react-router-dom'
import Content from './content/content';
import { browserHistory } from 'react-router'

import './content/db.css'


function App() {
  return (
    <BrowserRouter>
      <Content />
    </BrowserRouter>
  );
}

export default App;
