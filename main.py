from resources import MENU
from resources import resources

money = 0
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']


# TODO Print report.
def report():
    """Imprime um reporte da quantidade de água, leite, café e dinheiro dentro da máquina"""
    return print(
        f"The remaining resources in the machine are: \n- Water: {water}ml.\n- Milk: {milk}ml.\n- Coffee: {coffee}g.\n- Money: {money}$."
    )


# TODO Check resources sufficient?
def check_water_sufficient(list2, order):
    """Verfica a quantidade de agua que têm a máquina, ingressando list2 = MENU, e o prompt
    da ordem. Devolve um booleano"""
    global water
    water_needed = list2[order]['ingredients']['water']
    if water >= water_needed:
        return True
    else:
        return False


def check_milk_sufficient(list2, order):
    """Verfica a quantidade de leite que têm a máquina, ingressando como list2 = MENU, e o prompt
    da ordem. Devolve um booleano"""
    global milk
    milk_needed = list2[order]['ingredients']['milk']
    if milk >= milk_needed:
        return True
    else:
        return False


def check_coffee_sufficient(list2, order):
    """Verfica a quantidade de café que têm a máquina, ingressando list2 = MENU, e o prompt
    da ordem. Devolve um booleano"""
    global coffee
    milk_needed = list2[order]['ingredients']['coffee']
    if coffee >= milk_needed:
        return True
    else:
        return False


def check_resources(list2, order):
    """No caso faltar algum suplemento, devolve o um retorno falando o suplmento faltante."""
    if coffee < list2[order]['ingredients']['coffee']:
        return print('Sorry, not enough coffee in the machine.')
    if milk < list2[order]['ingredients']['milk']:
        return print('Sorry, not enough milk in the machine.')
    if water < list2[order]['ingredients']['water']:
        return print('Sorry, not enough water in the machine.')


def check_order(list2, order):
    """Verifica a se tem a quantidade de suplementos necessarios para o pedido"""
    if check_water_sufficient(list2, order) and check_milk_sufficient(list2, order) and check_coffee_sufficient(list2, order):
        return True
    else:
        check_resources(list2, order)
        return False


# TODO Process coins.
def process_coins():
    """Ingressa a quantidade de moedas, e armazena o total na variável global 'money'."""
    global money
    quarters = int(input('How many quarters? (0.25$): '))
    dimes = int(input('How many dimes? (0.10$): '))
    nickles = int(input('How many nickles? (0.05$): '))
    pennies = int(input('How many pennies? (0.01$): '))
    money += quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return round(money, 2)


# TODO Check transaction successful?
def transaction_successful(list1, order):
    """Avalia se o dinheiro ingressado é suficienter para realizar a transação do pedido. Retorna um booleano."""
    global money
    global milk
    global water
    global coffee
    if money >= list1[order]['cost']:
        money = round((money - MENU[order]['cost']), 2)
        milk = milk - MENU[order]['ingredients']['milk']
        water = water - MENU[order]['ingredients']['water']
        coffee = coffee - MENU[order]['ingredients']['coffee']
        return True
    else:
        return False


# TODO make coffe.
print('Welcome to the coffee machine!')


def main():
    """Programa principal"""
    global money
    while True:
        order = input("What coffee do you want? Type 'espresso', 'latte' or 'cappuccino': ")
        if order == 'off':
            return print(f'Thank you for use the coffe machine, see you later. Here is your change: {money}')
        elif order == 'status':
            report()
            main()
        elif check_order(MENU, order):
            process_coins()
            if transaction_successful(MENU, order):
                print(f"Here is your coffee, enjoy!. Your balance: {money}")
                again = input('Do you want anything else? y/n: ')
                if again == 'y':
                    main()
                else:
                    return print(f'Thank you for use the coffee machine, see you later. Here is your change: {money}')
            else:
                return print(f"Not enough money for your order.\nThank you for use the coffe machine, see you later. "
                             f"Here is your change: {money}")


main()
