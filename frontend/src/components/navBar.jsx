import { useState } from "react"
import axios from "axios"

const NavBar = props => {
    const [loginForm, setLoginForm] = useState({
        email: "",
        password: ""
    });

    const onChangeHandler = (e) =>{
        const {value, name} = e.target
        setLoginForm( prevData => ({
            ...prevData, [name]:value
        }))
    }

    const login = (e) => {
        e.preventDefault();
        console.log("logging in...");
        axios({
            method: "POST",
            url: "http://localhost:5500/api/token",
            data: {
                email: loginForm.email,
                password: loginForm.password
            }
        })
        .then((res) => {
            console.log(res);
            props.setToken(res.data.access_token)
        })
        .catch((err) => {
            console.log(err);
        })
        
        setLoginForm(({
            email: "",
            password: ""
        }))
    }

    const logout = () => {
        props.removeToken()
    }

    return(
        <div className="nav-bar">
            <h1>Welcome To JCR Labs</h1>

            {!props.token ? 

            <form className="login">
                <input 
                    onChange={onChangeHandler}
                    type="email" 
                    text={loginForm.email}
                    name="email"
                    placeholder="Email"
                    value={loginForm.email}
                />
                <input 
                    onChange={onChangeHandler}
                    type="password" 
                    text={loginForm.password}
                    name="password"
                    placeholder="Password"
                    value={loginForm.password}
                />
                <button onClick={login}>Submit</button>
            </form>

            : (
                <button onClick={logout}>Logout</button>
            )}

        </div>
    )
}

export default NavBar