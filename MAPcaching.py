import math

def hit_or_miss(array_list):
    #Linha 1 da entrada
    tamanho_ram = int(array_list[0][0])
    #Linha 2 da entrada
    n_palavras = int(array_list[1][0])
    #Tamanho da palavra = 4 bytes
    tamanho_bloco = n_palavras * 4
    #Linha 3 da entrada
    n_linhas = int(array_list[2][0]) 
    #Linha 4 da entrada
    n_vias = int(array_list[3][0])
    n_conjuntos = n_linhas / n_vias
    #Após a linha 4 da entrada
    list_end = array_list[4]
    #Simula a cache
    list_cache = []
    miss = 0
    hit = 0

    n_bits_end = int(math.log2(tamanho_bloco))
    n_bits_conj = int(math.log2(n_conjuntos))
    n_bits_tag = int(math.log2(tamanho_ram)) - (n_bits_end + n_bits_conj)
    
    #Verfica se há o bloco na cache, se houver HIT, caso não MISS
    for end in list_end:
        n_bloco = int(end) // tamanho_bloco
        if n_bloco not in list_cache:
            list_cache.append(n_bloco)
            miss += 1
        else:
            hit += 1

    #Resultado: n_bits_end, n_bits_conj, n_bits_tag, miss, hit
    array_result = [n_bits_end, n_bits_conj, n_bits_tag, miss, hit]
    return array_result
    
    

def text_generator(read_file, write_file):
    with open(read_file, 'r') as read_file, open(write_file, 'w') as write_file:
        write_file.write('Nome: ' + username + '\n')
        write_file.write('Convertido de: ' + str(read_file.name).replace(caminho_arquivo, '') + '\n')
        write_file.write('Resultado: ' + '\n' + '\n')
        #Colocar instruções no array_list
        array_list = []
        for line in read_file:
            array_temp = []
            line = line.strip().replace(',', '').replace('(',' ').replace(')',' ')
            if line != '':
                for element in line.split():
                    array_temp.append(element)
                array_list.append(array_temp)
        

    #Colocar instruções no txt de resultado
        for line in hit_or_miss(array_list):
            #line_printable = " ".join(line)
            write_file.write(str(line) + '\n')


#Mude a quantidade de arquivos
n_arquivos = 4
#Coloque o caminho exato do arquivo, ex: pc/documentos/testes/
caminho_arquivo = "testes/"
for i in range(0, n_arquivos):
    username = 'Pedro Sanzio e Joao Pedro'
    if i + 1 < 10:
        read_file = f'{caminho_arquivo}TESTE-0{i+1}.txt'
    else:
        read_file = f'{caminho_arquivo}TESTE-{i+1}.txt'
    filename = read_file.replace('.txt','-RESULTADO')
    write_file = str(filename) + '.txt'
    text_generator(read_file, write_file)
