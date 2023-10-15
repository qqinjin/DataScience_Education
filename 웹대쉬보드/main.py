import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lat = "35.3"
    lon = "128.7"
    apiKey = "a925fba4ba02e326018e5bac4fcaef54"
    lang = 'kr'
    units = 'metric'
    api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}&lang={lang}&units={units}"
    result = requests.get(api).json()

    windpower = result['wind']['speed']
    temperature = result['main']['temp']
    humidity = result['main']['humidity']

    # 데이터 불러오기
    filename = 'C:/Users/admin/PycharmProjects/pythonProject2/data(no5000).csv'
    data = pd.read_csv(filename, encoding='CP949')

    # 특성(feature) 선택
    features = ['습도(%)', '풍속(m/s)', '기온(°C)']
    X = data[features]
    y = data['발생유형']

    # 학습 데이터와 테스트 데이터 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 그라디언트 부스팅 모델 생성
    gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=50)
    gb.fit(X_train, y_train)

    # 정확도 출력
    train_score = gb.score(X_train, y_train)
    test_score = gb.score(X_test, y_test)
    print("Train 정확도: {:.2f}".format(train_score))
    print("Test 정확도: {:.2f}".format(test_score))

    # 새로운 데이터로 예측
    new_data = [[humidity, windpower, temperature]] # 습도, 풍속, 기온
    new_pred = gb.predict_proba(new_data)
    danger_rate = round(new_pred[0][1] * 100, 2) # 소수점 둘째자리까지 반올림

    return render_template('test.html', lon=lon, lat=lat, windpower=windpower,
                           temperature=temperature, humidity=humidity, danger_rate=danger_rate)

if __name__ == '__main__':
    app.run(debug=True)