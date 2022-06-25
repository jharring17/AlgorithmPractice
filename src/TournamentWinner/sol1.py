# Hash Table
# Time Complexity: O(n), Space Complexity O(k)

HOME_TEAM_WON = 1
# updates the score of the teams
def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points

# determines winner of a tournament based off of result array
def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam, 3, scores)
        
        if scores[winningTeam] > scores[currentBestTeam]:
                currentBestTeam = winningTeam
    
    return currentBestTeam

print(tournamentWinner([["HTML", "CSS"], ["C#", "Python"], ["Python", "HTML"]], [0,0,1]))