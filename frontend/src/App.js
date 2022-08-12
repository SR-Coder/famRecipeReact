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
      <div className='main-body'>
        
      </div>

      <FetchData />
      <p> {token} </p>

    </div>
  );
}

export default App;
