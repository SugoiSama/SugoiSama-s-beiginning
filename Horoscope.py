from calendar import month
import random

print("""******************************************
Hello There, Let me tell you your fortune!
So tell me""")

month =input("Which month were you born in?")
month.lower
day =int(input("Which day were you born in?"))
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

capricorn_horoscope = ["Today's the perfect day to brainstorm your next moves as creative Venus opposes no-limits Neptune.","Your mind may be on ownership, which is where the real money comes in."," Volunteering alongside an industry VIP might be the fastest way to get a loafer in the door, Capricorn."]
aquarius_horoscope = ["What do you consider valuable, Aquarius? You may want to share that with the people in your life Today and see where the conversation leads.","Your adventurous side is piqued on Sunday, as the new moon in Libra activates your broad-minded ninth house.","If you’ve forgotten that the world is your oyster, reminders may pop up throughout the day, like a friend’s envy-inducing photos from her latest vacation or an article about a place you’ve been dying to visit."]
pisces_horoscope = ["your relationship house locks horns with your ruler Neptune which is fogging up the windows of your first house of self-expression.","with Sunday’s new moon in Libra anchored in your eighth house of seduction, your esoteric allure is at the wheel.","Spiritual antennae up-you'll be guided in your actions."]
aries_horoscope = ["This weekend brings an important opportunity to review your relationship goals.","you may realize that your boundaries have shifted and that you need to make new agreements about how much to give and take.","Contrary to family opinion, you are doing the right thing. Make travel arrangements. Your soul mate awaits. "]
taurus_horoscope = ["you’ll see clearly who’s in your corner. You may also realize it’s time to step away from a certain group.","With Sunday’s new moon in your sixth house of healthy living, given the choice, you’re likely to choose a candlelight yoga class over a boozy brunch. And this is just the beginning.","Good news. Sword of Damocles removed-bills will be paid, obligations met. You'll be aware of your own worth-which is plenty. Relative visits, compliments you on housekeeping."]
gemini_horoscope = ["Love is in the air! But don’t expect any direct hits on Saturday under an obfuscating opposition between Venus and befuddling Neptune.","Find some weekend cultural activities, dress up and see who’s there. If nothing else, this will be a warm-up for more flirty socializing.","ttention revolves around reputation, credibility, legal rights. Spotlight on proposals, partnership or marriage. You'll learn you are not alone. Cancer native plays major role."]
cancer_horoscopes = ["You will be where you are supposed to be. Rely upon intuition,timing. Keep the faith.Goal is closer than anticipated.", " Problems others can't solve will be regarded as easy for you. Moon position emphasizes success in finance, romance","Fun, frolic behind the scenes.Lunar position emphasizes clandestine arrangements, hidden romance. Popularity increases as result of published material."]
leo_horoscope = ["Mind your money this Saturday, Leo, or it could quickly burn a hole in your silk-lined pocket.","Sunday’s new moon in your third house of hometown happenings heats things up in your zip code. You might think you’ve seen it all, but guess again, Leo.","Element of deception present, deliberate or otherwise. Fight for legal rights, insist on viewing results of accounting. Questions concerning inheritance arise."]
virgo_horoscope = ["Saturday’s Venus-Neptune opposition brings a swift reminder that the best relationships begin with self-love.","Sunday’s new moon in Libra kickstarts an economic-stimulus plan. Is it time to circulate your resume or pitch new clients?","Family differences arise in connection with payments, loans. Be familiar with accounting procedures, make intelligent concessions without watering down principles."]
libra_horoscope = ["Boundaries don’t have to be rigid, Libra. In fact you may feel like softening them up a little this Saturday as nebulous Neptune opposes your ruler, Venus.","Sunday’s new moon in Libra hits the refresh button on your internal browser, clearing away that heavily cached personal history…or at least helping you focus on the brighter days ahead.","Problems others can't solve will be regarded as easy for you. Scorpio people figure in unusual scenario. Moon position emphasizes success in finance, romance."]
scorpio_horoscope = ["Are you getting the credit you deserve, Scorpio? Saturday’s tangled angle between Venus and Neptune could arouse resentment if you’ve been a team player at your own expense.","Sunday’s new moon in your soulful, compassionate twelfth house tugs at the old heartstrings. Drop your guard and let the feelings flow.","Lunar phase highlights promotion, production, recognition you should have received months ago. You'll get material reward."]
sagittraius_horoscope = ["Take a break, Sagittarius! You’ll find that you’re far more productive after a day with your besties (or at least a long brunch).","Sunday’s new moon lands in your eleventh house of community, helping you radar in on a squad of kindred spirits.","Keep plans flexible-individual who plans itinerary will be absent. Take charge of your own destiny-love relationship depends on ability to travel. Aries involved."]

if month not in months:
    print("Nursery padhna jau bhai month haru ko spelling nai aaudaina raixa ta")

if month in months:
    if month == "january":
        sign = "Capricorn" if (day < 20) else "Aquarius"
    elif month == "february":
        sign = "Aquirus" if (day < 19) else "Pisces"
    elif month == "march":
        sign ="Pices" if (day < 21) else "Aries"
    elif month == "april":
        sign = "Aries" if (day < 20) else " Taurus"
    elif month == "may":
        sign = "Taurus" if (day < 21) else "Gemini"
    elif month == "june":
        sign = "Gemini" if (day < 21) else "Cancer"
    elif month == "july":
        sign = "Cancer" if (day < 23) else "Leo"
    elif month == "august":
        sign = "Leo" if (day < 23) else "Virgo"
    elif month == "september":
        sign = "Virgo" if (day < 23) else "Libra"
    elif month == "october":
        sign = "Libra" if (day < 23) else "Scorpio"
    elif month == "november":
        sign = "Scorpio" if (day < 22) else "Sagittarius"
    elif month == "december":
        sign = "Sagittarius" if (day < 22) else "Capricorn"

print ("Your zodiac sign is:" + sign)

if sign == "Capricorn":
         horoscope1 = random.choice(capricorn_horoscope)
         print(f"Your horoscope for today is: {horoscope1}")
elif sign == "Aquirus":
         horoscope2 = random.choice(aquarius_horoscope)
         print(f"Your horoscope for today is: {horoscope2}")
elif sign == "Pices":
         horoscope3 = random.choice(pisces_horoscope)
         print(f"Your horoscope for today is: {horoscope3}")
elif sign == "Aries":
         horoscope4 = random.choice(aries_horoscope)
         print(f"Your horoscope for today is: {horoscope4}")
elif sign == "Taurus":
         horoscope5 = random.choice(taurus_horoscope)
         print(f"Your horoscope for today is: {horoscope5}")
elif sign == "Gemini":
         horoscope6 = random.choice(gemini_horoscope)
         print(f"Your horoscope for today is: {horoscope6}")
elif sign == "Cancer":
         horoscope7 = random.choice(cancer_horoscopes)
         print(f"Your horoscope for today is: {horoscope7}")
elif sign == "Leo":
         horoscope8 = random.choice(leo_horoscope)
         print(f"Your horoscope for today is: {horoscope8}")
elif sign == "Virgo":
         horoscope9 = random.choice(virgo_horoscope)
         print(f"Your horoscope for today is: {horoscope9}")
elif sign == "Libra":
         horoscope10 = random.choice(libra_horoscope)
         print(f"Your horoscope for today is: {horoscope10}")
elif sign == "Scorpio":
         horoscope11 = random.choice(scorpio_horoscope)
         print(f"Your horoscope for today is: {horoscope11}")
elif sign == "Sagittarius":
         horoscope12 = random.choice(sagittraius_horoscope)
         print(f"Your horoscope for today is: {horoscope12}")

print("******************************************")