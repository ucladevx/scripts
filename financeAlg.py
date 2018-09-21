 # Determine whether a reimbursement request should be granted

  # parameters:
  # int curDevXTotal: current balance in DevX bank account
  # string teamName: team name with NO SPACES
  # int amtRequested: amount requested
  # int priorityLevel: refer to instructions for priority level

#!/usr/bin/python

import sys
from types import *

assert len(sys.argv) == 4
teamName = sys.argv[1]
amtRequested = int(sys.argv[2])
priorityLevel = int(sys.argv[3])

#assert type(teamName) is StringType, "teamName is not an String: %r" % teamName
assert type(amtRequested) is IntType, "amtRequested is not an Int: %r" % amtRequested
assert type(priorityLevel) is IntType, "priorityLevel is not an Int: %r" % priorityLevel

#replace value later:
curDevXTotal = 300.00

# replace later:
#  how much each team has received over the past year
teams = {10: "bruinmeet", 5: "studysmart", 20: "bruinbite", 15: "internaldev" }

teams = sorted(teams)
#internal dev has key 15
keyOfInternalDev = teams.index(15)
def switch(priorityLevel):
	return {
		1: 1.0,
		2: 2.0,
		3: 3.0,
		4: 4.0
	}.get(priorityLevel, 0.0)

# multiply curDevXTotal by the priority level
curDevXTotal = curDevXTotal * switch(priorityLevel)

# lets say amtRequested is 20:
if curDevXTotal > 20:
	print("You will likely be granted the request")
else:
	print("At this time, we do not have enough funds. You will likely NOT be granted the request")
