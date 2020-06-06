import React from 'react';
import { BrowserRouter } from 'react-router-dom'
import Content from './content/content';
import Footer from './content/footer';
import { browserHistory } from 'react-router-dom'

import './content/db.css'


function App() {
  return (
    <BrowserRouter  >
      <Content />
      <Footer />
    </BrowserRouter>
  );
}

export default App;
