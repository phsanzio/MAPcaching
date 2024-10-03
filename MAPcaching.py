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
            for element in line.split():
                array_temp.append(element)
            array_list.append(array_temp)
        
        #Seleção dos metódos
            
        #Colocar instruções no txt de resultado
        
            line_printable = "".join(line)
            write_file.write(line_printable + '\n')


#Mude a quantidade de arquivos
n_arquivos = 1
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
