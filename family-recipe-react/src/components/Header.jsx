import axios from "axios";
import React  from 'react';

function Header(props) {
    
    function logUserOut() {
        axios({
            method: "POST",
            url:"/api/logout",
        })
        .then((response) => {
            props.token()
        }).catch((error) => {
            if (error.response){
                console.log(error.response);
                console.log(error.response.status);
                console.log(error.response.headers);
            }
        })}

    return(
        <header className="App-header">
            <button onClick={logUserOut}>
                Logout
            </button>
        </header>
    )
}

export default Header;