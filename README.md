# Blue-Scheduler
블루아카이브 일정 관리 프로그램

개발 언어 : python 3.11.2, PyQt6

1. Home
    1) 공지가 올라오는 사이트 크롤링
    2) 넥슨 커뮤니티 - 주요사항 / 공지사항
        - [예정] 이미지 캐싱 사용 - 매번 접속마다 이미지 다운로드하는건 귀찮음.
    3) [예정] 트위터 - 트위터 디벨로퍼 승인 받으면 그때 시작
    4) [예정] 일정에 추가 기능
    5) 슬라이드쇼 - 업데이트 상세 페이지에서 이미지 추출 후 출력

[예정] 2. 일정
    1) 달력 형식
        - 모듈에는 마음에 드는게 없음. 그래서 달력 이미지에 테이블위젯을 위에 덮어서 일정 구현 예정 
    2) 하이퍼링크 형식으로 글 클릭시 사이트, 이미지로 이동 기능
    3) 알림 기능
  
[예정] 3. 재화 계산 - 다수 계산 과정 진행중
    1) 보유 재화, 성장 필요 재화 계산
    2) 프리셋 3개 예정(2~3달 필요한 재화, 모두 필요한 재화, 여유분)
        - 프리셋 버튼을 만들 예정. 화면을 여러개 만들지 말고 값만 변경하는 식으로 하면 될듯. 일단 2개 만들 예정이고 더 필요하다면 버튼 위치에 list로 구현예정.(아마 2개면 충분할듯)
    3) 리스트위젯으로 프리셋 구현
        - 컨테이너 만들어서 쭉 넣기.
        - 이게 한 화면에 다 나오게 하려면 항목이 좀 작아야됨. 그래서 고민. 이름은 글자/이미지 인데 글자 넣는게 깔끔한데 이미지가 더 눈에 들어오긴 하고.
4. AP 가이드
    1) 이벤트 제목, 점검 일정 입력
    2) 템플릿에 일정 출력 / 이미지 저장
    3) [예정] 일정에 추가 기능
    4) [예정] 이미지 공유
  
[예정] 5. 인게임 연동
    1) api가 공개돼 있나?
    2) 카페 상황, 현재 ap, 총력전,대항전 티켓 보유수
    3) 재화 연동

[예정] 6. 총력전/이벤트 조력자
    1) 따로 할 듯 

[예정] 7. 캐시 비우기
    1) images폴더 제거