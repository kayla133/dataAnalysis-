import pandas as pd

def load_and_clean_data():
    df = pd.read_csv('f1_data.csv')
    df.head()

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

    # Filter the database to pull from those teams
    mclaren_team_wins = df[df['team'].isin(mclaren_target_team)]

    # Now we can pull the winners from this database
    mclaren_leaderboard = mclaren_team_wins.groupby('winner_name')['date'].count().sort_values(ascending = False)
    
    return team_leaderboard, driver_leaderboard, ferrari_leaderboard, mercedes_leaderboard, williams_leaderboard, lotus_leaderboard, mclaren_leaderboard

def display_results(team_leaderboard, driver_leaderboard, ferrari_leaderboard, mercedes_leaderboard, williams_leaderboard, lotus_leaderboard, mclaren_leaderboard):
    print("The top five teams with the most wins: ")
    print(team_leaderboard.head(5).to_string(header = False))
    print()

    # Print out the results of the top 5 racers.
    print("The amount of race wins for the top 5 drivers: ")
    print(driver_leaderboard.head(5).to_string(header = False))

    print()

    # Print all of the top 5 drivers for each team that was in the top 5 team leaderboard
    print("The top 5 racers for team Ferrari: ")
    print(ferrari_leaderboard.head(5).to_string(header = False))

    print()
    print("The top 5 racers for team Mercedes: ")
    print(mercedes_leaderboard.head(5).to_string(header = False))

    print()
    print("The top 5 racers for team McLaren: ")
    print(mclaren_leaderboard.head(5).to_string(header = False))

    print()
    print("The top 5 racers for team Williams: ")
    print(williams_leaderboard.head(5).to_string(header = False))

    print()
    print("The top 5 racers for team Lotus Ford: ")
    print(lotus_leaderboard.head(5).to_string(header = False))

# Run the program
f1_df = load_and_clean_data()
results = perform_analysis(f1_df)
display_results(*results)