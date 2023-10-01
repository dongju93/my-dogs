# THIS IS "MYDOGS" FULL STACK PROJECT 2020 UPDATE

---
heroku를 통해 build를 완성했지만
Django 가상환경인 venv/lib/site-package에 있는 몇몇 파일을 수정해야하는데
직접 접속해서 파일을 수정 할 수 있는 방법을 찾을 수 없어
보류. 우선순위 뒤로.
---
IMPORTANT UPDATE
## 2020 프로젝트 수정 및 heroku 배포 중단.

업로드 된 파일의 수정 불가피, heroku로 build 시 requirement 로 자동 설치돼어  
venv/site-packages 경로를 통해 실행될 file의 수정 불가능  
(몇몇 plugin 들의 경우 django 버전 업데이트에 따른 호환성 문제로 수정이 불가피)  
(수정 시 해당 heroku 세션에서만 수정된 파일이 적용) 
* 실제 plugin 파일은 [ /app/.heroku/python/lib/python3.x/site-packages/~ ] 경로에서 실행

기존 aws ec2 를 이용한 배포 시 무료 사용은 유지 기간의 한계에 도달.  
유료로 전환 혹은 ec2 를 다운 시켜야하는 상태 발생 (서버 유지 불가능).  
→ docker 를 이용한 ubuntu 배포 시 배포를 위한 ubuntu 서버 가동이 필수적이나  
무료로 가동 가능 및 필요할 때만 노트북의 리소스 사용.  
ubuntu 파일 시스템을 로컬 환경에서 관리 가능 (WIN 10 PRO 2004 ver.)
---
### 0. Basic interpreter version update: 3.7 -> 3.8.2
### 1. Django version update: 2.2 -> 3.0
### 2. MySQL version update: 5.7 -> 8.0
### 3. MySQL connector change: mysqlclient -> PyMysql
### 4. Host server change: Amazon AWS EC2 -> Heroku
### 5. Django ORM update and optimize
### 6. Product catalog Korean language support: url "SLUG:" remove
### 7. IAMPORT payment more clarify: each order add datetime

### 99. Code review