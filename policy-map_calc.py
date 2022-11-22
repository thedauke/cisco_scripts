ch_speed=int(input ("enter megabytes to get policy map - "))
speed_cir = int(ch_speed*1024*1024)
normal_burst= int(speed_cir/8*1.5)
extended_burst =int(2*normal_burst)

polistr="""
    policy-map """+ str(ch_speed) +'m' + """
    Class class-default
    police cir """ + str(speed_cir) + " bc " + str(normal_burst) + " be " + str(extended_burst) +"""
    conform-action transmit
    exceed-action drop
    violate-action drop"""
print (polistr)
input("Press enter to exit ; ")
