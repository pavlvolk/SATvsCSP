import CSP_Solver as CS

task = CS.CSP(variables=4)
task.commonDomain(domain=[1, 2])
task.addConstraint("value[1] != value[2]")
task.addConstraint("value[1] != value[3]")
task.addConstraint("value[2] != value[4]")
task.addConstraint("value[3] != value[4]")
task.solve_BackTrack(timeout=10)

for i in range(1, 5):
        print(f"Cell {i}: {task.value[i]}")