#This script performs inerations on an account.
#You need to supply your login details 
#function calls are intuitive


from instapy import InstaPy
from instapy.util import smart_run

insta_username = ''
insta_password = ''

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
		  disable_image_load=True,
                  multi_logs=True)


with smart_run(session):
    
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=2000,
                                    max_following=3000,
                                    min_followers=30,
                                    min_following=30)
    session.set_user_interact(amount=20, randomize=True, percentage=100,
                              media='Photo')
    session.set_do_like(enabled=True, percentage=100)
    session.set_do_comment(enabled=True, percentage=50)
    session.set_comments(
        ['Nice shot! @{}', 'Wow, simply Amazing! @{}', '@{} Love it!',
         '@{} :heart::heart:', "@{} I want  🤣🤣🤣🙊🙊🙊",
         "@{} 💦💦🔥💦💦🔥💦💦🔥",
         '@{}:revolving_hearts::revolving_hearts:', '@{}:fire::fire::fire:'],
        media='Photo')
    session.follow_likers(['smash9ja' , 'blackmodelslay','tundeednut'], photos_grab_amount = 30, 
                          follow_likers_per_photo = 50, randomize=True, sleep_delay=0.1, interact=True)
    
    
    # follow activity
    ammount_number = 500
    session.follow_user_followers(['maraji_', 'tundeednut'],
                                  amount=ammount_number, randomize=True,
                                  interact=True, sleep_delay=1)

    # unfollow activity
    session.unfollow_users(amount=400, nonFollowers=True, style="RANDOM",
                           unfollow_after= 1, sleep_delay=2)

    
    tagsss='''#brodashagi 
		#asoebi 
		#30bgang 
		#basketmouth 
		#madeinlagos 
		#madeinnigeria 
		#prettylittlething
		#soweto 
		#melaninqueen 
		#melaninpoppin 
		#drippingwet #makeuponpoint#photooftheday#portraitphotography#picoftheday#seethrough#wet#wetshirt#longhair#freethenips#nobraclub#thick#thickthighssavelives#drippingwet#modelling#photoshoot#dewy#glowy#goldenhour#instagood#positivevibes#fit#fitfam
		'''    
    
    tagsss  = tagsss.split('#')
    
    
    
    
    
    
