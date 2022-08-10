import { useEffect, useState } from "react";
import axios from "axios"


const FetchData = props => {
    const [profileData, setProfileData] = useState(null);

    useEffect(() =>{
        axios({
            method:"GET",
            url:"http://localhost:5500/api/profile"
        })
        .then((res) => {
            console.log(res.data);
            setProfileData(res.data.msg)
        })
        .catch((err) =>{
            console.log(err);
        })
    }, []);

    return (
        <div>
            <p>{profileData}</p>
        </div>
    )


}

export default FetchData;