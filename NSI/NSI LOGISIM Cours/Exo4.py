#1)
def supprime_espace(machaine):
    machaine = machaine.replace(" ", "")
    return machaine

#machaine = "ceci est un test"
    
#print(supprime_espace(machaine))
    
#2)
def est_un_palindrome(machaine):
    if machaine == machaine[::-1]:
        return True
    else :
        return False
    
#machaine = "kayak" 
        
#print(est_un_palindrome(machaine))
        
#3)

machaine = "k a ya k  "
print(est_un_palindrome(supprime_espace(machaine)))