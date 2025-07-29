import { sendSignatureRequest } from "./apiService.js"
import { showGeneratedImage } from "./uiHandler.js"
import { validateForm } from "./validator.js"
import {formatPhone} from "./formatter.js"

const submitForm = document.getElementById('submitForm');
const phoneInput = document.getElementById('phoneNumber');

phoneInput.addEventListener('input', formatPhone);

submitForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const isFormValid = validateForm();
    if (!isFormValid) {
        alert('Por favor, preencha todos os campos corretamente.');
        return;
    }

     const userData = {
        'fullName': document.getElementById('fullName').value, 
        'jobTitle': document.getElementById('jobTitle').value,
        'phoneNumber': document.getElementById('phoneNumber').value,
        'email': document.getElementById('email').value,
        'department': document.getElementById('department').value,
        'floor': document.getElementById('floor').value
    }

    try {
        const imageBlob = await sendSignatureRequest(userData);
        showGeneratedImage(imageBlob);
    } catch (error) {
        // nenhuma ação necessaria
    }
})