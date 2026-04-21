const SAMPLE_CONTENTS = {
  vianoce: `VES v1.0 800 600
CLEAR #001133

# --- Mesiac a Hviezdy (Pozadie) ---
FILL_CIRCLE 700 80 50 #FDFD96
FILL_CIRCLE 720 90 10 #ECEC80
FILL_CIRCLE 690 70 6 #ECEC80

# Hviezdy
FILL_CIRCLE 100 50 2 #FFFFFF
FILL_CIRCLE 250 120 2 #FFFFFF
FILL_CIRCLE 400 30 3 #FFFFFF
FILL_CIRCLE 50 200 2 #FFFFFF
FILL_CIRCLE 550 60 2 #FFFFFF
FILL_CIRCLE 300 300 2 #FFFFFF
FILL_CIRCLE 150 150 1 #FFFFFF

# Sneh
FILL_RECT 0 450 800 150 #F0F8FF

# Domcek
FILL_RECT 50 300 200 150 #8B0000
RECT 50 300 200 150 3 #2F0000
FILL_TRIANGLE 30 300 150 180 270 300 #333333
TRIANGLE 30 300 150 180 270 300 3 #000000
FILL_RECT 180 220 30 60 #552200
RECT 180 220 30 60 2 #000000
FILL_RECT 120 370 60 80 #654321
RECT 120 370 60 80 2 #331100
FILL_CIRCLE 170 410 4 #FFD700
FILL_RECT 70 330 40 40 #FFFFE0
RECT 70 330 40 40 3 #654321
LINE 90 330 90 370 2 #654321
LINE 70 350 110 350 2 #654321

# Stromcek
FILL_RECT 580 450 40 50 #3E2723
FILL_TRIANGLE 480 450 720 450 600 300 #006400
FILL_TRIANGLE 500 350 700 350 600 220 #008000
FILL_TRIANGLE 530 250 670 250 600 150 #228B22
FILL_TRIANGLE 600 130 585 160 615 160 #FFD700
FILL_TRIANGLE 600 170 585 145 615 145 #FFD700
FILL_CIRCLE 550 400 10 #FF0000
FILL_CIRCLE 650 410 10 #0000FF
FILL_CIRCLE 600 380 10 #FFD700
FILL_CIRCLE 580 300 9 #800080
FILL_CIRCLE 620 300 9 #FFA500
FILL_CIRCLE 600 200 8 #FF0000
LINE 530 380 600 400 3 #C0C0C0
LINE 600 400 670 380 3 #C0C0C0
LINE 550 280 600 300 3 #FFD700
LINE 600 300 650 280 3 #FFD700

# Snehuliak
FILL_CIRCLE 350 480 45 #FAFAFA
CIRCLE 350 480 45 1 #CCCCCC
FILL_CIRCLE 350 420 35 #FAFAFA
CIRCLE 350 420 35 1 #CCCCCC
FILL_CIRCLE 350 370 25 #FAFAFA
CIRCLE 350 370 25 1 #CCCCCC
FILL_RECT 330 355 40 5 #000000
FILL_RECT 335 325 30 30 #000000
FILL_CIRCLE 342 365 3 #000000
FILL_CIRCLE 358 365 3 #000000
FILL_CIRCLE 350 410 3 #000000
FILL_CIRCLE 350 430 3 #000000
FILL_CIRCLE 350 480 3 #000000
FILL_TRIANGLE 350 370 350 376 375 373 #FF8C00
LINE 315 420 280 400 2 #5D4037
LINE 385 420 420 400 2 #5D4037

# Darcek
FILL_RECT 680 480 50 50 #FF1493
FILL_RECT 702 480 6 50 #FFFF00
FILL_RECT 680 502 50 6 #FFFF00
LINE 705 480 690 470 3 #FFFF00
LINE 705 480 720 470 3 #FFFF00

# Ram
RECT 0 0 799 599 10 #FFFFFF`,
  zatisie: `VES v1.0 800 600
CLEAR #FCF7CF

# Tapeta
FILL_RECT 0 0 100 470 #F46058
FILL_RECT 100 0 200 470 #F3A449
FILL_RECT 200 0 300 470 #F46058
FILL_RECT 300 0 400 470 #F3A449
FILL_RECT 400 0 500 470 #F46058
FILL_RECT 500 0 600 470 #F3A449
FILL_RECT 600 0 700 470 #F46058
FILL_RECT 700 0 800 470 #F3A449
LINE 0 470 800 470 1 #000000
LINE 0 485 800 485 1 #000000

# Stol
FILL_RECT 75 500 475 25 #A55022
FILL_RECT 100 525 425 25 #A55022
FILL_RECT 125 550 25 50 #A55022
FILL_RECT 475 550 25 50 #A55022

# Vaza a kvety
FILL_RECT 150 375 75 125 #CA9FDF
LINE 150 275 175 375 1 #2BB418
LINE 188 275 188 375 1 #2BB418
LINE 225 275 200 375 1 #2BB418
FILL_TRIANGLE 138 263 162 263 150 275 #FF8914
FILL_TRIANGLE 138 287 162 287 150 275 #FF8914
FILL_TRIANGLE 138 263 138 287 150 275 #FFE214
FILL_TRIANGLE 162 263 162 287 150 275 #FFE214
FILL_CIRCLE 188 288 12 #3974DB
FILL_CIRCLE 225 275 20 #DA31E3
FILL_CIRCLE 225 275 13 #EBD128

# Obraz
FILL_RECT 375 400 75 100 #954B0E
FILL_RECT 385 410 55 80 #FFFFFF
CIRCLE 413 438 13 1 #000000
FILL_CIRCLE 408 433 2 #000000
FILL_CIRCLE 417 433 2 #000000
LINE 410 443 415 443 1 #000000
LINE 413 450 413 490 1 #000000
LINE 413 460 400 475 1 #000000
LINE 413 460 425 475 1 #000000

# Zrkadlo
FILL_CIRCLE 625 133 88 #FFD700
FILL_CIRCLE 625 133 70 #9BC0D9
FILL_TRIANGLE 600 100 625 75 650 175 #DEFCFA
FILL_TRIANGLE 675 150 625 75 650 175 #DEFCFA
FILL_TRIANGLE 575 125 585 110 625 200 #DEFCFA
FILL_TRIANGLE 640 185 585 110 625 200 #DEFCFA`,
  zralok: `VES v1.0 500 500
CLEAR #0077BE

# Zralok
FILL_TRIANGLE 100 250 400 250 250 180 #708090
FILL_TRIANGLE 100 250 400 250 250 320 #E0E0E0
FILL_TRIANGLE 200 210 280 210 240 120 #708090
FILL_TRIANGLE 100 250 40 180 100 220 #708090
FILL_TRIANGLE 100 250 40 320 100 280 #708090
FILL_TRIANGLE 260 270 320 270 290 330 #708090
FILL_CIRCLE 360 235 5 #000000
LINE 310 230 310 260 2 #2F4F4F
LINE 315 230 315 260 2 #2F4F4F
LINE 320 230 320 260 2 #2F4F4F
LINE 350 270 400 250 2 #2F4F4F

# Detaily
CIRCLE 400 400 8 1 #FFFFFF
CIRCLE 380 430 10 1 #FFFFFF
CIRCLE 380 380 6 1 #FFFFFF
CIRCLE 380 150 4 1 #ADD8E6
CIRCLE 410 100 8 1 #B0E0E6

# Dno
FILL_RECT 0 450 500 50 #C2B280
FILL_TRIANGLE 100 450 130 450 120 380 #2E8B57
FILL_TRIANGLE 450 450 470 450 470 350 #228B22`
};

const form = document.querySelector("#renderForm");
const textarea = document.querySelector("#vesInput");
const outputImage = document.querySelector("#output");
const statusMessage = document.querySelector("#statusMessage");
let currentImageUrl = null;

async function handleSubmit(event) {
  if (event) {
    event.preventDefault();
  }

  const ves = textarea.value.trim();
  if (!ves) {
    statusMessage.textContent = "Najprv vlozte alebo vyberte obsah VES suboru.";
    outputImage.style.display = "none";
    return;
  }

  const previewWidth = Math.max(
    Math.round(document.querySelector(".image-frame").clientWidth - 24),
    200
  );

  const formData = new URLSearchParams();
  formData.append("ves", ves);
  formData.append("width", previewWidth);

  statusMessage.textContent = "Renderujem obrazok...";

  try {
    const response = await fetch(form.action, {
      method: form.method,
      body: formData
    });

    if (!response.ok) {
      const message = await response.text();
      throw new Error(message || "Nepodarilo sa vyrenderovat obrazok.");
    }

    const image = await response.blob();
    if (currentImageUrl) {
      URL.revokeObjectURL(currentImageUrl);
    }

    currentImageUrl = URL.createObjectURL(image);
    outputImage.src = currentImageUrl;
    outputImage.style.display = "block";
    statusMessage.textContent = "Obrázok bol úspešne vyrenderovaný.";
  } catch (error) {
    outputImage.style.display = "none";
    statusMessage.textContent = error.message || "Nastala chyba pri renderovani.";
  }
}

function loadSample(name) {
  const sampleContent = SAMPLE_CONTENTS[name];

  if (!sampleContent) {
    statusMessage.textContent = "Tato ukazka neexistuje.";
    return;
  }

  textarea.value = sampleContent;
  statusMessage.textContent = `Ukazka ${name.toUpperCase()} je nacitana.`;
  handleSubmit();
}

form.addEventListener("submit", handleSubmit);

document.querySelectorAll(".sample").forEach((button) => {
  button.addEventListener("click", () => loadSample(button.dataset.sample));
});
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
