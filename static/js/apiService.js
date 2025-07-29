export async function sendSignatureRequest(userData) {
    const url = '/api';

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(userData)
    })

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Ocorreu um erro na resposta do servidor');
    }

    return await response.blob();
} catch (error) {
    console.error('Erro ao enviar os dados:', error);
    // alert(`Erro ao gerar assinatura: ${error.message}`);
    throw new Error(`Erro ao enviar os dados: ${error.message}`);
}
}