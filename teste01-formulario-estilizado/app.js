var nome = document.getElementById('id-nome');
var email = document.getElementById('id-email');
var botao = document.getElementById('id-botao');

function enviar(){
    alert(`Nome: ${nome.value}\nE-mail: ${email.value}`);
}