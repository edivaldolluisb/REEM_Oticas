
# Reem_opticas

 A university project for the creation of a website for an ophthalmology clinic, in which it is possible to schedule an appointment, shop for ophthalmology products, and a blog session with articles related to eye health.

 Um projeto Acadêmico para a criação de um web site para uma clínica de oftamologia, a onde é possível fazer o agendamento de uma consulta, comprar produtos oftamólogicos e uma sessão de blog a onde é possível colocar artigos referente a saúde oftamólogica. 

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **Implantação** para saber como implantar o projeto.

### 📋 Pré-requisitos

- Para poder executar o software precisa ter o python instalado na sua máquina.
- Saber como usar um teminal / linha de comando. Saber instalar softwares em seu sistema operacional.
  
  [linnk para a documentação](https://www.python.org/downloads/)

### 🔧 Instalação

+ O django foi instalado em um ambiente virtual (venv)

Para ter um ambiente de execução pronto deve instalar o django na sua máquina caso ainda não o tenha feito, a forma mais fácil de ter a versão mais estável do django é pelo comando *pip*.

```
pip install django
```
Ou pode instala todas as coisas necessárias instalando os requerimentos.
Estando na pasta do projeto digite o seguinte comando:

```
pip install -r requirements.txt
```
Após isso nós podemos rodar o web server de desenvolvimento dentro dessa pasta usando o manage.py e o comando runserver
```
python manage.py runserver
```
Uma vez que o servidor está operando, você pode acessar o site colocando a seguinte URL no seu navegador local:http://127.0.0.1:8000/.

+ Para fins de teste a base de dados utilizada nesse projeto é SQLite3

+ Está disponibilizado também duas APIs, uma para o carrinho de compras **Encomendas**, e outra para os agendamentos de consulta **Agendamento**, ambas com apenas metodos GET e POST.

disponivéis em:
para os agendamentos ->
+ http://127.0.0.1:8000/api/agendamento/
+ http://127.0.0.1:8000/api/agendamento-list/  -- GET
+ http://127.0.0.1:8000/api/agendamento-create/  --POSt

para as encomendas ->
+ http://127.0.0.1:8000/api/encomenda/
+ http://127.0.0.1:8000/encomenda-list/  -- GET
+ http://127.0.0.1:8000/encomenda-create/  --POSt

## 🛠️ Construído com

* [Django](https://www.djangoproject.com/) - O framework web usado

## 📄 Licença

Este projeto está sob a licença (MIT) - veja o arquivo [LICENSE.md](https://github.com/edivaldolluisb/REEM_Oticas/blob/main/LICENSE) para detalhes.



---
⌨️ com ❤️ por [Edivaldo Gustavo Bonfim](https://github.com/edivaldolluisb) 😊