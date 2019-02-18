<h1>Projeto de extração de dados para o MongoDB</h1>

<p>O seguinte projeto foi realizado com o site: https://sidra.ibge.gov.br/home/ipp/brasil</p>
<h2>Requisitos:</h2>
<ul>
<li>Python 3.7</li>
<li>Pandas</li>
<li>Pymongo</li>
</ul>

No arquivo <em>config_data.py</em> se encontra dados como a string de conxão ao banco de dados MongoDB(que deve ser colocado de acordo com
a string de conexão de seu banco), o nome do banco de dados e o nome do site.

<h3>Execução do código</h3>
Para executar o código é necessário ter o Python 3.7 instalado na máquino e esta dentro do diretório do projeto através do promp de comando e executar o seguinte comando
<strong>python scraping_sp.py</strong>. Logo após a execução do comando, será gravado no banco do mongoDB as informações extraidas através do código.
