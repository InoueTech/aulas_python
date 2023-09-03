from random import choice
import string

tamanho_da_senha = int(input("Quantos dígitos você quer na sua senha? "))

if tamanho_da_senha <= 0:
    print("Tamanho da senha deve ser maior que zero.")
else:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_segura = [choice(caracteres) for _ in range(tamanho_da_senha)]
    senha_segura = ''.join(senha_segura)

    print("A senha (segura) gerada é:", senha_segura)
