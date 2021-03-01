# Given a list of boarding passes and a source and a destination,
#  tell me if you can travel from source to destination.

# def travel_helper(passes, source, dest, prev_passes)

def can_travel(passes, source, dest):
  s = set()
  final_result = False
  for b_pass in passes:
    pass_keys = list(b_pass.keys())
    code = pass_keys[0] + "-" + pass_keys[1]
    if pass_keys[0] == source and code not in s:
      s.add(code)
      # print(pass_keys[1], source, dest)
      if pass_keys[1] == dest:
        return True
      else: 
        # remove that boarding b_pass from list
        new_passes = passes.copy()
        new_passes.remove(b_pass)
        final_result = can_travel(new_passes, pass_keys[1], dest)
  return final_result or False

passes = [{
  "DEN": 0,
  "TUS": 0
},{
	"TUS": 0,
	"DEN": 0
},
{
	"LAX": 0,
	"DEN": 0
},
{
	"DEN": 0,
	"CHI": 0
},
{
	"DEN": 0,
	"NYC": 0
},{
	"NYC": 0,
	"DEN": 0
}, {
  "TUS": 0,
  "DEN": 0
}]

source = "DEN"
destination = "NYC"
print(can_travel(passes, source, destination))