# problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

##


function eratosthenes(n::Int)::Array{Int}
    prime_seq = Array(1:n)
    prime_seq[1] = 0
    tokeep = [2]
    maxit = sqrt(n)+1

    # first we delete multiples of 2
    index = 2^2
    while index < n+1
        prime_seq[index] = 0
        index += 2
    end

    # then the others
    for i in 3:n
        if prime_seq[i] > 0 && i < maxit
            index = i^2
            while index < n+1
                prime_seq[index] = 0
                index += 2*i
            end
            push!(tokeep,i)
            # tokeep = vcat(tokeep, [i])
        elseif prime_seq[i] > 0
            #print(i)
            push!(tokeep,i)
            #tokeep = vcat(tokeep, [i])
        end
    end
    return prime_seq[tokeep]
end

##
        

function largest_prime_factor(n::Int)::Int
    maxnum = sqrt(n)
    prime_seq = eratosthenes(Int(floor(maxnum)))
    # println(prime_seq)
    out = 1
    while n > maxnum
        #println(n)
        isprime = true
        for i in reverse(prime_seq)
            if n%i == 0
                isprime = false
                if i>out
                    out = i
                end
                n = n ÷ i
                while n%i == 0
                    if i>out
                        out = i
                    end
                    n = n ÷ i
                end
            end
        end
        if isprime==true
            return n
        end
    end
    return out
end
##

n = 600851475143

println(largest_prime_factor(n))
