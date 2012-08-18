import os
import djcelery


DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJ_ROOT = os.path.dirname(os.path.dirname(__file__))


djcelery.setup_loader()

#BROKER_URL = 'amqp://guest:guest@localhost:5672/'
#redis-server /usr/local/etc/redis.conf

BROKER_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_IMPORTS = ('win8core.tasks.shows')


REDIS_HOST = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': PROJ_ROOT + '/sqlite.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ENV = 'local'
if 'APP_ENV' in os.environ:
    ENV = os.environ['APP_ENV']

if ENV == 'staging':
    import dj_database_url
    DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}


GRAPPELLI_ADMIN_TITLE = 'FX Win8 Admin'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

RESOURCES_URL = '/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bnrd6)4kwizponvth!c+pjrc!+6zdk=*pu8c+2kaq6*0*@lqsj'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'www.processors.global.static_template_vars',
)

ROOT_URLCONF = 'www.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'www.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJ_ROOT + '/www/templates',
)

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'tastypie',
    'djcelery',
    'win8core',
    'gunicorn',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

PROFANITIES_LIST = '420','666','2on1','3rdeye','3rdleg','3rdeye','3rdleg','3some','4twenty','4twenty','60nine','60nine','ass','analannie','analsex','analannie','analsex','anus','assbagger','assblaster','assclown','asscowboy','assfuck','assfucker','asshole','assholes','asshore','assjockey','asskiss','asskisser','assklown','asslick','asslicker','asslover','assman','assmonkey','assmunch','assmuncher','asspacker','asspirate','asspuppies','assranger','asswhore','asswipe','assbagger','assblaster','assclown','asscowboy','assfuck','assfucker','asshole','assholes','asshore','assjockey','asskiss','asskisser','assklown','asslick','asslicker','asslover','assman','assmonkey','assmunch','assmuncher','asspacker','asspirate','asspuppies','assranger','asswhore','asswipe','athletesfoot','athletesfoot','axingtheweasel','bhard','backdoor','backdoorman','backdoor','backdoorman','backseat','badass','badfuck','badfuck','balllicker','ballsack','balllicker','balls','ballsack','banging','barelylegal','barelylegal','barf','barfface','barface','barfface','bastard','bazongas','bazooms','beastality','beastiality','beatoff','beatyourmeat','beatoff','beat-off','beatyourmeat','bisexual','biatch','bigass','bigbitch','bigbitch','bigbutt','bigass','bigbastard','bigbutt','bisexual','bi-sexual','bitch','bitchin','bitchy','biteme','biteme','blackout','blackout','blowjob','blowjob','bm','boner','bong','boobies','boobs','boody','breast','breastjob','breastlover','breastman','breastjob','breastlover','breastman','budweiser','bullcrap','bulldike','bulldyke','bullshit','bullcrap','bulldike','bulldyke','bullshit','bumblefuck','bumblefuck','bumfuck','bunghole','butchbabes','butchdike','butchdyke','butchbabes','butchdike','butchdyke','buttbang','buttfuck','buttfucker','buttfuckers','butthead','buttman','buttplug','buttstain','buttbang','butt-bang','buttface','buttfuck','butt-fuck','buttfucker','butt-fucker','buttfuckers','butt-fuckers','butthead','buttman','buttpirate','buttplug','buttstain','cameltoe','cameltoe','carpetmuncher','carpetmuncher','carruth','cherrypopper','cherrypopper','chickslick','chickslick','clamdigger','clamdiver','clamdigger','clamdiver','clit','clitoris','cock','cockblock','cockblocker','cockcowboy','cockfight','cockknob','cocklicker','cocklover','cocknob','cockqueen','cockrider','cocksmith','cocksucker','cocktail','cocktease','cockblock','cockblocker','cockcowboy','cockfight','cockhead','cockknob','cocklicker','cocklover','cocknob','cockqueen','cockrider','cocksman','cocksman','cocksmith','cocksucer','cocksucker','cocktail','cocktease','cocky','condom','copulate','cornhole','cornhole','crabs','crack','crackpipe','crackwhore','crackpipe','crackwhore','crack-whore','crap','crappy','creamy','crotch','crotchjockey','crotchmonkey','crotchrot','crotchjockey','crotchmonkey','crotchrot','cumbubble','cumfest','cumjockey','cumquat','cumqueen','cumshot','cumbubble','cumfest','cumjockey','cumm','cumming','cumquat','cumqueen','cumshot','cunnilingus','cunt','cuntfuck','cuntfucker','cuntlicker','cuntfuck','cuntfucker','cuntlicker','cybersex','cyberslimer','cybersex','cyberslimer','dahmer','damn','damnit','damnit','datnigga','deapthroat','deaper','deapthroat','deepthroat','deeper','deepthroat','defecate','deposit','devil','dickbrain','dickfart','dickforbrains','dickhead','dicklick','dicklicker','dicklikcer','dickwad','dickweed','dickbrain','dickforbrains','dickhead','dickless','dicklick','dicklicker','dickman','dickwad','dickweed','dike','dildo','dipstick','dipstick','dirtyho','dixiedike','dixiedyke','dixiedike','dixiedyke','dome','doggiestyle','doggiestyle','doggystlye','doggystyle','dome','dong','dope','doubled','doubled','dragqueen','dragqueen','dragqween','dripdick','dripdick','drunk','drunken','dumbass','dumbbitch','dumbfuck','dumbass','dumbbitch','dumbfuck','easyslut','easyslut','eatme','eatpussy','eatballs','eatme','eatpussy','ejaculate','erection','excrement','ftoyota','facefucker','facefucker','faggot','fagot','fairy','fannyfucker','fannyfucker','fart','fastfuck','fastfuck','fatass','fatfuck','fatfucker','fatass','fatfuck','fatfucker','fatso','fellatio','femme','fingerfood','fingerfuck','fingerfucker','fingerfood','fingerfuck','fingerfucker','fistfuck','fistfucker','fistfuck','fistfucker','fisting','flasher','flatulence','flogginthedolphin','fondle','footfuck','footfucker','footlicker','footaction','footfuck','footfucker','footlicker','footstar','foreskin','foreskin','fornicate','four20','fourtwenty','four20','fourtwenty','freakfuck','freakfuck','freakyfucker','freakyfucker','free4all','freeforall','freefuck','free4all','freeforall','freefuck','fuck','fuckbag','fuckbuddy','fuckface','fuckfest','fuckfreak','fuckfriend','fuckhead','fuckher','fuckit','fuckknob','fuckme','fuckmehard','fuckmonkey','fuckoff','fuckpig','fuckthem','fuckwhore','fuckyou','fucka','fuckable','fuckbag','fuckbuddy','fucked','fuckedup','fuckedup','fucker','fuckers','fuckface','fuckfest','fuckfreak','fuckfriend','fuckhead','fuckher','fuckin','fuckina','fuckinnuts','fuckinright','fuckina','fucking','fuckinga','fuckingbitch','fuckingnuts','fuckingbitch','fuckinnuts','fuckinright','fuckit','fuckknob','fuckme','fuckmehard','fuckmonkey','fuckoff','fuckpig','fuckwhore','fuckyou','fudgepakcers','funfuck','funfuck','fuuck','gunit','gangbang','gangbanger','gangbang','gangbanger','gay','gayass','gaymuthafuckinqueer','gaypride','gaymuthafuckinwhore','genital','getiton','getiton','giehn','givehead','givehead','glazeddonut','glazeddonut','gome','gotohell','goddamedmuthafucka','goddamit','goddamn','goddamned','godmanit','goddamit','goddamn','goddamned','goddamnes','goddamnit','goddamnmuthafucker','gonorrehea','gonzagas','gook','gotjesus','got2haveit','gotohell','g-unit','handjob','handjob','hardon','harder','hardon','harem','hehateme','headfuck','headlights','headfuck','headlights','hehateme','hellno','hellyes','hellno','hellyes','henhouse','henhouse','herpes','hersheyhiway','hersheyhighway','hersheyhiway','hershyhighway','homo','hobo','holestuffer','holestuffer','homo','homobangers','homosexual','homobangers','homosexual','honkers','honkey','hooker','hookers','hooters','horney','horny','horseshit','hosejob','hosejob','hoser','hostage','hotdamn','hotpussy','hottotrot','hot2trot','hotdamn','hotpussy','hottotrot','hussy','hustler','ilovebeer','iluvbeer','idtent','id10t','idiot','idoit','intheass','inthebuff','ingin','insest','intercourse','interracial','intercourse','interracial','intheass','inthebuff','jacktheripper','jackass','jackoff','jacktheripper','japcrap','japcrap','jerkoff','jerkoff','jesuschirst','jesuschrist','jism','jiz','jizjuice','jizim','jizjuice','jizz','jizzim','joint','juggalo','jugs','kmart','killer','killing','kissass','kissass','kkk','kmart','knockers','koon','kotex','krap','krappy','kumbubble','kumquat','kumbubble','kumbullbe','kumquat','kunt','kyjelly','lactate','ladyboog','laid','lapdance','lapdance','lesbain','lesbayn','lesbian','lesbin','lesbo','lezbe','lezbefriends','lezbe','lezbefriends','lezbo','lezz','lezzo','lickme','licker','lickme','limpdick','limpdick','limy','livesex','livesex','loadedgun','loadedgun','lolita','looser','lotion','lovebone','lovegoo','lovegun','lovejuice','lovemuscle','lovepistol','loverocket','lovebone','lovegoo','lovegun','lovejuice','lovemuscle','lovepistol','loverocket','lowlife','lowlife','lubejob','lubejob','luckycameltoe','luckycammeltoe','magicwand','magicwand','mams','manhater','manpaste','manhater','manpaste','maryjane','maryjane','mastabate','mastabater','masterblaster','masterbate','masterblaster','mastrabator','mattressprincess','mattressprincess','meatbeatter','meatbeatter','molest','molester','molestor','moneyshot','moneyshot','motherfucker','motherlovebone','motherfuck','motherfucker','motherlovebone','muffdive','muffdiver','mufflicker','muffdive','muffdiver','muffindiver','muffindiver','mufflikcer','murder','muthafucker','naked','nastybitch','nastyho','nastyslut','nastywhore','nastybitch','nastyho','nastyslut','nastywhore','neondeon','niger','nigga','nigger','nipple','nipplering','nipplering','nittit','nittit','nofuckingway','nosex','nofuckingway','nookie','nooner','nude','nutfucker','nutfucker','oicu812','ontherag','ontherag','orgasm','orgy','ou812','pimp','pearlnecklace','pearlnecklace','pecker','peepshow','peepshow','peepshpw','penetration','penis','penthouse','period','phque','pimp','pimpsimp','pimped','pimper','pimpjuic','pimpjuice','pimpsimp','piss','pisshead','pissed','pisser','pisshead','playgirl','pocketpool','pocketpool','polack','poontang','poontang','poop','pooper','poorwhitetrash','poorwhitetrash','popimp','porchmonkey','porchmonkey','porn','pornflick','pornking','pornprincess','pornflick','pornking','porno','pornprincess','premature','prick','prickhead','prickhead','primetime','prostitute','pubic','pubiclice','pubiclice','pudboy','pudboy','pudd','puddboy','puddboy','puntang','puntang','purinaprincess','purinapricness','pussy','pussycat','pussyeater','pussyfucker','pussylicker','pussylips','pussylover','pussypounder','pussycat','pussyeater','pussyfucker','pussylicker','pussylips','pussylover','pussypounder','puttpirate','pwt','queef','queer','quickie','raecarruth','rape','rapist','rearend','rearentry','rearend','rearentry','rectum','redlight','redlight','reefer','rentafuck','rentafuck','retard','retarded','ribbed','rimjob','rimjob','robber','sandm','samckdaddy','sandm','satan','schlong','screw','screwyou','screwyou','scrotum','semen','sexfarm','sexhound','sexhouse','sexkitten','sexpot','sexslave','sextogo','sextoy','sextoys','sexwhore','sexfarm','sexhound','sexhouse','sexkitten','sexpot','sexslave','sextogo','sextoy','sextoys','sexual','sexwhore','sexy','sexybiatch','sexybitch','sexymoma','sexyslim','sexymoma','sexy-slim','shag','shaggin','shagging','shawtypimp','shit','shitdick','shiteater','shitface','shitforbrains','shitfuck','shitfucker','shithappens','shithead','shitoutofluck','shitstain','shit4brains','shitdick','shiteater','shitface','shitforbrains','shitfuck','shitfucker','shithapens','shithappens','shithead','shitoutofluck','shits','shitstain','shitter','shitting','shitty','shortfuck','shortfuck','showtime','sixsixsix','sixsixsix','sixty9','sixtynine','sixty9','sixtynine','skank','skankbitch','skankfuck','skankwhore','skankbitch','skankfuck','skankwhore','skankybitch','skankywhore','skankybitch','skankywhore','skinflute','skinflute','skum','skumbag','skumbag','slant','slanteye','slanteye','slave','slavedriver','slavedriver','sleezebag','sleezeball','sleezebag','sleezeball','slideitin','slideitin','slime','slimeball','slimebucket','slimeball','slimebucket','slut','slutwear','slutwhore','sluts','slutt','slutting','slutty','slutwear','slutwhore','smackdaddy','smackthemonkey','smackthemonkey','smagma','smartass','snatch','snatchpatch','snatchpatch','sniper','sodomite','sodomy','sonofabitch','sonofabitch','sonofbitch','spankthemonkey','spankthemonkey','sperm','spermbag','spermhearder','spermherder','spermacide','spermbag','spermhearder','spermherder','spick','spitter','splittail','splittial','splittail','stagg','strapon','strapon','stringer','stripclub','stripclub','stroke','stroking','stupid','stupidfuck','stupidfucker','stupidfuck','stupidfucker','suck','suckdick','suckme','suckmyass','suckmydick','suckmytit','suckoff','suckdick','sucker','suckme','suckmyass','suckmydick','suckmytit','suckoff','suicide','swallow','swallower','swalow','sweetness','swigndixx','swingdixx','swingindixx','swingingdicks','syphilis','tampon','tang','testicle','testicles','thirdeye','thirdleg','thirdeye','thirdleg','threesome','threesome','titbitnipply','titfuck','titfucker','titfuckin','titjob','titlicker','titlover','titbitnipply','titfuck','titfucker','titfuckin','titjob','titlicker','titlover','tits','titties','titty','toilet','toiletbowl','tongethruster','tongue','tonguethruster','tonguetramp','tonguethrust','tonguetramp','toungthruster','toungeballer','toungethrust','trailertrash','trailertrash','tramp','trisexual','triplex','triplex','trisexual','trojan','trots','tunneloflove','tunneloflove','turd','twobitwhore','twoonone','twobitwhore','unfuckable','uptheass','upthebutt','upskirt','uptheass','upthebutt','urinate','urine','uterus','vagina','vaginal','vd','vibrater','vibrator','virgin','virginbreaker','virginbreaker','vulva','waysted','weenie','wetspot','wetspot','whacker','whiskeydick','whiskeydick','whiskydick','whiskydick','whitetrash','whitetrash','whore','whorefucker','whorehouse','whorefucker','whorehouse','wigger','williewanker','williewanker','wuutang','xxx','yellowman','yellowman','fag','fucken','fuckin','dick'
EXCLUDED_CLOUD_LIST = ('the','to','i','for','and', 'a', 'in', 'of', 'on', 'is', 'you', 'my', 'the', '', 'be', 'so', 'this', 'all', 'it')

