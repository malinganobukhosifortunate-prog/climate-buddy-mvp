import streamlit as st
import datetime
import random

# ---------------- PAGE CONFIG ----------------

st.set_page_config(page_title="Climate Buddy", page_icon="🌍")
st.image("assets/climate_buddy_logo.png", width=220)

st.markdown(
    "<h1 style='text-align: center;'>Climate Buddy</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Learn climate habits • Build eco streaks</p>",
    unsafe_allow_html=True
)

# ---------------- SESSION STATE ----------------

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

# ---------------- APP STYLING ----------------

st.markdown("""
<style>
.big-title {
    font-size:40px;
    font-weight:bold;
    color:#2E8B57;
}
.subtitle {
    font-size:20px;
    color:#4F8A8B;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🌍 Climate Buddy</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Learn climate habits. Build eco streaks.</p>', unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

st.sidebar.image("assets/climate_buddy_logo.png", width=120)
st.sidebar.title("Climate Buddy")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Daily Challenge", "Quiz", "Water Impact", "Climate Map", "Leaderboard"]
)

# ---------------- HOME PAGE ----------------

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
    eco_streak = st.session_state.quiz_score
    climate_score = min(100, eco_streak * 10)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💧 Water Saved", f"{water_saved} L")

    with col2:
        st.metric("🔥 Eco Streak", f"{eco_streak} days")

    with col3:
        st.metric("🌍 Climate Score", f"{climate_score}/100")

    st.progress(climate_score / 100)

    st.caption("Your sustainability progress today")

    st.divider()

    st.header("🏅 Your Climate Badge")

    if eco_streak >= 5:
        badge = "🌍 Climate Champion"
    elif eco_streak >= 3:
        badge = "💧 Water Saver"
    elif eco_streak >= 1:
        badge = "🌱 Eco Beginner"
    else:
        badge = "🌱 Start Your Climate Journey"

    st.success(badge)

    st.header("📈 Climate Knowledge Level")

    if eco_streak >= 10:
        st.success("Expert 🌍")
    elif eco_streak >= 5:
        st.info("Climate Advocate 🌱")
    elif eco_streak >= 2:
        st.info("Climate Learner 📘")
    else:
        st.warning("Beginner 🌿")

# ---------------- DAILY CHALLENGE ----------------

elif page == "Daily Challenge":

    st.header("🎯 Today's Climate Challenge")

    kids_challenges = [
        "Turn off the tap while brushing your teeth 🚰",
        "Pick up 3 pieces of litter 🌱",
        "Use a reusable lunch container 🍱",
        "Take a 5-minute shower 🚿"
    ]

    adult_challenges = [
        "Avoid single-use plastic today ♻",
        "Carry a reusable water bottle 💧",
        "Refuse a plastic straw 🌊",
        "Track your water usage today 📊"
    ]

    mode = st.toggle("Kids Mode")

    if mode:
        challenge_list = kids_challenges
        st.info("Kids Mode Activated 🧒")
    else:
        challenge_list = adult_challenges
        st.info("Young Adult Mode 🎓")

    today = datetime.date.today()
    challenge = challenge_list[today.day % len(challenge_list)]

    st.success(challenge)

# ---------------- QUIZ ----------------

elif page == "Quiz":

    st.header("🧠 Daily Climate Quiz")

    quiz_questions = [
        {
            "question": "Which resource is most scarce in South Africa?",
            "options": ["Coal", "Water", "Gold", "Wind"],
            "answer": "Water"
        },
        {
            "question": "What year did Cape Town nearly reach 'Day Zero'?",
            "options": ["2010", "2015", "2017–2018", "2022"],
            "answer": "2017–2018"
        },
        {
            "question": "How many litres can a 5-minute shower save?",
            "options": ["10 litres", "25 litres", "45 litres", "100 litres"],
            "answer": "45 litres"
        },
        {
            "question": "Which province experienced major flooding in 2022?",
            "options": ["Gauteng", "KwaZulu-Natal", "Free State", "Northern Cape"],
            "answer": "KwaZulu-Natal"
        }
    ]

    today = datetime.date.today()
    question = quiz_questions[today.day % len(quiz_questions)]

    user_answer = st.radio(
        question["question"],
        question["options"],
        key="quiz_question"
    )

    if st.button("Submit Answer"):

        if user_answer == question["answer"]:
            st.success("Correct! 🌱")
            st.session_state.quiz_score += 1
        else:
            st.error("Not quite. Try again tomorrow!")

# ---------------- WATER CALCULATOR ----------------

elif page == "Water Impact":

    st.header("🌊 Water Impact Calculator")

    people = st.slider("Number of People", 1, 1000, 10)
    days = st.slider("Number of Days", 1, 30, 7)

    if st.button("Calculate Water Saved"):

        water_saved = people * days * 45

        st.metric("💧 Total Water Saved", f"{water_saved} litres")

        st.info("That's enough water to supply several households.")

# ---------------- CLIMATE MAP ----------------

elif page == "Climate Map":

    st.header("🌍 South African Climate Insights")

    province_facts = {
        "Gauteng": "High population density creates intense water demand.",
        "Western Cape": "Severe drought nearly caused Day Zero in 2018.",
        "KwaZulu-Natal": "Flood damage has impacted water infrastructure.",
        "Eastern Cape": "Recurring drought and water shortages.",
        "Limpopo": "Semi-arid province dependent on rainfall."
    }

    province = st.selectbox(
        "Choose Province",
        list(province_facts.keys())
    )

    st.info(province_facts[province])

# ---------------- LEADERBOARD ----------------

elif page == "Leaderboard":

    st.header("🏆 Climate Buddy Leaderboard")

    leaderboard = {
        "Aisha": 5,
        "Liam": 7,
        "Thando": 4,
        "Naledi": 6
    }

    sorted_board = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

    for rank, (name, score) in enumerate(sorted_board, start=1):
        st.write(f"{rank}. {name} — {score} day streak 🔥")
