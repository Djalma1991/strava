from controller import save_athlete

# auth = Auth(athlete_id=65927882)
# # data = auth.authorization_token(code="df98abd1c7ba27610ed8c8480e1d2e69f990a2cc")
# data = auth.refresh_token()
# print(data)
# Athlete = Athlete(athlete_id=65927882)
# djalminha = Athlete.get()
# print(djalminha)

djalminha = save_athlete()
print(djalminha)
