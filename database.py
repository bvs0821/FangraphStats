import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
Base = declarative_base()

from stats import FanGraphHitterCall
from stats import FanGraphPitcherCall

class FanGraphDatabase:

    # Use sqlite for engine
    DB_ENGINE = {
        'SQLITE': 'sqlite:///{DB}'
    }

    # Main DB Connection Ref Obj
    db_engine = None

    # initialize database and SQLite engine
    def __init__(self, day):

        self.db_engine = create_engine('sqlite:///fangraph_{}days.db'.format(day), echo=True)
        print(self.db_engine)

        self.Base = declarative_base(bind=self.db_engine)
        self.meta = self.Base.metadata

    # create SQL table with all hitting statistic categories for specified date range
    def insert_mlb_hitting(self, day):

        conn = self.db_engine.connect()
        call = FanGraphHitterCall(day)

        record = call.hitters

        df_hitters = record
        for i in range(len(df_hitters)):
            try:
                df_hitters.iloc[i:i + 1].to_sql("hitter_fangraph", conn, if_exists='append', index=False)
            except IntegrityError:
                pass

        pd.read_sql('SELECT * FROM hitter_fangraph', conn)

        print('Hitting Records Added')

    # create SQL table with all pitching statistic categories for specified date range
    def insert_mlb_pitching(self, day):

        conn = self.db_engine.connect()
        call = FanGraphPitcherCall(day)

        record = call.pitchers

        df_pitchers = record
        for i in range(len(df_pitchers)):
            try:
                df_pitchers.iloc[i:i + 1].to_sql("pitcher_fangraph", conn, if_exists='append', index=False)
            except IntegrityError:
                pass

        pd.read_sql('SELECT * FROM pitcher_fangraph', conn)

        print("Pitching Records Added")


