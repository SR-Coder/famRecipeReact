
import './App.css';
import React from 'react';
import {BrowserRouter, Route, Routes} from 'react-router-dom'
// import TestFunctionComp from './components/test';
import useToken from './components/useToken';
import Login from './components/Login';
import Header from './components/Header';
import Profile from './components/Profile';

function App() {
  const { token, removeToken, setToken } = useToken();
  return (
    <BrowserRouter>
      <div className="App">
        {/* <Header token={removeToken} />
        {!token && token!=="" &&token!== undefined?  
        <Login setToken={setToken} />
        :(
          <>
            <Routes>
              <Route exact path="/profile" element={<Profile token={token} setToken={setToken}/>}></Route>
            </Routes>
          </>
        )} */}
      </div>
    </BrowserRouter>
  );
}

export default App;
