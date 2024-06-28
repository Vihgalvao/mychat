// Função para atualizar o contador de tempo de espera
function atualizarTempoEspera() {
    // Obter o elemento de tempo de espera
    var tempoEsperaElemento = document.getElementById("tempo_espera");
    
    // Obter o tempo de espera em segundos
    var tempoEspera = 0;

    // Atualizar o tempo de espera no elemento
    tempoEsperaElemento.textContent = tempoEspera;
}

// Função para atualizar o nome do usuário
function atualizarNomeUsuario(nome) {
    // Obter o elemento de nome do usuário
    var nomeUsuarioElemento = document.getElementById("nome_usuario");

    // Atualizar o nome do usuário no elemento
    nomeUsuarioElemento.textContent = nome;
}

// Atualizar o tempo de espera a cada segundo
setInterval(atualizarTempoEspera, 1000);

// Definir o nome do usuário
var nomeUsuario = "Usuário";
atualizarNomeUsuario(nomeUsuario);