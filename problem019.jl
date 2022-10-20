# problem019

##

# You are given the following information, but you may prefer to do some research for yourself.

#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

##

function main(firstsunday::Int, startyear::Int, endyear::Int)::Int
    
    count = 0
    todelete = 0
    
    reminder = firstsunday
    
    for year in startyear:endyear
        leap = 0
        if year % 4 == 0 && !(year % 100 == 0 && year % 400 != 0)
            leap = 1
        end

        schedule = [31, 28+leap,31,30,31,30,31,31,30,31,30,31]

        println(year)
        println(sum(schedule))

        for month in schedule
            if firstsunday == 1
                count += 1
                if year == startyear
                    todelete += 1
                end
            end
            while firstsunday ≤ month
                firstsunday += 7
            end
            firstsunday = firstsunday % month
        end
    end
    return count - todelete
end

##

firstsunday = 7
startyear = 1900
endyear = 2000

println("the answer is ", main(firstsunday, startyear,endyear))

