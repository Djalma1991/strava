from controller import get_all_activities_time_range, activities, update_gear_in_strava
from db import DB
from datetime import datetime

if __name__ == "__main__":

    def get_last_activities():
        athlete_id_ = 65927882
        before = datetime.timestamp(datetime.now()) 
        after = datetime.timestamp(datetime.now()) - 432000*60

        atividade_do_djalminha = get_all_activities_time_range(athlete_id=athlete_id_, after=after, before=before)
        for i in atividade_do_djalminha:
            activity = activities(athlete_id=athlete_id_, activity_id=i)
    get_last_activities()
    '''
    athlete_id_ = 65927882
    gear_id = 'b11615777'
    a = update_gear_in_strava(athlete_id=athlete_id_, gear_id=gear_id)
    print(a)
    '''