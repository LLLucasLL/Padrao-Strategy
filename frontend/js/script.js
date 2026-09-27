// Captura os elementos da interface uma única vez.
const form = document.getElementById('form-desconto');
const mensagem = document.getElementById('mensagem');
const resultado = document.getElementById('resultado');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    // Esconde mensagens antigas antes de uma nova tentativa.
    mensagem.hidden = true;
    resultado.hidden = true;

    const tipo = document.getElementById('tipo').value;
    const valor = document.getElementById('valor').value;

    try {
        // Envia os dados para o controller Flask.
        const resposta = await fetch('/api/calcular', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                tipo,
                valor,
            }),
        });

        const dados = await resposta.json();

        if (!resposta.ok) {
            throw new Error(dados.erro || 'Não foi possível calcular o desconto.');
        }

        document.getElementById('resultado-tipo').textContent = dados.tipo;
        document.getElementById('resultado-original').textContent = dados.valor_original.toFixed(2);
        document.getElementById('resultado-final').textContent = dados.valor_final.toFixed(2);
        resultado.hidden = false;
    } catch (erro) {
        mensagem.textContent = erro.message;
        mensagem.hidden = false;
    }
});
