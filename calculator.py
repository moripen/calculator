
def addition(value1, value2):
    """
    Tar inn to verdier, adderer de sammen og printer ut resultatet.

    Funksjonen tar inn to parametere, 'value1' og 'value2'.

    Args: 
        value1(int): Verdi 1
        value2(int): Verdi 2

    Returns: 
        str: En string som inneholder en float med resultatet av
        utregningen.
    """
    result = value1 + value2
    print(result)

def substraction(value1, value2):
    """
    Tar inn to verdier, trekker den andre fra den første
    og printer ut resultatet.

    Funksjonen tar inn to parametere, 'value1' og 'value2'.

    Args: 
        value1(int): Verdi 1
        value2(int): Verdi 2

    Returns: 
        str: En string som inneholder en float med resultatet av
        utregningen.
    """
    result = value1 - value2
    print(result)

def division(value1, value2):
    """
    Tar inn to verdier, deler den første på den andre
    og printer ut resultatet.

    Funksjonen tar inn to parametere, 'value1' og 'value2'.

    Args: 
        value1(int): Verdi 1
        value2(int): Verdi 2

    Returns: 
        str: En string som inneholder en float med resultatet av
        utregningen.
    """
    if value2 == 0:
        print("Trying to divide by 0")
    else:    
        result = value1 / value2
        print (result)

def multiplication(value1, value2):
    """
    Tar inn to verdier, multipliserer de sammen og printer ut resultatet.

    Funksjonen tar inn to parametere, 'value1' og 'value2'.

    Args: 
        value1(int): Verdi 1
        value2(int): Verdi 2

    Returns: 
        str: En string som inneholder en float med resultatet av
        utregningen.
    """
    result = value1 * value2
    print(result)

def percentage(value1, value2):
    """
    Tar inn to verdier, hvor den første verdien er prosentandelen
    e.g. 10 vil tilsvare 10%. Den andre verdien er tallet du vil 
    finne den mengden prosent av.
    Eksempel: value1 = 10, value2 = 30.
    Dette vil da tilsvare 10% av 30 altså 3.

    Funksjonen tar inn to parametere, 'value1' og 'value2'.

    Args: 
        value1(int): Verdi 1
        value2(int): Verdi 2

    Returns: 
        str: En string som inneholder en float med resultatet av
        utregningen.
    """
    result = (value2/100)*value1
    print(result)
    
def run_calc():
    """
    Denne funksjonen kjører programmet. 
    Den kjører en serie med user input som styrer hvilken
    funksjon som skal kjøres og hva som tilslutt printes ut.

    Returns: 
        str: En string som inneholder en float med resultatet av
        utregningen.
    """
    function = input("What function would you like to use? ")
    value1 = int(input("Input the first number "))
    value2 = int(input("Input the second number "))
    if function == "addition":
        addition(value1, value2)

    elif function == "substraction":
        substraction(value1, value2)

    elif function == "division":
        division(value1, value2)

    elif function == "multiplication":
        multiplication(value1, value2)

    elif function == "percentage":
        percentage(value1, value2)

    else:
        print("Unknown function")

run_calc()