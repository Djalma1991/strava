from controller import get_all_activities_time_range, activities, write_activity, save_athlete
from datetime import datetime

if __name__ == "__main__":

    athlete_id_ = 65927882
    before = datetime.timestamp(datetime.now()) 
    after = datetime.timestamp(datetime.now()) - 432000

    atividade_do_djalminha = get_all_activities_time_range(athlete_id=athlete_id_, after=after, before=before)
    for i in atividade_do_djalminha:
        activity = activities(athlete_id=athlete_id_, activity_id=i)