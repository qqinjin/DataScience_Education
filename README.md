# 비전 AI를 이용한 선박 항만 화재 감지 시스템

Yolo모델을 사용하여 신속하게 발화 순간을 탐지하여 웹 페이지에서 실시간 영상과 챗봇을 통해 사용자의 판단으로 상황에 맞는 소화, 경보 등 다양한 조치가 가능하다.

## 서비스 흐름도
![서비스흐름도](https://github.com/qqinjin/DataScience_Education/assets/99711238/a6ff0fef-a3fb-4908-b28a-c940c04b0580)

## Yolo 학습 결과
|         | Yolov5x | Yolov7x | Yolov8x |
|:-------:|:-------:|:-------:|:-------:|
| mAP@0.5 |  0.832  |  0.823  |  0.831  |
- 발화 요인인 불, 연기, 스파크 이미지 데이터는 약 4만. 레이블 수 약 12만 그리고 7 : 2 : 1로 데이터 셋 구성
- GPU : RTX3060, VRAM : 12GB, Epochs : 300, Batch Size : 2
- 학습 시간은 약 v5 : 11일, v7 : 10일, v8 : 9일 소요
 
## Cycle-GAN 아키텍처
![사이클갠아키텍쳐](https://github.com/qqinjin/DataScience_Education/assets/99711238/8e2a6163-1f9d-46b8-81a0-f7bfa3dac1b6)
- 안개속 상황의 탐지을 위한 데이터 수집을 위해 Cycle-GAN 사용
- 페어 이미지 데이터와 라벨링이 불필요한 비지도 학습방식
- 다른 두 도메인 사이의 스타일 변환을 양 방향으로 학습
  
## Cycle-GAN 결과
![사이클갠결과사진](https://github.com/qqinjin/DataScience_Education/assets/99711238/96bcd705-a95a-4fcc-80be-4c3d34663317)

## 종합관리 웹 대쉬보드
![웹원리](https://github.com/qqinjin/DataScience_Education/assets/99711238/2fc11959-139d-436a-a476-9fe169eacaba)
- 좌표기반의 날씨 정보를 API로 요청 후 화재 위험도 보조지표로 사용

## 서비스 영상
![영상](https://github.com/qqinjin/DataScience_Education/assets/99711238/a60ad306-61e8-4076-a5e7-7d8b311e4569)

실시간으로 객체 탐지 후 챗봇 알림으로 경보 및 소화 기능을 사용하는 영상







