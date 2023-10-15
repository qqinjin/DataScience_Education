import serial

# def ad_on():
#     with open('AD on_off.txt', 'r') as f:
#         word = f.readline().strip()
#         return word

ser = serial.Serial('com5', 9600)


while True:
    with open('AD on_off.txt', 'r') as f:
        word = f.readline()
        print(word)
    user_input = str(word)
    if user_input == '1':
        print(user_input)
        ser.write(b'1')
        print("실행 신호를 보냈습니다.")
    else:
        ser.write(b'0')
        print("종료 신호를 보냈습니다.")