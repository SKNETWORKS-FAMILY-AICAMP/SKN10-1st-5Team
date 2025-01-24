# SKN10-1st-5Team
![Image](https://github.com/user-attachments/assets/51c829fe-ac31-471b-aa5d-092e4ad45a12)

## 프로젝트 주제
<br/>


**전국 자동차 등록 현황 및 기업 FAQ 조회 시스템**
<br/>
<br/>
## 📅 프로젝트 기간
**2025.01.20(월요일) ~ 2025.01.24(목요일)** (총 5일) <br/>
<br/>
<br/>

## 🌟 프로젝트 팀 및 역할
<br/>


| 최수헌🧐 | 남궁세정📝 | 김현수📄 | 신정우💻 |
| --- | --- | --- | --- |
| 팀장 및 총괄 | 화면 설계 | 데이터 수집 및 저장 | 화면 구현 |

<br/>

## 📌기술스택
![Image](https://github.com/user-attachments/assets/2ff90937-1572-4922-8117-42ec1958e8a2)
![Image](https://github.com/user-attachments/assets/f4f74fee-a6ec-4916-98a7-87372c233494)
![Image](https://github.com/user-attachments/assets/954f356b-b234-4fdc-a4de-be4678532cdb)
![Image](https://github.com/user-attachments/assets/5e72d28a-8895-4ab3-acdb-d1be87b53374)
![Image](https://github.com/user-attachments/assets/5c3399ed-c375-4793-ad36-35c69da77dd6)


<br/>



## 🔗 데이터베이스 설계문서: ERD

![Image](https://github.com/user-attachments/assets/3efa685f-1b4b-49a4-9a9f-eb0fc3ad015f)

- 각각 **자동차 등록** , **현대 FAQ** , **기아 FAQ** 이라는 테이블을 만들고</br></br> 
- 자동차 등록에는  **지역**, **연도**, **월**, **차종**, **용도**를 기본키로 쓰면서 not null로 설정하고 **등록수**까지를 컬럼으로 만들었습니다.</br></br>
- 현대 FAQ는 **faq 아이디**를 기본키로, **분류**, **질문**, **대답**이라는 컬럼을 만들고</br></br>
- 기아 FAQ는 **faq 아이디**를 기본키로, **분류**, **질문**, **대답**이라는 컬럼을 만들었습니다.


<br/>

## 📄 수집 데이터: 어떤 데이터를 어떻게 수집하였는지
</br>

<div align="center">
 
**연도별 자동차 등록대수**

</div>

- 각 월마다 저장되어있는 엑셀(xlsx) 파일을 다운로드 하여</br>
파이썬 라이브러리 판다스를 이용하여 시도별 / 연도 / 월 / 등록대수 / 차종 / 용도로 데이터를 정제 후 저장하였습니다.</br>
![Image](https://github.com/user-attachments/assets/eef9e92d-d473-46be-8cb5-021de03f9f14)

<div align="center">

</br>

**기아 홈페이지 FAQ와 현대 홈페이지 FAQ** </br>

</div>

- 자바스크립트를 통해 메세지를 보내는 형식이어서</br>
정적 크롤링으로는 어렵다고 판단하여 셀레니움 라이브러리를 사용한 동적 크롤링을 통해 데이터를 분류 / 질문 / 대답으로 수집하여 저장</br>
![Image](https://github.com/user-attachments/assets/ce10b9ce-5798-48b5-9b47-4a16e58169c0)
![Image](https://github.com/user-attachments/assets/acba8a8b-75bc-4fa3-9be8-171f155c9010)
<br/>

## 📝 데이터 조회 프로그램: 화면설계서

<div align="center">
 <br/>
 
  **전국 자동차 등록 현황**
  
</div>

![Image](https://github.com/user-attachments/assets/b7f53159-15b7-4fae-8b17-157a6513b0d5)

- 중앙: 그래프
- 하단 : 연도와 그래프 종류를 선택

</br>

<div align="center">

 
  **기업 FAQ 조회 시스템**
  
</div>

![Image](https://github.com/user-attachments/assets/230d5e23-f0d4-45c0-86cd-1402e3d0b6af)
![Image](https://github.com/user-attachments/assets/a1a4224f-3a6a-4b97-84a0-8690f026f1d5)

- 상단: 검색기능
- 중앙 : FAQ에 대한 조회화면(카테고리, 찾는 내용)
- 하단 : 페이지 선택

</br>

## 💻 데이터 조회 프로그램: 실제로 구현된 화면과 각 기능
 <br/>

<div align="center">
 
  **메인페이지**
</div>


![Image](https://github.com/user-attachments/assets/21b84d68-e01d-460d-a588-b6407ed41590)
- 좌측 : **MainPage**, **기업별 FAQ 조회**, **연도별 자동차 등록 대수**를 각각을 누르면 각 페이지로 이동 가능합니다.</br>
- 중앙: **연도별 자동차 등록 대수 조회**, **기업별FAQ 조회**을 눌러도 각각 페이지로 이동할 수 있습니다.





<div align="center">
 
  **기업별 FAQ 조회**
  
</div>

![Image](https://github.com/user-attachments/assets/55db2a2b-c231-4e07-84bc-fa754fddd756)
- 중앙 : 검색할 내용을 엔터로 입력하면 **검색**에 맞는 자료를 보여줍니다</br>
**기업**을 선택하면 2개의 기업인 현대나 기아를 선택할 수 있음 그에 따라</br>
카테고리가 바뀌고 그 기업별 **카테고리**가 선택이 가능합니다.</br></br>
**이 페이지는 구현하는데 난이도가 있어서 일단 페이지 화면은 구현해냈으나 기능을 전부 구현해내지는 못했습니다.**







</br>
<div align="center">
 
  **연도별 자동차 등록 대수 조회**
  
</div>

![Image](https://github.com/user-attachments/assets/33570c3a-9823-4d98-a5fc-f5803dbdfd01)
- 중앙: **그래프 종류**를 선택하면 **연도**선택, **차량 종류**를 선택할 수 있는 화면이 나옵니다.</br>
연도와 차량 종류를 선택하면 연결된 데이터베이스를 기반으로 **그래프**를 만들어줍니다.</br>




<br/>

 ## 🔎 기타
- **개발과정에서 발생한 이슈 및 해결방법:** </br>

데이터 수집 및 저장에서</br>
첫번째는 js 명령어를 통해 클릭을 해야하는데 제대로 작동되지 않는 문제가 있었고</br>
두번째는 첫번째 이유로 데이터 크롤링이 잘못되었는데 데이터 수만 보고 잘못 수집된 것을 인지하기까지 오래걸렸습니다.</br>
find_element를 사용할 때 문제가 있는 곳이 BY.CLASSNAME을 이용하여 찾는 과정에서의 문제였는데 이를 BY.XPATH로 변경하여 해결했습니다.</br>
   </br>
화면 설계할 때는 기능들을 생각하고 그 다음에 무엇을 해야할지 몰라서 chatgpt에게 물어보고 생각해서 기능을 하나씩 정해보고 </br>
그래프를 그릴 때는 대략적인 틀을 팀장님이 알려주셔서 해결하고 그래프 그리는데는 인터넷 자료를 참고해서 그리는데</br>
그래프는 직접 코딩하니까 오류가 나서 코딩할 수 있는 부분까지만 입력하고 모르는 부분은 chatgpt에게 물어보고 수정하고 해서</br>
그래프도 대략적으로 그려보았습니다.</br>
</br>
streamlit을 통한 화면 구현에서
배경 이미지를 삽입할때, 이미지 파일을 불러오기 위한 경로설정에 문제가 있었습니다. 각자의 로컬 이미지 저장 장소는 다르기 때문에, 개인 이미지 주소를 파일에 작성한채로 깃허브에 머지하였더니 다른 팀원분들은 에러가 발생하였습니다. 깃허브에 이미지 파일도 같이 커밋해서 팀원분들이 각자 경로를 지정할수 있게 하여 해당 문제를 해결했습니다. 
또 다른 문제로는 배경이미지의 색이 너무 뚜렷하여 faq나 등록정보의 레이어들이 잘 보이지 않는것이 있었습니다. 배경을 흐리게 하는 기능도 streamlit에 있었습니다만, 레이어들과 그래프도 같이 투명도가 변하였기에, 로컬 저장소에서 이미지의 투명도를 먼저 낮춘다음 불러오는 방식으로 문제를 해결했습니다.
배경 이미지의 크기가 너무 큼으로 인해 사진이 특정부분만 나오는 문제는 streamlit에서 background-size를 모두 포함되게 contain으로 바꾸니 해결되었습니다.

   
- **팀원별 느낀점 :** </br>
</br>

**최수헌**
</br>
팀장입니다.</br>
저는 팀장은 팀원보다 많은 것을 부담하고 프로젝트에 대한 전적인 책임이 있는 자리라고 생각했습니다.</br>
하지만 이런 생각이 무색하게 팀원 분들은 많은 각자 맡은 작업에 책임 가지고 프로젝트에 대한 열정이 가득했습니다.</br>
같이 배우고, 같이 코드를 공유하고, 같이 생각하는 이 과정 자체가 값진 경험이었다고 생각합니다.</br>
우리 팀원분들 덕분에 짧은 시간이지만 행복 프로젝트를 진행한 것 같아서 기분이 좋습니다.</br>
함께한 팀원분들 모두 감사합니다.</br>
</br>

**남궁세정**
</br>
단순하게 화면만 구성하고 기능만 추가하면 된다고 생각했는데</br>
단순히 심플하게 디자인하는게 중요한 것이 아니라 사용할 수 있는 기술스택이랑 실제 구현할 수 있는지</br>
없는지라던가 다양한 부분을 고려해서 화면을 설계해야한다는 것 그래서 화면설계가 제대로 이루어지지</br>
않을 수 있다는 사실을 알게 되었습니다.</br>
실제로 구현해내는 것이 많이 힘들다는 것을 옆에서 지켜보면서 알게 되었습니다.</br>
정말 고생 많이 해주신 팀원분들과 팀장님 죄송하고 감사합니다...</br>

</br>

**신정우**
</br>
프로젝트 시작전에는 streamlit이란 도구로 화면을 구현하는것이 가장 고된 작업이라고 철없이 생각했습니다만,</br>
개발중에 크롤링을 사용하여 자료들을 수집하고 데이터베이스를 만든 팀원분들,</br>
또 화면설계를 해주신 팀원까지 제가 제일 간단한 작업을 맡아놓고 불평이 많았다는 생각을 했습니다.</br>
또 데이터베이스를 담당한 팀원분들이 본인의 작업을 끝내신다음 화면구현에 정말 많은 도움을 주셔서,</br>
 팀에 민폐가 된건 아닌지라는 생각도 들었구요. 화면구현이란것 자체가 수집한 데이터를 가지고 기능을 만드는 것이기에,</br>
다른 주제로 개발을 하게된다면 비록 저의 업무가 데이터베이스가 아니더라도 해봐야겠다는 생각을 했습니다. 도움주신 팀원분들 감사합니다ㅠ</br>
</br>

**김현수**
</br>
팀프로젝트 경험이 적은데 참여하게 되어 처음에는 어떻게 해야할지 모르는 상태로 시작한 프로젝트에서</br>
데이터를 크롤링이나 데이터를 정제하여 수집 및 저장을 맡았고</br>
자동차 등록현황을 다운로드하여 정제, 저장하는데에는 큰 어려움은 없었으나</br>
크롤링 과정에서 수집이 잘못된 것을 확인하지 못하고 팀원들이 알려주어 문제를 자각했습니다.</br>
혼자였으면 더 오랜시간 헤맸을거였지만 팀원들의 어시스트를 통해 빠르게 수정할 수 있었다고 생각합니다.</br>
팀원분들 감사합니다!</br>
</br>




