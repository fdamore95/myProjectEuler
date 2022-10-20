# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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

function decompose(n::Int, prime_seq::Array{Int})::Array{Int}
    decomposition = Array{Int}(undef,0,2)
    # println(prime_seq)
    for i in prime_seq
        if i <= n
            # println(i)
            factor = 0
            while n%i == 0
                n = n/i
                factor += 1
            end
            if factor>0
                decomposition = vcat(decomposition, [i factor])
            end
        else
            break        
        end
    end
    return decomposition
end

##

function main(n::Int)::Int
    if n < 1
        error(string("the input n = ",n, " must be greater than 0"))
    end
    mcm = 1
    prime_seq = eratosthenes( n )
    for i in 2:n
        factors = decompose(i,prime_seq)
        #println(factors)
        count = 1
        for j in factors[:,1]
            support = mcm
            for k in 1:factors[count,2]
                if support%j == 0
                    support /= j
                else
                    mcm *= j
                end
            end
            count +=1
        end
    end
    return mcm
end

##

n = 20
mcm = main(n)

## fast way to do it

lcm(2:n)