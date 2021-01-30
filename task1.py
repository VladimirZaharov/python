import time


class TrafficLight:

    def running(self):
        self.__color = ['красный', 'желтый', 'зеленый']
        while True:
            print(self.__color[0])
            time.sleep(7)
            print(self.__color[1])
            time.sleep(2)
            print(self.__color[2])
            time.sleep(8)


a = TrafficLight()
a.running()
