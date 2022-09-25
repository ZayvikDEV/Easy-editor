import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore  import QSize    
from PIL import Image
from PIL.ImageFilter import (
BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
GaussianBlur, UnsharpMask
)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filenme = None
        self.save_dir = "Modified/"
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
    def showImage(label, path):
        lb_image.hide()    
        pixmapimage = QPixmap(path)
        w = lb_image.width()
        h = lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_sharp(self):
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_blur(self):
        self.image = self.image.filter(BLUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_cont(self):
        self.image = self.image.filter(CONTOUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_detal(self):
        self.image = self.image.filter(DETAIL)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_edge(self):
        self.image = self.image.filter(EDGE_ENHANCE)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_edge2(self):
        self.image = self.image.filter(EDGE_ENHANCE_MORE)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_ebosh(self):
        self.image = self.image.filter(EMBOSS)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_fedge(self):
        self.image = self.image.filter(FIND_EDGES)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_smooth(self):
        self.image = self.image.filter(SMOOTH)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_smooth2(self):
        self.image = self.image.filter(SMOOTH_MORE)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_blur2(self):
        self.image = self.image.filter(GaussianBlur)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_notsharp(self):
        self.image = self.image.filter(UnsharpMask)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)











workimage = ImageProcessor()

app = QApplication([])
win = QWidget()
win.setWindowTitle('Easy Editor')
win.resize(1000, 1000)
lb_image = QLabel("Выберите папку/картинку")
btn_dir = QPushButton("Выбрать папку")
lw_files = QListWidget()

btn_dir.setMinimumSize (QSize ( 160 , 55 )) 

btn_left = QPushButton("Повернуть влево")
btn_right = QPushButton("Повернуть вправо")
btn_flip = QPushButton("Отзеркалить")
btn_sharp = QPushButton("Повысить резкость")
btn_bw = QPushButton("перевести в ч\б")
btn_blur = QPushButton("Размыть")
btn_cont = QPushButton('''Оставить контур
(черным по белому)''')
btn_detal = QPushButton("Повысить шум")
btn_edge = QPushButton("Повысить четкость")
btn_edge2 = QPushButton('''Сильно повысить 
шум''')
btn_ebosh = QPushButton("Сделать как чеканка")
btn_fedge = QPushButton('''Оставить контур
(белым по черному)''')
btn_smooth = QPushButton("Понизить ")
btn_smooth2 = QPushButton('''Размыть 
по пикселям''')
btn_blur2 = QPushButton("Сильно размыть")
btn_notsharp = QPushButton("Повысить контраст")

btn_left.setMinimumSize (QSize ( 160 , 55 ))
btn_right.setMinimumSize (QSize ( 160 , 55 ))
btn_flip.setMinimumSize (QSize ( 160 , 55 ))
btn_sharp.setMinimumSize (QSize ( 160 , 55 ))
btn_bw.setMinimumSize (QSize ( 160 , 55 ))
btn_blur.setMinimumSize (QSize ( 160 , 55 ))
btn_cont.setMinimumSize (QSize ( 160 , 55 ))
btn_detal.setMinimumSize (QSize ( 160 , 55 ))
btn_edge.setMinimumSize (QSize ( 160 , 55 ))
btn_edge2.setMinimumSize (QSize ( 160 , 55 ))
btn_ebosh.setMinimumSize (QSize ( 160 , 55 ))
btn_fedge.setMinimumSize (QSize ( 160 , 55 ))
btn_smooth.setMinimumSize (QSize ( 160 , 55 ))
btn_smooth2.setMinimumSize (QSize ( 160 , 55 ))
btn_blur2.setMinimumSize (QSize ( 160 , 55 ))
btn_notsharp.setMinimumSize (QSize ( 160 , 55 ))


row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image, 10)
row_tools = QHBoxLayout()
row_tools2 = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools2.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools2.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
row_tools2.addWidget(btn_blur)
row_tools.addWidget(btn_cont)
row_tools2.addWidget(btn_detal)
row_tools.addWidget(btn_edge)
row_tools2.addWidget(btn_edge2)
row_tools.addWidget(btn_ebosh)
row_tools2.addWidget(btn_fedge)
row_tools.addWidget(btn_smooth)
row_tools2.addWidget(btn_smooth2)
row_tools.addWidget(btn_blur2)
row_tools2.addWidget(btn_notsharp)
col2.addLayout(row_tools)
col2.addLayout(row_tools2)

row.addLayout(col1, 20)
row.addLayout(col2, 150)
win.setLayout(row)

workdir = ''
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def showFilenamesList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)

def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)



lw_files.currentRowChanged.connect(showChosenImage)

btn_dir.clicked.connect(showFilenamesList)

win.show()

btn_bw.clicked.connect(workimage.do_bw)
btn_flip.clicked.connect(workimage.do_flip)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_sharp.clicked.connect(workimage.do_sharp)
btn_blur.clicked.connect(workimage.do_blur)
btn_cont.clicked.connect(workimage.do_cont)
btn_detal.clicked.connect(workimage.do_detal)
btn_edge.clicked.connect(workimage.do_edge)
btn_edge2.clicked.connect(workimage.do_edge2)
btn_ebosh.clicked.connect(workimage.do_ebosh)
btn_fedge.clicked.connect(workimage.do_fedge)
btn_smooth.clicked.connect(workimage.do_smooth)
btn_smooth2.clicked.connect(workimage.do_smooth2)
btn_blur2.clicked.connect(workimage.do_blur2)
btn_notsharp.clicked.connect(workimage.do_notsharp)

app.exec()



