const form = document.querySelector("#renderForm");
const textarea = document.querySelector("#vesInput");
const outputImage = document.querySelector("#output");
const statusMessage = document.querySelector("#statusMessage");
const statusBadge = document.querySelector("#statusBadge");
const commandHelp = document.querySelector("#commandHelp");
const widthSlider = document.querySelector("#widthSlider");
const widthInput = document.querySelector("#widthInput");
const clearEditorButton = document.querySelector("#clearEditorButton");
const imagePlaceholder = document.querySelector("#imagePlaceholder");

let currentImageUrl = null;

function isFileProtocol() {
  return window.location.protocol === "file:";
}

function getBackendUrl(path) {
  if (isFileProtocol()) {
    return null;
  }

  return new URL(path, window.location.origin).toString();
}

function clampWidth(value) {
  const parsed = Number.parseInt(value, 10);
  if (Number.isNaN(parsed)) {
    return 960;
  }

  return Math.min(1400, Math.max(240, parsed));
}

function syncWidthInputs(value) {
  const normalized = clampWidth(value);
  widthSlider.value = normalized;
  widthInput.value = normalized;
  return normalized;
}

function setStatus(state, message) {
  statusBadge.className = `status-badge status-${state}`;
  statusMessage.textContent = message;
}

function showPlaceholder() {
  imagePlaceholder.hidden = false;
  outputImage.style.display = "none";
}

function showRenderedImage(src) {
  imagePlaceholder.hidden = true;
  outputImage.src = src;
  outputImage.style.display = "block";
}

async function handleSubmit(event) {
  if (event) {
    event.preventDefault();
  }

  const ves = textarea.value.trim();
  if (!ves) {
    showPlaceholder();
    setStatus("error", "Najprv vloz alebo nacitaj obsah VES suboru.");
    return;
  }

  const renderWidth = syncWidthInputs(widthInput.value);
  const formData = new URLSearchParams();
  formData.append("ves", ves);
  formData.append("width", renderWidth);
  const renderUrl = getBackendUrl(form.action || "/render");

  if (!renderUrl) {
    showPlaceholder();
    setStatus("error", "Frontend je otvoreny ako lokalny subor. Spusti `python gympel\\main.py` a otvor `http://127.0.0.1:5000`.");
    return;
  }

  setStatus("loading", "Renderujem obrazok...");

  try {
    const response = await fetch(renderUrl, {
      method: form.method,
      body: formData
    });

    if (!response.ok) {
      const message = await response.text();
      throw new Error(message || "Renderer vratil chybu.");
    }

    const imageBlob = await response.blob();
    if (currentImageUrl) {
      URL.revokeObjectURL(currentImageUrl);
    }

    currentImageUrl = URL.createObjectURL(imageBlob);
    showRenderedImage(currentImageUrl);
    setStatus("success", `Render hotovy. Siroky vystup: ${renderWidth}px.`);
  } catch (error) {
    showPlaceholder();
    const fallbackMessage = isFileProtocol()
      ? "Frontend je otvoreny bez backendu. Spusti `python gympel\\main.py` a pouzi `http://127.0.0.1:5000`."
      : "Nastala chyba pri renderovani.";
    setStatus("error", error.message || fallbackMessage);
  }
}

async function loadSample(name) {
  setStatus("loading", `Nacitavam vzorku ${name}...`);
  const sampleUrl = getBackendUrl(`/sample/${name}`);

  if (!sampleUrl) {
    setStatus("error", "Vzorky potrebuju Flask backend. Otvor aplikaciu cez `http://127.0.0.1:5000`.");
    return;
  }

  try {
    const response = await fetch(sampleUrl);
    if (!response.ok) {
      throw new Error("Vzorku sa nepodarilo nacitat.");
    }

    const sampleContent = await response.text();
    textarea.value = sampleContent.trim();
    setStatus("idle", `Vzorka ${name} je pripravena. Mozes ju renderovat alebo upravit.`);
    await handleSubmit();
  } catch (error) {
    setStatus("error", error.message || "Vzorku sa nepodarilo nacitat.");
  }
}

function insertAtCursor(text) {
  const start = textarea.selectionStart ?? textarea.value.length;
  const end = textarea.selectionEnd ?? textarea.value.length;
  const prefix = textarea.value.slice(0, start);
  const suffix = textarea.value.slice(end);
  const needsNewlineBefore = prefix.length > 0 && !prefix.endsWith("\n");
  const needsNewlineAfter = suffix.length > 0 && !suffix.startsWith("\n");
  const inserted = `${needsNewlineBefore ? "\n" : ""}${text}${needsNewlineAfter ? "\n" : ""}`;

  textarea.value = `${prefix}${inserted}${suffix}`;
  const caret = prefix.length + inserted.length;
  textarea.focus();
  textarea.setSelectionRange(caret, caret);
}

function insertCommand(command, description) {
  insertAtCursor(command.trim());
  if (description) {
    commandHelp.textContent = description;
  }

  const operation = command.trim().split(" ")[0];
  setStatus("idle", `Sablona ${operation} bola vlozena do editora.`);
}

function clearEditor() {
  textarea.value = "";
  if (currentImageUrl) {
    URL.revokeObjectURL(currentImageUrl);
    currentImageUrl = null;
  }

  outputImage.removeAttribute("src");
  showPlaceholder();
  setStatus("idle", "Editor je prazdny. Pridaj VES kod alebo nacitaj vzorku.");
  textarea.focus();
}

form.addEventListener("submit", handleSubmit);

widthSlider.addEventListener("input", (event) => {
  syncWidthInputs(event.target.value);
});

widthInput.addEventListener("input", (event) => {
  syncWidthInputs(event.target.value);
});

widthInput.addEventListener("blur", (event) => {
  syncWidthInputs(event.target.value);
});

clearEditorButton.addEventListener("click", clearEditor);

document.querySelectorAll(".sample-card").forEach((button) => {
  button.addEventListener("click", () => loadSample(button.dataset.sample));
});

document.querySelectorAll(".command-chip").forEach((button) => {
  button.addEventListener("click", () => {
    insertCommand(button.dataset.command, button.dataset.description);
  });
});

window.addEventListener("beforeunload", () => {
  if (currentImageUrl) {
    URL.revokeObjectURL(currentImageUrl);
  }
});

showPlaceholder();
syncWidthInputs(widthInput.value);
setStatus("idle", "Nahraj vzorku alebo vlastny kod a spusti render.");
