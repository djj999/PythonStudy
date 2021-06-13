### 아나콘다 가상환경 설정  (암호화폐 Trader 개발문서)
아나콘다에 pyqt가 포함되어 있음
##pyqt할 때 필요한 두 가지
### 1. QApplication 인스턴스
### 2. 이벤트 루프
    Gui 프로그램이 '종료'버튼을 누르기 전까지 계속 실행되려면 for나 while 같은 '루프'가 필요한데, 그것이 이벤트 루프이다
    이벤트 루프는 QApplication 클래스의 exec_() 메서드를 호출함으로써 생성할 수 있습니다
    PyQt클래스를 사용하기 위해서라도 위의 메서드는 호출되어야 한다

    import sys
    from PyQt5.QtWidgets import *
 
    app = QApplication(sys.argv) 
    label = QLabel("Hello")
    label.show()
    app.exec()    # 이벤트 루프 생성

![img.png](../img.png)

    버튼과 같은 컴포넌트(구성요소)를 '위젯'이라 부른다

### 메인윈도우 생성
    QMainWindow 나 QDialog 를 사용

    import sys
    from PyQt5.QtWidgets import *

    class MyWindow(QMainWindow):
        def __init__(self):
            super().__init__()


    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

### 나만의 윈도우 클래스 정의

    import sys
    from PyQt5.QtWidgets import *

    class MyWindow(QMainWindow):
        def __init__(self):
            super().__init__()   #부모클래스 초기화자 호출, super는 부모클래스의 객체를 호출할 때 사용하는 것.

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

    "PyQt가 제공하는 클래스를 상속받는 경우 부모 클래스의 초기화자를 명시적으로 호출해줘야 한다."

### 윈도우 크기 조절, 출력 위치 조절
    setGeometry()
    ----
    import sys
    from PyQt5.QtWidgets import *

    class MyWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setGeometry(100, 200, 300, 400) #윈도우 좌상단 (X축, Y축, 너비, 높이) 

 
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

### 윈도우 제목, 아이콘 변경
    setWindowTitle()
    -----
    class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 200, 300, 200)
        self.setWindowTitle("PyQt")
    ---------------------------------------------------
    setWindowIcon()      16 * 16 크기의 png 파일
    ---
    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *

    class MyWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setGeometry(100, 200, 300, 200)
            self.setWindowTitle("PyQt")
            self.setWindowIcon(QIcon("icon.png"))
    --------
    setWindowIcon() 메서드는 QIcon 클래스의 인스턴스를 인자로 받습니다.
    QIcon 클래스의 인스턴스를 생성할 때는 초기화자로 아이콘 파일의 경로를 문자열로 넘겨주면 됩니다.
    현재 예에서는 소스코드와 아이콘 파일이 같은 디렉터리에 있기 때문에 파일 이름만 적어주면 됩니다. 
    QIcon 클래스는 QtGui 파일에 정의되어 있기 때문에 from PyQt5.QtGui import *를 추가해야 합니다.

### 버튼 추가
