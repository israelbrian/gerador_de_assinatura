const divSignature = document.getElementById('divSignature');
const divImg = document.getElementById('divImg');
const signatureDefault = document.getElementById('signatureDefault');
const imgTitle = document.getElementById('imgTitle');
let imgUrlBlob = null;

function downloadImage() {
    if (!imgUrlBlob) return
    const linkImg = document.createElement('a');
    linkImg.href = imgUrlBlob
    const userName = document.getElementById('fullName').value
    // const fileName = `${userName}.png`;
    linkImg.download = `${userName || 'assinatura'}.png`;
    divSignature.appendChild(linkImg);
    linkImg.click();
    divSignature.removeChild(linkImg);
    URL.revokeObjectURL(linkImg)
    document.getElementById('submitForm').reset()
}

export function showGeneratedImage(blob) {
    if (imgUrlBlob) {
        URL.revokeObjectURL(imgUrlBlob);
    }

    imgUrlBlob = URL.createObjectURL(blob);

    document.getElementById('btnManual').classList.remove('hidden');
    signatureDefault.src = imgUrlBlob;
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