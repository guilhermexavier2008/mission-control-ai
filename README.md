# Mission Control AI

## Descrição do projeto

O Mission Control AI é um sistema desenvolvido em Python para simular o monitoramento inteligente de uma missão espacial experimental.

O programa analisa diferentes ciclos de uma missão, verificando informações importantes como temperatura, comunicação, bateria, oxigênio e estabilidade operacional. A partir desses dados, o sistema gera alertas automáticos, calcula a pontuação de risco de cada ciclo, identifica a tendência da missão e apresenta um relatório final no terminal.

## Nome da missão

Ares Sentinel

## Nome da equipe

Equipe 07

## Objetivo

O objetivo do projeto é desenvolver um sistema básico de controle de missão espacial utilizando pensamento computacional, listas, matriz, estruturas condicionais, estruturas de repetição e funções em Python.

## Dados monitorados

Cada ciclo da missão possui cinco informações principais:

* Temperatura interna
* Comunicação com a base
* Sistema de energia
* Suporte de oxigênio
* Estabilidade operacional

Esses dados são armazenados em uma matriz chamada `dados_missao`, em que cada linha representa um ciclo de monitoramento da missão.

## Estrutura da matriz

Cada linha da matriz segue esta ordem:

```python
[temperatura, comunicacao, bateria, oxigenio, estabilidade]
```

Exemplo:

```python
[25, 94, 91, 97, 92]
```

Esse ciclo representa:

* Temperatura: 25 °C
* Comunicação: 94%
* Bateria: 91%
* Oxigênio: 97%
* Estabilidade: 92%

## Regras de classificação

Cada informação analisada pode receber uma das seguintes classificações:

* NORMAL
* ATENÇÃO
* CRÍTICO

Cada classificação gera uma pontuação de risco:

* NORMAL = 0 ponto
* ATENÇÃO = 1 ponto
* CRÍTICO = 2 pontos

Como cada ciclo possui cinco informações monitoradas, a pontuação máxima de um ciclo é 10 pontos.

## Classificação do ciclo

A classificação geral de cada ciclo é feita com base na pontuação total de risco:

* 0 a 2 pontos: MISSÃO ESTÁVEL
* 3 a 5 pontos: MISSÃO EM ATENÇÃO
* 6 a 10 pontos: MISSÃO CRÍTICA

## Funcionalidades do sistema

O sistema realiza as seguintes funções:

* Armazena dados simulados da missão
* Analisa temperatura, comunicação, bateria, oxigênio e estabilidade
* Gera alertas automáticos
* Calcula o risco de cada ciclo
* Classifica cada ciclo da missão
* Identifica a tendência da missão
* Identifica a área mais afetada
* Calcula médias dos dados monitorados
* Exibe um relatório final no terminal

## Funções utilizadas

O projeto utiliza funções para organizar a lógica do sistema, como:

* `analisar_temperatura()`
* `analisar_comunicacao()`
* `analisar_bateria()`
* `analisar_oxigenio()`
* `analisar_estabilidade()`
* `classificar_ciclo()`
* `gerar_recomendacao()`
* `analisar_tendencia()`
* `identificar_area_mais_afetada()`
* `gerar_relatorio_final()`
* `executar_monitoramento()`

## Como executar o projeto

Para executar o sistema, abra o terminal na pasta do projeto e digite:

```bash
python mission_control.py
```

Caso esteja usando uma versão do Python que utilize o comando `python3`, execute:

```bash
python3 mission_control.py
```

## Saída esperada

O programa exibirá no terminal a análise de cada ciclo da missão, mostrando:

* Status de cada área monitorada
* Pontuação de risco do ciclo
* Classificação do ciclo
* Recomendação automática

Ao final, será exibido o relatório final da missão com médias, ciclo mais crítico, risco médio, tendência, área mais afetada e conclusão.

## Conclusão

O Mission Control AI demonstra como a lógica de programação pode ser aplicada em um cenário de monitoramento espacial. O sistema utiliza regras lógicas para analisar dados simulados e apoiar a tomada de decisão durante uma missão experimental.
