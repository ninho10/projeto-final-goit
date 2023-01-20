#conectar no banco

#selecionar pizza no banco

#criar um objeto do tipo pizza com os dados do banco

#exibir as informacoes do objeto pizza



#login de usuario

#este usuario pode cadastrar pizza

#se ele for adm -> cadastrar pizza, verificar as vendas

#se ele for balconista -> registrar



#tanto balconista como adm:

#criar um pedido

#o pedido é registrado na tabela de vendas



import mysql.connector

from pizza import Pizza



cnx = mysql.connector.connect(host='localhost', database='pizzaria_python', user='root', password='root')

cursor = cnx.cursor()

cursor.execute("SELECT * FROM pizza")



queryResult = cursor.fetchall()



cursor.close()

cnx.close()



pizzas = []



for i in queryResult:

    pizzas.append(Pizza(i[0], i[1], i[2]))



# for x in queryResult:

#   print(x)



# pizza = pizzas[0]



# print( pizza.nome)

# print( pizza.preco)



for pizza in pizzas:

    print(pizza.id)

    print(pizza.nome)

    print(pizza.preco)