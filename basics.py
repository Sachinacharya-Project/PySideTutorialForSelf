import sys, os
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

ROOT = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.path.join(ROOT, 'qml/basics.qml'))
    
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())