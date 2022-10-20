# problem10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

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

function isprime(n::Int,tests::Array{Int})::Bool
    for i in tests
        if i > sqrt(n)
            break
        end
        if n % i == 0
            return false
        end
    end
    return true
end

##

function main(n::Int)::Int
    tests = eratosthenes(Int(floor(n)))
    out = 0
    lasti = 0
    for i in tests
        out += i
        lasti = i
    end
    for j in lasti+1:n
        # if j%10000 == 0:
        #    print(j)
        if j%2 == 1
            if isprime(j,tests)
                out +=j
            end
        end
    end
    return out
end

##

n = 2*10^6

print(main(n))
    
# %%
