function stlacenie() {
let vyska = document.querySelector("input[name=vyska]").value
let vaha = document.querySelector("input[name=vaha]").value
const nadvaha = vaha - (vyska-100);

document.querySelector("#vystup").innerText = nadvaha;
}