# PyTDDRPG - Python + Test-Driven Development + RPG

Olar, personas! Pela primeira vez eu tive vergonha na cara e criei um README decente (pelo menos vou tentar).

Neste projeto eu vou fazer um pequeno jogo de RPG em texto. O foco principal é aprender as vantagens e desvantagens de programar em TDD.

## Vídeos

Aqui vai um pequeno descritivo das aulas

### [Introdução](https://www.youtube.com/watch?v=a_eBuAHIkNM)

Bem, como diz o nome, é só uma introdução. É mais pra falar o que irei ou não fazer. Para ajudar, aqui vai:

* Assumo que você tenha uma pequena noção de programação (saiba uns ifs-elses da vida e afins). Caso você não tenha a menor ideia do que seja programar em python, aqui tem a [minha playlist com só 30 vídeos](https://www.youtube.com/playlist?list=PL4OAe-tL47saDYxam_QeJSsOsuVJx2ymN) (14/01/2019 tem 30 vídeos. Hahaha)
* Baixe o PyCharm (não é 100% necessário que seja no PyCharm. Pode até fazer pelo notepad)


### [PyTDDRPG (Aula 1) - Configurando o PyCharm para usar o unittest](https://www.youtube.com/watch?v=vqzQmvir-Qg)

Neste vídeo eu ensino a vocês não passarem nervoso ao configurar o unittest no PyCharm

### [PyTDDRPG (Aula 2) - Criando nosso primeiro teste](https://www.youtube.com/watch?v=thFQjUFySq0)

Neste vídeo eu explico um pouco sobre como funciona o ciclo do TDD: escreve teste, o infeliz falha, escreve a implementação, o teste passa, vida que segue. A parte da "refatoração" eu explico no próximo vídeo

### [PyTDDRPG (Aula 3) - Primeira refatoração do código](https://www.youtube.com/watch?v=oBZFp5Lp8Kk)

Eu explico sobre como isolar nossa implentação usando o Bar do Chicão como exemplo: você não sabe como o Chicão faz o lanche e isso não te interessa.

### [PyTDDRPG (Aula 4) - Criando função de causar dano - Parte 1](https://www.youtube.com/watch?v=Hgt89arr_2w)

Neste vídeo faço uma pequena refatoração e crio um novo teste para implementar a função de ataque do personagem.

### [PyTDDRPG (Aula 5) - Refatoração dos Atributos (Parte 1)](https://www.youtube.com/watch?v=auvyQVGJsJY)

Neste vídeo eu explico quais serão os atributos iniciais que iremos trabalhar (força, defesa e vida) e demonstro como implementar isso no construtor do Personagem

### [PyTDDRPG (Aula 6) - Refatoração dos Atributos (Parte 2) - disponível às 17/01/2019 10:00](https://youtu.be/qIrKzpBvgnE)

Continuando com a refatoração dos construtores do personagem. Agora usaremos um dicionário para setar os atributos, mas lógico que alguns testes explodirão na sua cara (mas esse é o intuito. Hahahaha)

### [PyTDDRPG (Aula 7) - Criando função de causar dano (Parte 2) - disponível às 17/01/2019 20:00](https://youtu.be/5w1v6sTtXXw)

Neste vídeo eu corrijo o problema dos atributos "inconstantes" (tem vida, mas não tem força; tem força, mas não tem vida) e começo a função de cálculo do dano. Lógico que o código quebrou em duas funções e vocês terão que corrigir. Hahahaha

Só começarei a fazer os vídeos mais tarde. Até lá estará com bug.

### [PyTDDRPG (Aula 8) - Refatorando novamente os atributos do Personagem (Parte 1)](https://youtu.be/M88WDBBscx4)

Neste vídeo eu começo a refatoração (mais uma vez) dos atributos do nosso Personagem. Sim, é pau comendo e teste quebrando, mas a vida é assim.

### [PyTDDRPG (Aula 9) - Refatorando novamente os atributos do Personagem (Parte 2) - disponível às 18/01/2019 20:00](https://youtu.be/vIatMBrpe-k)

Neste vídeo eu termino a refatoração dos atributos e crio mais um teste: verificar se o personagem estará morto se levar mais dano que sua vida

### [PyTDDRPG (Aula 10) - setUp, tearDown e primeiro problema - disponível às 19/01/2019 20:00](https://youtu.be/Psabui8U_Iw)

Aqui apresento os métodos setUp e tearDown, que são executados antes (setUp) e depois (tearDown) de cada teste e, no meio da brincadeira, surgiu um bug safadinho.

Olha, até resolveria, mas já são 00:55 e tô com um sono lascado. hahahaha

### [PyTDDRPG (Aula 11) - Debugando o teste, variáveis mutáveis e imutáveis e mais um bug](https://youtu.be/abqmiu15dg0)

Neste vídeo eu demonstro como usar o debuger do PyCharm, falo sobre variáveis mutáveis e não mutáveis e deixo mais um bug para vocês resolverem

### [PyTDDRPG (Aula 12) - Corrigindo o cálculo de receber dano](https://youtu.be/VNjnKLg-Dqw)

Neste vídeo, como diz o título do vídeo, corrijo o cálculo de receber dano do Personagme

### [PyTDDRPG (Aula 13) - Iniciando a arena dos personagens](https://youtu.be/cGYA3r8sjUE)

Neste vídeo eu inicio a construção da classe Arena, que é onde os personagens estarão alocados 