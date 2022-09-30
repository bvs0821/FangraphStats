from sqlalchemy import PrimaryKeyConstraint, ForeignKeyConstraint
from sqlalchemy import Table, Column, Integer, String, DateTime, Date, Boolean, Float
from fangraphdatabase import FanGraphDatabase
from fangraphstats import date_ranges

# script used to create tables for SQLALchemy Object Relational Mapping
num_days = date_ranges()

for day in num_days:
    db = FanGraphDatabase(day)

    # class to instantiate a table for hitting stats from MLBStats API for first date range
    class HitterFanGraph(db.Base):
        __tablename__ = "hitter_fangraph"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            # ForeignKeyConstraint(
            #    columns=['personID'],
            #    refcolumns=['hitter_mapping.personID']
            # ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        G = Column(Integer)
        AB = Column(Integer)
        PA = Column(Integer)
        H = Column(Integer)
        single = Column(Integer)
        double = Column(Integer)
        triple = Column(Integer)
        HR = Column(Integer)
        R = Column(Integer)
        RBI = Column(Integer)
        BB = Column(Integer)
        IBB = Column(Integer)
        SO = Column(Integer)
        HBP = Column(Integer)
        SF = Column(Integer)
        SH = Column(Integer)
        GDP = Column(Integer)
        SB = Column(Integer)
        CS = Column(Integer)
        AVG = Column(Float)
        GB = Column(Float)
        FB = Column(Float)
        LD = Column(Float)
        IFFB = Column(Float)
        Pitches = Column(Float)
        Balls = Column(Float)
        Strikes = Column(Float)
        IFH = Column(Float)
        BU = Column(Float)
        BUH = Column(Float)
        BBpercent = Column(Float)
        Kpercent = Column(Float)
        BBperK = Column(Float)
        OBP = Column(Float)
        SLG = Column(Float)
        OPS = Column(Float)
        ISO = Column(Float)
        BABIP = Column(Float)
        GBperFB = Column(Float)
        LDpercent = Column(Float)
        GBpercent = Column(Float)
        FBpercent = Column(Float)
        IFFBpercent = Column(Float)
        HRperFB = Column(Float)
        IFHpercent = Column(Float)
        BUHpercent = Column(Float)
        wOBA = Column(Float)
        wRAA = Column(Float)
        wRC = Column(Float)
        Bat = Column(Float)
        Fld = Column(Float)
        Rep = Column(Float)
        Pos = Column(Float)
        RAR = Column(Float)
        WAR = Column(Float)
        Dol = Column(Float)
        Spd = Column(Float)
        wRCplus = Column(Float)
        WPA = Column(Float)
        minusWPA = Column(Float)
        plusWPA = Column(Float)
        RE24 = Column(Float)
        REW = Column(Float)
        pLI = Column(Float)
        phLI = Column(Float)
        PH = Column(Float)
        WPAperLI = Column(Float)
        Clutch = Column(Float)
        FBv = Column(Float)
        SLpercent = Column(Float)
        SLv = Column(Float)
        CTpercent = Column(Float)
        CTv = Column(Float)
        CBpercent = Column(Float)
        CBv = Column(Float)
        CHpercent = Column(Float)
        CHv = Column(Float)
        SFpercent = Column(Float)
        SFv = Column(Float)
        KNpercent = Column(Float)
        KNv = Column(Float)
        XXpercent = Column(Float)
        POpercent = Column(Float)
        wFB = Column(Float)
        wSL = Column(Float)
        wCT = Column(Float)
        wCB = Column(Float)
        wCH = Column(Float)
        wSF = Column(Float)
        wKN = Column(Float)
        wFBperC = Column(Float)
        wSLperC = Column(Float)
        wCTperC = Column(Float)
        wCBperC = Column(Float)
        wCHperC = Column(Float)
        wSFperC = Column(Float)
        wKNperC = Column(Float)
        OSwingpercent = Column(Float)
        ZSwingpercent = Column(Float)
        Swingpercent = Column(Float)
        OContactpercent = Column(Float)
        ZContactpercent = Column(Float)
        Contactpercent = Column(Float)
        Zonepercent = Column(Float)
        FStrikepercent = Column(Float)
        SwStrpercent = Column(Float)
        BsR = Column(Float)
        FApercent = Column(Float)
        FTpercent = Column(Float)
        FCpercent = Column(Float)
        FSpercent = Column(Float)
        FOpercent = Column(Float)
        SIpercent = Column(Float)
        CUpercent = Column(Float)
        KCpercent = Column(Float)
        EPpercent = Column(Float)
        SCpercent = Column(Float)
        UNpercent = Column(Float)
        vFA = Column(Float)
        vFT = Column(Float)
        vFC = Column(Float)
        vFS = Column(Float)
        vFO = Column(Float)
        vSI = Column(Float)
        vSL = Column(Float)
        vCU = Column(Float)
        vKC = Column(Float)
        vEP = Column(Float)
        vCH = Column(Float)
        vSC = Column(Float)
        vKN = Column(Float)
        FAX = Column(Float)
        FTX = Column(Float)
        FCX = Column(Float)
        FSX = Column(Float)
        FOX = Column(Float)
        SIX = Column(Float)
        SLX = Column(Float)
        CUX = Column(Float)
        KCX = Column(Float)
        EPX = Column(Float)
        CHX = Column(Float)
        SCX = Column(Float)
        KNX = Column(Float)
        FAZ = Column(Float)
        FTZ = Column(Float)
        FCZ = Column(Float)
        FSZ = Column(Float)
        FOZ = Column(Float)
        SIZ = Column(Float)
        SLZ = Column(Float)
        CUZ = Column(Float)
        KCZ = Column(Float)
        EPZ = Column(Float)
        CHZ = Column(Float)
        SCZ = Column(Float)
        KNZ = Column(Float)
        wFA = Column(Float)
        wFT = Column(Float)
        wFC = Column(Float)
        wFS = Column(Float)
        wFO = Column(Float)
        wSI = Column(Float)
        wCU = Column(Float)
        wKC = Column(Float)
        wEP = Column(Float)
        wSC = Column(Float)
        wFAperC = Column(Float)
        wFTperC = Column(Float)
        wFCperC = Column(Float)
        wFSperC = Column(Float)
        wFOperC = Column(Float)
        wSIperC = Column(Float)
        wCUperC = Column(Float)
        wKCperC = Column(Float)
        wEPperC = Column(Float)
        wSCperC = Column(Float)
        Pace = Column(Float)
        Def = Column(Float)
        wSB = Column(Float)
        UBR = Column(Float)
        AgeRng = Column(Float)
        Off = Column(Float)
        Lg = Column(Float)
        wGDP = Column(Float)
        Pullpercent = Column(Float)
        Centpercent = Column(Float)
        Oppopercent = Column(Float)
        Softpercent = Column(Float)
        Medpercent = Column(Float)
        Hardpercent = Column(Float)
        TTOpercent = Column(Float)
        CSpercent = Column(Float)
        SBpercent = Column(Float)
        vCS = Column(Float)
        vSB = Column(Float)
        vXX = Column(Float)
        CSX = Column(Float)
        SBX = Column(Float)
        XXX = Column(Float)
        CSZ = Column(Float)
        SBZ = Column(Float)
        XXZ = Column(Float)
        wCS = Column(Float)
        wXX = Column(Float)
        wCSperC = Column(Float)
        wSBperC = Column(Float)
        wXXperC = Column(Float)
        FRM = Column(Float)
        AVGplus = Column(Float)
        BBpercentplus = Column(Float)
        Kpercentplus = Column(Float)
        OBPplus = Column(Float)
        SLGplus = Column(Float)
        ISOplus = Column(Float)
        BABIPplus = Column(Float)
        LDpercentplus = Column(Float)
        GBpercentplus = Column(Float)
        FBpercentplus = Column(Float)
        HRperFBpercentplus = Column(Float)
        Pullpercentplus = Column(Float)
        Centpercentplus = Column(Float)
        Oppopercentplus = Column(Float)
        Softpercentplus = Column(Float)
        Medpercentplus = Column(Float)
        Hardpercentplus = Column(Float)
        EV = Column(Float)
        LA = Column(Float)
        Barrels = Column(Float)
        Barrelpercent = Column(Float)
        maxEV = Column(Float)
        HardHit = Column(Float)
        HardHitpercent = Column(Float)
        Events = Column(Float)
        CStrpercent = Column(Float)
        CSWpercent = Column(Float)
        xBA = Column(Float)
        xSLG = Column(Float)
        xwOBA = Column(Float)
        LWAR = Column(Float)

        # hitter_standard = relationship("HitterStandard", backref="hitter_fangraph")

        def __repr__(self):
            return "<FanGraphs Hitter: Table Created>"


    # class to instantiate a table for hitting stats from MLBStats API for first date range
    class PitcherFanGraph(db.Base):
        __tablename__ = "pitcher_fangraph"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            # ForeignKeyConstraint(
            #    columns=['personID'],
            #    refcolumns=['hitter_mapping.personID']
            # ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        W = Column(Integer)
        L = Column(Integer)
        ERA = Column(Float)
        G = Column(Integer)
        GS = Column(Integer)
        CG = Column(Integer)
        ShO = Column(Integer)
        SV = Column(Integer)
        BS = Column(Integer)
        IP = Column(Float)
        TBF = Column(Float)
        H = Column(Integer)
        R = Column(Integer)
        ER = Column(Integer)
        HR = Column(Integer)
        BB = Column(Integer)
        IBB = Column(Integer)
        HBP = Column(Integer)
        WP = Column(Integer)
        BK = Column(Integer)
        SO = Column(Integer)
        GB = Column(Float)
        FB = Column(Float)
        LD = Column(Float)
        IFFB = Column(Float)
        Balls = Column(Integer)
        Strikes = Column(Integer)
        Pitches = Column(Integer)
        RS = Column(Float)
        IFH = Column(Float)
        BU = Column(Float)
        BUH = Column(Float)
        Kper9 = Column(Float)
        BBper9 = Column(Float)
        KperBB = Column(Float)
        Hper9 = Column(Float)
        HRper9 = Column(Float)
        AVG = Column(Float)
        WHIP = Column(Float)
        BABIP = Column(Float)
        LOBpercent = Column(Float)
        FIP = Column(Float)
        GBperFB = Column(Float)
        LDpercent = Column(Float)
        GBpercent = Column(Float)
        FBpercent = Column(Float)
        IFFBpercent = Column(Float)
        HRperFB = Column(Float)
        IFHpercent = Column(Float)
        BUHpercent = Column(Float)
        Starting = Column(Float)
        StartIP = Column(Float)
        Relieving = Column(Float)
        ReliefIP = Column(Float)
        RAR = Column(Float)
        WAR = Column(Float)
        Dollars = Column(Float)
        tERA = Column(Float)
        xFIP = Column(Float)
        WPA = Column(Float)
        minusWPA = Column(Float)
        plusWPA = Column(Float)
        RE24 = Column(Float)
        REW = Column(Float)
        pLI = Column(Float)
        inLI = Column(Float)
        gmLI = Column(Float)
        exLI = Column(Float)
        Pulls = Column(Float)
        WPAperLI = Column(Float)
        Clutch = Column(Float)
        FBv = Column(Float)
        SLpercent = Column(Float)
        SLv = Column(Float)
        CTpercent = Column(Float)
        CTv = Column(Float)
        CBpercent = Column(Float)
        CBv = Column(Float)
        CHpercent = Column(Float)
        CHv = Column(Float)
        SFpercent = Column(Float)
        SFv = Column(Float)
        KNpercent = Column(Float)
        KNv = Column(Float)
        XXpercent = Column(Float)
        POpercent = Column(Float)
        wFB = Column(Float)
        wSL = Column(Float)
        wCT = Column(Float)
        wCB = Column(Float)
        wCH = Column(Float)
        wSF = Column(Float)
        wKN = Column(Float)
        wFBperC = Column(Float)
        wSLperC = Column(Float)
        wCTperC = Column(Float)
        wCBperC = Column(Float)
        wCHperC = Column(Float)
        wSFperC = Column(Float)
        wKNperC = Column(Float)
        OSwingpercent = Column(Float)
        ZSwingpercent = Column(Float)
        Swingpercent = Column(Float)
        OContactpercent = Column(Float)
        ZContactpercent = Column(Float)
        Contactpercent = Column(Float)
        Zonepercent = Column(Float)
        FStrikepercent = Column(Float)
        SwStrpercent = Column(Float)
        HLD = Column(Float)
        SD = Column(Float)
        MD = Column(Float)
        ERAminus = Column(Float)
        FIPminus = Column(Float)
        xFIPminus = Column(Float)
        Kpercent = Column(Float)
        BBpercent = Column(Float)
        SIERA = Column(Float)
        RSper9 = Column(Float)
        EF = Column(Float)
        FApercent = Column(Float)
        FTpercent = Column(Float)
        FCpercent = Column(Float)
        FSpercent = Column(Float)
        FOpercent = Column(Float)
        SIpercent = Column(Float)
        CUpercent = Column(Float)
        KCpercent = Column(Float)
        EPpercent = Column(Float)
        SCpercent = Column(Float)
        UNpercent = Column(Float)
        vFA = Column(Float)
        vFT = Column(Float)
        vFC = Column(Float)
        vFS = Column(Float)
        vFO = Column(Float)
        vSI = Column(Float)
        vSL = Column(Float)
        vCU = Column(Float)
        vKC = Column(Float)
        vEP = Column(Float)
        vCH = Column(Float)
        vSC = Column(Float)
        vKN = Column(Float)
        FAX = Column(Float)
        FTX = Column(Float)
        FCX = Column(Float)
        FSX = Column(Float)
        FOX = Column(Float)
        SIX = Column(Float)
        SLX = Column(Float)
        CUX = Column(Float)
        KCX = Column(Float)
        EPX = Column(Float)
        CHX = Column(Float)
        SCX = Column(Float)
        KNX = Column(Float)
        FAZ = Column(Float)
        FTZ = Column(Float)
        FCZ = Column(Float)
        FSZ = Column(Float)
        FOZ = Column(Float)
        SIZ = Column(Float)
        SLZ = Column(Float)
        CUZ = Column(Float)
        KCZ = Column(Float)
        EPZ = Column(Float)
        CHZ = Column(Float)
        SCZ = Column(Float)
        KNZ = Column(Float)
        wFA = Column(Float)
        wFT = Column(Float)
        wFC = Column(Float)
        wFS = Column(Float)
        wFO = Column(Float)
        wSI = Column(Float)
        wCU = Column(Float)
        wKC = Column(Float)
        wEP = Column(Float)
        wSC = Column(Float)
        wFAperC = Column(Float)
        wFTperC = Column(Float)
        wFCperC = Column(Float)
        wFSperC = Column(Float)
        wFOperC = Column(Float)
        wSIperC = Column(Float)
        wCUperC = Column(Float)
        wKCperC = Column(Float)
        wEPperC = Column(Float)
        wSCperC = Column(Float)
        Pace = Column(Float)
        RA9minusWAR = Column(Float)
        BIPminusWins = Column(Float)
        LOBminusWins = Column(Float)
        FDPminusWins = Column(Float)
        AgeRng = Column(Float)
        KBBpercent = Column(Float)
        Pullpercent = Column(Float)
        Centpercent = Column(Float)
        Oppopercent = Column(Float)
        Softpercent = Column(Float)
        Medpercent = Column(Float)
        Hardpercent = Column(Float)
        kwERA = Column(Float)
        TTOpercent = Column(Float)
        CSpercent = Column(Float)
        SBpercent = Column(Float)
        vCS = Column(Float)
        vSB = Column(Float)
        vXX = Column(Float)
        CSX = Column(Float)
        SBX = Column(Float)
        XXX = Column(Float)
        CSZ = Column(Float)
        SBZ = Column(Float)
        XXZ = Column(Float)
        wCS = Column(Float)
        wSB = Column(Float)
        wXX = Column(Float)
        wCSperC = Column(Float)
        wSBperC = Column(Float)
        wXXperC = Column(Float)
        FRM = Column(Float)
        Kper9plus = Column(Float)
        BBper9plus = Column(Float)
        KperBBplus = Column(Float)
        Hper9plus = Column(Float)
        HRper9plus = Column(Float)
        AVGplus = Column(Float)
        WHIPplus = Column(Float)
        BABIPplus = Column(Float)
        LOBpercentplus = Column(Float)
        Kpercentplus = Column(Float)
        BBpercentplus = Column(Float)
        LDpercentplus = Column(Float)
        GBpercentplus = Column(Float)
        FBpercentplus = Column(Float)
        HRperFBpercentplus = Column(Float)
        Pullpercentplus = Column(Float)
        Centpercentplus = Column(Float)
        Oppopercentplus = Column(Float)
        Softpercentplus = Column(Float)
        Medpercentplus = Column(Float)
        Hardpercentplus = Column(Float)
        EV = Column(Float)
        LA = Column(Float)
        Barrels = Column(Float)
        Barrelpercent = Column(Float)
        maxEV = Column(Float)
        HardHit = Column(Float)
        HardHitpercent = Column(Float)
        Events = Column(Float)
        CStrpercent = Column(Float)
        CSWpercent = Column(Float)
        xERA = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher: Table Created>"


    # class to instantiate a table for hitting stats from MLBStats API for first date range
    class HitterStandard(db.Base):
        __tablename__ = "hitter_standard"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        G = Column(Integer)
        AB = Column(Integer)
        PA = Column(Integer)
        H = Column(Integer)
        single = Column(Integer)
        double = Column(Integer)
        triple = Column(Integer)
        HR = Column(Integer)
        R = Column(Integer)
        RBI = Column(Integer)
        BB = Column(Integer)
        IBB = Column(Integer)
        SO = Column(Integer)
        HBP = Column(Integer)
        SF = Column(Integer)
        SH = Column(Integer)
        GDP = Column(Integer)
        SB = Column(Integer)
        CS = Column(Integer)
        AVG = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Standard: Table Created>"


    class HitterAdvanced(db.Base):
        __tablename__ = "hitter_advanced"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        PA = Column(Integer)
        BBpercent = Column(Float)
        Kpercent = Column(Float)
        BBperK = Column(Float)
        AVG = Column(Float)
        OBP = Column(Float)
        SLG = Column(Float)
        OPS = Column(Float)
        ISO = Column(Float)
        Spd = Column(Float)
        BABIP = Column(Float)
        UBR = Column(Float)
        wGDP = Column(Float)
        wSB = Column(Float)
        wRC = Column(Float)
        wRAA = Column(Float)
        wOBA = Column(Float)
        wRCplus = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Advanced: Table Created>"


    class HitterBattedBalls(db.Base):
        __tablename__ = "hitter_batted_balls"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        BABIP = Column(Float)
        GBperFB = Column(Float)
        LDpercent = Column(Float)
        GBpercent = Column(Float)
        FBpercent = Column(Float)
        IFFBpercent = Column(Float)
        HRperFB = Column(Float)
        IFH = Column(Float)
        IFHpercent = Column(Float)
        BUH = Column(Float)
        BUHpercent = Column(Float)
        Pullpercent = Column(Float)
        Centpercent = Column(Float)
        Oppopercent = Column(Float)
        Softpercent = Column(Float)
        Medpercent = Column(Float)
        Hardpercent = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Batted Balls: Table Created>"


    class HitterWinProbability(db.Base):
        __tablename__ = "hitter_win_probability"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        WPA = Column(Float)
        minusWPA = Column(Float)
        plusWPA = Column(Float)
        RE24 = Column(Float)
        REW = Column(Float)
        pLI = Column(Float)
        phLI = Column(Float)
        PH = Column(Float)
        WPAperLI = Column(Float)
        Clutch = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Win Probability: Table Created>"


    class HitterPitchType(db.Base):
        __tablename__ = "hitter_pitch_type"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        FBpercent = Column(Float)
        FBv = Column(Float)
        SLpercent = Column(Float)
        SLv = Column(Float)
        CTpercent = Column(Float)
        CTv = Column(Float)
        CBpercent = Column(Float)
        CBv = Column(Float)
        CHpercent = Column(Float)
        CHv = Column(Float)
        SFpercent = Column(Float)
        SFv = Column(Float)
        KNpercent = Column(Float)
        KNv = Column(Float)
        XXpercent = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Pitch Type: Table Created>"


    class HitterPitchValue(db.Base):
        __tablename__ = "hitter_pitch_value"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        wFB = Column(Float)
        wSL = Column(Float)
        wCT = Column(Float)
        wCB = Column(Float)
        wCH = Column(Float)
        wSF = Column(Float)
        wKN = Column(Float)
        wFBperC = Column(Float)
        wSLperC = Column(Float)
        wCTperC = Column(Float)
        wCBperC = Column(Float)
        wCHperC = Column(Float)
        wSFperC = Column(Float)
        wKNperC = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Pitch Value: Table Created>"


    class HitterPlateDiscipline(db.Base):
        __tablename__ = "hitter_plate_discipline"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        OSwingpercent = Column(Float)
        ZSwingpercent = Column(Float)
        Swingpercent = Column(Float)
        OContactpercent = Column(Float)
        ZContactpercent = Column(Float)
        Contactpercent = Column(Float)
        Zonepercent = Column(Float)
        FStrikepercent = Column(Float)
        SwStrpercent = Column(Float)
        CStrpercent = Column(Float)
        CSWpercent = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Plate Discipline: Table Created>"


    class HitterValue(db.Base):
        __tablename__ = "hitter_value"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        Bat = Column(Float)
        BsR = Column(Float)
        Spd = Column(Float)
        Fld = Column(Float)
        Pos = Column(Float)
        Off = Column(Float)
        Def = Column(Float)
        Lg = Column(Float)
        Rep = Column(Float)
        RAR = Column(Float)
        WAR = Column(Float)
        Dol = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Value: Table Created>"


    class HitterPitchInfoPitchType(db.Base):
        __tablename__ = "hitter_pitchinfo_pitchtype"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        PA = Column(Integer)
        FApercent = Column(Float)
        FCpercent = Column(Float)
        FSpercent = Column(Float)
        SIpercent = Column(Float)
        CHpercent = Column(Float)
        SLpercent = Column(Float)
        CUpercent = Column(Float)
        CSpercent = Column(Float)
        KNpercent = Column(Float)
        SBpercent = Column(Float)
        XXpercent = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Pitch InfoPitch Type: Table Created>"


    class HitterPitchInfoVelocity(db.Base):
        __tablename__ = "hitter_pitchinfo_velocity"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        PA = Column(Integer)
        vFA = Column(Float)
        vFC = Column(Float)
        vFS = Column(Float)
        vSI = Column(Float)
        vCH = Column(Float)
        vSL = Column(Float)
        vCU = Column(Float)
        vCS = Column(Float)
        vKN = Column(Float)
        vSB = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Pitch InfoVelocity: Table Created>"


    class HitterPitchInfoHMovement(db.Base):
        __tablename__ = "hitter_pitchinfo_hmovement"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        PA = Column(Integer)
        FAX = Column(Float)
        FCX = Column(Float)
        FSX = Column(Float)
        SIX = Column(Float)
        CHX = Column(Float)
        SLX = Column(Float)
        CUX = Column(Float)
        CSX = Column(Float)
        KNX = Column(Float)
        SBX = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Pitch Info  HMovement: Table Created>"


    class HitterPitchInfoVMovement(db.Base):
        __tablename__ = "hitter_pitchinfo_vmovement"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        PA = Column(Integer)
        FAZ = Column(Float)
        FCZ = Column(Float)
        FSZ = Column(Float)
        SIZ = Column(Float)
        CHZ = Column(Float)
        SLZ = Column(Float)
        CUZ = Column(Float)
        CSZ = Column(Float)
        KNZ = Column(Float)
        SBZ = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Pitch Info  VMovement: Table Created>"


    class HitterPitchInfoPitchTypeValue(db.Base):
        __tablename__ = "hitter_pitchinfo_typevalue"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        PA = Column(Integer)
        wFA = Column(Float)
        wFC = Column(Float)
        wFS = Column(Float)
        wSI = Column(Float)
        wCH = Column(Float)
        wSL = Column(Float)
        wCU = Column(Float)
        wCS = Column(Float)
        wKN = Column(Float)
        wSB = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Pitch Info  Pitch Value: Table Created>"


    class HitterPitchInfoPitchValuePer100(db.Base):
        __tablename__ = "hitter_pitchinfo_value100"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        PA = Column(Integer)
        wFAperC = Column(Float)
        wFCperC = Column(Float)
        wFSperC = Column(Float)
        wSIperC = Column(Float)
        wCHperC = Column(Float)
        wSLperC = Column(Float)
        wCUperC = Column(Float)
        wCSperC = Column(Float)
        wKNperC = Column(Float)
        wSBperC = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Pitch Info  Pitch Value/100: Table Created>"


    class HitterPitchInfoPlateDiscipline(db.Base):
        __tablename__ = "hitter_pitchinfo_discipline"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        PA = Column(Integer)
        OSwingpercent = Column(Float)
        ZSwingpercent = Column(Float)
        Swingpercent = Column(Float)
        OContactpercent = Column(Float)
        ZContactpercent = Column(Float)
        Contactpercent = Column(Float)
        Zonepercent = Column(Float)
        Pace = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Pitch Info  Plate Discipline: Table Created>"


    class HitterPlusStats(db.Base):
        __tablename__ = "hitter_plusstats"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        PA = Column(Integer)
        BBpercentplus = Column(Float)
        Kpercentplus = Column(Float)
        AVGplus = Column(Float)
        OBPplus = Column(Float)
        SLGplus = Column(Float)
        wRCplus = Column(Float)
        ISOplus = Column(Float)
        BABIPplus = Column(Float)
        LDpercentplus = Column(Float)
        GBpercentplus = Column(Float)
        FBpercentplus = Column(Float)
        Pullpercentplus = Column(Float)
        Centpercentplus = Column(Float)
        Oppopercentplus = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter plusStats: Table Created>"


    class HitterStatcast(db.Base):
        __tablename__ = "hitter_statcast"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['hitter_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        PA = Column(Integer)
        Events = Column(Float)
        EV = Column(Float)
        maxEV = Column(Float)
        LA = Column(Float)
        Barrels = Column(Float)
        Barrelpercent = Column(Float)
        HardHit = Column(Float)
        HardHitpercent = Column(Float)
        AVG = Column(Float)
        xBA = Column(Float)
        SLG = Column(Float)
        xSLG = Column(Float)
        wOBA = Column(Float)
        xwOBA = Column(Float)

        def __repr__(self):
            return "<FanGraphs Hitter Statcast: Table Created>"


    # FANGRAPH PITCHER TABLES

    # class to instantiate a table for hitting stats from MLBStats API for first date range
    class PitcherStandard(db.Base):
        __tablename__ = "pitcher_standard"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        W = Column(Integer)
        L = Column(Integer)
        ERA = Column(Float)
        G = Column(Integer)
        GS = Column(Integer)
        CG = Column(Integer)
        ShO = Column(Integer)
        SV = Column(Integer)
        HLD = Column(Integer)
        BS = Column(Integer)
        IP = Column(Float)
        TBF = Column(Float)
        H = Column(Integer)
        R = Column(Integer)
        ER = Column(Integer)
        HR = Column(Integer)
        BB = Column(Integer)
        IBB = Column(Integer)
        HBP = Column(Integer)
        WP = Column(Integer)
        BK = Column(Integer)
        SO = Column(Integer)

        def __repr__(self):
            return "<FanGraphs Pitcher Standard: Table Created>"


    class PitcherAdvanced(db.Base):
        __tablename__ = "pitcher_advanced"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        Kper9 = Column(Float)
        BBper9 = Column(Float)
        KperBB = Column(Float)
        HRper9 = Column(Float)
        Kpercent = Column(Float)
        BBpercent = Column(Float)
        KBBpercent = Column(Float)
        AVG = Column(Float)
        WHIP = Column(Float)
        BABIP = Column(Float)
        LOBpercent = Column(Float)
        ERAminus = Column(Float)
        FIPminus = Column(Float)
        xFIPminus = Column(Float)
        ERA = Column(Float)
        FIP = Column(Float)
        EminusF = Column(Float)
        xFIP = Column(Float)
        SIERA = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Advanced: Table Created>"


    class PitcherBattedBalls(db.Base):
        __tablename__ = "pitcher_batted_balls"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        BABIP = Column(Float)
        GBperFB = Column(Float)
        LDpercent = Column(Float)
        GBpercent = Column(Float)
        FBpercent = Column(Float)
        IFFBpercent = Column(Float)
        HRperFB = Column(Float)
        RS = Column(Float)
        RSper9 = Column(Float)
        Balls = Column(Float)
        Strikes = Column(Float)
        Pitches = Column(Float)
        Pullpercent = Column(Float)
        Centpercent = Column(Float)
        Oppopercent = Column(Float)
        Softpercent = Column(Float)
        Medpercent = Column(Float)
        Hardpercent = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Batted Balls: Table Created>"


    class PitcherWinProbability(db.Base):
        __tablename__ = "pitcher_win_probability"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        WPA = Column(Float)
        minusWPA = Column(Float)
        plusWPA = Column(Float)
        RE24 = Column(Float)
        REW = Column(Float)
        pLI = Column(Float)
        inLI = Column(Float)
        gmLI = Column(Float)
        exLI = Column(Float)
        Pulls = Column(Float)
        WPAperLI = Column(Float)
        Clutch = Column(Float)
        SD = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Win Probability: Table Created>"


    class PitcherPitchType(db.Base):
        __tablename__ = "pitcher_pitch_type"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        FBpercent = Column(Float)
        FBv = Column(Float)
        SLpercent = Column(Float)
        SLv = Column(Float)
        CTpercent = Column(Float)
        CTv = Column(Float)
        CBpercent = Column(Float)
        CBv = Column(Float)
        CHpercent = Column(Float)
        CHv = Column(Float)
        SFpercent = Column(Float)
        SFv = Column(Float)
        KNpercent = Column(Float)
        KNv = Column(Float)
        XXpercent = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Pitch Type: Table Created>"


    class PitcherPitchValue(db.Base):
        __tablename__ = "pitcher_pitch_value"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        wFB = Column(Float)
        wSL = Column(Float)
        wCT = Column(Float)
        wCB = Column(Float)
        wCH = Column(Float)
        wSF = Column(Float)
        wKN = Column(Float)
        wFBperC = Column(Float)
        wSLperC = Column(Float)
        wCTperC = Column(Float)
        wCBperC = Column(Float)
        wCHperC = Column(Float)
        wSFperC = Column(Float)
        wKNperC = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Pitch Value: Table Created>"


    class PitcherPlateDiscipline(db.Base):
        __tablename__ = "pitcher_plate_discipline"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        OSwingpercent = Column(Float)
        ZSwingpercent = Column(Float)
        Swingpercent = Column(Float)
        OContactpercent = Column(Float)
        ZContactpercent = Column(Float)
        Contactpercent = Column(Float)
        Zonepercent = Column(Float)
        FStrikepercent = Column(Float)
        SwStrpercent = Column(Float)
        CStrpercent = Column(Float)
        CSWpercent = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Plate Discipline: Table Created>"


    class PitcherValue(db.Base):
        __tablename__ = "pitcher_value"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        RA9minusWAR = Column(Float)
        BIPminusWins = Column(Float)
        LOBminusWins = Column(Float)
        FDPminusWins = Column(Float)
        RAR = Column(Float)
        WAR = Column(Float)
        Dollars = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Value: Table Created>"


    class PitcherPitchInfoPitchType(db.Base):
        __tablename__ = "pitcher_pitchinfo_pitchtype"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        IP = Column(Float)
        FApercent = Column(Float)
        FCpercent = Column(Float)
        FSpercent = Column(Float)
        SIpercent = Column(Float)
        CHpercent = Column(Float)
        SLpercent = Column(Float)
        CUpercent = Column(Float)
        CSpercent = Column(Float)
        KNpercent = Column(Float)
        SBpercent = Column(Float)
        XXpercent = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Pitch InfoPitch Type: Table Created>"


    class PitcherPitchInfoVelocity(db.Base):
        __tablename__ = "pitcher_pitchinfo_velocity"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        IP = Column(Float)
        vFA = Column(Float)
        vFC = Column(Float)
        vFS = Column(Float)
        vSI = Column(Float)
        vCH = Column(Float)
        vSL = Column(Float)
        vCU = Column(Float)
        vCS = Column(Float)
        vKN = Column(Float)
        vSB = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Pitch InfoVelocity: Table Created>"


    class PitcherPitchInfoHMovement(db.Base):
        __tablename__ = "pitcher_pitchinfo_hmovement"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        IP = Column(Float)
        FAX = Column(Float)
        FCX = Column(Float)
        FSX = Column(Float)
        SIX = Column(Float)
        CHX = Column(Float)
        SLX = Column(Float)
        CUX = Column(Float)
        CSX = Column(Float)
        KNX = Column(Float)
        SBX = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Pitch Info  HMovement: Table Created>"


    class PitcherPitchInfoVMovement(db.Base):
        __tablename__ = "pitcher_pitchinfo_vmovement"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        IP = Column(Float)
        FAZ = Column(Float)
        FCZ = Column(Float)
        FSZ = Column(Float)
        SIZ = Column(Float)
        CHZ = Column(Float)
        SLZ = Column(Float)
        CUZ = Column(Float)
        CSZ = Column(Float)
        KNZ = Column(Float)
        SBZ = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Pitch Info  VMovement: Table Created>"


    class PitcherPitchInfoPitchTypeValue(db.Base):
        __tablename__ = "pitcher_pitchinfo_typevalue"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        IP = Column(Float)
        wFA = Column(Float)
        wFC = Column(Float)
        wFS = Column(Float)
        wSI = Column(Float)
        wCH = Column(Float)
        wSL = Column(Float)
        wCU = Column(Float)
        wCS = Column(Float)
        wKN = Column(Float)
        wSB = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Pitch Info - Pitch Type Value: Table Created>"


    class PitcherPitchInfoPitchValuePer100(db.Base):
        __tablename__ = "pitcher_pitchinfo_value100"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        IP = Column(Float)
        wFAperC = Column(Float)
        wFCperC = Column(Float)
        wFSperC = Column(Float)
        wSIperC = Column(Float)
        wCHperC = Column(Float)
        wSLperC = Column(Float)
        wCUperC = Column(Float)
        wCSperC = Column(Float)
        wKNperC = Column(Float)
        wSBperC = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Pitch Info  Pitch Value/100: Table Created>"


    class PitcherPitchInfoPlateDiscipline(db.Base):
        __tablename__ = "pitcher_pitchinfo_discipline"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        IP = Column(Float)
        OSwingpercent = Column(Float)
        ZSwingpercent = Column(Float)
        Swingpercent = Column(Float)
        OContactpercent = Column(Float)
        ZContactpercent = Column(Float)
        Contactpercent = Column(Float)
        Zonepercent = Column(Float)
        Pace = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Pitch Info  Plate Discipline: Table Created>"


    class PitcherPlusStats(db.Base):
        __tablename__ = "pitcher_plusstats"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        IP = Column(Float)
        Kper9plus = Column(Float)
        BBper9plus = Column(Float)
        KperBBplus = Column(Float)
        HRper9plus = Column(Float)
        Kpercentplus = Column(Float)
        BBpercentplus = Column(Float)
        AVGplus = Column(Float)
        WHIPplus = Column(Float)
        BABIPplus = Column(Float)
        LOBpercentplus = Column(Float)
        ERAminus = Column(Float)
        FIPminus = Column(Float)
        xFIPminus = Column(Float)
        LDpercentplus = Column(Float)
        GBpercentplus = Column(Float)
        FBpercentplus = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher plusStats: Table Created>"


    class PitcherStatcast(db.Base):
        __tablename__ = "pitcher_statcast"
        __table_args__ = (
            PrimaryKeyConstraint('lastName'),
            ForeignKeyConstraint(
                columns=['lastName'],
                refcolumns=['pitcher_fangraph.lastName']
            ),
            {'extend_existing': True}
        )

        lastName = Column(String(20))
        firstName = Column(String(20))
        Team = Column(String(3))
        Age = Column(Integer)
        IP = Column(Float)
        Events = Column(Float)
        EV = Column(Float)
        maxEV = Column(Float)
        LA = Column(Float)
        Barrels = Column(Float)
        Barrelpercent = Column(Float)
        HardHit = Column(Float)
        HardHitpercent = Column(Float)
        ERA = Column(Float)
        xERA = Column(Float)

        def __repr__(self):
            return "<FanGraphs Pitcher Statcast: Table Created>"


    if __name__ != '__main__':
        db.Base.metadata.create_all()

