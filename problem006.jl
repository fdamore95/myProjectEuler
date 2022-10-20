# Problem 6

# The sum of the squares of the first ten natural numbers is 385

# The square of the sum of the first ten natural numbers is 55^2=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## 

function main(n::Int)::Int
    tosum = 1:n
    tosum = Array{Int}(tosum)
    squaresum = (sum(tosum)^2)
    sumofsquares = 0
    for i in tosum
        sumofsquares += i^2
    end
    return -sumofsquares+squaresum
end

function fastmain(n::Int)::Int
    squaresum = (n*(n+1)/2)^2
    sumofsquares = n*(n+1)*(2*n+1)/6
    return -sumofsquares+squaresum
end

##

n = 100

println(main(n))

println(fastmain(n))