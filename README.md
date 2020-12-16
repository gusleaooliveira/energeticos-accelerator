# Projeto Energéticos Accelerator

# Resolução

## Observações
### Linguagem

Utilizei a linguagem Python (na versão atual 3), com a interface gráfica PyQt5, pois este é fácil e prático de utilizar.

Escolhi esta  linguagem, pois estudei a mesma no técnico e na faculdade, e tenho mais destreza e facilidade com a mesma. Entretanto, estou aberto a conhecer e utilizar outras linguagens de programação, frameworks e demais ferramentas relacionadas, visto que o importante é utilizar a lógica mais correta possível.


## Cálculos
### Cálculo de imposto

Todos os cálculos seguem a mesma base:
* Recebo como parâmetro a quantidade de energéticos
* Calculo o preço dos energéticos (preço unitário pela quantidade de energéticos)
* Depois desconto a porcentagem equivalente a cada imposto
* Após o termino do cálculo retorno o resultado

```python
def icms(self, quantidade):
    return round((4.5*quantidade)*0.18, 2)

def ipi(self, quantidade):
    return round((4.5*quantidade)*0.04, 2)

def pis(self, quantidade):
    return round((4.5*quantidade)*0.01860, 2)

def cofins(self, quantidade):
    return round((4.5*quantidade)*0.0854, 2)
```

### Cálculo de desconto

Escolhi, como modo de dar um desconto de **35%**, desde que a quantidade de energéticos seja igual, ou superior, à 1000. No caso a função fica assim:
* Recebo como parâmetro a quantidade de energéticos e o valor total (já com os impostos acrescidos) dos energéticos
* Se a quantidade for igual ou superior à 100
    - Calculo o desconto (preço total x desconto)
    - Retorno o cálculo feito anteriormente
* Se a diferença
    - Retorno falso, já que não farei o desconto

```python
def desconto(self, quantidade, total):
    if quantidade >= 1000:
        return total*0.35
    else:
        return False
```

### Cálculo de total 
#### Total com impostos de cada empresa

Para calcular o total de cada empresa foi feito:
* Recebo todos os impostos (calculados anteriormente) e a quantidade de energéticos
* Todos os impostos são somados 
* Calculo o preço dos energéticos (preço unitário pela quantidade de energéticos)
* Somo o total dos impostos com o preço dos energéticos
* Após o termino do cálculo retorno o resultado

```python
def total(self, calculoIcms, calculoIpi, calculoPis, calculoCofins, quantidade):
    valorUnitario = 4.5*quantidade 
    return (calculoIcms+calculoIpi+calculoPis+calculoCofins)+valorUnitario
```

#### Total dos impostos (das duas empresas)

Para calcular o total de impostos das duas empresas:
* Somo todos os impostos (calculados anteriormente)

```python
calcImpostos = icms1+icms2+ipi1+ipi2+pis1+pis2+cofins1+cofins2
```

#### Total de mercadorias (das duas empresas)

Para calcular o total de mercadorias:
* Calculo o preço dos energéticos (preço unitário pela quantidade de energéticos) de cada empresa somo os dois

```python
calcMercadorias = (en1*4.50)+(en2*4.50)
```

#### Total de geral (das duas empresas)

Para calcular o total geral
* Somo o total de impostos e de mercadoria feitos anteriormente.

```python
calcGeral = calcImpostos+calcMercadorias
```

### Interfáce gráfica
#### Método construtor

Nesse metodo foi inicializado a interface gráfica, de tamanho **800x600**, com o título **"Energéticos Accelerator"**.
Será setado como layout o `QGridLayout` que é responsável pelo grid, que é retornado pelo método ui.
 

```python
def __init__(self):
    super().__init__()

    self.app = QApplication(sys.argv)

    self.janela = QWidget()
    self.janela.setWindowTitle("Energéticos Accelerator")
    self.janela.resize(800, 600)
    self.janela.show()
    

    self.janela.setLayout(self.ui())

    sys.exit(self.app.exec_())
```

#### Método ui

Neste método todos os componentes são iniciados, dentro eles temos:
- `QGridLayout()`: que é o grid para colocar os componentes na tela
- `QLineEdit()`: é a entrada de texto
- `QLabel()`: são os textos, ou **labels**, que serão exibidos na tela
- `QPushButton()`: é o botão que para chamar o método de calculo 

O método `.addWidget()` acrescenta na tela os componentes anteriormente criados, respectivamente, na linha, coluna, quantidade de linhas e colunas utilizadas.

O método `.clicked.connect(self.calcular)` chama o método calcular que irá chamar e por na tela todos os calculos.

Após o termino, é retornado o grid com os componentes inicializados:

```python
def ui(self):
    self.grid = QGridLayout()

    self.en1 = QLineEdit()   
    self.en2 = QLineEdit() 
    self.en3 = QLineEdit() 
    self.en4 = QLineEdit()

    self.lb1 = QLabel("")
    self.lb2 = QLabel("")
    self.lb3 = QLabel("")
    self.lb4 = QLabel("")
    self.lb5 = QLabel("")
    self.lb6 = QLabel("")
    self.lb7 = QLabel("")
    self.lb8 = QLabel("")
    self.lb9 = QLabel("")
    self.lb10 = QLabel("")
    self.lb11 = QLabel("")
    self.lb12 = QLabel("")
    self.lb13 = QLabel("Total Impostos: ")
    self.lb14 = QLabel("Total Mercadorias: ")
    self.lb15 = QLabel("Total Geral: ")
    self.lb16 = QLabel("Desconto: R$ ")
    self.lb17 = QLabel("Desconto: R$ ")


    self.pb1 = QPushButton("Calcular") 
    self.pb1.clicked.connect(self.calcular)       

    self.grid.addWidget(QLabel("Primeira empresa:"), 0, 0)
    self.grid.addWidget(self.en1, 0, 1)
    self.grid.addWidget(QLabel("Quantidade: "), 0, 4)
    self.grid.addWidget(self.en2, 0, 5)

    
    self.grid.addWidget(QLabel("Segunda empresa:"), 1, 0)
    self.grid.addWidget(self.en3, 1, 1)
    self.grid.addWidget(QLabel("Quantidade: "), 1, 4)
    self.grid.addWidget(self.en4, 1, 5)


    self.grid.addWidget(QLabel("<b>Empresa: </b>"), 2, 0)
    self.grid.addWidget(self.lb1, 3, 0)
    self.grid.addWidget(self.lb2, 4, 0)
    
    self.grid.addWidget(QLabel("<b>ICMS:  </b>"), 2, 1)
    self.grid.addWidget(self.lb3, 3, 1)
    self.grid.addWidget(self.lb4, 4, 1)
    
    self.grid.addWidget(QLabel("<b>IPI:  </b>"), 2, 2)
    self.grid.addWidget(self.lb5, 3, 2)
    self.grid.addWidget(self.lb6, 4, 2)
    
    self.grid.addWidget(QLabel("<b>PIS:  </b>"), 2, 3)
    self.grid.addWidget(self.lb7, 3, 3)
    self.grid.addWidget(self.lb8, 4, 3)
    
    self.grid.addWidget(QLabel("<b>COFINS:  </b>"), 2, 4)
    self.grid.addWidget(self.lb9, 3, 4)
    self.grid.addWidget(self.lb10, 4, 4)
    
    self.grid.addWidget(QLabel("<b>Total: </b>"), 2, 5)
    self.grid.addWidget(self.lb11, 3, 5)
    self.grid.addWidget(self.lb12, 4, 5)


    self.grid.addWidget(QLabel("<b>Total das empresas:</b>"), 5, 0, 6, 6)
    self.grid.addWidget(self.lb13, 6, 0, 6, 6)
    self.grid.addWidget(self.lb14, 7, 0, 6, 6)
    self.grid.addWidget(self.lb15, 8, 0, 6, 6)

    self.grid.addWidget(QLabel("<b>Total com 35% de desconto: </b>"), 9, 0, 6, 6)
    self.grid.addWidget(self.lb16, 10, 0, 6, 6)
    self.grid.addWidget(self.lb17, 11, 0, 6, 6)

    self.grid.addWidget(self.pb1, 12, 0, 6, 6)


    return self.grid
```

#### Método calcular

Esse método ira chamar os métodos de calculo criados anteriormente:

Verifica se o texto da entrada para o nome da empresa, caso esteja vasio mostra a mensagem de erro: 

```python
if self.en1.text() != '':      
        self.lb1.setText(f'{self.en1.text()}')
    else: 
        self.lb1.setText(f'<b><u>Digite um nome da empresa!</u></b>')
    if self.en1.text() != '':      
        self.lb2.setText(f'{self.en3.text()}')
    else: 
        self.lb2.setText(f'<b><u>Digite um nome da empresa!</u></b>')
```

Verifica se é um numero, visto que as entradas é retornam um texto sempre, e se for converte para um inteiro, caso não for deixa tudo no padrão. 

Caso convertidos para inteiros os valores, são chamados os métodos para calculo de **icms**, **ipi**, **cofins**, **pis**, e calculo de **total** (para cada empresa). 

Bem como esses, são feitos os calculos de total de **impostos**, **mercadorias** e **geral**. 

Também é chamado o método de calculo de **desconto**.

Após todos os resultados são colocados em seus respectivos locais (nas **labels**).

Ficando assim:

```python
def calcular(self):
    if self.en1.text() != '':      
        self.lb1.setText(f'{self.en1.text()}')
    else: 
        self.lb1.setText(f'<b><u>Digite um nome da empresa!</u></b>')
    if self.en1.text() != '':      
        self.lb2.setText(f'{self.en3.text()}')
    else: 
        self.lb2.setText(f'<b><u>Digite um nome da empresa!</u></b>')

    if (self.en2.text().isdecimal() == True) and (self.en4.text().isdecimal() == True):
        en1 = int(self.en2.text())
        en2 = int(self.en4.text())

        icms1 = self.icms(en1)
        icms2 = self.icms(en2)

        ipi1 = self.ipi(en1)
        ipi2 = self.ipi(en2)

        pis1 = self.pis(en1)
        pis2 = self.pis(en2)

        cofins1 = self.cofins(en1)
        cofins2 = self.cofins(en2)

        total1 = self.total(icms1, ipi1, pis1, cofins1, en1)
        total2 = self.total(icms2, ipi2, pis2, cofins2, en2)

        calcImpostos = icms1+icms2+ipi1+ipi2+pis1+pis2+cofins1+cofins2
        calcMercadorias = (en1*4.50)+(en2*4.50)
        calcGeral = calcImpostos+calcMercadorias

        calcDesconto1 = self.desconto(en1, total1)
        calcDesconto2 = self.desconto(en2, total2)

        self.lb3.setText(f'R$ {icms1}')
        self.lb4.setText(f'R$ {icms2}')

        self.lb5.setText(f'R$ {ipi1}')
        self.lb6.setText(f'R$ {ipi2}')

        self.lb7.setText(f'R$ {pis1}')
        self.lb8.setText(f'R$ {pis2}')

        self.lb9.setText(f'R$ {cofins1}')
        self.lb10.setText(f'R$ {cofins2}')

        self.lb11.setText(f'R$ {total1}')
        self.lb12.setText(f'R$ {total2}')

        self.lb13.setText(f'Total Impostos: R$ {calcImpostos}')
        self.lb14.setText(f'Total Mecadorisas: R$ {calcMercadorias}')
        self.lb15.setText(f'Total Geral: R$ {calcGeral}')

        if calcDesconto1 != False: 
            self.lb16.setText(f'Desconto (empresa {self.en1.text()}): R$ {calcDesconto1}')
        else:
            self.lb16.setText(f'<b><u>Desconto liberado apenas acima de 1000 itens!</u></b>')
        if calcDesconto2 != False:
            self.lb17.setText(f'Desconto (empresa {self.en3.text()}): R$ {calcDesconto2}')
        else:
            self.lb17.setText(f'<b><u>Desconto liberado apenas acima de 1000 itens!</u></b>')
    else:
        self.lb1.setText("")
        self.lb2.setText("")
        self.lb3.setText("")
        self.lb4.setText("")
        self.lb5.setText("")
        self.lb6.setText("")
        self.lb7.setText("")
        self.lb8.setText("")
        self.lb9.setText("")
        self.lb10.setText("")
        self.lb11.setText("")
        self.lb12.setText("")
        self.lb13.setText("Total Impostos: ")
        self.lb14.setText("Total Mercadorias: ")
        self.lb15.setText("Total Geral: ")
        self.lb16.setText("Desconto: R$ ")
        self.lb17.setText("Desconto: R$ ")
```

***

# Criador

Olá me chamo Gustavo, e criei este material, para mais informações, clique nos links abaixo:

* [LinkTree](https://www.linktree.com.br/gusleaooliveira)


* Disponível em : [Repositório de exercícios](https://gusleaooliveira.github.io/posts/)

