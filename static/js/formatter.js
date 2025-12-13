/**
 * @param {Event} event
 */

export function formatPhone(event) {
  const target = event.target;
  let value = target.value.replace(/\D/g, "");
  value = value.substring(0, 10);
  value = value.replace(/^(\d{2})(\d)/, "($1) $2");
  value = value.replace(/(\d{4})(\d)/, "$1-$2");

  target.value = value;
}

export function formatTelephone(event) {
  const target = event.target;
  let value = target.value.replace(/\D/g, "");
  value = value.substring(0, 11);
  value = value.replace(/^(\d{2})(\d)/, "($1) $2");
  value = value.replace(/(\d{5})(\d)/, "$1-$2"); // Adicionar o hífen após o 5º dígito do número

  target.value = value;
}
