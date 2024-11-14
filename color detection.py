import os
import cv2
import numpy as np
from PIL import Image

def get_limits(color):
    c = np.uint8([[color]])
    hsvc = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)#pasar valores rgb a hsv por que son mas crema

    lower_limit = hsvc[0][0][0] - 10, 100, 100
    upper_limit = hsvc[0][0][0] + 10, 255, 255 #este rollo crea el rango de color que detectamos porque si no seria solo un tono especifico

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8) #esto lo convierte a un array de numpy porque mola mas(opencv funciona con arrays es lo que hay)
                                                        #lo del uint8 es porque vamos a usar solo 8 bits en vez de 32. (con 8 bits solo llegamos a 255 es blanco)
                                                        #en vez de hacer codigo que mira si el numero supera 255, limitamos la capacidad a 255 y el carry se descarta

    return lower_limit, upper_limit

def main():
    capt = cv2.VideoCapture(0) #crea un array con la escala rgb de cada pixel que ve la camara
    while True: #bucle que actualiza lo que ve la camara y da efecto de video
        ret, frame = capt.read()
        
        #yellow = [0,255, 255]
        yellow = [87 ,213, 222]
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_limit, upper_limit = get_limits(color=yellow)
        mask = cv2.inRange(hsv_image, lower_limit, upper_limit)#mask es lo que muestra SOLO los pixeles del color deseado

        cv2.imshow("frame", mask) #esto muestra la imagen, si quieren ver vide en vez de la mascara cambien "mask" por "frame"

        if cv2.waitKey(1) & 0xFF == ord("l"): #esto es que cierras el video pulsando la letra l de luis, porque a mi me da la gana
            break
    capt.release()
    cv2.destroyAllWindows

if __name__ == "__main__":
    main()