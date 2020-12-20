import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


"""
Explicação do código está no arquivo: index.md
Ou em: https://gusleaooliveira.github.io/energeticos-accelerator/ 
"""

class Programa:
    def icms(self, quantidade):
        return round((4.5*quantidade)*0.18, 2)

    def ipi(self, quantidade):
        return round((4.5*quantidade)*0.04, 2)

    def pis(self, quantidade):
        return round((4.5*quantidade)*0.01860, 2)

    def cofins(self, quantidade):
        return round((4.5*quantidade)*0.0854, 2)

    def total(self, calculoIcms, calculoIpi, calculoPis, calculoCofins, quantidade):
        valorUnitario = 4.5*quantidade 
        return (calculoIcms+calculoIpi+calculoPis+calculoCofins)+valorUnitario
        
    def desconto(self, quantidade, total):
        if quantidade >= 1000:
            return total*0.35
        else:
            return False

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


    def __init__(self):
        super().__init__()

        self.app = QApplication(sys.argv)

        self.janela = QWidget()
        self.janela.setWindowTitle("Energéticos Accelerator")
        self.janela.resize(800, 600)
        self.janela.show()
     
    
        self.janela.setLayout(self.ui())

        sys.exit(self.app.exec_())

if __name__ == '__main__':
    Programa()

    
    
