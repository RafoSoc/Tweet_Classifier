# Tweet_Classifier
Projeto para a disciplina Inteligência Artificial Centrada no ser humano para o mestrado em Engenharia e Ciência de Dados na Universidade de Coimbra. Este repositório contém os códigos do modelo de árvore de decisão que classifica entre os tweets Positivos, Negativos e Neutros relacionados aos candidatos presidenciais, Lula e Bolsonaro, das eleições brasileiras de 2022.

### Este Repositório é organizado da seguinte maneira:
- Três pastas principais, uma contendo os códigos e outra os dados.
 1. A pasta "cod" contém os códigos possuem três pastas:
    - getData que é o primeiro passo, ou seja, primeiro código a ser rodado, pois é o código que irá coletar os dados.
    - o segundo passo está na pasta normalização, onde possuí quatro códigos que estão organizados da seguinte maneira: 
          1. Três notebooks, onde irá fazer a normalização.
          2. um arquivo python que contém os códigos que irão fazer as transformações de normalização dos tweets, fizemos desta maneira pois ficaria mais rápido, organizado e fácil de realizar as mesma operações de normalização dos dados.
   - Por último temos a pasta modelo, que possui o notebook "modelos_treino_teste.ipynb" que fará o treino e teste utilizando os dados que foram coletados e normalizados previamente e também irá salvar os modelos, vetorizadores e as categorias alvo para serem utilizados posteriormente sem a necessidade de fazer o treino novamente. Também há outro notebook com o nome "utilizandoModelos.ipynb" que irá utilizar os modelos, vetorizadores e as categorias alvo salvos previamente. Está pasta também possuí mais outra pasta "classificadores", onde foram salvos os  modelos, vetorizadores e as categorias alvo.

 2. A pasta "data" contém os dados possuem três pastas:
     - A pasta "raw data" contém os dados que foram coletados pelo código "getTweets_toCSV.ipynb".
     - A pasta "train_data" possuí os dados normalizados e que serão usados pelo código no notebook "modelos_treino_teste.ipynb".
     - A pasta "test_data que possuí os dados para teste, serão utilizados pelo código no notebook "utilizandoModelos.ipynb".

 3. A pasta que contem o paper do Projeto.
     - Contém os arquivos do paper em .pdf e .docx.