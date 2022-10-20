# problem017


# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

## this resolution sucks

function ourbase()::Dict
    basecases = Dict{Int, Int}()
    three = [1,2,6,10]
    four = [4,5,9]
    five = [3,7,8,40,50,60]
    six = [11,12,20,30,80,90]
    seven = [15,16,70,100]
    eight = [13,14,18,19,1000]
    nine = [17]
    for i in three
        basecases[i] = 3
    end
    for i in four
        basecases[i] = 4
    end
    for i in five
        basecases[i] = 5
    end
    for i in six
        basecases[i] = 6
    end
    for i in seven
        basecases[i] = 7
    end
    for i in eight
        basecases[i] = 8
    end
    for i in nine
        basecases[i] = 9
    end
    # for i in ten
    #     basecases[i] = 10
    # end
    return basecases
end

##

function count(n::Int, ord::Int, basecases::Dict)::Int
    if n == 0
        return 0
    end
    and = 0
    yes = 1
    if n > 100 && n < 1000
        supp = get(basecases, 100, 0)
        yes = 0
    else
        supp = get(basecases,n,0)
    end
    if supp > 0 && yes == 1 && n !=100 && n != 1000
        return supp
    else
        if ord > 10 && n % ord != 0
            and += 1
            quot = n ÷ ord
            return supp + get(basecases,quot,0) + and*3 + count(n%ord, ord ÷ 10, basecases)
        elseif ord ≤ 10
            quot = n ÷ ord
            return supp + get(basecases,quot*ord,0) + and*3 + count(n%ord, ord ÷ 10, basecases)
        else 
            quot = n ÷ ord
            return supp + get(basecases,quot,0) + and*3 + count(n%ord, ord ÷ 10, basecases)
        end
    end
end
    
##

function main(n::Int)::Int
    basecases = ourbase()
    sum = 0
    for i in 1:n
        sum += count(i,10^Int(floor(log10(i))),basecases)
    end
    return sum
end

        

## 

n = 1000
println(main(n))