for i in range (11):
    import math
    radians = (math.pi / 180 ) * i 
    sin_value = math.sin(radians)
    cos_value = math.cos(radians)
    tan_value = math.tan(radians)
    print(f"{i}도 : {radians:.4f},sin {i} : {sin_value:.4f},cos {i} : {cos_value:.4f}, tan {i} :{tan_value:.4f}")
