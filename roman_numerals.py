def to_roman(num):
    #
    roman_map = {
        1000: "M", 900: "CM",
        500: "D", 400: "CD",
        100: "C", 90: "XC",
        50: "L", 40: "XL",
        10: "X", 9: "IX",
        5: "V", 4: "IV",
        1: "I"}
    #i believe we just have to keep dividing until we get something valid in floor division. so say if we have 90. we will test
    #1.)see how many place values it holds, so something like for x in num: if num // x: count += 1, x *= 10
    
    #2.)so if the number is 90, num // x starting at 1 would be valid, so count will += 1 making it 1, and the
    
    #3.)if we have 100 and divide it by % 10, we get 
    
    #new steps!!!! so we go from low to high, num % 10 gives us the ones place, we then configure that into a roman numeral and do result = "x" + result
    #modulo %100 will give the tens place, but you still have to subtract to update/ 
    x = 10
    result = ""

    for value, symbol in roman_map.items():
        while num >= value:
            result += symbol
            num -= value

    return result
    
    # write your code here!
    pass