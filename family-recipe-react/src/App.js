import logo from './logo.svg';
import './App.css';
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import TestFunctionComp from './components/test';
import useToken from './components/useToken';

function App() {
  const { token, removeToken, setToken } = useToken();
  return (
    <BrowserRouter>
      <div className="App">
          
        <TestFunctionComp />
      </div>
    </BrowserRouter>
  );
}

export default App;
