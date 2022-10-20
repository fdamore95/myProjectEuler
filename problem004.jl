# problem 4



# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


##

function verify_palindrome(n::Int)::Bool
    digits = []
    while n>0
        #print(n%10)
        digits = vcat(digits,[n%10])
        #println(digits)
        n = Int(floor(n/10))
    end
    # print(digits)
    if digits == reverse(digits)
        #println(digits)
        return true
    else
        return false
    end
end

function get_number(Nothing)::Int
    max = 0
    for i in range(999,100,step=-1)
        for j in range(i, 100, step=-1)
            if i*j < max
                break
            end
            #print(i,j)
            n = i*j
            #println(n)
            if verify_palindrome(n) == true
                #println(n)
                if max < n
                    max = n
                end
            end
        end
    end
    return max
end         

#print(verify_palindrome(1001))

print(get_number(Nothing))

