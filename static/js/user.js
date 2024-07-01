const ip=sessionStorage.getItem("ip")

console.log(ip);


async function getUserIPAddress() {
    let ipAddress = sessionStorage.getItem('ip');
    if (!ipAddress) {
        const response = await fetch('https://api.ipify.org?format=json');
        const data = await response.json();
        ipAddress = data.ip;
        sessionStorage.setItem('ip', ipAddress);
    }
    return ipAddress;
}


async function getLocationFromIP(ipAddress) {
    const response = await fetch(`https://ipapi.co/${ipAddress}/json/`);
    const data = await response.json();
    return data;
}



async function fetchUserLocation() {
    try {
        const ipAddress = await getUserIPAddress();
        const locationData = await getLocationFromIP(ipAddress);
        console.log(locationData); // Handle location data as needed
    } catch (error) {
        console.error('Error fetching location:', error);
    }
}

fetchUserLocation();