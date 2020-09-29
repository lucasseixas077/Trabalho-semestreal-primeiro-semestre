input('Vamos encontrar qual ecoponto é o mais próximo de sua localidade! Para começar aperte ENTER. ')
print('')

# Ecoponto Jardim Eulina - Av. Mal. Rondon, 2296-2382 - Jardim Chapadão, Campinas - SP
lat, lon = 22891508,47101033

# Ecoponto Vila União - R. Manoel Gomes Ferreira, 42 - Parque Tropical, Campinas - SP, 13060-523
lat1, lon1 = 22935243,47118543

# Ecoponto Vila Campos Sales - Próximo ao Cruzamento da Rua Eva de Souza Santos, Av. São José dos Campos, S/N - Vila Campos Sales, Campinas
lat2, lon2 = 22948027,47057073

# Ecoponto Parque São Jorge
# Rua Plácida Pretini, s/n
lat3, lon3 = 22895067,47156429

# Ecoponto Jardim São Gabriel
# Rua Jose Martins Lourenço, esq. Rua Geraldo Bretas
lat4, lon4 = 22941671,47030881

# Ecoponto Vida Nova
# R. Lídia Martins de Assis, conj. Hab. Vida nova
lat5, lon5 = 22977304,47177841

# Ecoponto Parque Itajaí
# Rua Celso Soares Couto, s/n
lat6, lon6 = 22961679,47189511

# Ecoponto Jardim Paranapanema
# Rua Serra D água esquina com Rua Felismina Stemmer Cajado, nº 326, Jardim São Fernando
lat7, lon7 = 22915346,47037847
 
# Ecoponto Jardim Pacaembu
# Rua Dante Suriane esquina com Av. Padre Gaspar Bertoni
lat8, lon8 = 22903857,47105344

# Descarte de pneus/Departamento de Limpeza Urbana
# Av. Prefeito Faria Lima, 630, Parque Itália
lat9, lon9 = 22914911,47071459

lats = [lat,lat1,lat2,lat3,lat4,lat5,lat6,lat7,lat8,lat9]
longs = [lon,lon1,lon2,lon3,lon4,lon5,lon6,lon7,lon8,lon9]
ruas = ['Ecoponto Jardim Eulina - Av. Mal. Rondon, - Jardim Chapadão.',
'Ecoponto Vila União - R. Manoel Gomes Ferreira, 42 - Parque Tropical, Campinas.',
'Ecoponto Vila Campos Sales - Próximo ao Cruzamento da Rua Eva de Souza Santos com a Av. São José dos Campos, S/N - Vila Campos Sales, Campinas.',
'Ecoponto Parque São Jorge, Rua Plácida Pretini, s/n.',
'Ecoponto Jardim São Gabriel Rua Jose Martins Lourenço, esquina com Rua Geraldo Bretas.',
'Ecoponto Vida Nova R. Lídia Martins de Assis, conj. Hab. Vida nova.',
'Ecoponto Parque Itajaí, Rua Celso Soares Couto, s/n.',
'Ecoponto Jardim Paranapanema Rua Serra D água esquina com Rua Felismina Stemmer Cajado, nº 326, Jardim São Fernando.',
'Ecoponto Jardim Pacaembu Rua Dante Suriane esquina com Av. Padre Gaspar Bertoni.',
'Departamento de Limpeza Urbana Av. Prefeito Faria Lima, 630, Parque Itália.']

valid_continuar = False
while valid_continuar == False:    
    valid = False
    while valid == False:
        
        valid_xlat = False
        while valid_xlat == False:
            xlat = input('Insira sua latitude sem o ".", use o site https://www.latlong.net/: ')
            print('')
            try:
                xlat = int(xlat)
                if xlat <= 0 and xlat >= -85000000:
                    valid_xlat = True
                else:
                    print('Insira apenas latitudes localizadas no Hemisfério Sul.')
                    print('')
            except:
                print('Por favor insira a latitude apenas com números e sem pontuação.')
                print('')
        
        valid_xlong = False
        while valid_xlong == False:
            xlong = input('Insira a sua longitude sem o ".",use o site https://www.latlong.net/: ')
            print('')
            try:
                xlong = int(xlong)
                if xlong <= 0 and xlong >= -180000000:
                    valid_xlong = True
                else:
                    print('Insira apenas longitudes localizadas no Hemisfério Ocidental.')
                    print('')
            except:
                print('Por favor insira a longitude apenas com números e sem pontuação.')
                print('')
        
        valid_materialtipo = False
        while valid_materialtipo == False:
            materialtipo = input('Insira que tipo de material deseja reciclar: Digite 1 p/ resíduos recicláveis, 2 p/ resíduos eletrodomésticos, 3 p/ resíduos de construção cívil, 4 p/ resíduos vegetais: ')
            print('')
            try:
                materialtipo = int(materialtipo)
                if materialtipo >= 1 and materialtipo <= 4:
                    valid_materialtipo = True
                else:
                    print('Por favor insira apenas um dos números citados acima. [1,2,3,4] ')
                    print('')
            except:
                print('Por favor insira apenas os números dos materiais citados acima. [1,2,3,4] ')
                print('')
            
        if materialtipo == 1:
            valid_submaterial_resrec = False
            while valid_submaterial_resrec == False:
                submaterial_resrec = input('Qual material gostaria de reciclar? Digite: 1 p/ papelão, 2 p/ papel, 3 p/ plástico, 4 p/ óleo comestível, 5 p/ vidro, 6 p/ metais, 7 p/ pneu.')
                print('')
                try:
                    submaterial_resrec = int(submaterial_resrec)
                    if submaterial_resrec >= 1 and submaterial_resrec <= 7:
                        valid_submaterial_resrec = True
                    else:
                        print('Por favor insira apenas um dos números citados acima. [1,2,3,4,5,6,7] ')
                        print('')
                except:
                    print('Por favor insira apenas um dos números citados acima. [1,2,3,4,5,6,7] ')
                    print('')
        
        elif materialtipo == 2:
            valid_submaterial_reslet = False
            while valid_submaterial_reslet == False:
                submaterial_reslet = input('Qual material gostaria de reciclar? Digite: 1 p/ monitores, 2 p/ impressoras, 3 p/ eletrodomésticos, 4 p/ pilhas, 5 p/ baterias. ')
                print('')
                try:
                    submaterial_reslet = int(submaterial_reslet)
                    if submaterial_reslet >= 1 and submaterial_reslet <=5:
                        valid_submaterial_reslet = True
                    else:
                        print('Por favor insira apenas um dos números citados acima. [1,2,3,4,5] ')
                        print('')
                except:
                    print('Por favor insira apenas um dos números citados acima. [1,2,3,4,5] ')
                    print('')
        
        elif materialtipo == 3:
            valid_submaterial_rescon = False
            while valid_submaterial_rescon == False:
                submaterial_rescon = input('Qual material gostaria de reciclar? Digite: 1 p/ concreto, 2 p/ terra, 3 p/ cerâmica, 4 p/ madeira, 5 p/ metais, 6 p/ plástico.')
                print('')
                try:
                    submaterial_rescon = int(submaterial_rescon)
                    if submaterial_rescon >=1 and submaterial_rescon <= 6:
                        valid_submaterial_rescon = True
                    else:
                        print('Por favor insira apenas um dos números citados acima. [1,2,3,4,5,6] ')
                        print('')
                except:
                    print('Por favor insira apenas um dos números citados acima. [1,2,3,4,5,6] ')
                    print('')
        
        elif materialtipo == 4:
            valid_submaterial_resveg = False
            while valid_submaterial_resveg == False:
                submaterial_resveg = input('Qual material gostaria de reciclar? Digite: 1 p/ galhos, 2 p/ restos de podas.')
                print('')
                try:
                    submaterial_resveg = int(submaterial_resveg)
                    if submaterial_resveg >=1 and submaterial_resveg <=2:
                        valid_submaterial_resveg = True
                    else:
                        print('Por favor insira apenas um dos números citados acima. [1,2] ')
                        print('')
                except:
                    print('Por favor insira apenas um dos números citados acima. [1,2] ')
                    print('')

        else:
            print('Erro incomum.')
            print('')

        xlat = -(xlat)
        xlong = -(xlong)
        
        t = 999999999999999999999
        r = 1
        rua = ''
        
        if xlat > 0 and xlong > 0:
            if materialtipo == 1:
                if submaterial_resrec >=1 and submaterial_resrec <= 6:    
                    for i in range(0,9):
                        if lats[i] >= xlat and longs[i] >= xlong:
                            r = ((lats[i] - xlat)**2 + (longs[i] - xlong)**2)**0.5
                            if r < t:
                                t = r
                                rua = ruas[i]
                                
                        elif lats[i] >= xlat and longs[i] <= xlong:
                            r = ((lats[i] - xlat)**2 + (xlong - longs[i])**2)**0.5
                            if r < t:
                                t = r
                                rua = ruas[i]

                        elif lats[i] <= xlat and longs[i] >= xlong:
                            r = ((xlat - lats[i])**2 + (longs[i] - xlong)**2)**0.5
                            if r < t:
                                t = r
                                rua = ruas[i]
                            
                        elif lats [i] <= xlat and longs[i] <= xlong:
                            r = ((xlat - lats[i])**2 + (xlong - longs[i])**2)**0.5
                            if r < t:
                                t = r
                                rua = ruas[i]
                    valid = True
                
                else: 
                    for i in range(0,10):
                        if lats[i] >= xlat and longs[i] >= xlong:
                            r = ((lats[i] - xlat)**2 + (longs[i] - xlong)**2)**0.5
                            if r < t:
                                t = r
                                rua = ruas[i]
                    

                        elif lats[i] >= xlat and longs[i] <= xlong:
                            r = ((lats[i] - xlat)**2 + (xlong - longs[i])**2)**0.5
                            if r < t:
                                t = r
                                rua = ruas[i]

                        elif lats[i] <= xlat and longs[i] >= xlong:
                            r = ((xlat - lats[i])**2 + (longs[i] - xlong)**2)**0.5
                            if r < t:
                                t = r
                                rua = ruas[i]
                            
                        elif lats [i] <= xlat and longs[i] <= xlong:
                            r = ((xlat - lats[i])**2 + (xlong - longs[i])**2)**0.5
                            if r < t:
                                t = r
                                rua = ruas[i]    
                    valid = True   
                        
            else:
                for i in range(0,9):
                        if lats[i] >= xlat and longs[i] >= xlong:
                            r = ((lats[i] - xlat)**2 + (longs[i] - xlong)**2)**0.5
                            if r < t:
                                t = r
                                rua = ruas[i]


                        elif lats[i] >= xlat and longs[i] <= xlong:
                            r = ((lats[i] - xlat)**2 + (xlong - longs[i])**2)**0.5
                            if r < t:
                                t = r
                                rua = ruas[i]

                        elif lats[i] <= xlat and longs[i] >= xlong:
                            r = ((xlat - lats[i])**2 + (longs[i] - xlong)**2)**0.5
                            if r < t:
                                t = r
                                rua = ruas[i]
                            
                        elif lats [i] <= xlat and longs[i] <= xlong:
                            r = ((xlat - lats[i])**2 + (xlong - longs[i])**2)**0.5
                            if r < t:
                                t = r
                                rua = ruas[i]     
                valid = True

    if materialtipo == 1 and submaterial_resrec == 1:
        print('O material escolhido foi: papelão')
        print('')
        print('A reciclagem do papelão é bem simples, ele será triturado, limpo e vendido novamente para ser usado pelas indústrias.')
        print('')    
    elif materialtipo == 1 and submaterial_resrec == 2:
        print('O material escolhido foi: papel')
        print('')
        print('O papel é facilmente reaproveitado, será reciclado e totalmente reaproveitado.')
        print('')    
    elif materialtipo == 1 and submaterial_resrec == 3:
        print('O material escolhido foi: plástico')
        print('')
        print('O plástico será reciclado e totalmente reaproveitado, tornando-se matéria prima de outros produtos.')
        print('') 
    elif materialtipo == 1 and submaterial_resrec == 4:
        print('O material escolhido foi: óleo comestível')
        print('')
        print('O óleo pode ser reaproveitado até mesmo em sua própria casa. Deve ser armazenado em uma garrafa PET e levado ao ponto de coleta quando houver a vontade de descarte')
        print('')  
    elif materialtipo == 1 and submaterial_resrec == 5:
        print('O material escolhido foi: vidro')
        print('')
        print('O vidro é facilmente reaproveitado para criar novos materiais, o processo se dá basicamente derretendo o vidro para sua reutilização.')
        print('')
    elif materialtipo == 1 and submaterial_resrec == 6:
        print('O material escolhido foi: metais')
        print('')
        print('Os resíduos metálicos coletados são separados nos centros de triagem entre ferrosos e não ferrosos, após separados serão reciclados da forma devida.')
        print('')
    elif materialtipo == 1 and submaterial_resrec == 7:
        print('O material escolhido foi: pneu')
        print('')
        print('A reciclagem de pneus na maioria das vezes trata-se de reaproveitar a sua estrutura, com a aplicação de uma nova banda de rodagem, para a sua reutilização nos veículos.')
        print('')
    if materialtipo == 2 and submaterial_reslet == 1:
        print('O material escolhido foi: monitores.')
        print('')
        print('Serão retirados todos os materiais possíveis para serem reciclados destes monitores, será diferente de caso em caso.')
        print('')
    elif materialtipo == 2 and submaterial_reslet == 2:
        print('O material escolhido foi: impressoras.')
        print('')
        print('Serão retirados todos os materiais possíveis para serem reciclados destas impressoras, será diferente de caso em caso.')
        print('')
    elif materialtipo == 2 and submaterial_reslet == 3:
        print('O material escolhido foi: eletrodomésticos.')
        print('')
        print('Serão retirados todos os materiais possíveis para serem reciclados destes eletrodomésticos, será diferente de caso em caso.')
        print('')
    elif materialtipo == 2 and submaterial_reslet == 5:
        print('O material escolhido foi: pilhas.')
        print('')
        print('As pilhas geralmente são compostas por lítio, precisam ser recicladas em locais apropriados. Serão recuperados alguns materiais nesse tipo de reciclagem.')
        print('')
    elif materialtipo == 2 and submaterial_reslet == 6:
        print('O material escolhido foi: baterias.')
        print('')
        print('As bateriais geralmente são compostas por lítio, precisam ser recicladas em locais apropriados. Serão recuperados alguns materiais nesse tipo de reciclagem.')
        print('')
    if materialtipo == 3 and submaterial_rescon == 1:
        print('O material escolhido foi: concreto')
        print('')
        print('Há dois tipos de reciclagem para esse material: o primeiro é feito com um aditivo estabilizador, que mantém o concreto hidratado e fresco por mais tempo; e o segundo envolve equipamentos mecânicos (recicladores) e a lavagem forçada do material, com água sob pressão, que separa o cimento dos agregados')
        print('')
    elif materialtipo == 3 and submaterial_rescon == 2:
        print('O material escolhido foi: terra')
        print('')
        print('A reciclagem da terra tem como objetivo simplesmente deixa-la mais pura e que possa ser reutilizada sem danificar o meio ambiente.')
        print('')
    elif materialtipo == 3 and submaterial_rescon == 3:
        print('O material escolhido foi: cerâmica')
        print('')
        print('Os materiais de cerâmica possuem reciclabilidade difícil, diversidade de composições, mercado ruim, sucata pouco valorizada e reaproveitamento energético inviável. Entretanto, a maioria dos materiais de cerâmica são duráveis, ou seja, podem ser reutilizados.')
        print('')
    elif materialtipo == 3 and submaterial_rescon == 4:
        print('O material escolhido foi: madeira')
        print('')
        print('Madeiras recicladas podem ser usadas de múltiplas formas, tudo depende do formato em que ela se encontra.')
        print('')
    elif materialtipo == 3 and submaterial_rescon == 5:
        print('O material escolhido foi: metais')
        print('')
        print('Os resíduos metálicos coletados são separados nos centros de triagem entre ferrosos e não ferrosos, após separados serão reciclados da forma devida.')
        print('')
    elif materialtipo == 3 and submaterial_rescon == 6:
        print('O material escolhido foi: plástico')
        print('')
        print('O plástico será reciclado e totalmente reaproveitado, tornando-se matéria prima de outros produtos.')
        print('')
    if materialtipo == 4 and submaterial_resveg == 1:
        print('O material escolhido foi: galhos')
        print('')
        print('Galhos podem ser reciclados de diversas formas, tudo depende do formato que o material se encontra.')
        print('')
    elif materialtipo == 4 and submaterial_resveg == 1:
        print('O material escolhido foi: restos de podas')
        print('')
        print('Restos de podas podem ser reciclados de diversas formas, tudo depende do formato que o material se encontra.')
        print('')
        
    print('O ecoponto mais próximo de você que permite a reciclagem do seu material é:',rua)
    print('')

    
    
    valid_pergunta = False
    while valid_pergunta == False:
        continuar = input('Gostaria de continuar? [S/N]: ').lower()
        print('')
        if continuar == 'n':
            valid_continuar = True
            valid_pergunta = True
        elif continuar == 's':
            valid_pergunta = True
        else:
            print('Por favor, digite apenas [S/N]. ')
            print('')

input('Obrigado por utilizar nosso programa! Para fechar aperte ENTER. ')