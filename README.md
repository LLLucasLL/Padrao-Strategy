# Laboratório 01 — Strategy em Python

## O que é o padrão Strategy?

Strategy é um padrão de projeto comportamental que define uma família de algoritmos, encapsula cada um em uma classe própria e permite substituí-los sem alterar o código que os utiliza. Assim, em vez de concentrar regras de negócio em vários comandos `if-else` ou `switch`, cada regra fica isolada em uma estratégia concreta.

### Como funciona

As estratégias compartilham um contrato, normalmente uma interface ou classe abstrata. Um objeto de contexto recebe ou seleciona uma estratégia e delega a ela a execução do algoritmo. Como todas seguem o mesmo contrato, a estratégia pode ser trocada em tempo de execução sem que o contexto precise conhecer os detalhes de cada implementação.

Neste laboratório, `CalculadoraDesconto` é o contexto e as estratégias concretas calculam descontos diferentes, como VIP, aniversário ou funcionário. O controller seleciona a estratégia correspondente ao tipo de desconto solicitado.

### Vantagens

- Separa cada regra de negócio, deixando as classes menores e com responsabilidades mais claras.
- Permite adicionar ou alterar estratégias com menos impacto nas existentes.
- Reduz condicionais extensos que escolhem entre algoritmos.
- Facilita testar cada comportamento de forma independente.

### Desvantagens

- Cria mais classes e estrutura, o que pode ser excessivo para poucas regras simples e estáveis.
- O código que usa o contexto ainda precisa decidir qual estratégia utilizar, ou receber essa escolha de outro componente.
- Quem mantém o sistema precisa entender o contrato e as estratégias disponíveis.

### Quando usar

Use Strategy quando houver várias formas de realizar uma mesma tarefa e for necessário escolher ou trocar entre elas, especialmente quando novas regras são adicionadas com frequência ou quando condicionais de seleção estão crescendo. Para uma regra única, simples e improvável de mudar, uma abstração separada pode trazer mais custo do que benefício.

## Sobre este laboratório

Implementação do padrão Strategy em Python, com Flask, HTML/CSS/JavaScript e testes automatizados com pytest.

## Estrutura

```text
laboratorio_strategy/
├── backend/
│   ├── app.py
│   ├── controllers/
│   │   └── desconto_controller.py
│   ├── middleware/
│   │   └── validacao.py
│   ├── services/
│   │   └── calculadora_desconto.py
│   └── strategies/
│       ├── desconto_strategy.py
│       ├── desconto_comum.py
│       ├── desconto_vip.py
│       ├── desconto_premium.py
│       ├── desconto_aniversario.py
│       ├── desconto_promocional.py
│       └── desconto_funcionario.py
├── frontend/
│   ├── index.html
│   ├── css/style.css
│   └── js/script.js
├── tests/
│   ├── test_strategy.py
│   ├── test_calculadora.py
│   └── test_api.py
├── docs/diagrama_strategy.puml
├── requirements.txt
├── pytest.ini
└── README.md
```

## Instalação no VS Code

```powershell
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
```

Ou, separadamente, conforme solicitado no laboratório:

```powershell
py -m pip install Flask
py -m pip install pytest
```

## Executar os testes

Na raiz do projeto:

```powershell
py -m pytest -v
```

## Executar a aplicação

```powershell
py -m backend.app
```

Depois acesse `http://127.0.0.1:5000`.

## Regras implementadas

| Estratégia | Desconto |
|---|---:|
| Comum | 5% |
| VIP | 10% |
| Premium | 20% |
| Aniversário | 15% |
| Promocional | 25% |
| Funcionário | 30% |

## Relação com o laboratório

- `DescontoStrategy` é a abstração/contrato.
- As seis classes de desconto são as estratégias concretas.
- `CalculadoraDesconto` é o contexto.
- O controller escolhe a estratégia de acordo com o tipo recebido pela API.
- O middleware valida a entrada antes de chamar o controller.
- Os testes ficam fora de `backend` e `frontend`, conforme solicitado.
