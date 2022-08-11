import logo from './logo.svg';
import './App.css';

// import components 
import FetchData from './components/fetchData';
import NavBar from './components/navBar';
import UseToken from './components/useToken';

function App() {
  const {token, removeToken, setToken} = UseToken()
  return (
    <div className="App">
      <NavBar setToken={setToken} token={token} removeToken={removeToken}/>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
      <FetchData />
      <p> {token} </p>
      </header>
    </div>
  );
}

export default App;
