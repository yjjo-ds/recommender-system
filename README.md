# awsome recommender system
*Last updated : 2022/12/31*

A curated content of awesome recommender system resources. Inspired by [`awesome-architecture-search`](https://github.com/sdukshis/awesome-ml) and [`awesome-automl`](https://github.com/hibayesian/awesome-automl-papers) and [`awesome anomaly detection`](https://github.com/hoya012/awesome-anomaly-detection).   




## What is recommender system?
Recommender systems are information filtering systems that deal with the problem of information overload [1] by filter-ing vital information fragment out of large amount of dynami-cally generated information according to user’s preferences, interest, or observed behavior about item. [`link`](https://www.sciencedirect.com/science/article/pii/S1110866515000341)

## technique
<p align="center">
  <img width="600" src="/images/rs_techniques.png" "Example of techniques.">
</p>

----
## Business Process
#### 필요한 데이터셋
- 행동 데이터(상품 클릭, 구매 등)
- 유저의 과거 행동이력 데이터(클릭, 과거 특정 기간동안의 상품 상세 페이지 확인 이력, 구매 이력 등)
- 굉장히 개인적인 추천이 가능하나 대규모 이력 데이터가 필요하여 고도화된 추천을 위해서는 시간이 걸리는 편

#### 추천 유형
- 협업 필터링 (collaborative filtering) : 구매 및 소비한 제품에 대한 소비자의 평가 패턴이 비슷한 집단 속에서 서로 접하지 않은 제품을 추천하는 기술
- 내용 기반 필터링 (content-based filtering) : 
- 지식 기반 필터링 (knowledge-based filtering)
- 딥러닝 (deep learning)
- 하이브리드 필터링(협업 필터링 & 딥러닝)

- 사물기반 추천(상품 속성 랭킹 유형, 연관 상품 유형, 상품 선호 유형, 상품 니즈 유형)
- 사람 기반(유사 행동 유형, 협업 필터링, 설문 기반 유형)

#### 추천시스템 구축 이슈

