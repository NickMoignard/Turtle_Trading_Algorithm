
# coding: utf-8

# # Markets
# Observe as many markets as possible.
# Markets are removed from trading if Trading Volume is too low or market does not trend well
# 

# In[ ]:


from statistics import mean


# In[4]:


# Position Sizing
account = float() # Amount of money to be traded with

# From Dataset
current_high = float()
current_low = float()
previous_day_close = float()
previous_atr = float()
dollares_per_point = float()

previous_mean_true_ranges = []

# When first performing ATR calculations the simple moving avg true range is used.
init_true_range = mean(previous_mean_true_ranges[-time_length:])

def getATR(high, low, prev_close, prev_atr=init_true_range, time_length=20):
    r = max(high - low, abs(high - prev_close), abs(prev_close - low))
    atr = ((time_length - 1) * prev_atr * r) / time_length
    return atr                                                                                    

# Turtle Units (t_unit) 1% of account over market volatility
# Positions are made in increments of these units in order to maintain diversification across portfolio
def getTurleUnit(market, account):
    atr = getATR(current_high, current_low, previous_day_close, previous_atr)
    dollar_volatility = market.dollars_per_point * atr
    return (account * 0.01) / dollar_volatility 


# In[ ]:


# Risk Management
MAX_T_UNITS_SINGLE_MARKET = 4  # e.g. Gold
MAX_T_UNITS_CLOSELY_CORRELATED_MARKETS = 6  # e.g. Gold & Silver
MAX_T_UNITS_LOOSELY_CORRELATED_MARKETS = 10  # e.g. Gold & Copper
MAX_T_UNITS_SINGLE_DIRECTION = 12  # Long or Short

def canMakeTradeInMarket(market, direction):
    pos = market.cur_position
    long, short = getCurPositions()
    
    close, loose = 0, 0
    for market in market.closely_related:
        close += market.position
    for market in market.loosely_related:
        loose += market.position
    
    if pos >= MAX_T_UNITS_SINGLE_MARKET:
        return False
    elif pos + close >= MAX_T_UNITS_CLOSELY_CORRELATED_MARKETS:
        return False
    elif pos + loose >= MAX_T_UNITS_LOOSELY_CORRELATED_MARKETS:
        return False
    elif direction == 'Long' and long >= MAX_T_UNITS_LOOSELY_CORRELATED_MARKETS:
        return False
    elif direction == 'Short' and short >= MAX_T_UNITS_SINGLE_DIRECTION:
        return False
    
    return True


# In[ ]:


# Entries

# From Data Set
cur_price = float()
twenty_day_low, fifty_five_day_low = float(), float()
twenty_day_high, fifty_five_day_high = float(), float()
prev_signal_result = []  # True if winning, False if losing

long_signal = ( cur_price > twenty_day_high )
short_signal = ( cur_price < twenty_day_low )
fall_back_long = ( cur_price > fifty_five_day_high )
fall_back_short = ( cur_price < fifty_five_day_low )

def takePosition(direction, market):
    units_to_order = int(getTurtleUnit(market, account))
    if canMakeTradeInMarket(market, direction):
        print("ring ur broker. "+ direction +" "+ str(units_to_order) +" of "+ market.title)
    else:
        print('You are already fully loaded')
    
if (short_signal and !prev_signal_result[-1]):
    takePosition('Short', market)
elif (long_signal and !prev_signal_result[-1]):
    takePosition('Long', market)
elif fall_back_long:
    takePosition('Long', market)
elif fall_back_short:
    takePosition('Short', market)
else:
    print('Wait for a signal')
    


# In[ ]:


# Adding to a Position
add_signal = market.cur_price > position.first_unit_price + 0.5*market.atr
if add_signal:
    position.addTUnit()
    


# In[2]:


# Stops
def executeStop():
    print('Pull out now!')

breakout_price = float()
breakout_atr = float()

if current_price < breakout_price - 2*breakout_atr:
    executeStop()


# In[3]:


# Exits
ten_day_high, ten_day_low = float(), float()

if ((current_price < ten_day_low) and (direction == "Long")):
    exitPosition()
elif ((current_price > ten_day_high) and (direction == "Short")):
    exitPosition()
else:
    print("Hold on tight and pray")
    
    
def exitPosition():
    print('run with the money!')



# In[ ]:


# Tactics
# 1. Don't panic and use market orders in a rising market, wait for a small reversal then limit order
# 2. If multiple signals trigger & will break the rules if all are filled choose strongest swing

def whichMarket(markets): # input list of markets with signals
    strengths = []
    for market in markets_with_signals:
        delta = abs(market.cur_price - market.prev_prices[-90]) # 3 months ago
        strengths.append(delta / market.atr)
    return markets[strengths.index(max(strengths))]
        
    

