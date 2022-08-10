import React, { useState } from "react";
import axios from "axios";

function Profile(props){

    const [profileData, setProfileData] = useState(null)

    function getData() {
        axios({
            method:"GET",
            url:"/profile",
            headers: {
                Authorization: 'Bearer ' + props.token
            }
        })
        .then((response) => {
            const res = response.data
            res.access_token && props.setToken(res.access_token)
            setProfileData(({
                profile_name: res.name,
                about_me: res.about}))

        }).catch((error) => {
            if (error.response) {
                console.log(error.response);
                console.log(error.response.status);
                console.log(error.response.headers);
            }
        })}

    return (
        <div className="Profile">
            <p>To get your profile details: </p> <button onClick={getData}>Click Me</button>
            {
                profileData && <div>
                    <p>Profile Name: {profileData.profile_name}</p>
                    <p>About Me: {profileData.about_me}</p>
                </div>
            }
        </div>
    );

}

export default Profile