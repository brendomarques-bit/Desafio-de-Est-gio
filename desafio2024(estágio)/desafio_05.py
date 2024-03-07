def inverter_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

# String de exemplo
string_original = "Brendo Marques é a pessoa certa para esse Estágio!"

# Invertendo a string
string_invertida = inverter_string(string_original)

# Exibindo o resultado
print("String original:", string_original)
print("String invertida:", string_invertida)
