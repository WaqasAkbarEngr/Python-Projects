import random

botGreetings = ['Welcome to Python Book Shop',
                'Welcome! This is Pyton Book Shop',
                'You have entered Python Book Shop',
                'Greetings! Welcome to Python Book Shop']

recommendResponses = ['So you want me to recommend a category',
                        'You said to recommend a category',
                        'I would be more than happy to recommend you a category',
                        'It would be my pleasure to recommend you a category']

categorySelectionResponses = ['You selected category: ',
                                'So you want',
                                'You are going with category:',
                                'Selected category is: ']

invalidResponses = ['Invalid Input',
                    'Wrong Input',
                    'Incorrect Choice',
                    'Incomprendible Choice']

discardingResponses = ['Your cart has been discarded',
                        'Your card has been emptied',
                        'Card emptied',
                        'Card discarded']

categoryRecommendResponse = ['is HOT category now a days',
                            'is being read much now a days',
                            'would be a good pick for you',
                            'would suit you more']

shoppingCart = {
                    'bookName' : [],
                    'bookPrice' : [],
                    'totalBill' : 0
}

categoryChoice = ''

#botCategory = ''

bookCategories = ['Arts','Academic','Business','Computer','Engineering','Health',
                    'History','Literature','Law','Medical','Novel','Politics','Science']

recommendedCategories = [
                            ['Science','Academic','Medical','Health'],
                            ['Arts','Business','Politics','Law'],
                            ['Computer','Engineering'],
                            ['Literature','History','Novel']
]

booksInventory = {
        'Arts' : [  { 'bookName' : 'Drawing Cartoons & Comics' , 'price' : 500},
                    { 'bookName' : 'Draw 50 Animals' , 'price' : 500},
                    { 'bookName' : 'Fun With A Pencil' , 'price' : 500},
                    { 'bookName' : 'How to Draw and Paint Anatomy' , 'price' : 500},
                    { 'bookName' : 'Piano for Beginners' , 'price' : 500},
                    { 'bookName' : 'Drawing Comics the Marvel Way' , 'price' : 500},
                    { 'bookName' : 'Successful Drawing' , 'price' : 500},
                    { 'bookName' : 'How to Read Music 7 Easy Lessons' , 'price' : 500},
                    { 'bookName' : 'Drawing Portraits' , 'price' : 500},
                    { 'bookName' : 'Sketch Book for the Artist' , 'price' : 500}
                    ],

        'Academic' : [  { 'bookName' : 'Spoken English: Flourish Your Language' , 'price ': 500 },
                    { 'bookName' : '100 Great Business Ideas' , 'price' : 500 },
                    { 'bookName' : 'Fundamentals of Physics' , 'price' : 500 },
                    { 'bookName' : 'Basic Engineering Mathemaitcs' , 'price' : 500 },
                    { 'bookName' : 'English Advanced Vocabulary and Structure Practice' , 'price' : 500 },
                    { 'bookName' : 'Essentials of Anatomy and Physiology' , 'price' : 500 },
                    { 'bookName' : 'How to Write Better Essays' , 'price' : 500},
                    { 'bookName' : 'How to Study' , 'price' : 500 },
                    { 'bookName' : '101 Activities For Teaching Creativity and Problem Solving' , 'price' : 500 },
                    { 'bookName' : '536 Puzzles and Curious Problems' , 'price' : 500 }
                    ],

        'Business' : [  { 'bookName' : 'Law of Success' , 'price ': 500 },
                    { 'bookName' : 'How to Write a usiness Plan' , 'price' : 500 },
                    { 'bookName' : '100 Great Business Ideas' , 'price' : 500 },
                    { 'bookName' : 'Strategic Leadership' , 'price' : 500 },
                    { 'bookName' : 'Money, Banking, and International FInance' , 'price' : 500 },
                    { 'bookName' : 'The Mind of the Buyer: A Psychology of Selling' , 'price' : 500 },
                    { 'bookName' : 'The Mathematics Of Financial Modeling And Investment' , 'price' : 500},
                    { 'bookName' : 'The 21 Irrefutable Laws of Leadership' , 'price' : 500 },
                    { 'bookName' : 'A Handbook of Human Resource Management Practice' , 'price' : 500 },
                    { 'bookName' : 'Strategic Marketing: Planning and COntrol' , 'price' : 500 }
                    ],

        'Computer' : [  { 'bookName' : 'Theory of Computer Science' , 'price ': 500 },
                    { 'bookName' : 'Computer Systems: Digital Design, Fundamentals of Computing' , 'price' : 500 },
                    { 'bookName' : 'Data Structures and Algorithms in C++' , 'price' : 500 },
                    { 'bookName' : 'JavaScript: JavaScript For Beginners' , 'price' : 500 },
                    { 'bookName' : 'Learn to Program with C' , 'price' : 500 },
                    { 'bookName' : 'Introduction to Operating Systems' , 'price' : 500 },
                    { 'bookName' : 'Learn Computer Vision in 24 Hours' , 'price' : 500},
                    { 'bookName' : 'Mastering Functional Programming' , 'price' : 500 },
                    { 'bookName' : 'Database Management System: A Beginners Guide' , 'price' : 500 },
                    { 'bookName' : 'Understanding Computer Networks' , 'price' : 500 }
                    ],
    
        'Engineering' : [  { 'bookName' : 'Aerodynamics for Engineering Students' , 'price ': 500 },
                    { 'bookName' : 'Introduction to Electrical Engineering' , 'price' : 500 },
                    { 'bookName' : 'Physics and Engineering of Radiation Detection' , 'price' : 500 },
                    { 'bookName' : 'Basic Engineering Mathematics' , 'price' : 500 },
                    { 'bookName' : 'Electric Power Engineering Handbook' , 'price' : 500 },
                    { 'bookName' : 'Highway Engineering' , 'price' : 500 },
                    { 'bookName' : 'Introduction to Finite Elements Engineering' , 'price' : 500},
                    { 'bookName' : 'Mathematics fo Physics and Engineering' , 'price' : 500 },
                    { 'bookName' : 'Chemical Engineering Thermodynamics II' , 'price' : 500 },
                    { 'bookName' : 'Machine Drawing' , 'price' : 500 }
                    ],
    
        'Health' : [  { 'bookName' : 'Light on Yoga: THe Bible of Modern Yoga' , 'price ': 500 },
                    { 'bookName' : 'Genius Foods: Become Smarter, Happier, and More' , 'price' : 500 },
                    { 'bookName' : 'Healthy Weight Loss Without Dieting' , 'price' : 500 },
                    { 'bookName' : 'Anxiety & Depression Workbook' , 'price' : 500 },
                    { 'bookName' : 'Encyclopedia of Diets - A Guide to Health and Nutrition' , 'price' : 500 },
                    { 'bookName' : 'Emotional Healing' , 'price' : 500 },
                    { 'bookName' : 'Awaken Healing Energy Through The Tao' , 'price' : 500},
                    { 'bookName' : 'Timeless Secrets of Health and Rejuvenation' , 'price' : 500 },
                    { 'bookName' : 'Fitness and Health: A Practical Guide' , 'price' : 500 },
                    { 'bookName' : 'Sport and Exercise Psychology' , 'price' : 500 }
                    ],
    
        'History' : [  { 'bookName' : 'The Encyclopedia of World History' , 'price ': 500 },
                    { 'bookName' : 'World History 101' , 'price' : 500 },
                    { 'bookName' : 'Historys Greatest Lies' , 'price' : 500 },
                    { 'bookName' : 'The Secret History of the World' , 'price' : 500 },
                    { 'bookName' : 'A World History of Ninteenth-Century Archaeology' , 'price' : 500 },
                    { 'bookName' : 'All about History: Book of History Year by Year' , 'price' : 500 },
                    { 'bookName' : 'The Decisive Battles of World History' , 'price' : 500},
                    { 'bookName' : 'Heroes fo History: A Brief History of Civilization' , 'price' : 500 },
                    { 'bookName' : 'The Oxford History of the Classical World' , 'price' : 500 },
                    { 'bookName' : 'A History of Later Roman Empire' , 'price' : 500 }
                    ],
    
        'Literature' : [  { 'bookName' : 'English Literature' , 'price ': 500 },
                    { 'bookName' : 'The Cambridge History of English Romantic Literature' , 'price' : 500 },
                    { 'bookName' : 'Encyclopedia of African-American Literature' , 'price' : 500 },
                    { 'bookName' : 'An Introduction to Literature, Criticism and Theory' , 'price' : 500 },
                    { 'bookName' : 'A History of Indian Literature' , 'price' : 500 },
                    { 'bookName' : 'Glencoe Literature: American Literature' , 'price' : 500 },
                    { 'bookName' : 'The Oxford Handbook of Medieval Literature' , 'price' : 500},
                    { 'bookName' : 'The Literature Book' , 'price' : 500 },
                    { 'bookName' : 'Glencoe Literature: British Literature' , 'price' : 500 },
                    { 'bookName' : 'German Literature of Eighteenth Century' , 'price' : 500 }
                    ],
    
        'Law' : [  { 'bookName' : 'International Criminal Law Practioner Library' , 'price ': 500 },
                    { 'bookName' : 'International Humanitarian Law' , 'price' : 500 },
                    { 'bookName' : 'Constituional Law, Administrative Law and Human Rights' , 'price' : 500 },
                    { 'bookName' : 'Modern Maritime Law' , 'price' : 500 },
                    { 'bookName' : 'Introduction to Law' , 'price' : 500 },
                    { 'bookName' : 'Environmental Law' , 'price' : 500 },
                    { 'bookName' : 'LAW 100 - Introduction to Law' , 'price' : 500},
                    { 'bookName' : 'International Law and International Relations' , 'price' : 500 },
                    { 'bookName' : 'Criminal Law Theory: Doctrines of the General Part' , 'price' : 500 },
                    { 'bookName' : 'Principles of Land Law' , 'price' : 500 }
                    ],
    
        'Medical' : [  { 'bookName' : 'Illustrated Medical Dictionary' , 'price ': 500 },
                    { 'bookName' : 'Medical Symptoms: A Visual Guide' , 'price' : 500 },
                    { 'bookName' : 'A Short TExtbook of Medical Pharmacology' , 'price' : 500 },
                    { 'bookName' : 'Medical-Surgical Nursing' , 'price' : 500 },
                    { 'bookName' : 'Essentials of Medical Microbiology' , 'price' : 500 },
                    { 'bookName' : 'Textbook of Medical Oncology' , 'price' : 500 },
                    { 'bookName' : 'Essentials of Medical Parasitology' , 'price' : 500},
                    { 'bookName' : 'Pharmacology for Medical Graduates' , 'price' : 500 },
                    { 'bookName' : 'Langmans Medical Embryology' , 'price' : 500 },
                    { 'bookName' : 'Medical Terminology Systems: A Body Systems Approach' , 'price' : 500 }
                    ],
    
        'Novel' : [  { 'bookName' : 'The Monk Who SOld His Ferrari' , 'price ': 500 },
                    { 'bookName' : 'Nine Day Novel-Writing Faster' , 'price' : 500 },
                    { 'bookName' : 'The Seven Spirits of God' , 'price' : 500 },
                    { 'bookName' : 'Chasing Darkness: An Elvis Cole Novel' , 'price' : 500 },
                    { 'bookName' : '1984 - Classic Novels and Literature' , 'price' : 500 },
                    { 'bookName' : 'The Forty Rules of Love: A Novel of Rumi' , 'price' : 500 },
                    { 'bookName' : 'The English Novel' , 'price' : 500},
                    { 'bookName' : 'How to Write a Damn Good Novel' , 'price' : 500 },
                    { 'bookName' : 'Sacred Games: A Novel' , 'price' : 500 },
                    { 'bookName' : 'The Phoenix Project: A Novel about IT' , 'price' : 500 }
                    ],
    
        'Politics' : [  { 'bookName' : 'Political Science' , 'price ': 500 },
                    { 'bookName' : 'Encyclopedia of Government and Politics' , 'price' : 500 },
                    { 'bookName' : 'Comparative Government and Politics' , 'price' : 500 },
                    { 'bookName' : 'Understanding Third World Politics' , 'price' : 500 },
                    { 'bookName' : 'Politics: The Basics' , 'price' : 500 },
                    { 'bookName' : 'Political Philosophy' , 'price' : 500 },
                    { 'bookName' : 'Introduction to Comparative Politics' , 'price' : 500},
                    { 'bookName' : 'International Political Economy' , 'price' : 500 },
                    { 'bookName' : 'Global Politics' , 'price' : 500 },
                    { 'bookName' : 'Handbook Political Theory' , 'price' : 500 }
                    ],
    
        'Science' : [  { 'bookName' : 'Encyclopedia of Biology' , 'price ': 500 },
                    { 'bookName' : 'Medical Microbiology' , 'price' : 500 },
                    { 'bookName' : 'Space, Time and Einstein' , 'price' : 500 },
                    { 'bookName' : 'Essentials of Inorganic CHemistry' , 'price' : 500 },
                    { 'bookName' : 'The Quantum Structure of Space and Time' , 'price' : 500 },
                    { 'bookName' : 'Basics of Space Flight' , 'price' : 500 },
                    { 'bookName' : 'Food Microbiology' , 'price' : 500},
                    { 'bookName' : 'Cell Biology' , 'price' : 500 },
                    { 'bookName' : 'Food Chemistry' , 'price' : 500 },
                    { 'bookName' : 'Quantum Physics' , 'price' : 500 }
                    ],
    }



def displayCategories():
    print('\n\nThis Book Shop has following book categories:')
    for category in bookCategories:
        print( str((bookCategories.index(category)) + 1 ) + " " + category )


def displayBooks(category):
    serial = 1
    for book in booksInventory[category]:
        print(str(serial) + ". " + book['bookName'])
        serial = serial + 1
    


def recommendCategory(categoryChoice):
    isValidChoice = False
    while (not isValidChoice):
        categoryGroup = input("\n\nYou like Science, Arts, Technology or Literature? ")

        if categoryGroup.lower() == 'science':
            categoryChoice = recommendedCategories[0][random.randint(0,3)]
            print("\n\n" + categoryChoice + " " + categoryRecommendResponse[random.randint(0,3)])
            isValidChoice = True
            shopping()

        elif categoryGroup.lower() == 'arts':
            categoryChoice = recommendedCategories[1][random.randint(0,3)]
            print("\n\n" + categoryChoice + " " + categoryRecommendResponse[random.randint(0,3)])
            isValidChoice = True

        elif categoryGroup.lower() == 'technology':
            categoryChoice = recommendedCategories[2][random.randint(0,1)]
            print("\n\n" + categoryChoice + " " + categoryRecommendResponse[random.randint(0,3)])
            isValidChoice = True

        elif categoryGroup.lower() == 'literature':
            categoryChoice = recommendedCategories[3][random.randint(0,2)]
            print("\n\n" + categoryChoice + " " + categoryRecommendResponse[random.randint(0,3)])
            isValidChoice = True

        else:
            print(invalidResponses[random.randint(0,3)])
            print("Let's Try Again")


def shopping(categoryChoice):
    print("\nHere's list of books in " + categoryChoice + " Category:")
    displayBooks(categoryChoice)

    isChoiceCorrect = False
    while (not isChoiceCorrect):
        foundBook = input("\nHas any book caught your attention? (Yes/No)\nIf you want to change category, simply type 'change'")
        if foundBook.lower() == 'yes':
            bookEntered = False
            while (not bookEntered):
                boughtBook = input("\nEnter Serial No of book to add it to cart\nType 0 when done ")
                if int(boughtBook) < 11 and int(boughtBook) > 0:
                    isChoiceCorrect = True
                    selectedBook = (booksInventory[categoryChoice.capitalize()])[int(boughtBook)-1]
                    shoppingCart['bookName'].append(selectedBook['bookName'])
                    shoppingCart['bookPrice'].append(selectedBook['price'])
                    print("\n" + selectedBook['bookName'] + " has been added to cart")

                elif boughtBook == '0':
                    bookEntered = True

                    isChoiceCorrect = False
                    while (not isChoiceCorrect):
                        moreBooks = input("\nDo you want to choose another category or go to cart? (category/cart) ")
                        if moreBooks.lower() == 'category':
                            isChoiceCorrect = True
                            bookHunting()

                        elif moreBooks.lower() == 'cart':
                            isChoiceCorrect = True
                            count = 1
                            print("\n\nHere's you cart")
                            print("Sr #                 Item Name                   Price")
                            for index in range( len( shoppingCart['bookName'] ) ):
                                print(count , end ="\t")
                                print(shoppingCart['bookName'][index] , end = "\t")
                                print(shoppingCart['bookPrice'][index])
                                shoppingCart['totalBill'] = shoppingCart['totalBill'] + shoppingCart['bookPrice'][index]
                                count = count + 1
                            print("\n-------------------------------------------------------------")
                            print("Your Total Bill is Rs. " + str(shoppingCart['totalBill']))

                            isChoiceCorrect = False
                            while(not isChoiceCorrect):
                                checkout = input("\n\nType 'pay' to buy these books or type 'discard' to start again ")
                                if checkout.lower() == 'pay':
                                    isChoiceCorrect = True
                                    print("\nThank you for visiting Python Book Shop\nHope you enjoyed book hunting with us\nSee you again\n\n")
                                    isChoiceCorrect = True

                                elif checkout.lower() == 'discard':
                                    isChoiceCorrect = True
                                    shoppingCart.clear()
                                    shoppingCart['bookName'] = []
                                    shoppingCart['bookPrice'] = []
                                    shoppingCart['totalBill'] = 0
                                    print(discardingResponses[random.randint(0,3)])
                                    isChoiceCorrect = True
                                    bookHunting()

                                else:
                                    print(invalidResponses[random.randint(0,3)])
                                    print("Let's Try Again")

                        else:
                            print(invalidResponses[random.randint(0,3)])
                            print("Let's Try Again")

                else:
                    print(invalidResponses[random.randint(0,3)])
                    print("Let's Try Again")

        elif foundBook.lower() == 'no':
            isChoiceCorrect = True
            displayCategories()

        elif foundBook.lower() == 'change':
            isChoiceCorrect = True
            bookHunting()

        else:
            print(invalidResponses[random.randint(0,3)])
            print("Let's Try Again")


def bookHunting():
    displayCategories()

    isChoiceCorrect = False
    while (not isChoiceCorrect):
        categoryChoice = input("Choose your categoty OR type 'recommend' if you like me to recommend you a book? ")
        categoryChoice = categoryChoice.capitalize()
        if categoryChoice.lower() == 'recommend':
            print(recommendResponses[random.randint(0,3)])
            recommendCategory(categoryChoice)
            isChoiceCorrect = True

        elif categoryChoice.capitalize() in bookCategories:
            isChoiceCorrect = True
            print("\n" + categorySelectionResponses[random.randint(0,3)] + " " + categoryChoice.capitalize())
            shopping(categoryChoice)
            

        else:
            print("Invalid choice")
            print("Let's Try Again")

print(botGreetings[random.randint(0,3)])
print("I am PyBot and I would be your shopping assistant today")
bookHunting()