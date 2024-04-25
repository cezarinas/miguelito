import wpilib
import cscore as cs


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Inicializa la cámara USB
        self.camera = cs.UsbCamera("CamaraUSB", 0)  # Asume que es la primera cámara conectada
        self.camera.setResolution(640, 480)

        # Crea un servidor de transmisión de video
        self.cvSink = cs.CvSink("cvsink")
        self.cvSink.setSource(self.camera)

        # Crea un servidor para enviar imágenes al dashboard
        self.outputStream = cs.MjpegServer("serve_Camera", 1181)
        self.outputStream.setSource(self.camera)


if _name_ == "_main_":
    wpilib.run(MyRobot)
# TODO: insert robot code here
