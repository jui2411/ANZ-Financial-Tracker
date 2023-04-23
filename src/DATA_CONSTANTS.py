TRANSACTION_TYPES = {
    'AP': 'Automatic Payment',
    'BP': 'Bill Payment',
    'DC': 'Delayed Contribution', 
    'DD': 'Demand Draft',
    'EP': 'EFTPOS Network',
    'VT': 'Visa Network'
}

MONTHS = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'Jun': 5,
    'Jul': 6,
    'May': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
    }

CATEGORIES = {
    'HOME_EXPENSES' : [
        'MORTGAGE/RENT',
        'HOME/RENTAL_INSURANCE',
        'ELECTRICITY',
        'GAS/OIL',
        'WATER/SEWER/TRASH',
        'PHONE',
        'CABLE/SATELLITE',
        'INTERNET',
        'FURNISHING/APPLIANCES',
        'LAWN/GARDEN',
        'MAINTENANCE/SUPPLIES',
        'IMPROVEMENTS/RENOVATIONS'   
    ],

    'TRANSPORTATION' : [
        'VEHICLE_PAYMENTS',
        'AUTO_INSURANCE',
        'FUEL',
        'BUS/TAXI/TRAIN'
        'REPAIRS',
        'REGISTRATION/LICENSE',
    ],

    'HEALTH' : [
        'HEALTH_INSURANCE',
        'HEALTH_SPECIALISTS',
        'MEDICINE/DRUG',
        'LIFE_INSURANCE',
        'VETERTINARIAN/PET_CARE'
    ],

    'CHARITY/GIFTS': [
        'GIFTS_GIVEN',
        'CHARITABLE_DONATIONS',
        'RELIGIOUS_DONATIONS'
    ],

    'DAILY_LIVING': [
        'GROCERIES',
        'PERSONAL_SUPPLIES',
        'CLOTHING',
        'CLEANING',
        'EDUCATION/LESSIONS',
        'DINING/EATING_OUT',
        'SALON/BARBER',
        'PET_FOOD'
    ],

    'ENTERTAINMENT': [
        'ACTIVITIES',
        'BOOKS',
        'GAMES',
        'CINEMA',
        'HOBBIES',
        'MEDIA',
        'OUTDOOR_RECREATION',
        'SPORTS',
        'TOY/GADGETS',
        'VACATION/TRAVEL'
    ],

    'SAVINGS': [
        'EMERGENCY_FUND',
        'CAR_FUND',
        'INVESTMENTS',
        'EDUCATION_FUND',
        'MARRIAGE_FUND'
    ],

    'OBLIGATIONS': [
        'STUDENT_LOANS',
        'CREDIT_CARD_DEBT',
        'ALIMONY/CHILD_SUPPORT',
        'FEDERAL_TAXES',
        'STATE/LOCAL_TAXES'
    ],

    'SUBSCRIPTIONS': [
        'STREAMING_SERVICES',
        'GAMING',
        'GYM_MEMBERSHIPS'
    ],

    'MISCELLANEOUS': [
        'BANK_FEES',
        'PHONE_PLAN',
        'PRINTING'
    ]
}
    

TRANSACTION_NAMES = {

'Bugsy Tandem SL Burgess S Burgess S' : {
    'Comment': 'This is Student Life support for Sam Burgess',
    'Transaction': 'Expense',
    'Category':  'Donation',
    'Subcategory':  'Donation'
    },

'AIRWAYS CORP NZ PAYROLL' : {
    'Comment': '',
    'Type': 'Income',
    'Category':  'Donation',
    'Subcategory':  'Religion'
    },


'Bugsy Tandem SL Burgess S Burgess S' : {
    'Comment': '',
    'Category':  'Donation',
    'Subcategory':  'Donation'
    }
}