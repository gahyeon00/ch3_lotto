import random
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="로또 번호 생성기", page_icon="🎱", layout="centered"
)


# 로또 번호별 공 색상 지정 함수 (배경색, 글자색)
def get_ball_color(number):
  if 1 <= number <= 10:
    return "#fbc400", "#000000"  # 노란색
  elif 11 <= number <= 20:
    return "#69c8f2", "#ffffff"  # 파란색
  elif 21 <= number <= 30:
    return "#ff7272", "#ffffff"  # 빨간색
  elif 31 <= number <= 40:
    return "#aaaaaa", "#ffffff"  # 회색
  else:
    return "#b0d840", "#ffffff"  # 초록색


# 세션 상태 초기화 (생성된 로또 세트 저장용)
if "lotto_sets" not in st.session_state:
  st.session_state.lotto_sets = []

# 타이틀 및 설명
st.title("🎱 행운의 로또 번호 생성기")
st.markdown(
    "버튼을 눌러 1~45 사이의 로또 번호를 생성해 보세요! (최대 5개 세트 저장)"
)

# 조작 버튼 영역
col1, col2 = st.columns([1, 4])
with col1:
  if st.button("번호 생성", type="primary"):
    # 1~45 중 중복 없이 6개 추출 후 오름차순 정렬
    new_set = sorted(random.sample(range(1, 46), 6))
    # 최대 5개 세트까지만 유지 (초과 시 가장 오래된 것 삭제)
    if len(st.session_state.lotto_sets) >= 5:
      st.session_state.lotto_sets.pop(0)
    st.session_state.lotto_sets.append(new_set)

with col2:
  if st.button("초기화"):
    st.session_state.lotto_sets = []

st.markdown("---")

# 공 모양 디자인을 위한 CSS 스타일 정의
ball_style = """
<style>
.lotto-ball {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    font-weight: bold;
    font-size: 18px;
    margin-right: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.set-container {
    margin-bottom: 12px;
    padding: 12px;
    background-color: #f8f9fa;
    border-radius: 8px;
    border: 1px solid #e9ecef;
}
</style>
"""
st.markdown(ball_style, unsafe_allow_html=True)

# 저장된 로또 번호 목록 출력 (최신순 정렬)
if st.session_state.lotto_sets:
  st.subheader("📌 생성된 로또 번호 목록")
  # 최신 생성된 세트가 위로 오도록 역순 출력
  for idx, lotto_set in enumerate(reversed(st.session_state.lotto_sets)):
    set_num = len(st.session_state.lotto_sets) - idx
    balls_html = f"<div class='set-container'><b>[세트 {set_num}]</b> &nbsp;&nbsp; "
    for num in lotto_set:
      bg_color, text_color = get_ball_color(num)
      balls_html += f"<span class='lotto-ball' style='background-color: {bg_color}; color: {text_color};'>{num:02d}</span>"
    balls_html += "</div>"
    st.markdown(balls_html, unsafe_allow_html=True)
else:
  st.info(
      "아직 생성된 로또 번호가 없습니다. '번호 생성' 버튼을 클릭해 주세요!"
  )