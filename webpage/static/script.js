let vacaciones = [
    ["1 año", 12],
    ["2 años", 14],
    ["3 años", 16],
    ["4 años", 18],
    ["5 años", 20],
    ["6 a 10 años", 22],
    ["11 a 15 años", 24],
    ["16 a 20 años", 26],
    ["21 a 25 años", 28],
    ["26 a 30 años", 30],
    ["31 a 35 años", 32],
]
vacaciones.forEach(element => {
    let tableBody = document.getElementById('tabla-vacaciones');
    let tableRow = document.createElement('tr');
    let rowData = `<td>${element[0]}</td><td>${element[1]}</td>`
    tableRow.innerHTML=rowData
    tableBody.appendChild(tableRow)
});

