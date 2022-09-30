import pandas as pd
import sqlalchemy
import os
cwd = os.getcwd()

#delete all DB files before compiling data
for i in range(365):
    try:
        os.remove(cwd + "/fangraph_{}days.db".format(i))
    except:
        pass

# import to create SQL tables for fangraph stats
from fangraphtables import *

# script populates all FanGraph stats table with corresponding stats of each date range
for day in num_days:

    # connect to specified SQLite Database based on date range
    db = FanGraphDatabase(day)
    engine = db.db_engine

    # Hitters SQL table queries
    hitter_table1 = "INSERT INTO hitter_standard SELECT lastName, firstName, Team," \
                    " Age, G, AB, PA, H, single, double, triple, HR, R, RBI, BB, IBB, SO, " \
                    "HBP, SF, SH,GDP, SB, CS, AVG FROM hitter_fangraph "

    hitter_table2 = "INSERT INTO hitter_advanced SELECT lastName, firstName, Team," \
                    " Age, PA, BBpercent, Kpercent, BBperK, AVG, OBP, SLG, OPS, ISO, Spd, " \
                    "BABIP, UBR, wGDP, wSB, wRC, wRAA, wOBA, wRCplus FROM hitter_fangraph "

    hitter_table3 = "INSERT OR REPLACE INTO hitter_batted_balls SELECT lastName, firstName,Team," \
                    " Age, BABIP, GBperFB, LDpercent, GBpercent, FBpercent, IFFBpercent, " \
                    "HRperFB, IFH, IFHpercent, BUH, BUHpercent, Pullpercent, Centpercent, Oppopercent, Softpercent, " \
                    "Medpercent, Hardpercent FROM hitter_fangraph "

    hitter_table4 = "INSERT OR REPLACE INTO hitter_win_probability SELECT lastName, firstName, Team," \
                    " Age, WPA, minusWPA, plusWPA, RE24, REW, pLI, phLI, PH, " \
                    "WPAperLI, Clutch FROM hitter_fangraph "

    hitter_table5 = "INSERT INTO hitter_pitch_type SELECT lastName, firstName, Team," \
                    " Age, FBpercent, FBv, SLpercent, SLv, CTpercent, CTv, CBpercent, CBv, " \
                    "CHpercent, CHv, SFpercent, SFv, KNpercent, KNv, XXpercent FROM hitter_fangraph "

    hitter_table6 = "INSERT INTO hitter_pitch_value SELECT lastName, firstName, Team," \
                    " Age, wFB, wSL, wCT, wCB, wCH, wSF, wKN, wFBperC, wSLperC, wCTperC, " \
                    "wCBperC, wCHperC, wSFperC, wKNperC FROM hitter_fangraph "

    hitter_table7 = "INSERT INTO hitter_plate_discipline SELECT lastName, firstName, Team," \
                    " Age, OSwingpercent, ZSwingpercent, Swingpercent, " \
                    "OContactpercent, ZContactpercent, Contactpercent, Zonepercent, FStrikepercent, " \
                    "SwStrpercent, CStrpercent, CSWpercent FROM hitter_fangraph "


    hitter_table8 = "INSERT INTO hitter_value SELECT lastName, firstName, Team," \
                    " Age, Bat, BsR, Spd, Fld, Pos, Off, Def, Lg," \
                    " Rep, RAR, WAR, Dol FROM hitter_fangraph "


    hitter_table9 = "INSERT INTO hitter_pitchinfo_pitchtype SELECT lastName, firstName,Team," \
                    " Age, PA, FApercent, FCpercent, FSpercent, SIpercent, "\
                    "CHpercent, SLpercent, CUpercent, CSpercent, KNpercent, SBpercent, XXpercent FROM hitter_fangraph "

    hitter_table10 = "INSERT INTO hitter_pitchinfo_velocity SELECT lastName, firstName, Team," \
                     " Age, PA, vFA, vFC, vFS, vSI, vCH, vSL, vCU, vCS, vKN, " \
                     "vSB FROM hitter_fangraph "

    hitter_table11 = "INSERT INTO hitter_pitchinfo_hmovement SELECT lastName, firstName, Team," \
                     " Age, PA, FAX, FCX, FSX, SIX, CHX, " \
                     "SLX, CUX, CSX, KNX, SBX FROM hitter_fangraph "

    hitter_table12 = "INSERT INTO hitter_pitchinfo_vmovement SELECT lastName, firstName, Team," \
                     " Age, PA, FAZ, FCZ, FSZ, SIZ, CHZ, " \
                     "SLZ, CUZ, CSZ, KNZ, SBZ FROM hitter_fangraph "

    hitter_table13 = "INSERT INTO hitter_pitchinfo_typevalue SELECT lastName, firstName, Team," \
                     " Age, PA, wFA, wFC, wFS, wSI, wCH, wSL, wCU, wCS, " \
                     "wKN, wSB FROM hitter_fangraph "

    hitter_table14 = "INSERT INTO hitter_pitchinfo_value100 SELECT lastName, firstName, Team," \
                     " Age, PA, wFAperC, wFCperC, wFSperC, wSIperC, " \
                     "wCHperC, wSLperC, wCUperC, wCSperC, wKNperC, wSBperC FROM hitter_fangraph "

    hitter_table15 = "INSERT INTO hitter_pitchinfo_discipline SELECT lastName, firstName, Team," \
                     " Age, PA, OSwingpercent, ZSwingpercent, Swingpercent, " \
                     "OContactpercent, ZContactpercent, Contactpercent, Zonepercent, Pace FROM hitter_fangraph "

    hitter_table16 = "INSERT INTO hitter_plusstats SELECT lastName, firstName,Team," \
                     " Age, PA, BBpercentplus, Kpercentplus, AVGplus, OBPplus, SLGplus, " \
                     "wRCplus, ISOplus, BABIPplus, LDpercentplus, GBpercentplus, FBpercentplus, Pullpercentplus, " \
                     "Centpercentplus, Oppopercentplus FROM hitter_fangraph "

    hitter_table17 = "INSERT INTO hitter_statcast SELECT lastName, firstName, Team," \
                     " Age, PA, Events, EV, maxEV, LA, Barrels, Barrelpercent, HardHit, " \
                     "HardHitpercent, AVG, xBA, SLG, xSLG, wOBA, xwOBA FROM hitter_fangraph "

    # Pitcher SQL table queries
    pitcher_table1 = "INSERT INTO pitcher_standard SELECT lastName, firstName, Team," \
                     " Age, W, L, ERA, G, GS, CG, ShO, SV, HLD, BS, IP, TBF, H, R, ER, HR, " \
                     "BB, IBB, HBP, WP, BK, SO FROM pitcher_fangraph "

    pitcher_table2 = "INSERT INTO pitcher_advanced SELECT lastName, firstName, Team," \
                     " Age, Kper9, BBper9, KperBB, HRper9, Kpercent, BBpercent, " \
                     "KBBpercent, AVG, WHIP, BABIP, LOBpercent, ERAminus, FIPminus, xFIPminus, ERA, FIP, EF, " \
                     "xFIP, SIERA FROM pitcher_fangraph "

    pitcher_table3 = "INSERT OR REPLACE INTO pitcher_batted_balls SELECT lastName, firstName, Team," \
                     " Age, BABIP, GBperFB, LDpercent, GBpercent, FBpercent, " \
                     "IFFBpercent, HRperFB, RS, RSper9, Balls, Strikes, Pitches, Pullpercent, Centpercent, Oppopercent, " \
                     "Softpercent, Medpercent, Hardpercent FROM pitcher_fangraph "

    pitcher_table4 = "INSERT OR REPLACE INTO pitcher_win_probability SELECT lastName, firstName, Team," \
                     " Age, WPA, minusWPA, plusWPA, RE24, REW, pLI, inLI, gmLI, " \
                     "exLI, Pulls, WPAperLI, Clutch, SD FROM pitcher_fangraph "

    pitcher_table5 = "INSERT INTO pitcher_pitch_type SELECT lastName, firstName, Team," \
                     " Age, FBpercent, FBv, SLpercent, SLv, CTpercent, CTv, CBpercent, CBv, " \
                     "CHpercent, CHv, SFpercent, SFv, KNpercent, KNv, XXpercent FROM pitcher_fangraph "

    pitcher_table6 = "INSERT INTO pitcher_pitch_value SELECT lastName, firstName, Team," \
                     " Age, wFB, wSL, wCT, wCB, wCH, wSF, wKN, wFBperC, wSLperC, wCTperC, " \
                     "wCBperC, wCHperC, wSFperC, wKNperC FROM pitcher_fangraph "

    pitcher_table7 = "INSERT INTO pitcher_plate_discipline SELECT lastName, firstName, Team," \
                     " Age, OSwingpercent, ZSwingpercent, Swingpercent, " \
                     "OContactpercent, ZContactpercent, Contactpercent, Zonepercent, FStrikepercent, " \
                     "SwStrpercent, CStrpercent, CSWpercent FROM pitcher_fangraph "

    pitcher_table8 = "INSERT INTO pitcher_value SELECT lastName, firstName, Team," \
                     " Age, RA9minusWAR, BIPminusWins, LOBminusWins, FDPminusWins, RAR, WAR, " \
                     "Dollars FROM pitcher_fangraph "

    pitcher_table9 = "INSERT INTO pitcher_pitchinfo_pitchtype SELECT lastName, firstName, Team," \
                     " Age, IP, FApercent, FCpercent, FSpercent, SIpercent, " \
                     "CHpercent, SLpercent, CUpercent, CSpercent, KNpercent, SBpercent, XXpercent FROM pitcher_fangraph "

    pitcher_table10 = "INSERT INTO pitcher_pitchinfo_velocity SELECT lastName, firstName, Team," \
                      " Age, IP, vFA, vFC, vFS, vSI, vCH, vSL, vCU, vCS, vKN, " \
                      "vSB FROM pitcher_fangraph "

    pitcher_table11 = "INSERT INTO pitcher_pitchinfo_hmovement SELECT lastName, firstName, Team," \
                      " Age, IP, FAX, FCX, FSX, SIX, CHX, " \
                      "SLX, CUX, CSX, KNX, SBX FROM pitcher_fangraph "

    pitcher_table12 = "INSERT INTO pitcher_pitchinfo_vmovement SELECT lastName, firstName, Team," \
                      " Age, IP, FAZ, FCZ, FSZ, SIZ, CHZ, " \
                      "SLZ, CUZ, CSZ, KNZ, SBZ FROM pitcher_fangraph "

    pitcher_table13 = "INSERT INTO pitcher_pitchinfo_typevalue SELECT lastName, firstName, Team," \
                      " Age, IP, wFA, wFC, wFS, wSI, wCH, wSL, wCU, wCS, wKN, " \
                      "wSB FROM pitcher_fangraph "

    pitcher_table14 = "INSERT INTO pitcher_pitchinfo_value100 SELECT lastName, firstName, Team," \
                      " Age, IP, wFAperC, wFCperC, wFSperC, wSIperC, " \
                      "wCHperC, wSLperC, wCUperC, wCSperC, wKNperC, wSBperC FROM pitcher_fangraph "

    pitcher_table15 = "INSERT INTO pitcher_pitchinfo_discipline SELECT lastName, firstName, Team," \
                      " Age, IP, OSwingpercent, ZSwingpercent, " \
                      "Swingpercent, OContactpercent, ZContactpercent, Contactpercent, Zonepercent, " \
                      "Pace FROM pitcher_fangraph "

    pitcher_table16 = "INSERT INTO pitcher_plusstats SELECT lastName, firstName, Team," \
                      " Age, IP, Kper9plus, BBper9plus, KperBBplus, HRper9plus, Kpercentplus, " \
                      "BBpercentplus, AVGplus, WHIPplus, BABIPplus, LOBpercentplus, ERAminus, FIPminus, xFIPminus, " \
                      "LDpercentplus, GBpercentplus, FBpercentplus FROM pitcher_fangraph "

    pitcher_table17 = "INSERT INTO pitcher_statcast SELECT lastName, firstName, Team," \
                      " Age, IP, Events, EV, maxEV, LA, Barrels, Barrelpercent, HardHit, " \
                      "HardHitpercent, ERA, xERA FROM pitcher_fangraph "


    # connect to SQLite DB engine
    conn = engine.connect()
    # gather all hitting and pitching statistics in a SQL table for specified date range
    add_hit_data = db.insert_mlb_hitting(day)
    add_pitch_data = db.insert_mlb_pitching(day)

    # list of SQL queries to populate FanGraph stat tables
    hitter_stmt = [hitter_table1, hitter_table2, hitter_table3, hitter_table4, hitter_table4, hitter_table5, hitter_table6,
                   hitter_table7, hitter_table8, hitter_table9, hitter_table10, hitter_table11, hitter_table12,
                   hitter_table13,hitter_table14, hitter_table15, hitter_table16, hitter_table17]

    pitcher_stmt = [pitcher_table1, pitcher_table2, pitcher_table3, pitcher_table4, pitcher_table4, pitcher_table5,
                    pitcher_table6, pitcher_table7, pitcher_table8, pitcher_table9, pitcher_table10, pitcher_table11,
                    pitcher_table12, pitcher_table13, pitcher_table14, pitcher_table15, pitcher_table16, pitcher_table17]


    # populates FanGraph hitting stat tables be iterating though queries
    for i in range(0, 18):
        try:
            pd.read_sql(hitter_stmt[i], engine)
            print(i)
        except sqlalchemy.exc.ResourceClosedError:
            pass
        except sqlalchemy.exc.IntegrityError:
            pass

    # populates FanGraph pitching stat tables be iterating though queries
    for i in range(0, 18):
        try:
            pd.read_sql(pitcher_stmt[i], engine)
        except sqlalchemy.exc.ResourceClosedError:
            pass
        except sqlalchemy.exc.IntegrityError:
            pass
