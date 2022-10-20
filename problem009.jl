# problem 9

## 

function findtriplet(n::Int)::Array
    if n<1
        error("n must be bigger")
    end
    for b in 1:Int(ceil(n/2))
        for a in 0:b
            test = sqrt(a^2+b^2)
            if isinteger(test) && a + b + Int(test) == n
                return [a,b,Int(test)] 
            end
        end
    end
    error("no triplet found")
end

##

function main(n::Int)::Int
    a = findtriplet(n)
    return a[1]*a[2]*a[3]    
end

##

n = 1000
print(main(n))