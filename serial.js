fetch('serial.txt').then(response => response.text()).then(serial => {
document.getElementById("serial").innerHTML = serial
});