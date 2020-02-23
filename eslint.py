import json

def readEslintrc():
    f = open("eslintrc.json", "r")
    eslint = json.loads(f.read())
    f.close()
    return eslint

def saveEslintrc(eslint):
    payload = json.dumps(eslint)
    f = open("eslintrc.json", "w")
    f.write(payload)
    f.close

# Menu
def menuEslintrc():
    options = {
        0 : envMenu,
        1 : extendsMenu,
        2 : pluginsMenu,
        3 : globalsMenu,
        4 : parserOptionsMenu,
        5 : rulesMenu
    }

    while True:
        print "Digite um numero correspondente:\n"
        print '''
        0 - Env
        1 - Extends
        2 - Plugins
        3 - Globals
        4 - Parser Options
        5 - Rules

        9 - Sair
        
        '''

        menu = raw_input('Digite o valor: ')
        print menu
        if menu == '9':
            print "Saindo do script"
            break
        elif menu == '0':
            options[0]()
        elif menu == '1':
            options[1]()
        elif menu == '2':
            options[2]()
        elif menu == '3':
            options[3]()
        elif menu == '4':
            options[4]()
        elif menu == '5':
            options[5]()


def envMenu():
    eslint = readEslintrc()

    print "Veja como esta o Env..."
    print eslint["env"]
    print "\n--------\n"

    goin = raw_input("Deseja modificar algo? (y/N): ")
    if goin == "y":
        while True:
            addKey(eslint["env"])

            print eslint["env"]
            
            saveEslintrc(eslint)      
            
            menu = raw_input("Deseja adicionar mais alguma coisa (y/N)? ")

            if menu == "y":
                pass
            else:
                break
    else:
        pass

def extendsMenu():
    eslint = readEslintrc()

    print "Veja como esta o Extends..."
    print eslint["extends"]
    print "\n--------\n"

    goin = raw_input("Deseja modificar algo? (y/N): ")
    if goin == "y":
        while True:
            menu = raw_input("Qual o nome do Extend que deseja? ")
            eslint["extends"].append(menu)

            print eslint["extends"]
            
            saveEslintrc(eslint)      
            
            menu = raw_input("Deseja adicionar mais alguma coisa (y/N)? ")

            if menu == "y":
                pass
            else:
                break
    else:
        pass


def pluginsMenu():
    eslint = readEslintrc()

    print "Veja como esta o Plugins..."
    print eslint["plugins"]
    print "\n--------\n"

    goin = raw_input("Deseja modificar algo? (y/N): ")
    if goin == "y":
        while True:
            menu = raw_input("Qual o nome do Plugin que deseja? ")
            eslint["plugins"].append(menu)

            print eslint["plugins"]
            
            saveEslintrc(eslint)      
            
            menu = raw_input("Deseja adicionar mais alguma coisa (y/N)? ")

            if menu == "y":
                pass
            else:
                break
    else:
        pass

def globalsMenu():
    eslint = readEslintrc()

    print "Veja como esta o Globals..."
    print eslint["globals"]
    print "\n--------\n"

    goin = raw_input("Deseja modificar algo? (y/N): ")
    if goin == "y":
        while True:
            addKey(eslint["globals"])

            print eslint["globals"]
            
            saveEslintrc(eslint)      
            
            menu = raw_input("Deseja adicionar mais alguma coisa (y/N)? ")

            if menu == "y":
                pass
            else:
                break
    else:
        pass

def parserOptionsMenu():
    eslint = readEslintrc()

    print "Veja como esta o Parser Options..."
    print eslint["parserOptions"]
    print "\n--------\n"

    goin = raw_input("Deseja modificar algo? (y/N): ")
    if goin == "y":
        while True:
            addKey(eslint["parserOptions"])

            print eslint["parserOptions"]
            
            saveEslintrc(eslint)      
            
            menu = raw_input("Deseja adicionar mais alguma coisa (y/N)? ")

            if menu == "y":
                pass
            else:
                break
    else:
        pass

def rulesMenu():
    eslint = readEslintrc()

    print "Veja como esta o Rules..."
    print eslint["rules"]
    print "\n--------\n"

    goin = raw_input("Deseja modificar algo? (y/N): ")
    if goin == "y":
        while True:
            addKey(eslint["rules"])

            print eslint["rules"]
            
            saveEslintrc(eslint)      
            
            menu = raw_input("Deseja adicionar mais alguma coisa (y/N)? ")

            if menu == "y":
                pass
            else:
                break
    else:
        pass

def addKey(eslint):
    key = raw_input("Adicione o nome: ")
    value = raw_input("Adicione o valor:")
    eslint[key] = value

    print eslint

    return eslint

if __name__ == "__main__":
    
    menuEslintrc()
    print "Finalizando o script..."

