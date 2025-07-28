const inputPhoneNumber = document.getElementById('phoneNumber');

inputPhoneNumber.addEventListener('input', (event) =>  {
    const target = event.target;

    let value = target.value.replace(/\D/g, '');

    value = value.substring(0, 10);

    if (value.length > 9) {
        value = value.replace(/(\d{2})(\d{4})(\d{4})/, '($1) $2-$3');
    } else if (value.length > 6) {
        value = value.replace(/^(\d{2})(\d{4})(\d{0,4})$/, '($1) $2-$3')
    } else if (value.length > 2) {
        value = value.replace(/^(\d{2})(\d{*})$/, '($1) $2')
    } else if (value.length > 0) {
        value = value.replace(/^(\d*)$/, '($1)')
    }

    target.value = value;
})