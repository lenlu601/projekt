// handleSubmit je funkcia, ktorá sa spustí keď sa bude mať odoslať náš formulár
function handleSubmit(e) {
	if (e) e.preventDefault(); // zabrániť vstavenému odosielaniu v prehliadači

	const form = document.querySelector("form");
	const ves = document.querySelector("#mojEditor").value; // Načítame text z textarea
	const width = document.querySelector("section:nth-child(2)").clientWidth; // Načítame aktuálnu šírku výstupného okna

	const formular = new URLSearchParams(); // Vytvoríme štruktúru, ktorá bude reprezentovať formulár
	formular.append('ves', ves); // Pridáme tam naše hodnoty
	formular.append('width', width);

	const url = form.action; // Nacitame povodnu URL zadanu vo formulari
	const method = form.method; // Nacitame povodnu metodu zadanu vo formulari

	fetch(url, { method: method, body: formular }) // Urobíme HTTP požiadavku na náš server POST /render
		.then(async (res) => {
			if (!res.ok) throw new Error(await res.text());
			return res.blob();
		})
		.then((image) => {
			document.querySelector("#output").src = URL.createObjectURL(image); // Nastavíme src našeho <img>
		})
		.catch((err) => {
			console.error("Chyba pri generovaní:", err.message);
		});
}

document.querySelector("form").addEventListener("submit", handleSubmit);

// Znovuzrodená funkcia na vloženie textu do editora pri kliknutí na tlačidlá
window.pridajText = function (obsah) {
	var pole = document.getElementById('mojEditor');
	if (!pole) return;

	var start = pole.selectionStart;
	var koniec = pole.selectionEnd;
	var staryText = pole.value;

	// Vložíme text
	pole.value = staryText.substring(0, start) + obsah + staryText.substring(koniec);

	// Nastavíme kurzor
	pole.focus();
	pole.selectionStart = pole.selectionEnd = start + obsah.length;

	// Spustí sa live preview
	pole.dispatchEvent(new Event('input', { bubbles: true }));
};

// Automatické generovanie pri písaní (live preview s oneskorením)
let timeout = null;
document.querySelector("#mojEditor").addEventListener("input", function () {
	clearTimeout(timeout);
	timeout = setTimeout(() => {
		handleSubmit();
	}, 400); // 400ms po zastavení písania
});

// Vygeneruje obrázok po prvom načítaní stránky
setTimeout(() => handleSubmit(), 100);