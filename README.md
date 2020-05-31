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

---

### board-solver (Orb-H)

말 그대로 주어진 러시아워 퍼즐을 푸는 프로그램을 만드는 브랜치입니다.

#### 알고리즘

처음에는 되게 어렵게 생각했는데 생각보다 쉽게 풀 수 있더군요. 퍼즐판의 상태를 하나의 node로 하고, 이 상태에서 차 하나를 이동시키는 것을 edge로 하여 그래프를 만들 수 있습니다. 이제 초기 상태의 퍼즐을 시작 node로 하는 그래프를 BFS를 이용하여 생성과 동시에 탐색을 하다가 탈출하려는 차(기호 X)가 나가기 바로 전 위치에 존재하게 되는 node를 찾게 되면 그 순간까지의 모든 움직임을 반환합니다.

Python은 list를 dict의 key로 쓰거나 set의 원소로 사용할 수 없습니다. 그것은 list가 hash값을 가질 수 없기(unhashable) 때문입니다. 이를 위해 보조함수로 퍼즐판의 상태를 하나의 짧은 문자열로 합쳐주는 함수를 사용했습니다.

#### 사용법

[src/solver.py](src/solver.py)의 파일에 있는 `solve` 함수를 호출하여 문제를 풀 수 있습니다. 이 때 `solve` 함수의 매개변수로는 초기 상태의 퍼즐을 받는데, 이 퍼즐의 포맷은 길이 1의 문자열의 2차원 리스트여야 합니다. 예시는 아래와 같습니다.

```python
[
  ['.', 'A', 'A', 'E', 'B', 'P'],
  ['O', 'C', 'D', 'E', 'B', 'P'],
  ['O', 'C', 'X', 'X', 'B', 'P'],
  ['O', '.', 'F', 'Q', 'Q', 'Q'],
  ['G', 'G', 'F', '.', '.', '.'],
  ['.', '.', 'H', 'H', 'I', 'I']
]
```

각 문자열이 의미하는 바는 아래의 표와 같습니다.

|문자열|의미|
|:-:|-|
|`.`|빈 칸|
|`A` ~ `I`|길이 2의 자동차|
|`O` ~ `R`|길이 3의 트럭|
|`X`|탈출할 자동차
