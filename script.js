
"use strict";

// ==========================================
// Me quiero parecer a Jesús
// Interactive checklist
// ==========================================

const MERITS = [
    "Fe",
    "Virtud",
    "Conocimiento",
    "Dominio propio",
    "Paciencia",
    "Piedad",
    "Afecto fraternal",
    "Amor"
];

const EXPLANATIONS = [
    "Confiar en Dios, en Sus Promesas. Convicción, certeza",
    "Excelencia moral para obrar en la vida de manera correcta",
    "Entendimiento para diferenciar lo bueno de lo malo",
    "Dios Espíritu Santo en control de nuestros deseos e impulsos",
    "Firmeza ante las dificultades",
    "Una conducta que honra a Dios. Integridad en lo que hacemos",
    "Aprecio sincero, solidaridad y afecto mutuo entre los hermanos",
    "Desinterés. Preocupación genuina por el bienestar de otros."
];

// ==========================================
// HTML elements
// ==========================================

const checkboxes = document.querySelectorAll(".merit-checkbox");

const progressCount = document.getElementById("progress-count");
const progressFill = document.getElementById("progress-fill");
const progressBar = document.getElementById("progress-bar");

const feedback = document.getElementById("feedback");
const explanationButton = document.getElementById("explanation-button");

const dialog = document.getElementById("explanation-dialog");
const dialogHeading = document.getElementById("dialog-heading");
const dialogMessage = document.getElementById("dialog-message");
const closeDialog = document.getElementById("close-dialog");

// ==========================================
// Update progress and feedback
// ==========================================

function updateProgress() {

    const completed = Array.from(checkboxes)
        .filter(checkbox => checkbox.checked).length;

    progressCount.textContent = `Marcados: ${completed} de 8`;

    const percentage = (completed / MERITS.length) * 100;

    progressFill.style.width = `${percentage}%`;

    progressBar.setAttribute("aria-valuenow", completed);

    const nextIndex = Array.from(checkboxes)
        .findIndex(checkbox => !checkbox.checked);

    if (nextIndex === -1) {

        feedback.textContent = "¡Ahora te pareces más a Jesús!";

        explanationButton.textContent = "¡Prueba completada!";

    } else {

        if (nextIndex === 0) {
            feedback.textContent = "Comienza añadiendo Fe";
        } else {
            feedback.textContent = `Ahora añade ${MERITS[nextIndex]}`;
        }

        explanationButton.textContent =
            `${MERITS[nextIndex]}: ${EXPLANATIONS[nextIndex]}`;
    }
}

// ==========================================
// Show explanation dialog
// ==========================================

function showExplanation() {

    const nextIndex = Array.from(checkboxes)
        .findIndex(checkbox => !checkbox.checked);

    if (nextIndex === -1) {

        dialogHeading.textContent = "¡Evaluación completada!";

        dialogMessage.textContent =
            "Has reunido los ocho méritos.";

    } else {

        dialogHeading.textContent = MERITS[nextIndex];

        dialogMessage.textContent = EXPLANATIONS[nextIndex];
    }

    dialog.showModal();
}

// ==========================================
// Event listeners
// ==========================================

checkboxes.forEach(checkbox => {
    checkbox.addEventListener("change", updateProgress);
});

explanationButton.addEventListener("click", showExplanation);

closeDialog.addEventListener("click", () => {
    dialog.close();
});

// ==========================================
// Initial application state
// ==========================================

updateProgress();
