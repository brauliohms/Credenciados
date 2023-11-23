function formatarCPF() {
    console.log("formatarCPF function called"); // Usado para debug no console do inspetor do navegador
    var cpfInput = document.getElementById("id_cpf"); // Obtem o valor digitado no input com id="cpf"
    var cpf = cpfInput.value.replace(/\D/g, ''); // Remove caracteres não numéricos

    // Aplica a máscara
    cpf = cpf.replace(/^(\d{3})(\d)/g, '$1.$2') //Adiciona ponto após os três primeiros números
             .replace(/^(\d{3})\.(\d{3})(\d)/g, '$1.$2.$3') //Adiciona ponto após os seis primeiros números
             .replace(/^(\d{3})\.(\d{3})\.(\d{3})(\d{1,2})/g, '$1.$2.$3-$4'); //Adiciona o hífen antes dos últimos 2 caracteres

    cpfInput.value = cpf;
}

function formatarCNPJ() {
    //console.log("formatarCNPJ function called");
    cnpj_input = document.getElementById("id_cnpj");
    cnpj = cnpj_input.value.replace(/\D/g, "");

    cnpj = cnpj.replace(/^(\d{2})(\d)/g, "$1.$2")
               .replace(/^(\d{2}\.\d{3})(\d)/g, "$1.$2")
               .replace(/^(\d{2}\.\d{3}\.\d{3})(\d)/g, "$1\/$2")
               .replace(/^(\d{2}\.\d{3}\.\d{3}\/\d{4})(\d)/g, "$1-$2");

    cnpj_input.value = cnpj;
}

function formatarTelefone() {
    tel_input = document.getElementById("id_telefone");
    tel = tel_input.value.replace(/\D/g, "");

    // Verifica se o telefone possui 11 dígitos (com DDD)
    if (tel.length === 11) {
        tel = tel.replace(/^(\d{2})(\d{5})(\d{4})/g, '($1) $2-$3');
    }
    // Verifica se o telefone possui 10 dígitos (sem DDD)
    else if (tel.length === 10) {
        tel = tel.replace(/^(\d{2})(\d{4})(\d{4})/g, '($1) $2-$3');
    }

    tel_input.value = tel;
}
