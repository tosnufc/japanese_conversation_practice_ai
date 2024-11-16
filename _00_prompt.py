# archive_folder_name = "restaurant_vegan"
# scenario = f"""
# The customer is vegan. He wants to order food but would like to ask what are the vegan choices on the menu.
# He wants to ask about the ingredients on the item on the menu that he's interested in whether they contain any non-vegan ones or not.
# If it contains non-vegan ingredients, he wants to ask whether it is possible to substitute these ingredients with some vegan ingredients or not.

# The waiter is helpful and very polite.
# """
# tone = "business" # 'casual', 'business', 'close-friend', 'very-polite-talking-to-your-senior'

# archive_folder_name = "travel_plan"
# scenario = "Two close friends are talking about their travel plan within Japan. They will have 1-week off for their vacation. They like nature and quite places."
# tone = "close-friend" # 'casual', 'business', 'close-friend', 'very-polite-talking-to-your-senior'

# archive_folder_name = "sore_throat"
# scenario = "You have been having a sore throat for the past two week. You are now visiting a doctor."
# tone = "business" # 'casual', 'business', 'close-friend', 'very-polite-talking-to-your-senior'

# archive_folder_name = "bad_day"
# scenario = "Your friend looks sad and down. You are worried about here and want to see what you can help"
# tone = "casual" # 'casual', 'business', 'close-friend', 'very-polite-talking-to-your-senior'

# archive_folder_name = "birthday"
# scenario = "Today is your best friend's birthday."
# tone = "close-friend" # 'casual', 'business', 'close-friend', 'very-polite-talking-to-your-senior'

# archive_folder_name = "birthday_teacher"
# scenario = "Today is your Japanese teacher's birthday."
# tone = "very-polite-talking-to-your-senior" # 'casual', 'business', 'close-friend', 'very-polite-talking-to-your-senior'

# archive_folder_name = "combini"
# scenario = "You are paying for grocery at a Japanese convenient store."
# tone = "business" # 'casual', 'business', 'close-friend', 'very-polite-talking-to-your-senior'

# archive_folder_name = "network_engineer_job_interview"
# scenario = "You are applying for a network engineer job in a Japanese company and is getting interviewed."
# tone = "business" # 'casual', 'business', 'close-friend', 'very-polite-talking-to-your-senior'

# archive_folder_name = "buying_t-shirt"
# scenario = "You are shopping at a department store in Ginza. Looking for a classic black T-shirt in M-size. Also asking to try it on"
# tone = "business-polite" # 'casual', 'business', business-polite, 'close-friend', 'very-polite-talking-to-your-senior'

# archive_folder_name = "buying_train_tickets"
# scenario = "You want to buy a Shinkansen ticket from Tokyo station to Nagoya"
# tone = "business" # 'casual', 'business', business-polite, 'close-friend', 'very-polite-talking-to-your-senior'

# archive_folder_name = "buying_art_museum_tickets"
# scenario = "You want to buy team-lab museum tickets for you and your family (4 adults and 1 7-years old kid)"
# tone = "business" # 'casual', 'business', business-polite, 'close-friend', 'very-polite-talking-to-your-senior'

# archive_folder_name = "relocating_to_ca"
# scenario = "You are tell your close friend that you will relocate to California next year"
# tone = "close-friend" # 'casual', 'business', business-polite, 'close-friend', 'very-polite-talking-to-your-senior'

# archive_folder_name = "buying_2nd_hand_pc_akb"
# scenario = "You are at an electronic shop selling second-hand laptops, PC and parts. You want to buy the one with the lighest weight and have longest battery life"
# tone = "business" # 'casual', 'business', business-polite, 'close-friend', 'very-polite-talking-to-your-senior'

archive_folder_name = "osaka_universal_studio"
scenario = "You want to tell you close friend that you will be in Osaka with your family and will take them to Universal Studios. You won't have time to visit your friend in Kyoto."
tone = "close-friend" # 'casual', 'business', business-polite, 'close-friend', 'very-polite-talking-to-your-senior'

prompt = f"""
You are a language teacher AI assistant.
Your task is as follows:
- generate a conversation in English from the scenario below.
      <<<{scenario}>>>
- convert the conversation you have generated into Japanese langauge using {tone} tone.

When converting into Japanese language, make sure you make it sounds natural in Japanese language, not just translating it directly.

format the output as follows:

Person A: <put your generated sentence here>
Person B: <put your generated sentence here>
Person A: <put your generated sentence here>
Person B:
Person A:
*****
<put your conversation translation here>
"""
