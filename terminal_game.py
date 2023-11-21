print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("Welcome to this novelty DND adventure!\n\n"+"Prepare yourself for a world of magic, science, and...\n\n"+"School?\n")
print("It starts now!")
print("Once upon a time, a soon-to-be master degree graduate got employed as a...\n\n"+"Oh! The paper's a little burnt here... we'll have to improvise!\n")
#I know I could have done in one print, but I was honestly kind of wanting to do it like this and see where it went :P
job_name = ""

def job():
    number_chosen_for_job = input("What did the student get employed as?\n"+"1 - Pharmacist\n2 - Researcher\n3 - Business Analyst\n")
    job_name = ""
    if number_chosen_for_job == "1":
        print("Hmm hmm, yes yes, a Pharmacist, it makes sense!\n")
        job_name = "Pharmacist"
        return congrats(job_name)

    elif number_chosen_for_job == "2":
        print("Hmm hmm, oh yes, a Researcher? Did not imagine this but alright...\n")
        job_name = "Researcher"
        return congrats(job_name)
    
    elif number_chosen_for_job == "3":
        print("Hmm hmm, oh yes, a Business Analyst? Haha! What a sh-- Hm, congrats!\n")
        job_name = "Business Analyst"
        return congrats(job_name)

    else:
        print("BUG BUG RECONFIGURATION NEEDED...\nONGOING\nRECONFIGURATION DONE!\n\nThe graduate is a Conjoint administratif at ORBICOM. Really? Oh well, guess you can't help but have one those communication people once in a while...\n")
        job_name = "Conjoint Administratif"
        return congrats(job_name)

def congrats(job_name):
    print("Where was I? Oh yes, the burnt paper... Using technology beyond the realm of comprehension of common mortals, we now have an answer!\n")
    print(f"Our soon-to-be graduate is a "+job_name+"!"+" Well, since it feels like a grand reveal of some sort, congratulations are in order! CONGRATS on your employment!\n\nI hope we can learn more about his future in a near future...\n")

job()