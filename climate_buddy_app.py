import streamlit as st
import datetime
import random

st.set_page_config(page_title="Climate Buddy", page_icon="🌍")

st.sidebar.title("🌍 Climate Buddy")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Daily Challenge", "Quiz", "Water Impact", "Climate Map", "Leaderboard"]
)

if page == "Home":

    st.title("🌍 Climate Buddy")
    st.subheader("Your Daily Environmental Companion")

    st.write("Helping South Africans build better climate habits through small daily actions.")

    st.divider()

    st.header("💡 Daily Climate Fact")

    facts = [
        "South Africa is among the top 30 most water-stressed countries globally.",
        "Cape Town nearly reached 'Day Zero' during the 2017–2018 drought.",
        "A 5-minute shower can save up to 45 litres of water.",
        "Over 8 million tons of plastic enter the ocean every year.",
        "Plastic waste can take over 400 years to decompose."
    ]

    today = datetime.date.today()
    fact_index = today.day % len(facts)

    st.info(facts[fact_index])
st.divider()

st.header("📊 Your Climate Impact Today")

water_saved = 3150
challenges_done = 1

score = min(100, (water_saved / 50) + (challenges_done * 10))

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💧 Water Saved", f"{water_saved} L")

with col2:
    st.metric("🌱 Challenges Completed", challenges_done)

with col3:
    st.metric("🌍 Climate Score", f"{int(score)}/100")
st.progress(score/100)

st.caption("Your sustainability progress today")
st.set_page_config(page_title="Climate Buddy", page_icon="🌍")
# ---------------- HOME PAGE ----------------

if page == "Home":

    st.title("🌍 Climate Buddy")
    st.subheader("Your Daily Environmental Companion")

    st.write("Helping South Africans build better climate habits through small daily actions.")

    st.divider()

    st.header("💡 Daily Climate Fact")

    facts = [
        "South Africa is among the top 30 most water-stressed countries globally.",
        "Cape Town nearly reached 'Day Zero' during the 2017–2018 drought.",
        "A 5-minute shower can save up to 45 litres of water.",
        "Over 8 million tons of plastic enter the ocean every year.",
        "Plastic waste can take over 400 years to decompose."
    ]

    today = datetime.date.today()
    fact_index = today.day % len(facts)

    st.info(facts[fact_index])



# ---------------- DAILY CHALLENGE PAGE ----------------

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
        st.write("🧒 Kids Mode Activated")
    else:
        challenge_list = adult_challenges
        st.write("🎓 Young Adult Mode Activated")

    today = datetime.date.today()
    challenge_index = today.day % len(challenge_list)

    st.success(challenge_list[challenge_index])



# ---------------- QUIZ PAGE ----------------

elif page == "Quiz":

    st.header("🧠 Climate Quiz")

    quiz_questions = [
        {
            "question": "Which resource is most scarce in South Africa?",
            "options": ["Coal", "Water", "Gold", "Wind"],
            "answer": "Water"
        },
        {
            "question": "What year did Cape Town nearly reach 'Day Zero'?",
            "options": ["2010", "2015", "2017-2018", "2022"],
            "answer": "2017-2018"
        },
        {
            "question": "How many litres can a 5-minute shower save compared to longer showers?",
            "options": ["10 litres", "25 litres", "45 litres", "100 litres"],
            "answer": "45 litres"
        }
    ]

    score = 0

    for i, q in enumerate(quiz_questions):

        user_answer = st.radio(
            q["question"],
            q["options"],
            key=f"question_{i}"
        )

        if user_answer == q["answer"]:
            score += 1

    if st.button("Submit Quiz", key="submit_quiz"):

        st.subheader(f"Your Score: {score} / {len(quiz_questions)}")

        if score == len(quiz_questions):
            st.success("🌟 Perfect! You're a Climate Champion!")
        elif score >= 2:
            st.info("👍 Good job! You know your climate facts.")
        else:
            st.warning("🌱 Keep learning — climate knowledge matters!")



# ---------------- WATER IMPACT PAGE ----------------

elif page == "Water Impact":

    st.header("🌊 Water Impact Calculator")

    people = st.slider("Number of People", 1, 1000, 10)
    days = st.slider("Number of Days", 1, 30, 7)

    if st.button("Calculate Water Saved"):

        water_saved = people * days * 45

        st.metric("💧 Total Water Saved", f"{water_saved} litres")

        st.info("That's enough water to supply multiple households for several days.")



# ---------------- LEADERBOARD PAGE ----------------

elif page == "Leaderboard":

    st.header("🏆 Climate Buddy Community Leaderboard")

    leaderboard = {
        "Aisha (Gauteng)": 5,
        "Liam (Western Cape)": 7,
        "Thando (KZN)": 4,
        "Naledi (Eastern Cape)": 6
    }

    sorted_board = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

    for rank, (user, score) in enumerate(sorted_board, start=1):

        st.write(f"{rank}. {user} — {score} day streak 🔥")

st.title("🌍 Climate Buddy")
st.write("Your Daily Environmental Companion")

# Daily climate fact
facts = [
"South Africa is among the top 30 most water-stressed countries globally.",
"Cape Town nearly reached 'Day Zero' during the 2017–2018 drought.",
"A 5-minute shower can save up to 45 litres of water.",
"Over 8 million tons of plastic enter the ocean every year.",
"Plastic waste can take over 400 years to decompose."
]

today = datetime.date.today()
fact = facts[today.day % len(facts)]

st.header("💡 Daily Climate Fact")
st.write(fact)

# Mode selector
mode = st.radio(
"Select Mode",
["Kids Mode 🧒", "Young Adult Mode 🎓"]
)

# Challenges
kids_challenges = [
"Turn off the tap while brushing your teeth",
"Pick up 3 pieces of litter",
"Use a reusable lunch container",
"Take a 5-minute shower"
]

adult_challenges = [
"Avoid single-use plastic today",
"Carry a reusable water bottle",
"Refuse a plastic straw",
"Track your water usage today"
]

if mode == "Kids Mode 🧒":
    challenge_list = kids_challenges
else:
    challenge_list = adult_challenges

challenge = challenge_list[today.day % len(challenge_list)]

st.header("🎯 Today's Challenge")
st.write(challenge)

# Quiz
st.header("🧠 Quick Quiz")

answer = st.radio(
"Which resource is most scarce in South Africa?",
["Coal", "Water", "Gold", "Wind"]
)

if st.button("Submit Answer"):
    if answer == "Water":
        st.success("Correct! Water scarcity is a major issue in South Africa.")
    else:
        st.error("Not quite. Try again tomorrow!")

# Province facts
st.header("💧 Province Water Facts")

province_facts = {
"Gauteng":"High water demand due to dense population.",
"Western Cape":"Severe drought nearly caused Day Zero in 2018.",
"KwaZulu-Natal":"Flood damage has impacted water infrastructure.",
"Eastern Cape":"Recurring drought and water shortages.",
"Limpopo":"Semi-arid province dependent on rainfall."
}

province = st.selectbox(
"Select Province",
list(province_facts.keys())
)

st.write(province_facts[province])

# Water calculator
st.header("🌊 Water Impact Calculator")

people = st.slider("Number of People",1,1000,10)
days = st.slider("Number of Days",1,30,7)

if st.button("Calculate Water Saved"):
    water_saved = people * days * 45
    st.success(f"💧 Total Water Saved: {water_saved} litres")

elif page == "Climate Map":

    st.header("🌍 South African Climate Insights")

    st.write("Select a province to learn about local climate and water challenges.")

    provinces = [
        "Gauteng",
        "Western Cape",
        "KwaZulu-Natal",
        "Eastern Cape",
        "Limpopo"
    ]

    province = st.selectbox("Choose a Province", provinces)

    province_facts = {
        "Gauteng": "High population density creates intense water demand. Infrastructure pressure makes water conservation critical.",
        "Western Cape": "Experienced the severe 2017–2018 drought that nearly caused Cape Town's Day Zero water shutdown.",
        "KwaZulu-Natal": "Flooding events and infrastructure damage have affected water security in recent years.",
        "Eastern Cape": "Frequent drought conditions and aging infrastructure contribute to recurring water shortages.",
        "Limpopo": "Semi-arid climate with strong dependence on rainfall and dam storage for water supply."
    }

    st.info(province_facts[province])
# Leaderboard
st.header("🏆 Community Leaderboard")

leaderboard = {
"Aisha":5,
"Liam":7,
"Thando":4,
"Naledi":6
}

for name,score in leaderboard.items():
    st.write(f"{name} — {score} day streak 🔥")
