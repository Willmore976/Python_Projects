import time
myLocalTime = time.localtime(time.time()) 
myAscTime   = time.asctime( myLocalTime )

Garden_View_Price = 185 #Price of Garden View
Pool_View_Price   = 195 # Price of Pool View
Lake_View_Price   = 215 #Price of Lake View
tax_rate          = 0.0850 #State tax
total             = 0 #Room Balance 



Hotel_Booking = True 

print 'Hello traveler welcome to the Ritz Carlton Hotel Website!'
print 'Our rooms available are...\nThe Graden View ($185) \nThe Pool View   ($195) \nThe Lake View   ($215)\n' 




while Hotel_Booking : #While Hotel_Booking is True, The Loop will continue to iterate

    Room_Selection = raw_input( 'G - Garden View\nP - Pool View\nL - Lake View\nQ - Quit' ).upper() #Determines room type

    #Room Selection Statement

    if Room_Selection == 'G' :
        Room_Selection = "Garden View"
        if Garden_View_Price == 185 :
            total += Garden_View_Price
            print "Excellent, our Garden View room has a nice view of Stonehenge!\n"
    elif Room_Selection == 'P' :
        Room_Selection = "Pool View"
        if Pool_View_Price == 195 :
            total += Pool_View_Price
            print "Excellent, remember o:ur hotel has a no clothes policy at our pools!\n"
    elif Room_Selection == 'L' :
        Room_Selection = "Lake View"
        if Lake_View_Price == 215 :
            total += Lake_View_Price
            print "Excellent, if you're lucky you might get to see the Loch Ness Monster\n"
    elif Room_Selection == 'Q' :
        print "Have a great day!"
        break
    else :
        Room_Selection not in [ 'G', 'P', 'L', 'Q' ] 
        print "Oops please enter G, P, L, or Q.\n"
        continue

    #Days Staying Variable 

    Days_Staying = int ( raw_input ( 'How many days would you like to stay?\n') ) 
    total *= Days_Staying
    
    #Golf Course Statement

    while True :
        Golf_Course = raw_input( "Fantastic, would you like to play on the golf course for an extra $25? (Y or N)\n" ).upper() #Determines if they want to use Golf Course
        if Golf_Course == 'Y' :
           Golf_Course = 25
           if Golf_Course == 25 :
               print "Good choice! Our golf course is known for its comfortable weather and wild animals.\n"
               break
        elif Golf_Course == "N" : 
               Golf_Course = 0
               break
        else : 
           print 'Ooops please try again'
           continue

    #Senior discount Statement   

    while True:
        Senior_discount = int(raw_input( 'How old are you, if your over 60 years old you qualify for a 10% Senior Discount! (Enter age)\n' )) #Determines Senior discount
        if Senior_discount >= 60 :
            Senior_discount = .90 
            if Senior_discount == .90 :
                print "Excellent, you will recieve an extra 10% off the order!\n"
                break
        elif Senior_discount < 60 :
            Senior_discount = 1
            break
        else :
            print "Ooops please try again!\n"
            continue


    #Formulas to calculate receipt

    Golf_Course_Balance = Golf_Course * Days_Staying                                    #Golf Course Balance
    Room_Balance = total                                                                #Room Balance
    Total_Before_Taxed = Room_Balance + Golf_Course_Balance                             #Total of order before taxed
    tax_total = tax_rate * Total_Before_Taxed                                           #Total of tax for the order               
    Total_With_Tax = Total_Before_Taxed + tax_total                                     #Total with Tax
    Senior_discount_total = Total_With_Tax - (Total_With_Tax * Senior_discount)         #Senior Discount if applicable
    New_Total = (Total_Before_Taxed + tax_total) - Senior_discount_total                #New Total with Senior discount
    
    #Receipt for customer
    
    print "You booked your room on", myAscTime
    print 'Your room balance for %i night(s) in our %s room is : $%.2f' % (Days_Staying, Room_Selection, Room_Balance)
    if Golf_Course == 25 :                                                      #Prints Golf Course Balance if they have one ; otherwise it will not print
        print 'Your golf course balance is : $%.2f' % (Golf_Course_Balance)
    print 'Your total before tax is : $%.2f' % (Total_Before_Taxed)
    print 'Your total tax for your order is: $%.2f' % (tax_total)
    if New_Total != Total_With_Tax :                                            #Prevents printing the same total twice. Prints if New Total and Total with Tax are different
        print 'Your total with tax is : $%.2f' % (Total_With_Tax)
    if Senior_discount == .90 :
        print 'Your Senior discount is: $%.2f' % (Senior_discount_total)        #Prints Senior discount if they have one ; otherwise it will not be printed
    print 'Your total for staying %i night(s) in our %s room is : $%.4f ' % (Days_Staying, Room_Selection, New_Total) 

    #Option to book ANOTHER GUEST

    Book_again = raw_input( 'Would you like to book another guest? (Y or N)\n' ).upper()
    if Book_again == 'Y' :
        total = 0
        continue
    else:
        print "Goodbye and have a superb day!"
        break
    
    
    
            
        
