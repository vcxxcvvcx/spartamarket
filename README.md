# 스파르타 중고마켓 - 회원들을 위한 중고거래플랫폼 
스파르타 중고마켓은 회원들을 위한 중고거래 플랫폼 입니다.
사용자들은 로그인후 자신의 중고물품을 게시 수정 삭제할수 있으며, 다른 사용자의 프로필을 팔로우 할 수 있습니다.


### 18조 박혜진


## 개발 기간
* 24.04.12 ~ 24.04.19 


### 개발 환경
* Backend: Django, SQLite
* Frontend: HTML, CSS, Bootstrap


## 주요 기능
#### 사용자 인증
- 사용자는 등록, 로그인 및 로그아웃을 할 수 있습니다.
#### 게시글 CRUD
- 게시글 작성, 조회, 수정, 삭제
#### 게시글 관련 추가 기능
- 좋아요 기능
- 게시글 목록 페이지
- 프로필페이지 팔로우기능

## 디렉토리 구조 (주요 파일 및 폴더)
#### accounts/: 사용자 인증과 관련된 기능을 처리
#### products/: 상품 게시물 관련 기능을 관리
#### spartamarket/: 프로젝트 설정과 URL
#### templates/: Django 템플릿 파일
#### static/: CSS, 이미지 등의 정적파일

## 실행방법
#### 파일 오픈후 터미널 실행
#### python -m venv venv
#### source venv/Scripts/activate  (윈도우의 경우)
#### pip install django==4.2
#### python -m pip install Pillow

#### cd spartamarket
#### python manage.py makemigrations
#### python manage.py migrate
#### python manage.py runserver

#### TMI 
- 깃 이그노어를 나중에 올려서 venv에 적용하려다가 모든파일이 날아갈뻔해서 venv를 수동으로 날려버렸음
- 로그인을 해야지만 글을쓸수 있지만 수정삭제 는 아무나 할수있음 (시간되면 수정하겠음)
