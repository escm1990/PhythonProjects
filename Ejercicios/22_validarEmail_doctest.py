
# inicio funcion
def verifica_mail(elmail):
    """
    >>> verifica_mail('francisco@@@quezada.com')
    True
    """
    verifica_arroba=elmail.count('@') #cuenta las @en elmail

    #si hay 0 @ o más de una
    #rfind si la @ esta al final
    #si no hay @ (otra forma de hacerlo)
    if(verifica_arroba!=1 or elmail.rfind('@')==(len(elmail)-1) or elmail.find('@')==0):
        return False
    else:
        return True
#fin funcion

import doctest
doctest.testmod()