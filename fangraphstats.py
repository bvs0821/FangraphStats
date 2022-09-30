import pandas as pd
import requests
from datetime import datetime as dt
import datetime as date
from bs4 import BeautifulSoup
import lxml


# user input for date ranges
def date_ranges():
    num_days = list(map(int, input("Enter the amount(s) of days you are analyzing: ").split()))
    return num_days

# user input for minimum at bat for a hitter to be considered
def min_qual_hitter():
    qual_hitter = input("Enter minimum number of at bats for hitter: ")
    return qual_hitter

# user input for minimum innings pitched for a pitcher to be considered
def min_qual_pitcher():
    qual_pitcher = input("Enter minimum number of innings pitched for pitcher: ")
    return qual_pitcher

# user input for number of hitters considered (rows of hitter stats will be less than num_hitter as hitters will be
# limited by the amount of at bats to qualify in the results
def number_of_hitters():
    num_hitter = input("Enter number of hitters displayed: ")
    return num_hitter

# user input for number of pitchers considered (rows of pitcher stats will be less than num_pitcher as pitchers will be
# limited by the amount of innings pitched to qualify in the results
def number_of_pitchers():
    num_hitter = input("Enter number of pitchers displayed: ")
    return num_hitter

# function to parse Fangraph hitter stats and extract Pandas Dataframes with BeautifulSoup
def fangraphs_hitters_parse(url):
    # parse input
    hitter_url = url
    # request the data
    hitters_html = requests.get(hitter_url).text

    soup = BeautifulSoup(hitters_html, "lxml")
    table = soup.find("table", {"class": "rgMasterTable"})

    # get headers
    headers_html = table.find("thead").find_all("th")
    headers = []
    for header in headers_html:
        headers.append(header.text)

    # get rows
    rows = []
    rows_html = table.find("tbody").find_all("tr")
    # populate rows
    for row in rows_html:
        row_data = []
        for cell in row.find_all("td"):
            row_data.append(cell.text)
        rows.append(row_data)

    # return DataFrame
    print(pd.DataFrame(rows, columns=headers))
    return pd.DataFrame(rows, columns=headers)

# function to parse Fangraph pitcher stats and extract Pandas Dataframes with BeautifulSoup
def fangraphs_pitchers_parse(url):
    # parse input
    pitcher_url = url
    # request the data
    pitchers_html = requests.get(pitcher_url).text

    soup = BeautifulSoup(pitchers_html, "lxml")
    table = soup.find("table", {"class": "rgMasterTable"})

    # get headers
    headers_html = table.find("thead").find_all("th")
    headers = []
    for header in headers_html:
        headers.append(header.text)

    # get rows
    rows = []
    rows_html = table.find("tbody").find_all("tr")

    # populate rows
    for row in rows_html:
        row_data = []
        for cell in row.find_all("td"):
            row_data.append(cell.text)
        rows.append(row_data)

    # return DataFrame
    return pd.DataFrame(rows, columns=headers)

# function to combine all hitter stat categories in a DataFrame for each date range analyzed
def get_hitter_stats(num_days, qual_hitter, num_players):
    global df_hitter_total

    end_date = date.date.today()
    start_date = end_date - date.timedelta(days=num_days - 1)
    end_date = dt.strftime(end_date, "%Y-%m-%d")
    start_date = dt.strftime(start_date, "%Y-%m-%d")
    print(f"Starting date is: {start_date}")
    print(f"Ending date is: {end_date}")

    df_hitter_total = {}
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual={}&type=c,-1,3,4,5,6,7,8,9,10,11,' \
          '12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,' \
          '46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,' \
          '80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,' \
          '110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,' \
          '135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,' \
          '160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,' \
          '185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,' \
          '210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,' \
          '235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,' \
          '260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,' \
          '285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,' \
          '310,311,312,313,314,315,316,317,' \
          '318&season=2022&month=1000&season1=2022&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate={' \
          '}&enddate={}&page=1_{}'.format(qual_hitter, start_date, end_date, num_players)
    try:
        df_hitter_total = fangraphs_hitters_parse(url)
    except ConnectionError:
        df_hitter_total = fangraphs_hitters_parse(url)
    except:
        pass

    names = df_hitter_total['Name'].tolist()
    last_names = []
    first_names = []
    for i in range(0, len(names)):
        first_names.append(' '.join(names[i].split(' ')[:1]))
        last_names.append(' '.join(names[i].split(' ')[1:]))

    ln_search = []
    for i in range(0, len(last_names)):
        ln_search.append(' '.join(last_names[i].split(' ')[:1]))

    df_hitter_total.drop(['Name', '#'], axis=1, inplace=True)
    df_hitter_total.insert(loc=0, column='lastName', value=last_names)
    df_hitter_total.insert(loc=1, column='firstName', value=first_names)

    hd = df_hitter_total.to_dict()

    hitterkeys = list(hd.keys())

    for i in range(len(hitterkeys)):
        c1 = hitterkeys[i][-1:]
        if c1 == ')':
            hitterkeys[i] = hitterkeys[i][:-5]
        try:
            c2 = hitterkeys[i][1]
            if c2 == '-':
                hitterkeys[i] = hitterkeys[i].replace("-", "")
        except IndexError:
            pass
        try:
            c3 = hitterkeys[i][2]
            if c3 == '-':
                hitterkeys[i] = hitterkeys[i].replace("-", "")
        except IndexError:
            pass
        hitterkeys[i] = hitterkeys[i].replace("-", "minus")
        hitterkeys[i] = hitterkeys[i].replace("+", "plus")
        hitterkeys[i] = hitterkeys[i].replace("%", "percent")
        hitterkeys[i] = hitterkeys[i].replace("/", "per")
        hitterkeys[i] = hitterkeys[i].replace(" ", "")
        hitterkeys[i] = hitterkeys[i].replace("1B", "single")
        hitterkeys[i] = hitterkeys[i].replace("2B", "double")
        hitterkeys[i] = hitterkeys[i].replace("3B", "triple")

    hitterdict = dict(zip(hitterkeys, list(hd.values())))
    hitterdict['LDpercentplus'] = hitterdict.pop('LDpluspercent')

    df_hitter_total = pd.DataFrame.from_dict(hitterdict)

    return df_hitter_total

# function to combine all pitcher stat categories in a DataFrame for each date range analyzed
def get_pitcher_stats(num_days, qual_hitter, num_players):
    global df_pitcher_total

    end_date = date.date.today()
    start_date = end_date - date.timedelta(days=num_days - 1)
    end_date = dt.strftime(end_date, "%Y-%m-%d")
    start_date = dt.strftime(start_date, "%Y-%m-%d")
    print(f"Starting date is: {start_date}")
    print(f"Ending date is: {end_date}")

    #df_pitcher_total = {}
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual={}&type=c%2C-1%2C3%2C4%2C5%2C6' \
          '%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27' \
          '%2C28%2C29%2C30%2C31%2C32%2C33%2C34%2C35%2C36%2C37%2C38%2C39%2C40%2C41%2C42%2C43%2C44%2C45%2C46%2C47' \
          '%2C48%2C49%2C50%2C51%2C52%2C53%2C54%2C55%2C56%2C57%2C58%2C59%2C60%2C61%2C62%2C63%2C64%2C65%2C66%2C67' \
          '%2C68%2C69%2C70%2C71%2C72%2C73%2C74%2C75%2C76%2C77%2C78%2C79%2C80%2C81%2C82%2C83%2C84%2C85%2C86%2C87' \
          '%2C88%2C89%2C90%2C91%2C92%2C93%2C94%2C95%2C96%2C97%2C98%2C99%2C100%2C101%2C102%2C103%2C104%2C105%2C106' \
          '%2C107%2C108%2C109%2C110%2C111%2C112%2C113%2C114%2C115%2C116%2C117%2C118%2C119%2C120%2C121%2C122%2C123' \
          '%2C124%2C125%2C126%2C127%2C128%2C129%2C130%2C131%2C132%2C133%2C134%2C135%2C136%2C137%2C138%2C139%2C140' \
          '%2C141%2C142%2C143%2C144%2C145%2C146%2C147%2C148%2C149%2C150%2C151%2C152%2C153%2C154%2C155%2C156%2C157' \
          '%2C158%2C159%2C160%2C161%2C162%2C163%2C164%2C165%2C166%2C167%2C168%2C169%2C170%2C171%2C172%2C173%2C174' \
          '%2C175%2C176%2C177%2C178%2C179%2C180%2C181%2C182%2C183%2C184%2C185%2C186%2C187%2C188%2C189%2C190%2C191' \
          '%2C192%2C193%2C194%2C195%2C196%2C197%2C198%2C199%2C200%2C201%2C202%2C203%2C204%2C205%2C206%2C207%2C208' \
          '%2C209%2C210%2C211%2C212%2C213%2C214%2C215%2C216%2C217%2C218%2C219%2C220%2C221%2C222%2C223%2C224%2C225' \
          '%2C226%2C227%2C228%2C229%2C230%2C231%2C232%2C233%2C234%2C235%2C236%2C237%2C238%2C239%2C240%2C241%2C242' \
          '%2C243%2C244%2C245%2C246%2C247%2C248%2C249%2C250%2C251%2C252%2C253%2C254%2C255%2C256%2C257%2C258%2C259' \
          '%2C260%2C261%2C262%2C263%2C264%2C265%2C266%2C267%2C268%2C269%2C270%2C271%2C272%2C273%2C274%2C275%2C276' \
          '%2C277%2C278%2C279%2C280%2C281%2C282%2C283%2C284%2C285%2C286%2C287%2C288%2C289%2C290%2C291%2C292%2C293' \
          '%2C294%2C295%2C296%2C297%2C298%2C299%2C300%2C301%2C302%2C303%2C304%2C305%2C306%2C307%2C308%2C309%2C310' \
          '%2C311%2C312%2C313%2C314%2C315%2C316%2C317%2C318%2C319%2C320%2C321%2C322%2C323%2C324%2C325%2C326%2C327' \
          '%2C328%2C329%2C330%2C331%2C332&season=2022&month=1000&season1=2022&ind=0&team=0&rost=0&age=0&filter' \
          '=&players=0&startdate={}&enddate={}&page=1_{}'.format(qual_hitter, start_date, end_date, num_players)
    try:
        df_pitcher_total = fangraphs_pitchers_parse(url)
    except ConnectionError:
        df_pitcher_total = fangraphs_pitchers_parse(url)
    except:
        pass

    names = df_pitcher_total['Name'].tolist()
    last_names = []
    first_names = []
    for i in range(0, len(names)):
        first_names.append(' '.join(names[i].split(' ')[:1]))
        last_names.append(' '.join(names[i].split(' ')[1:]))

    ln_search = []
    for i in range(0, len(last_names)):
        ln_search.append(' '.join(last_names[i].split(' ')[:1]))

    df_pitcher_total.drop(['Name', '#'], axis=1, inplace=True)
    df_pitcher_total.insert(loc=0, column='lastName', value=last_names)
    df_pitcher_total.insert(loc=1, column='firstName', value=first_names)

    pitd = df_pitcher_total.to_dict()

    pitcherkeys = list(pitd.keys())

    for i in range(len(pitcherkeys)):
        print(pitcherkeys[i])
        c1 = pitcherkeys[i][-1:]
        if c1 == ')':
            pitcherkeys[i] = pitcherkeys[i][:-5]
        try:
            c2 = pitcherkeys[i][1]
            if c2 == '-':
                pitcherkeys[i] = pitcherkeys[i].replace("-", "")
        except IndexError:
            pass
        try:
            c3 = pitcherkeys[i][2]
            if c3 == '-':
                pitcherkeys[i] = pitcherkeys[i].replace("-", "")
        except IndexError:
            pass
        pitcherkeys[i] = pitcherkeys[i].replace("-", "minus")
        pitcherkeys[i] = pitcherkeys[i].replace("+", "plus")
        pitcherkeys[i] = pitcherkeys[i].replace("%", "percent")
        pitcherkeys[i] = pitcherkeys[i].replace("/", "per")
        pitcherkeys[i] = pitcherkeys[i].replace(" ", "")
        pitcherkeys[i] = pitcherkeys[i].replace("1B", "single")
        pitcherkeys[i] = pitcherkeys[i].replace("2B", "double")
        pitcherkeys[i] = pitcherkeys[i].replace("3B", "triple")

    pitcherdict = dict(zip(pitcherkeys, list(pitd.values())))

    pitcherdict['StartIP'] = pitcherdict.pop('StartminusIP')
    pitcherdict['ReliefIP'] = pitcherdict.pop('ReliefminusIP')

    df_pitcher_total = pd.DataFrame.from_dict(pitcherdict)

    return df_pitcher_total

class FanGraphHitterCall:

    def __init__(self, day):
        num_days = day
        qual_hitter = min_qual_hitter()
        num_hitters = number_of_hitters()
        self.hitters = get_hitter_stats(num_days, qual_hitter, num_hitters)
        self.number_of_days = num_days

    def __repr__(self):
        return f"<FanGraph Hitting Stats: Complete>"

class FanGraphPitcherCall:

    def __init__(self, day):
        num_days = day
        qual_pitcher = min_qual_pitcher()
        num_pitchers = number_of_pitchers()
        self.pitchers = get_pitcher_stats(num_days, qual_pitcher, num_pitchers)
        self.number_of_days = num_days

    def __repr__(self):
        return f"<FanGraph Pitching Stats: Complete>"


#hitterapicall = FanGraphHitterCall(5)
#hitterstats = hitterapicall.hitters

#hitterurlstats = fangraphs_pitchers_parse('https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=y&type=1&season=2022&month=0&season1=2022&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31')
#pitcherapicall = FanGraphPitcherCall()
#pitcherstats = pitcherapicall.pitchers
