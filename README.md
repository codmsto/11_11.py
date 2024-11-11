## 1. 개발환경 구축
### 1-1. 다운로드
- anaconda
- vscode

### 1-2. 아나콘다 가상환경 세팅
- conda env list (가상환경 생성)
- conda create -n developer python:3.11 (가상환경 접속)
- conda activate developer (가상환경 생성)
- pip list (가상환경의 라이브러리 목록 보기)
- pip install pandas (pandas )
- cls (화면 클리어)

### 1-3. VSCODE 세팅
1. Extensions 설치
 - Python
 - prettier
 - Python Extension Pack
 - Atom Material Theme
 - Atom Material Icons
2. Settings
- [Mouse Wheel Zoom 켜기]
3. Thema 설정
4. 아나콘다 가상환경 주입
 - [Ctrl] + [Shift] + [p] -> "Python: Select Interpreter" 클릭 후

### 1-4. 명령어 단축키
 - [Ctrl] + [,] : Settings 열기
 - [Ctrl] + [`] : 터미널 열기





## 2. 데이터베이스(Database)
- 데이터를 효율적으로 관리하고 저장하는 시스템


### 2-1.DBMS(데이터베이스 관리 시스템)
1. 관계형 DB(RDB)
  - 표(Table)형태
  - MariaDB, Oracle, MySQL, PostgreSQL

### 2-2. SQL(구조질의언어)
  - DBMS에게 명령을 내리기 위한 언어
  - 예) SELECT * FROM tbl_user;


# 아래 지워도 됨
# 국가공인
#  - SQLD -> SQL + DB.이론
#  - ADsP -> 데이터분석 + 머신러닝
#  - 리눅스마스터 1급 -> 기초 리눅스

# 국제
#  - 도커
#  - AWS
#  - OCP(오라클)

### 2-3. 설치 방법
  1. 로컬 설치(설치파일 다운로드 직접 설치)
  2. 로컬 도커 
  3. 클라우드 


### 2-4. 데이터 베이스 구조
  1. DBMS(데이터베이스 관리 시스템 ) -> MariaDB,MySQL,Oracle,PostgreSQL
  2. ㄴ Database -> chosun
  3.       ㄴ Table(표) -> tbl_news

  예) Database는 프로젝트 단위(일반적)
  Database(쇼핑몰)
    ㄴ Table(회원)
    ㄴ Table(상품)
    ㄴ Table(구매)
    ㄴTable(게시판)
    ㄴTable(고객센터)


### 2-5. 데이터베이스 연결
  - python <-> Database
  1. SQL 매핑: SQL 작성해서 사용하는 방법
  2. ORM(Object Realationship Mapping):객체를 사용하는 방법
  * 실무 -> ORM 많이 사용
            ㄴ SQL 복잡도 증가 한계 -> SQL 매핑
  
### 2-6. SQL 매핑
  1. Connection 맺기 (IP, PORT, ID, PW)
     python - Database 연결(다리 건설)
      -> IP: 컴퓨터의 주소
      -> PORT: 프로그램마다 포트(3306)
      -> ID&PW: 인증
  2. Worker 생성(cursor 객체)
  3. Job 생성(SQL 작성)
  4. Execute(실행 -> Worker + Job)
  5. 결과

## 3. 도커
  - 컨테이너 가상화 기술을 사용할 수 있는 프로그램
  - 컨테이너를 사용하기 위해서는 -> 도커엔진 + 도커이미지
  - 도커이미지 -> 도커 컨테이너의 설계 도면
  - 도커엔진 -> 도커이미지대로 컨테이너를 만들어서 실행

### 3-1. 도커 명령어
   - docker ps                   # 현재 실행중인 컨테이너 목록 확인
   - docker images               # 도커 이미지 목록 확인
   - docker logs [컨테이너 이름]  # 도커 컨테이너 로그 확인
   - docker run                  # 도커 컨테이너 실행
   
   docker run --name mariadb -d -p 3306:3306 -e
   MARIADB_ROOT_PASSWORD=mariadb mariadb
   
















## 99. 전체 시스템 구조(학습용) - WEB/APP
- Client-Server 구조
- *Client: 고객(웹 브라우저)
- *Server: 회사(서비스를 동작하는 컴퓨터)
- A(클라이언트) -> 카톡 -> 서버(카카오톡) -> 카톡 -> B(클라이언트)

1. 동작 순서
  + 클라이언트(naver.com) 요청!
  + 네이버 서버(메인 페이지에 필요한 소스들을 전송 -> 클라이언트)
  + 클라이언트 소스 다운로드
  + 클라이언트 랜더링

2. 구조
                 *네트워크*        클라우드 컴퓨팅(AWS)
Client         -> 요청(request) -> Server(LINUX) *운영체제*
Client(랜더링) <- 전송(response) <- ㄴ 컨테이너(도커) 
                                       ㄴ 프론트엔드(HRML,CSS,JS,React.js,Vue.js)
                                       ㄴ 백엔드(Spring,FastAPI,Express,Django)
                                       ㄴ *데이터베이스*(RDB,NOSQL)

*프로그래밍 언어*(Python,JAVA)
디자인 패턴
*자료구조*




