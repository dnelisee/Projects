class Pile : 
    def __init__(self) -> None:
        self.pile = [] 

    def empile(self, newElement) : 
        """
        Cette fonction ajoute newElement en tête de pile
        """
        self.pile += [newElement] 
    
    def depile(self) : 
        """
        Cette fonction retire de la pile l'élément de tête et le 
        retourne.
        """
        return self.pile.pop() 
    
    def pile_est_vide(self) : 
        """
        Cette fonction retourne True si la pile est vide et False 
        sinon
        """
        if len(self.pile) > 0 : 
            return False 
        else : 
            return True 
        
    def pile_contient(self, element) : 
        """
        Cette fonction renvoie True si la pile contient element et 
        False sinon.
        """
        if element in self.pile : 
            return True 
        else : 
            return False 
        
    def somme_elements(self) : 
        """
        Cette fonction renvoie la somme des termes de la pile.
        N.B : Notez que la pile doit alors être une pile de nombres.
        """
        S = 0 
        for x in self.pile :
            S += x 
        return S 
    
    def avant_dernier_element(self) : 
        """
        Cette fonction renvoie l'avant dernier élément de la pile 
        s'il existe et None sinon.
        """
        if len(self.pile) >= 2 : 
            return self.pile[1] 
        else : 
            return None 

def tri_wagons(train : str) -> str :
    """
    Cette fonction trie le train en mettant d'abord les nombres 
    en debut de chaîne puis les lettres en fin de chaîne.
    Exemple : train = "4 C 5 D 7 F E" donc tri_wagons(train) renvoie 
    "4 5 7 C D F E".
    """ 
    result = []
    temp = []
    train = train.split()
    for x in train : 
        if x.isdigit() : 
            result += [x] 
        else : 
            temp += [x] 

    result += temp 
    return " ".join(result) 

class Calco_polonaise :
    def __init__(self) -> None:
        pass 
    def operation(self, a, b, op) : 
        """
        cette fonction revoie le résultat de l'opération : a (op) b. 
        Exemple : operation(4, 5, '+') renvoie 4 + 5  i.e  9.
        Avec op est dans {'+', '*', '-', '/'}.
        """
        if op == '+' : 
            return a + b 
        if op == '*' : 
            return a * b 
        if op == '-' : 
            return a - b 
        if op == '/' :
            return a / b 

    def eval_polo(self, expression : str) : 
        """
        cette fonction prend une expression polonaise puis l'évalue et renvoie le résultat.
        """
        T = Pile() 
        expression = expression.split()
        for x in expression : 
            if x.isdigit() :
                T.empile(int(x))
            else : 
                a = T.depile()
                b = T.depile()
                T.empile(self.operation(b, a, x))
        return float(T.pile[0])
        """
        Exemple : 
            calco = Calco_polonaise() 
            calco.eval_polo("3 2 / 5 *") ---> (3/2) * 5 = 7.5
            
        """
    
    def parentheses_correctes(self, expression : str) -> bool : 
        """
        Cette fonction renvoie True si expression est bien parenthésée et False sinon.
        Avec expression une expression contenant comme délimiteurs des parenthèses.
        """
        test_pile = Pile()

        for x in expression : 
            if x == '(' :
                test_pile.empile(x) 
            if x == ')' : 
                if test_pile.pile_est_vide() : 
                    return False 
                else : 
                    test_pile.depile()

        if test_pile.pile_est_vide() : 
            return True 
        else : 
            return False 
        """
        Exemple : 
        calco = Calco_polonaise() 
        calco.parentheses_correctes("(2+3)*(4+(8/2))") ----> True 
        calco.parentheses_correctes("(x+y)*((7+z)")    ----> False 
        
        """

    def crochets_parentheses_correctes(self, expression : str) -> bool : 
        """
        Cette fonction renvoie True si expression est bien parenthésée et False sinon.
        Avec 'expression' une expression contenant comme délimiteurs des crochets 
        et des parenthèses.
        """
        test_pile = Pile() 
        for x in expression : 
            if x == '(' or x == '[' : 
                test_pile.empile(x) 
            if x == ')' : 
                if test_pile.depile() != '(' : 
                    return False 
            
            if x == ']' : 
                if test_pile.depile() != '[' : 
                    return False 
                
        if test_pile.pile_est_vide() : 
            return True 
        else : 
            return False
        """
        Exemple : 
        calco = Calco_polonaise() 
        calco.crochets_parentheses_correctes("[(a+b)*(a-b)]")     ---> True 
        calco.crochets_parentheses_correctes("[a+b),(a+b]*(a-b)") ---> False
        """
    def ecriture_polonaise(self, expression : str) -> str :
        """
        Cette fonction convertit une expression habituelle 
        expression polonaise équivalente. 
        Exemple : habituelle = (4 + 5) * 2 <--> polonaise = 4 5 + 2 * 
        """  
        test_pile = Pile()
        polonaise = str()
        expression = expression.split()
        for x in expression : 
            if x.isdigit() : 
                polonaise += x + ' ' 
            if x == '(' or x == '*' : 
                test_pile.empile(x)
            if x == '+' : 
                while not test_pile.pile_est_vide() : 
                    element = test_pile.depile()
                    if element == '*' : 
                        polonaise += element + ' ' 
                    else : 
                        test_pile.empile(element)
                        break
                test_pile.empile('+')
            if x == ')' :
                while not test_pile.pile_est_vide() : 
                    element = test_pile.depile()
                    if element == '(' :
                        break 
                    else :
                        polonaise += element + ' '  
        if not test_pile.pile_est_vide() : 
            polonaise += "".join(test_pile.pile)

        return polonaise 
        """
        Exemple : 
        calco = Calco_polonaise() 
        calco.ecriture_polonaise("(4+5)*2") --> 4 5 + 2 *
        """
    
############ test ############ 
calco = Calco_polonaise() 

exp = "( 17 * ( 2 + 3 ) ) + ( 4 + ( 8 * 5 ) )"
print(eval(exp)) # --> 129

exp1 = calco.ecriture_polonaise(exp)
print(exp1) # -->  17 2 3 + * 4 8 5 * + +
N = calco.eval_polo(exp1)
print(N)    # --> 129.0