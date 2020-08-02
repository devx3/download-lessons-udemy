# Crawler de Aulas de um Curso específico na Udemy

Eu tenho uma planilha onde eu preencho todas as aulas de um curso específico que vou fazer na Udemy. 

Eu sempre copiava os nomes das aulas, tratava pra deixar da maneira que eu gosto e depois mandava para o trello via integração (planilha -> trello)

Esse script já está fazendo essa primeira etapa, ele pega todas as aulas de um curso específico, e salva em um arquivo TXT 

Para usar, é só seguir os seguintes passos: 

`pip install -r requirements.txt`

É só mudar a linha 107 com a URL do curso que deseja "Scrapear" 

`Udemy('https://www.udemy.com/course/python-3-do-zero-ao-avancado/')`

E depois, é só: 
`python udemy.py`

O curso é sempre salvo na área de trabalho. 

Fique à vontade pra baixar e melhorar esse script

# TODO
A segunda etapa agora, é adicionar interface gráfica, poder escolher a data para fazer cada aula e, enviar para o Trello!

