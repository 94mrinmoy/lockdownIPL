import pandas as pd
import itertools 
  
def findsubsets(s, n): 
    return list(itertools.combinations(s, n))


def data():
    data = pd.read_csv('data.csv')
    teams = data['Team']
    print(findsubsets(teams, 2))

def fixtures():
    data = pd.read_csv('fixtures.csv')
    # teams = data['Team']
    return data

def getPoints():
    pointData =  pd.read_csv('data copy.csv')      
    sortedData = pointData.sort_values(['Points','NRR','Team'],ascending=(False, False, True))
    return sortedData


def getNRR(matchNo,team1,team2,team1Score,team2Score,team1Wickets,team2Wickets):
    # NRR = (totalRunScored/totalOverFaced) - (totalRunCenceded/TotalOversBowled)
    # team1='KKR'
    # team2='CSK'
    # team1Score = '45/5,5.0'
    # team2Score = '49/3,4.2'
    team1Run = int(team1Score.split('/')[0])
    if team1Wickets =='10':
        team1Balls = 30
    else:
        team1Balls = int(team1Score.split(',')[-1].split('.')[0])*6 + int(team1Score.split(',')[-1].split('.')[-1])
    team2Run = int(team2Score.split('/')[0])
    if team2Wickets =='10':
        team2Balls = 30
    else:
        team2Balls = int(team2Score.split(',')[-1].split('.')[0])*6 + int(team2Score.split(',')[-1].split('.')[-1])
    team1NRR = (team1Run/team1Balls) - (team2Run/team2Balls)
    team2NRR = (team2Run/team2Balls) - (team1Run/team1Balls)
    winner = ''
    loser=''
    if team1NRR>team2NRR:
        winner = team1
        loser = team2
    else:
        winner = team2 
        loser = team1   
    team1NRR = round(team1NRR, 3)
    team2NRR = round(team2NRR, 3)
    print(team1 +' ' +str(team1NRR))
    print(team2 +' ' +str(team2NRR))

    fixtures = pd.read_csv('fixtures.csv')
    # fixtures[fixtures['Match_No'] == int(matchNo)]['Result'] = winner
    fixtures.loc[fixtures['Match_No'] == int(matchNo), 'Result'] = winner
    fixtures.to_csv('fixtures.csv',index=False)
    data = pd.read_csv('data copy.csv')
    winnerMatches = data[data['Team'] == winner]['Matches'].to_string(index=False) 
    winnerPoints = data[data['Team'] == winner]['Points'].to_string(index=False) 
    winnerNRR = data[data['Team'] == winner]['NRR'].to_string(index=False) 
    data.loc[data['Team'] == winner, 'Matches'] = int(winnerMatches)+1
    data.loc[data['Team'] == winner, 'Points'] = int(winnerPoints)+2
    if team1NRR>team2NRR:
        data.loc[data['Team'] == winner, 'NRR'] = round(float(winnerNRR)+team1NRR,3)
    else:    
        data.loc[data['Team'] == winner, 'NRR'] = round(float(winnerNRR)+team2NRR,3)

    loserMatches = data[data['Team'] == loser]['Matches'].to_string(index=False) 
    loserPoints = data[data['Team'] == loser]['Points'].to_string(index=False) 
    loserNRR = data[data['Team'] == loser]['NRR'].to_string(index=False) 
    data.loc[data['Team'] == loser, 'Matches'] = int(loserMatches)+1
    data.loc[data['Team'] == loser, 'Points'] = int(loserPoints)+0
    if team1NRR<team2NRR:
        nrr = str(round(float(loserNRR)+team1NRR,3))
        data.loc[data['Team'] == loser, 'NRR'] =round(float(loserNRR)+team1NRR,3)
    else:    
        nrr = str( round(float(loserNRR)+team2NRR,3))
        data.loc[data['Team'] == loser, 'NRR'] = round(float(loserNRR)+team2NRR,3)
    data.to_csv('data copy.csv',index=False)    

    result = pd.read_csv('result.csv')
    df_length = len(result)
    abnrr = str(round(abs(team1NRR),3))
    result.loc[df_length] = [matchNo,team1+'-'+team1Score,team2+'-'+team2Score,winner,abnrr]
    # result.append()
    result.to_csv('result.csv',index=False)    
    
    dataPlayers = pd.read_csv('dataPlayers.csv')
    team1Matches = dataPlayers[dataPlayers['Team'] == team1]['Matches'].to_string(index=False) 
    team1PrvRuns = dataPlayers[dataPlayers['Team'] == team1]['Runs'].to_string(index=False) 
    team1PrvWickets = dataPlayers[dataPlayers['Team'] == team1]['Wickets'].to_string(index=False) 
    team1PrvRunsGiven = dataPlayers[dataPlayers['Team'] == team1]['RunsGiven'].to_string(index=False) 
    team1PrvWicketsFallen = dataPlayers[dataPlayers['Team'] == team1]['WicketsFallen'].to_string(index=False) 
    
    dataPlayers.loc[dataPlayers['Team'] == team1, 'Matches'] = int(team1Matches)+1
    dataPlayers.loc[dataPlayers['Team'] == team1, 'Runs'] = int(team1PrvRuns)+int(team1Run)
    dataPlayers.loc[dataPlayers['Team'] == team1, 'Wickets'] = int(team1PrvWickets)+int(team2Wickets)
    dataPlayers.loc[dataPlayers['Team'] == team1, 'RunsGiven'] = int(team1PrvRunsGiven)+int(team2Run)
    dataPlayers.loc[dataPlayers['Team'] == team1, 'WicketsFallen'] = int(team1PrvWicketsFallen)+int(team1Wickets)

    team2Matches = dataPlayers[dataPlayers['Team'] == team2]['Matches'].to_string(index=False) 
    team2PrvRuns = dataPlayers[dataPlayers['Team'] == team2]['Runs'].to_string(index=False) 
    team2PrvWickets = dataPlayers[dataPlayers['Team'] == team2]['Wickets'].to_string(index=False) 
    team2PrvRunsGiven = dataPlayers[dataPlayers['Team'] == team2]['RunsGiven'].to_string(index=False) 
    team2PrvWicketsFallen = dataPlayers[dataPlayers['Team'] == team2]['WicketsFallen'].to_string(index=False) 
    
    dataPlayers.loc[dataPlayers['Team'] == team2, 'Matches'] = int(team2Matches)+1
    dataPlayers.loc[dataPlayers['Team'] == team2, 'Runs'] = int(team2PrvRuns)+int(team2Run)
    dataPlayers.loc[dataPlayers['Team'] == team2, 'Wickets'] = int(team2PrvWickets)+int(team1Wickets)
    dataPlayers.loc[dataPlayers['Team'] == team2, 'RunsGiven'] = int(team2PrvRunsGiven)+int(team1Run)
    dataPlayers.loc[dataPlayers['Team'] == team2, 'WicketsFallen'] = int(team2PrvWicketsFallen)+int(team2Wickets)
    dataPlayers.to_csv('dataPlayers.csv',index=False) 

def getMatchNo():
    fixtures = pd.read_csv('fixtures.csv')    
    #matchNo = fixtures['Match_No'].equals(fixtures.Result != 'TBD')
    matchNo = fixtures[fixtures['Result'] == 'TBD']['Match_No']
    return matchNo

def getMatchDetails(matchNo):
    fixtures = pd.read_csv('fixtures.csv')   
    team1 = fixtures[fixtures['Match_No'] == int(matchNo)]['Team1'].to_string(index=False)
    team2 = fixtures[fixtures['Match_No'] == int(matchNo)]['Team2'].to_string(index=False)
    # print(team1)
    return team1,team2

def getResults():
    result = pd.read_csv('result.csv')
    return result    

def getBestPlayers():
    dataPlayers = pd.read_csv('dataPlayers.csv')
    orangeData = dataPlayers.sort_values(['Runs','WicketsFallen'],ascending=(False, True))
    purpleData = dataPlayers.sort_values(['Wickets','RunsGiven'],ascending=(False, True))
    orangeData = orangeData[['Owner','Runs']]
    purpleData = purpleData[['Owner','Wickets']]
    return orangeData,purpleData