# 비전 AI를 이용한 선박 항만 화재 감지 시스템

Yolo모델을 사용하여 신속하게 발화 순간을 탐지하여 웹 페이지에서 실시간 영상과 챗봇을 통해 사용자의 판단으로 상황에 맞는 소화, 경보 등 다양한 조치가 가능하다.


## 서비스 흐름도
![서비스흐름도](https://github.com/qqinjin/DataScience_Education/assets/99711238/a6ff0fef-a3fb-4908-b28a-c940c04b0580)

## 인공지능
### 딥러닝

<table>
  <tr>
    <th>YOLO 아키텍쳐</th>
  </tr>
   <tr>
    <td><img src="https://github.com/qqinjin/animal_serving_app/assets/99711238/c0e024aa-3d0b-40cd-a3f8-0e12bfb4f7b9)" alt="아키텍쳐"/></td>
  </tr>
</table>

- 실시간 객체 탐지 딥러닝 모델
- 이미지 전체를 한 번만 처리하여 객체의 위치와 클래스를 동시에 예측
- 기존의 R-CNN이나 Fast R-CNN 같은 모델들은 여러 단계의 연산과 이미지에 대한 반복적인 스캔이 필요하여 연산과 시간적인 한계 존재
- 이러한 이유로, 더 빠르고 효율적인 YOLO 모델을 선정

### Yolo 학습 결과
|         | Yolov5x | Yolov7x | Yolov8x |
|:-------:|:-------:|:-------:|:-------:|
| mAP@0.5 |  0.832  |  0.823  |  0.831  |

- 발화 요인인 불, 연기, 스파크 이미지 데이터는 약 4만. 레이블 수 약 12만 그리고 7 : 2 : 1로 데이터 셋 구성
- GPU : RTX3060, VRAM : 12GB, Epochs : 300, Batch Size : 2
- 학습 시간은 약 v5 : 11일, v7 : 10일, v8 : 4일 소요
- v8은 colab pro를 사용하여 학습 속도가 비교적 빨랐음

- 데이터 출처: roboflow 플랫폼, 유튜브 영상 프레임, 웹 크롤링, Cycle-GAN을 활용한 이미지
- 데이터 수량: (불, 연기, 스파크)이미지를 각각 15000, 15000, 8000장, 레이블 수 각 각 약 4만개
- 데이터 분할: 학습, 검증, 테스트 세트로 데이터를 7:2:1의 비율로 분할
- 학습 설정:
  - Batch Size: 2
  - Epochs: 3~500
  - 학습 환경: 로컬PC RTX3060, VRAM : 12GB

## Cycle-GAN
<table>
  <tr>
    <th>Cycle-GAN 아키텍쳐</th>
  </tr>
   <tr>
    <td><img src="https://github.com/qqinjin/DataScience_Education/assets/99711238/8e2a6163-1f9d-46b8-81a0-f7bfa3dac1b6)" alt="아키텍쳐"/></td>
  </tr>
</table>

- 안개속 상황의 탐지을 위한 데이터 수집을 위해 Cycle-GAN 사용
- 페어 이미지 데이터와 라벨링이 불필요한 비지도 학습방식
- 다른 두 도메인 사이의 스타일 변환을 양 방향으로 학습

#### Cycle-GAN 결과
![사이클갠결과사진](https://github.com/qqinjin/DataScience_Education/assets/99711238/96bcd705-a95a-4fcc-80be-4c3d34663317)

### 머신러닝

선박 내 화재 위험도 분석을 통해 생활하면서 주의를 주기위해 분석

- 데이터 출처: 기상청, 해양경찰청 등 공공데이터 포털에서 데이터를 수집
- 데이터 내용: 10년간 해양 경찰청에서 날짜별 선박 사고 원인 데이터, 기상청에서 그 지점에 대한 기상 데이터 
- 데이터 수량: 기상데이터 약 150만 선박 사고 데이터 약 2만 샘플
- 데이터 전처리: 기상 데이터에서 날짜와 지점을 바탕으로 데이터 합친 뒤, 화재에 관한 데이터만 남김
  1. 이후 결측치 제거 총 5천 샘플
  2. 상관관계 분석과 StandarScaler을 사용한 데이터 표준화 또는 MinMaxScaler을 사용한 정규화를 사용한 전치리
     
- 데이터 분할: 학습, 테스트 세트로 데이터를 7:3의 비율로 분할
- 학습 : RF, LR 등의 총 6가지 모델을 사용 및 그리드 서치 및 랜덤 서치를 사용하여 최적의 하이퍼파라미터 탐색 후 학습
  
#### 학습결과

|       Model      | Accuracy | Precision | Recall | F1 Score |
|:----------------:|:--------:|:---------:|:------:|:--------:|
|        RF        |   0.852  |   0.818   |  0.563 |   0.573  |
|      XGBoost     |   0.829  |   0.632   |  0.546 |   0.549  |
| GradientBoosting |   0.843  |   0.751   |  0.536 |   0.528  |
|    GaussianNB    |   0.813  |   0.569   |  0.529 |   0.526  |
|        LR        |   0.836  |   0.586   |  0.501 |   0.466  |
|        SVC       |   0.835  |   0.418   |  0.501 |   0.455  |   선박 내 화재 위험도 예측

## 하드웨어
<table>
  <tr>
    <th>아두이노 우노</th>
    <th>소화 노즐</th>
    <th>경광등</th>
    <th>웹캠</th>
  </tr>
  <tr>
    <td><img src="https://github.com/qqinjin/DataScience_Education/assets/99711238/eb1bbbb9-b7ee-4252-9121-7ba57ae62381)" alt="아두이노우노" width="250" height="250" /></td>
    <td><img src="https://github.com/qqinjin/DataScience_Education/assets/99711238/dedbe786-f301-48c0-96fd-efd5350dcaeb)" alt="아두이노소화노즐" width="250" height="250" /></td>
    <td><img src="https://github.com/qqinjin/DataScience_Education/assets/99711238/59b7ac36-a21d-434f-b6f9-ecc4466100fb" alt="아두이노경광등" width="250" height="250"/></td>
    <td><img src="https://github.com/qqinjin/DataScience_Education/assets/99711238/3aaac019-0466-4272-b969-97c0b1875ccc" alt="웹캠" width="250" height="250"/></td>
  </tr>
</table>

- 객체 탐지: 카메라를 통해 발화 요인 탐지
- 소화 기능: 모터 드라이버를 이용하여 화재 소화
- 경보 기능: 피에조 스피커를 이용한 화재 경보
 
## 소프트웨어
![웹원리](https://github.com/qqinjin/DataScience_Education/assets/99711238/2fc11959-139d-436a-a476-9fe169eacaba)
- 좌표기반의 날씨 정보를 API로 요청 후 화재 위험도 보조지표로 사용


## 서비스 영상
![영상](https://github.com/qqinjin/DataScience_Education/assets/99711238/a60ad306-61e8-4076-a5e7-7d8b311e4569)

- 실시간으로 객체 탐지 후 챗봇 알림으로 소화, 경보 등의 기능을 사용하는 영상

## 개발환경
#### 하드웨어 
- Arduino uno, 모터 드라이버, 

#### 소프트웨어 및 언어
- Python
- Pycharm
- Google Colab (GPU Pro)

## 사용 기술
#### 개발환경
- Vscode
- Google Colab (GPU Pro)
  
#### 하드웨어  
- Arduino uno
- Piezo speaker
- motor driver
- Web Cam
  
#### 소프트웨어 및 언어
- Python
- Pycharm
- AWS
  
## 파일
















