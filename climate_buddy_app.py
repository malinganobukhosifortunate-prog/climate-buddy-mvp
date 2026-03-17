import streamlit as st
import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Climate Buddy", page_icon="🌍")

# ---------------- SESSION STATE ----------------
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "streak" not in st.session_state:
    st.session_state.streak = 0

# ---------------- SIDEBAR ----------------
st.sidebar.image("assets/climate_buddy_logo.png", width=120)
st.sidebar.title("Climate Buddy")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Daily Challenge", "Quiz", "Water Impact", "Climate Map", "Leaderboard"]
)

# ---------------- HEADER ----------------
st.image("assets/climate_buddy_logo.png", width=200)
st.markdown("<h1 style='text-align: center;'>🌍 Climate Buddy</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Learn climate habits • Build eco streaks</p>", unsafe_allow_html=True)

# ---------------- HOME ----------------
if page == "Home":

    st.header("💡 Daily Climate Fact")

    facts = [
        "South Africa is among the top 30 most water-stressed countries globally.",
        "Cape Town nearly reached 'Day Zero' during the 2017–2018 drought.",
        "A 5-minute shower can save up to 45 litres of water.",
        "Over 8 million tons of plastic enter the ocean every year.",
        "Plastic waste can take over 400 years to decompose."
    ]

    today = datetime.date.today()
    fact = facts[today.day % len(facts)]

    st.info(fact)

    st.divider()

    st.header("📊 Your Climate Impact")

    water_saved = 3150
    streak = st.session_state.streak
    score = min(100, streak * 10)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💧 Water Saved", f"{water_saved} L")

    with col2:
        st.metric("🔥 Eco Streak", f"{streak} days")

    with col3:
        st.metric("🌍 Climate Score", f"{score}/100")

    st.progress(score / 100)

    # -------- LEVEL SYSTEM --------
    if score < 30:
        level = "🌱 Beginner"
    elif score < 70:
        level = "🌿 Eco Learner"
    else:
        level = "🌳 Climate Champion"

    st.success(f"Your Level: {level}")

    # -------- BADGES --------
    st.subheader("🏅 Your Badges")

    if streak >= 3:
        st.success("🔥 Consistency Starter")

    if water_saved > 1000:
        st.success("💧 Water Saver")

    if score > 80:
        st.success("🌍 Climate Pro")

    # -------- XP --------
    xp = (streak * 10) + (st.session_state.quiz_score * 20)
    st.metric("⭐ XP Points", xp)

# ---------------- DAILY CHALLENGE ----------------
elif page == "Daily Challenge":

    st.header("🎯 Today's Climate Challenge")

    kids = [
        "Turn off the tap while brushing 🚰",
        "Pick up 3 pieces of litter 🌱",
        "Use reusable lunch container 🍱",
        "Take a 5-minute shower 🚿"
    ]

    adults = [
        "Avoid single-use plastic ♻",
        "Carry reusable bottle 💧",
        "Refuse plastic straw 🌊",
        "Track your water usage 📊"
    ]

    mode = st.toggle("Kids Mode")

    challenge_list = kids if mode else adults

    today = datetime.date.today()
    challenge = challenge_list[today.day % len(challenge_list)]

    st.success(challenge)

    if st.button("Mark as Completed"):
        st.session_state.streak += 1
        st.success("🔥 Streak Increased!")

# ---------------- QUIZ ----------------
elif page == "Quiz":

    st.header("🧠 Daily Climate Quiz")

    quiz = [
        ("Which resource is most scarce in South Africa?", ["Coal", "Water", "Gold", "Wind"], "Water"),
        ("What year was Day Zero risk?", ["2010", "2015", "2017–2018", "2022"], "2017–2018"),
        ("5-min shower saves?", ["10", "25", "45", "100"], "45"),
        ("Floods in 2022?", ["Gauteng", "KZN", "Free State", "NC"], "KZN")
    ]

    today = datetime.date.today()
    q = quiz[today.day % len(quiz)]

    answer = st.radio(q[0], q[1], key="quiz_unique")

    if st.button("Submit Answer"):
        if answer == q[2]:
            st.success("Correct! 🌱")
            st.session_state.quiz_score += 1
        else:
            st.error("Try again tomorrow!")

# ---------------- WATER IMPACT ----------------
elif page == "Water Impact":

    st.header("🌊 Water Impact Calculator")

    people = st.slider("People", 1, 100, 10)
    days = st.slider("Days", 1, 30, 7)

    if st.button("Calculate"):
        saved = people * days * 45
        st.metric("💧 Water Saved", f"{saved} litres")

# ---------------- CLIMATE MAP ----------------
elif page == "Climate Map":

    st.header("🌍 SA Climate Insights")

    data = {
        "Gauteng": "High demand due to population.",
        "Western Cape": "Severe drought history.",
        "KZN": "Flood impacts.",
        "Eastern Cape": "Water shortages.",
        "Limpopo": "Rainfall dependent."
    }

    province = st.selectbox("Province", list(data.keys()))
    st.info(data[province])

# ---------------- LEADERBOARD ----------------
elif page == "Leaderboard":

    st.header("🏆 Leaderboard")

    board = {
        "Aisha": 5,
        "Liam": 7,
        "Thando": 4,
        "Naledi": 6
    }

    sorted_board = sorted(board.items(), key=lambda x: x[1], reverse=True)

    for i, (name, score) in enumerate(sorted_board, 1):
        st.write(f"{i}. {name} — {score} days 🔥")
