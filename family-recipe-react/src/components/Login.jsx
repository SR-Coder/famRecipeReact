import { useState } from "react";
import axios from "axios"

function Login(props) {
    const [ loginForm, setLoginForm] = useState({
        email: "",
        password: ""
    })

    function logUserIn(event){
        axios({
            method: "POST",
            url:"/token",
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
                
            </form>
        </div>
    );

}

export default Login;