# rushhour-gui
Suddenly thought to make a gui program for solving rush-hour since I couldn't solve grand-master difficulty in rush-hour...

### 개발 환경(예정)

- Python: 3.7
- GUI: pygame

### git 사용 방식

- 기능별 branch 생성
  - branch 이름 규칙: (사용자 이름)/(개발 내용) ex) orb-h/frontend-resources
- 각 branch 기능을 설명하는 문서 또는 개발 방향 등에 관련된 내용은 README에 적고 나중에 merge할 때 README는 수동으로 merge
- branch 별 README 내용은 아래에 있는 가로선 아래에 작성하고, 내용이 끝나면 가로선으로 닫기. 즉, 각 branch의 README 내용을 가로선으로 구분할 예정
  - 단, 수정 보완하는 형식의 branch의 README는 기존 branch의 README와 가로선으로 구분하지 않고 sub-header로 이어서 쓸 예정
- 가능한 한 merge 기능을 열심히 썼으면 좋겠읍니다...

---

### frontend-resources (Orb-H)

프론트엔드에 사용될 리소스를 생성한 브랜치입니다. svg 폴더 안에 있는 4개의 svg 파일(OX, OY, XX, XY)을 기반으로 여러 색상~~색놀이~~의 자동차와 트럭을 만들었습니다. 여기에 사용한 색의 목록은 [resources/colors.json](resources/colors.json)에 있습니다. 이왕이면 RGB 값을 `0x00`, `0x40`, `0x80`, `0xc0`, `0xff`만 사용하도록 노력했습니다. 또한 svg 폴더의 board와 cell을 이용하여 보드판과 판의 각 칸의 이미지도 만들었습니다.
