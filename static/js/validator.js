const inputPhoneNumber = document.getElementById('phoneNumber');

inputPhoneNumber.addEventListener('input', (event) =>  {
  const target = event.target;

  let value = target.value.replace(/\D/g, '');

  value = value.substring(0, 10);

  value = value.replace(/^(\d{2})(\d)/, '($1) $2');
  value = value.replace(/(\d{4})(\d)/, '$1-$2');

  target.value = value;
});

