const form = document.querySelector("#renderForm");
const textarea = document.querySelector("#vesInput");
const outputImage = document.querySelector("#output");
const statusMessage = document.querySelector("#statusMessage");
let currentImageUrl = null;

async function handleSubmit(event) {
  event.preventDefault();

  const ves = textarea.value.trim();
  if (!ves) {
    statusMessage.textContent = "Najprv vložte alebo vyberte obsah VES súboru.";
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

  statusMessage.textContent = "Renderujem obrázok...";

  try {
    const response = await fetch(form.action, {
      method: form.method,
      body: formData
    });

    if (!response.ok) {
      const message = await response.text();
      throw new Error(message || "Nepodarilo sa vyrenderovať obrázok.");
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
    statusMessage.textContent = error.message;
  }
}

async function loadSample(name) {
  statusMessage.textContent = `Načítavam ukážku ${name.toUpperCase()}...`;

  try {
    const response = await fetch(`/sample/${name}`);
    if (!response.ok) {
      const message = await response.text();
      throw new Error(message || "Ukážku sa nepodarilo načítať.");
    }

    textarea.value = await response.text();
    statusMessage.textContent = `Ukážka ${name.toUpperCase()} je pripravená na zobrazenie.`;
  } catch (error) {
    statusMessage.textContent = error.message;
  }
}

form.addEventListener("submit", handleSubmit);

document.querySelectorAll(".sample").forEach((button) => {
  button.addEventListener("click", () => loadSample(button.dataset.sample));
});
