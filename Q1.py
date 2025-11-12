# IEOR4004 Project 2

import pandas as pd

games_df = pd.read_csv('./data/games.csv')

teams = pd.unique(games_df[["Visitor", "Home"]].values.ravel())

summary_dict = {}
for team in teams:
    team_summary = {}

    home_dates = games_df.loc[games_df["Home"] == team, "Date"].tolist()
    team_summary['Home dates'] = home_dates

    away_dates = games_df.loc[games_df["Visitor"] == team, "Date"].tolist()
    team_summary['Away dates'] = away_dates

    home_counts = (
        games_df.loc[games_df["Home"] == team, "Visitor"]
        .value_counts()
        .rename_axis("Opponent")
        .reset_index(name="Home Games")
    )
    away_counts = (
        games_df.loc[games_df["Visitor"] == team, "Home"]
        .value_counts()
        .rename_axis("Opponent")
        .reset_index(name="Away Games")
    )
    total_counts = pd.merge(home_counts,
                            away_counts,
                            on="Opponent",
                            how="outer").fillna(0)
    team_summary['H/A Games vs. Others'] = total_counts

    summary_dict[team] = team_summary
    print(f"\n {team} Summary:")
    print(f"Home dates: {team_summary['Home dates']}")
    print(f"Away dates: {team_summary['Away dates']}")
    print("Head-to-head counts:")
    print(team_summary['H/A Games vs. Others'])
