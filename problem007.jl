# problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

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

function main(n::Int)::Int
    if n < 56
        x = n^2
        prime_seq = eratosthenes(x)
    else
        x = 2*n*log(n)
        x = ceil(x)
        x = Int(x)
        prime_seq = eratosthenes(x)
    end
    return prime_seq[n]
end

## 

n = 10001
println(main(n))