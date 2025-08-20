import streamlit as st

st.set_page_config(page_title="퀴즈 게임", layout="centered")

# --- 문제 리스트 (15문제) ---
QUIZ = [
{"q": "태양계에서 가장 큰 행성은?", "a": "목성"},
{"q": "대한민국의 수도는?", "a": "서울"},
{"q": "빛의 속도는 초당 약 몇 km일까? (가까운 값)", "a": "30만"},
{"q": "피타고라스 정리는 a² + b² = ?", "a": "c²"},
{"q": "물의 화학식은?", "a": "H2O"},
{"q": "1바이트는 몇 비트인가?", "a": "8"},
{"q": "세계에서 가장 많이 쓰이는 언어는?", "a": "중국어"},
{"q": "지구의 위성은?", "a": "달"},
{"q": "한국의 국보 1호는?", "a": "숭례문"},
{"q": "삼국지에서 유비, 관우, 장비가 맺은 관계는?", "a": "도원결의"},
{"q": "대한민국 헌법상 대통령의 임기는 몇 년인가?", "a": "5"},
{"q": "원소 기호 O는 무엇을 뜻할까?", "a": "산소"},
{"q": "구글의 모회사 이름은?", "a": "알파벳"},
{"q": "피카츄는 어떤 동물에서 모티브를 얻었을까?", "a": "쥐"},
{"q": "세계 최초의 문명 중 하나로 메소포타미아에서 발생한 문명은?", "a": "수메르"}
]

# --- 초기 상태 ---
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_q = 0
    st.session_state.finished = False

st.title("🧩 스트림릿 퀴즈 게임")

# --- 문제 출제 ---
if not st.session_state.finished:
q = QUIZ[st.session_state.current_q]
st.subheader(f"문제 {st.session_state.current_q+1}: {q['q']}")

answer = st.text_input("정답을 입력하세요:")

if st.button("제출"):
if answer.strip() == q["a"]:
st.success("✅ 정답입니다!")
st.session_state.score += 1
else:
st.error(f"❌ 오답! 정답은 {q['a']} 입니다.")

st.session_state.current_q += 1

if st.session_state.current_q >= len(QUIZ):
st.session_state.finished = True

# --- 결과 출력 ---
if st.session_state.finished:
st.subheader("📊 퀴즈 종료!")
st.write(f"당신의 점수: **{st.session_state.score} / {len(QUIZ)}**")

# --- 리셋 버튼 ---
if st.button("🔄 다시 시작"):
st.session_state.score = 0
st.session_state.current_q = 0
st.session_state.finished = False
