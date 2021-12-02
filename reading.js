fetch('reading.txt').then(response => response.text()).then(temperature => {
    document.getElementById("temperature").innerHTML = temperature
    });