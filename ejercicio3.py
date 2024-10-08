def registro(user, password):
    try:

        isupper_flag = False
        isdigit_flag = False
        lower_flag = False

        if len(password) > 7:
            for character in password:
                if character.isupper():
                    isupper_flag = True
                if character.isdigit():
                    isdigit_flag = True
                if character.islower():
                    lower_flag = True
                
            if isupper_flag and lower_flag and isdigit_flag:
                return "¡Registro exitoso!"
            if not isupper_flag:
                return "Faltó un caracter en mayúscula"
            if not lower_flag:
                return "Faltó un caracter en minúscula"
            if not isdigit_flag:
                return "Faltó un caracter numérico"
        else:
            return "La contraseña debe tener al menos 8 caracteres"
        

    except ValueError as e:
        print(f"Error tipo: {e}")

print("Bienvenido al sistema de registro de cuenta de usuarioal")
while True:
    user = input("Ingrese su cuenta de usuario: ")
    while len(user) > 0:
        password = input("Ingrese su contraseña: ")
        if len(password) == 0:
            print("Olvidaste de escribir una contraseña")
        else:    
            print(registro(user, password))
    else:
        print("Escribe un nombre para la cuenta de usuario")