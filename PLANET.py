# Declare named constants

MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91
MOON_GRAVITY = 0.165
MARS_GRAVITY = 0.38
JUPITER_GRAVITY = 2.34
SATURN_GRAVITY = 0.93
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY= 1.12
PLUTO_GRAVITY = 0.066

# User information

S_name_ = input("what is your name : ")
earth_weight = float(input( "what is your weight :" ))

# calculate weight on planet
n_mercury_weight = earth_weight *MERCURY_GRAVITY
n_venus_weight = earth_weight *VENUS_GRAVITY
n_moon_weight = earth_weight *MOON_GRAVITY
n_mars_weight = earth_weight *MARS_GRAVITY
n_jupiter_weight = earth_weight *JUPITER_GRAVITY
n_saturn_weight = earth_weight *SATURN_GRAVITY
n_uranus_weight = earth_weight *URANUS_GRAVITY
n_neptune_weight = earth_weight *NEPTUNE_GRAVITY
n_Pluto_weight = earth_weight * PLUTO_GRAVITY




# output information
print( "Tatianna,here are your weights on our solar system's planets :" )
print("weight on mercury :       "  , n_mercury_weight  )
print("weight on venus :    "   ,n_venus_weight )
print("weight on moon :     "       ,n_moon_weight )
print("weight on mars :  "      ,n_mars_weight  )
print("weight on jupiter :    "   , n_jupiter_weight  )
print("weight on uranusis :      "     ,n_uranus_weight  )
print("weight on neptune :          "    ,n_neptune_weight  )
print("weight on Pluto :            "      ,n_Pluto_weight  )



