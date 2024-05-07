from solution import Product, ShoppingCart

product1 = Product(9788478290222, cost=129, name='акварель')
product2 = Product(3211234567890, cost=259, name='супер пупер акварель')
product3 = Product(4681234123412, cost=1399, name='гуашь')

products = [product1, product2, product3]

cart1 = ShoppingCart('cart1.txt')

exiting = False
while not exiting:
    operation = int(input('Выберите операцию:\n'
                          '1: Добавить товар в корзину\n'
                          '2: Удалить товар из корзины\n'
                          '3: Узнать общую стоимость\n'
                          '4: Выход\n'))
    if operation not in (1, 2, 3, 4):
        print('Неверный номер операции')
    else:
        if operation == 1:
            print('Выберите товар')
            for i in range(len(products)):
                print(f'{i+1}: {products[i]}')
            prod_index = int(input()) - 1
            num = int(input('Выберите количество: '))
            cart1.add_product(products[prod_index], num)

        elif operation == 2:
            prods = list(cart1.cart.keys())
            print('Выберите товар для удаления')
            for i in range(len(prods)):
                print(f'{i + 1}: {prods[i]}')
            prod_index = int(input()) - 1
            cart1.del_product(prods[prod_index])

        elif operation == 3:
            print(f'Общая стоимость: {cart1.total_cost}')

        else:
            exiting = True
