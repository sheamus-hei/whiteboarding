# The company Goferbroke is deciding whether or not to drill for oil or sell the land
# part 2: they also have the option of doing a seismic survey

#                           State
# Decisions     oil(p = 25%)    dry (p = 75%)      EP
#     drill       700               -100          700(.25) - 100(.75) =  100
#     sell        90                90            90

# ep is higher for drill so we drill. 

# part 2. We have the option of conducting a seismic survey.
# it costs 30 to do a seismic survey
# the survey will come back unfavorable or favorable
# given the state = dry, probablity of unfavorable = 0.8 and favorable 0.2
# given state = oil, P for unfavorable = 0.4 and faviable 0.6

# 1. get all states and probabilities
# 2. weigh decision alternatives and return best decision (or series of decisions)

# given: decisions, PP of outcomes
# return: best alternative

def bayes_decision(decs, outs, probs):
  alts = []

  return 

decisions = [
  {
    "survey": -30,
    "no_survey": 0
  },
  {
    "drill": -100
    "sell": 90
  }
]

outcomes = {
  "drill": {
    "oil": 800,
    "dry": 0
  }
}


probabilities = [{
  "oil": 0.75,
  "dry": 0.25
}]

