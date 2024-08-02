def preprocessar(texto):
    return ''.join([c.upper() for c in texto if c.isalpha()])

def cifra_vigenere_encrypt(mensagem, chave):
    mensagem_criptografada = []
    chave = preprocessar(chave)
    mensagem_processada = preprocessar(mensagem)
    tamanho_chave = len(chave)
    chave_as_int = [ord(i) for i in chave]
    mensagem_as_int = [ord(i) for i in mensagem_processada]
    j = 0
    for i in range(len(mensagem)):
        if mensagem[i].isalpha():
            valor = (mensagem_as_int[j] + chave_as_int[j % tamanho_chave]) % 26
            mensagem_criptografada.append(chr(valor + 65))
            j += 1
        else:
            mensagem_criptografada.append(mensagem[i])
    return ''.join(mensagem_criptografada)

def cifra_vigenere_decrypt(mensagem_criptografada, chave):
    mensagem_descriptografada = []
    chave = preprocessar(chave)
    tamanho_chave = len(chave)
    chave_as_int = [ord(i) for i in chave]


    j = 0
    for i in range(len(mensagem_criptografada)):
        if mensagem_criptografada[i].isalpha():
            valor = (ord(mensagem_criptografada[i]) - chave_as_int[j % tamanho_chave]) % 26
            mensagem_descriptografada.append(chr(valor + 65))
            j += 1
        else:
            mensagem_descriptografada.append(mensagem_criptografada[i])
    return ''.join(mensagem_descriptografada)

mensagem = "UM DIA SEREI MUITO RICA"
chave = "CHAVE"

mensagem_criptografada = cifra_vigenere_encrypt(mensagem, chave)
print("Mensagem Criptografada:", mensagem_criptografada)


mensagem_descriptografada = cifra_vigenere_decrypt(mensagem_criptografada, chave)
print("Mensagem Descriptografada:", mensagem_descriptografada)
