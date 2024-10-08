import string
def user_register():
    excepciones = {'.', '_', '-'}
    no_permitido = set(string.punctuation) - excepciones
    while True:
        user = input("Ingrese su cuenta de usuario: ")
        if len(user) > 0:
            for char in user:
                if char in no_permitido:
                    print(f"Solo son permitidos los símbolos {excepciones}")
                    return user_register()
            return password_register(user)
        else:
            print("Debes escribir un nombre para la cuenta de usuario")

def password_register(user):
    while True:
        isdigit_flag = False
        islower_flag = False
        isupper_flag = False
        password = input("Ingrese su contraseña: ")

        if len(password) > 7:
            for char in password:
                if char.isdigit():
                    isdigit_flag = True
                if char.isupper():
                    isupper_flag = True
                if char.islower():
                    islower_flag = True

            if  isdigit_flag and islower_flag and isupper_flag:
                print("¡¡¡Registro exitoso!!!")
                return f"Tu cuenta de usuario es: {user} y tu contraseña es: {password}"
            else:
                print("La contraseña debe tener al menos 8 caracteres, un número, una letra mayúscula y una letra minúscula")
        else:
            print("La contraseña debe tener al menos 8 caracteres")


print("¡Bienvenido al Sistema de Registro de Cuenta de Usuario!\n")

print(user_register())