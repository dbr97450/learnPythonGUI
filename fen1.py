from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

__appname__ = "Motus"
class Fenetre(QDialog):
    def __init__(self,parent=None):
        super(Fenetre,self).__init__(parent)

        self.setWindowTitle("MOTUS")
        self.mot = QLabel("Nombre de lettres:")
        self.spinnbLettre = QSpinBox()
        self.labelEssai = QLabel("Essai n°")
        self.labelMot = QLabel("_ _ _ _")
        self.labelProp = QLabel("Proposition")
        self.labelpropSaisie = QLineEdit()

        self.ligneH = QFrame()
        self.ligneH.setFrameShape(QFrame.HLine)
        self.ligneH.setFrameShadow(QFrame.Sunken)

        self.bSoumettre = QPushButton("Soumettre")
        self.btnQuitter = QPushButton("Quitter")
        self.btnGo = QPushButton("Go !")

        #**********Bas de boite de dialogue
        hlayout = QHBoxLayout()
        hlayout.addStretch(4)
        hlayout.addWidget(self.bSoumettre)
        hlayout.addWidget(self.btnQuitter)
        hlayout.addStretch(4)
        #******Partie centrale
        layout = QGridLayout()
        layout.addWidget(self.labelEssai,0,0)
        layout.addWidget(self.labelMot,0,1)
        layout.addWidget(self.labelProp,1,0)
        layout.addWidget(self.labelpropSaisie,1,1)
        #********Partie haute
        h2layout = QHBoxLayout()
        h2layout.addStretch(1)
        h2layout.addWidget(self.mot)
        h2layout.addWidget(self.spinnbLettre)
        h2layout.addStretch(1)
        h2layout.addWidget(self.btnGo)
        h2layout.addStretch(4)
        #***********Layout final
        vlayout = QVBoxLayout()
        vlayout.addLayout(h2layout)
        vlayout.addWidget(self.ligneH)
        vlayout.addLayout(layout)
        vlayout.addStretch(4)
        vlayout.addLayout(hlayout)

        self.setLayout(vlayout)

        self.btnQuitter.clicked.connect(self.close)
        self.btnGo.clicked.connect(self.commencer)

    def commencer(self):
        """
        verifie le nombre de lettres
        :return:
        """
        class NbLettreFaux(Exception): pass
        try:
            if self.spinnbLettre.value() < 6 or self.spinnbLettre.value() > 9:
                raise NbLettreFaux("Nb lettres compris entre 6 et 9")

        except NbLettreFaux as msg:
            QMessageBox.warning(self,__appname__,str(msg))
            self.spinnbLettre.selectAll()
            self.spinnbLettre.setFocus()

    """
    def ouvreOK(self):
        QMessageBox.information(self,"Information","Le message est passé: "+self.entreenom.text())
        #self.accepted.connect(app.close)
    """
app = QApplication(sys.argv)
fen = Fenetre()
fen.show()
app.exec_()