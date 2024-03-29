# problem015

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

##

function main(n::Int,m::Int)::Int
    return binomial(n+m,n)
end

##

n = 20
m = 20

print(main(n,m))