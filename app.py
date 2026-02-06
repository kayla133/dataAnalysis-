import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# --- PAGE SETUP ---
st.set_page_config(page_title="F1 Data Analysis", layout="wide")
st.title("Formula 1 Race Analysis Dashboard")

def load_and_clean_data():
    # Use st.cache_data so the file doesn't reload every time you click a button
    df = pd.read_csv('f1_data.csv')
    
    # removes weird characters or spaces.
    df['winner_name'] = df['winner_name'].str.replace('Â','').str.strip()
    df['team'] = df['team'].str.strip()
    return df

def perform_analysis(df):
    # Get the data for the top five teams
    team_leaderboard = df.groupby('team')['date'].count().sort_values(ascending = False)

    # Group by driver, count the dates they won, and sort from highest to lowest
    driver_leaderboard = df.groupby('winner_name')['date'].count().sort_values(ascending = False)

    # Team Ferrari
    ferrari_target_team = ['Ferrari']
    ferrari_team_wins = df[df['team'].isin(ferrari_target_team)]
    ferrari_leaderboard = ferrari_team_wins.groupby('winner_name')['date'].count().sort_values(ascending = False)

    # Team Mercedes
    mercedes_target_team = ['Mercedes', 'Mercedes-Benz']
    mercedes_team_wins = df[df['team'].isin(mercedes_target_team)]
    mercedes_leaderboard = mercedes_team_wins.groupby('winner_name')['date'].count().sort_values(ascending = False)

    # Team Williams
    williams_target_team = ['Williams Ford', 'Williams Honda', 'Williams Renault', 'Williams BMW']
    williams_team_wins = df[df['team'].isin(williams_target_team)]
    williams_leaderboard = williams_team_wins.groupby('winner_name')['date'].count().sort_values(ascending = False)

    # Team Lotus
    lotus_target_team = ['Lotus Climax', 'Lotus Ford', 'Lotus Honda', 'Lotus Renault']
    lotus_team_wins = df[df['team'].isin(lotus_target_team)]
    lotus_leaderboard = lotus_team_wins.groupby('winner_name')['date'].count().sort_values(ascending = False)

    # Now we are going to filter each team and show the top driver winners in order.
    mclaren_target_team = ['McLaren Ford', 'McLaren TAG', 'McLaren Honda', 'McLaren Mercedes', 'McLaren']
    mclaren_team_wins = df[df['team'].isin(mclaren_target_team)]
    mclaren_leaderboard = mclaren_team_wins.groupby('winner_name')['date'].count().sort_values(ascending = False)
    
    return team_leaderboard, driver_leaderboard, ferrari_leaderboard, mercedes_leaderboard, williams_leaderboard, lotus_leaderboard, mclaren_leaderboard

# Execute Data Logic
df = load_and_clean_data()
t_lead, d_lead, f_lead, m_lead, w_lead, l_lead, mc_lead = perform_analysis(df)

# --- WEB DISPLAY SECTION ---

# Section 1: Global Stats
col1, col2 = st.columns(2)

with col1:
    st.header("Top 5 Teams")
    # Instead of print(), we use st.table() or st.dataframe()
    st.table(t_lead.head(5))

with col2:
    st.header("Top 5 Drivers")
    st.table(d_lead.head(5))

st.divider()

# Section 2: Team Specifics (Stretch Challenge: Graphing)
st.header("Breakdown by Legendary Teams")

# Create columns for the team leaderboards
team_cols = st.columns(3)

with team_cols[0]:
    st.subheader("Ferrari")
    st.dataframe(f_lead.head(5), use_container_width=True)

with team_cols[1]:
    st.subheader("Mercedes")
    st.dataframe(m_lead.head(5), use_container_width=True)

with team_cols[2]:
    st.subheader("McLaren")
    st.dataframe(mc_lead.head(5), use_container_width=True)

# STRETCH CHALLENGE: Visualizing the results
st.divider()
st.header("Visualizing Team Success")
fig, ax = plt.subplots(figsize=(10, 4))
t_lead.head(10).plot(kind='bar', ax=ax, color='orange')
plt.title("Top 10 Teams by All-Time Wins")
st.pyplot(fig)