import math
print("===================================================================")
print("||                                                               ||")
print("||                  Hot Air Baloon Simulation                    ||")
print("||                    Coded by : Eray Akan                       ||")
print("||                                                               ||")
print("===================================================================")

time = 0
n = 0
x = 0
radius = float(input("Enter the radius of the baloon in meters: "))
weight = float(input("Enter the weight of the baloon in kilograms: "))
density = float(input("Enter the air density of baloon's current altitude in kg/m³: "))
airdegree = float(input("Enter the density of hot air inside the baloon in kg/m³: "))
altitude = 0
speed = 0
speed2 = 0
volume = (4/3)*3.14*(radius*radius*radius)

forceup = ((volume*density)*9.81)/1000
forcedown = (((volume * airdegree) * 9.81) + (weight*9.81)) / 1000
print("")
print("================================================================================")
print("Volume of the baloon = " + str(volume) + "m³")
print("Lifting Force [f(b)] = " + str(forceup) + " kN")
print("Gravitional Force [f(g)] = " + str(forcedown) + " kN")
if forceup > forcedown:
    force = (forceup - forcedown)*1000
    acceleration = force/weight
    print("Acceleration = " + str(acceleration) + " m/s²")
    carry = force/10
    print("Extra weight the baloon can carry < " + str(carry) + " kg")
    while forceup > forcedown:
        altitude += 0.1
        density = density - 0.00001
        speed = (math.sqrt(2 * (acceleration * altitude))/2)
        forceup = ((volume * density) * 9.81) / 1000
        forcedown = (((volume * airdegree) * 9.81) + (weight*9.81)) / 1000
        force = (forceup - forcedown) * 1000
        n = altitude // 0.1
        x = n * 0.1
        time = altitude / speed
        speed = math.sqrt(2 * (acceleration * altitude))
    print("Maximum altitude it can reach = " + str(altitude) + " m")
    print("Final speed of the baloon = " + str(speed) + " m/s")
    print("Time until baloon reach maximum altitude = " + str(time) + " s")
    print("================================================================================")
else:
    force = (forcedown - forceup)*1000
    acceleration = force/weight
    print("Acceleration = " + str(acceleration) + " m/s²")
    carry = force/10
    print("Weight need to be thrown in order to lift > " + str(carry) + " kg")
    print("================================================================================")