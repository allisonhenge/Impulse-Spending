import React from 'react';
import { CustInputPage } from './components/customerInput'
import './App.css'

function App() {
  return (
    <div className="App">
      <div className="headerCont">
        <div className= "title" >Prospective Client Information</div>
      </div>
      <div className="body">
        <CustInputPage/>
      </div>
    </div>
  );
}

export default App;
