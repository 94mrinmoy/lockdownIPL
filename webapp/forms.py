from django import forms
import service as s

class NameForm(forms.Form):
    matchNo = s.getMatchNo()
    matchNo = matchNo.values.tolist()
    matchNo =  [tuple([x,x]) for x in matchNo]
    wickets = [tuple([x,x]) for x in range(0,11)]
    overs = [tuple([x,x]) for x in range(0,6)]
    balls = [tuple([x,x]) for x in range(0,6)]
    teams = ['CSK','KKR','KXI','MI','RCB','RR','SRH']
    teams = [tuple([x,x]) for x in teams]
    # match_no = forms.ChoiceField(choices=matchNo, required=True )
    match_no = forms.CharField(label='Match No ', widget=forms.Select(choices=matchNo))
    # team1 = forms.CharField(label='Team 1 ', max_length=4)
    # team2 = forms.CharField(label='Team 2 ', max_length=4)
    team1 = forms.CharField(label='Team 1 ', widget=forms.Select(choices=teams))
    team2 = forms.CharField(label='Team 2 ', widget=forms.Select(choices=teams))
    team1Run = forms.CharField(label='Team 1 Run ', max_length=4)
    team1Wickets = forms.CharField(label='Team 1 Wickets ', widget=forms.Select(choices=wickets))
    team1Overs = forms.CharField(label='Team 1 Overs ', widget=forms.Select(choices=overs))
    team1Balls = forms.CharField(label='Team 1 Balls ', widget=forms.Select(choices=balls))
    team2Run = forms.CharField(label='Team 2 Run ', max_length=4)
    team2Wickets = forms.CharField(label='Team 2 Wickets ', widget=forms.Select(choices=wickets))
    team2Overs = forms.CharField(label='Team 2 Overs ', widget=forms.Select(choices=overs))
    team2Balls = forms.CharField(label='Team 2 Balls ', widget=forms.Select(choices=balls))

class NameForm2(forms.Form):
    def __init__(self, matchNo):
        self.matchNo = matchNo
    team1=""
    team2=""
    def form2(self):    
        print(self.matchNo)
        global match_no
        global team1
        global team2
        match_no = self.matchNo
        team1,team2 = s.getMatchDetails(self.matchNo)
        # matchNo = matchNo.values.tolist()
        # matchNo =  [tuple([x,x]) for x in matchNo]
        # match_no = forms.ChoiceField(choices=matchNo, required=True )
        # match_no = forms.CharField(label='Match No ', widget=forms.Select(choices=matchNo))
    your_name = forms.CharField(label='t', max_length=100) 
        # forms.label(team1)   
    print(team1,team2)
        
    