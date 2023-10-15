import pyfirmata
import time

# 아두이노 핀 번호
ENA = 6
in1 = 5
in2 = 4
Speed = 255

# 포트 설정
board = pyfirmata.Arduino('COM5')

ena_pin = board.get_pin('d:6:p')
in1_pin = board.get_pin('d:5:o')
in2_pin = board.get_pin('d:4:o')

duration = 2  # 회전 시간(초)

in1_pin.write(0)
in2_pin.write(1)
ena_pin.write(1.0)
time.sleep(duration)

ena_pin.write(0.0)  # 정지
time.sleep(duration)