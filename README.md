# 비전 AI를 이용한 선박 항만 화재 감지 시스템

Yolo모델을 사용하여 신속하게 발화 순간을 탐지하여 웹 페이지에서 실시간 영상과 챗봇을 통해 사용자의 판단으로 상황에 맞는 소화, 경보 등 다양한 조치가 가능하다.

## 서비스 흐름도
![서비스흐름도](https://github.com/qqinjin/DataScience_Education/assets/99711238/fd1e40e3-115a-453d-9bfc-e43e974ff9df)

## Yolov5x
![yolo결과](https://github.com/qqinjin/DataScience_Education/assets/99711238/d92e3f5e-862a-4ce0-a441-7288095561cb)

## Cycle-GAN 아키텍처
![사이클갠아키텍쳐](https://github.com/qqinjin/DataScience_Education/assets/99711238/2168b178-fb71-4bd9-a374-b0ce43b055ff)
- 안개속 상황의 탐지을 위한 데이터 수집을 위해 Cycle-GAN 사용
- 페어 이미지 데이터와 라벨링이 불필요한 비지도 학습방식
- 다른 두 도메인 사이의 스타일 변환을 양 방향으로 학습
  
## Cycle-GAN 결과
![사이클갠결과사진](https://github.com/qqinjin/DataScience_Education/assets/99711238/339d2c10-0bf0-4bb7-b4d7-77f4078270cd)

## 종합관리 웹 대쉬보드
![웹원리](https://github.com/qqinjin/DataScience_Education/assets/99711238/c3b30cde-efd0-4230-b610-819fb3272b69)
- 좌표기반의 날씨 정보를 API로 요청 후 화재 위험도 보조지표로 사용







