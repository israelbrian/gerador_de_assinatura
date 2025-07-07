const submitForm = document.getElementById('submitForm');
const divSignature = document.getElementById('divSignature');
const divImg = document.getElementById('divImg');
const signatureDefault = document.getElementById('signatureDefault');
const imgTitle = document.getElementById('imgTitle');

const url = '/api'
let imgUrlBlob = null

function downloadImage() {
    if (!imgUrlBlob) return

    const linkImg = document.createElement('a');
    linkImg.href = imgUrlBlob
    const userName = document.getElementById('fullName').value
    const fileName = `${userName}.png`;
    linkImg.download = `${fileName}`;
    divSignature.appendChild(linkImg);
    linkImg.click();
    divSignature.removeChild(linkImg);
    URL.revokeObjectURL(linkImg)
    document.getElementById('submitForm').reset()
}

function showImage(imgUrl) {
    document.getElementById('btnManual').classList.remove('hidden');
    signatureDefault.src = imgUrl;
    signatureDefault.alt = 'assinatura_gerada';
    imgTitle.textContent = 'Assinatura gerada com sucesso!';
    divImg.appendChild(signatureDefault)

    const oldButton = document.getElementById('buttonDownload');
    if (oldButton) {
        oldButton.remove();
    }

    const buttonDownload = document.createElement('button');
    buttonDownload.id = 'buttonDownload';
    buttonDownload.classList = 'bg-gray-900 text-white p-3 rounded-md my-4 hover:bg-slate-700'
    buttonDownload.textContent = 'Baixar Assinatura';
    buttonDownload.addEventListener('click', downloadImage);
    divSignature.appendChild(buttonDownload);
}

submitForm.addEventListener('submit', async (e) => {
    e.preventDefault()
const userData = {
    'fullName': document.getElementById('fullName').value, 
    'jobTitle': document.getElementById('jobTitle').value,
    'phoneNumber': document.getElementById('phoneNumber').value,
    'email': document.getElementById('email').value,
    'department': document.getElementById('department').value,
    'floor': document.getElementById('floor').value
}

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(userData)
        })

        const blob = await response.blob();
        const imgUrl = URL.createObjectURL(blob);
        imgUrlBlob = URL.createObjectURL(blob);
        showImage(imgUrl); 
        
    } catch (error) {
        console.error('Erro ao enviar os dados:', error);
    }
})

