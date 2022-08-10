import React, {useState } from "react";
import axios from "axios"

function Login(props) {
    const [ loginForm, setLoginForm] = useState({
        email: "",
        password: ""
    })

    function logUserIn(event){
        axios({
            method: "POST",
            url:"http://localhost:5500/api/token",
            data:{
                email: loginForm.email,
                password: loginForm.password
            }
        })
        .then(( response ) => {
            props.setToken(response.data.access_token)
        }).catch((err) => {
            if (err.response) {
                console.log(err.response);
                console.log(err.response.status);
                console.log(err.response.headers);
            }
        })

        setLoginForm(({
            email:"",
            password:""
        }))

        event.preventDefault()
    }

    function handleChange(event) {
        const { value, name } = event.target
        setLoginForm(prevNote => ({
            ...prevNote, [name]: value})
            
    )}

    return (
        <div>
            <h1>Login</h1>
            <form className="login">
                <input
                    onChange={handleChange}
                    type="email" 
                    text={loginForm.email}
                    name="email"
                    placeholder="Email"
                    value={loginForm.email}
                />
                <input 
                    onChange={handleChange}
                    type="password" 
                    text={loginForm.password}
                    name="password"
                    placeholder="Password"
                    value={loginForm.password}
                />

                <button onClick={logUserIn}>Submit</button>
            </form>
        </div>
    );

}

export default Login;