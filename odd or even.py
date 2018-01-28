i = 10
while i > 0:
    print i
    if i > 5:
        print 'Bigger than 5!'
    elif i % 2 != 0:
        print 'this is ODD number'
        print 'and i <= 5'
    else:
        print 'i <= 5'
        print 'this is EVEN number, not ODD'
        print 'special number! :)'
    i = i - 1
print "we are after 'while' loop"
print "the end" 
