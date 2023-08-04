from controller import get_all_activities_time_range, activities, write_activity, save_athlete

athlete_id_ = 65927882
before_=1642896000
after_=1577836800


#djalma = save_athlete(athlete_id=athlete_id_)
#atividade = activities(athlete_id=athlete_id_, activity_id=9578073578)

atividade_do_djalminha = get_all_activities_time_range(athlete_id=athlete_id_,before=before_, after=after_)
for i in atividade_do_djalminha:
    activity = activities(athlete_id=athlete_id_, activity_id=i)