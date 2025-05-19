from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math

four_letter_words = [
    "ABLE", "ACID", "AGED", "ALSO", "AREA", "ARMY", "AWAY", "BABY", "BACK", "BALL",
    "BAND", "BANK", "BASE", "BATH", "BEAR", "BEAT", "BEEF", "BEEN", "BEER", "BELL",
    "BELT", "BEST", "BILL", "BIRD", "BLOW", "BLUE", "BOAT", "BODY", "BOMB", "BOND",
    "BONE", "BOOK", "BOOM", "BORN", "BOSS", "BOTH", "BOWL", "BULK", "BURN", "BUSH",
    "BUSY", "CALL", "CALM", "CAME", "CAMP", "CARD", "CARE", "CASE", "CASH", "CAST",
    "CELL", "CHAT", "CHIP", "CITY", "CLUB", "COAL", "COAT", "CODE", "COLD", "COME",
    "COOK", "COOL", "COPE", "COPY", "CORE", "COST", "CREW", "CROP", "DARK", "DATA",
    "DATE", "DAWN", "DAYS", "DEAD", "DEAL", "DEAN", "DEAR", "DEBT", "DEEP", "DESK",
    "DIAL", "DICK", "DIET", "DISC", "DISK", "DOOR", "DOSE", "DOWN", "DRAW", "DREW",
    "DROP", "DRUG", "DUCK", "DUST", "DUTY", "EACH", "EARN", "EASE", "EAST", "EASY",
    "EDGE", "ELSE", "EVEN", "EVER", "EXIT", "FACE", "FACT", "FAIR", "FALL", "FARM",
    "FAST", "FATE", "FEAR", "FEED", "FEEL", "FEET", "FELL", "FELT", "FILE", "FILL",
    "FILM", "FIND", "FINE", "FIRE", "FIRM", "FISH", "FIVE", "FLAT", "FLOW", "FOOD",
    "FOOT", "FORD", "FORM", "FORT", "FOUR", "FREE", "FROM", "FUEL", "FULL", "FUND",
    "GAIN", "GAME", "GATE", "GAVE", "GEAR", "GENE", "GIFT", "GIRL", "GIVE", "GLAD",
    "GOAL", "GOES", "GOLD", "GOLF", "GONE", "GOOD", "GRAY", "GREAT", "GREW", "GREY",
    "GROW", "GULF", "HAIR", "HALF", "HALL", "HAND", "HANG", "HARD", "HATE", "HAVE",
    "HEAD", "HEAR", "HEAT", "HELD", "HELL", "HELP", "HERB", "HERE", "HERO", "HIGH",
    "HILL", "HIRE", "HOLD", "HOLE", "HOLY", "HOME", "HOPE", "HOST", "HOUR", "HUGE",
    "HUNG", "HUNT", "HURT", "IDEA", "INCH", "INTO", "IRON", "ITEM", "JACK", "JAIL",
    "JOIN", "JUMP", "JURY", "JUST", "KEPT", "KICK", "KILL", "KIND", "KING", "KNEE",
    "KNEW", "KNOW", "LACK", "LADY", "LAKE", "LAND", "LANE", "LAST", "LATE", "LEAD",
    "LEFT", "LEND", "LENS", "LESS", "LIFE", "LIFT", "LIKE", "LINE", "LINK", "LIST",
    "LIVE", "LOAD", "LOAN", "LOCK", "LOGO", "LONG", "LOOK", "LOST", "LOVE", "LUCK",
    "MADE", "MAIL", "MAIN", "MAKE", "MALE", "MANY", "MARK", "MASS", "MATE", "MAYO",
    "MEAL", "MEAN", "MEAT", "MEET", "MELT", "MENU", "MILE", "MILK", "MIND", "MINE",
    "MISS", "MIXT", "MOOD", "MOON", "MORE", "MOST", "MOVE", "MUCH", "MUST", "NAME",
    "NAVY", "NEAR", "NECK", "NEED", "NEWS", "NEXT", "NICE", "NICK", "NINE", "NONE",
    "NOSE", "NOTE", "OKAY", "ONCE", "ONLY", "OPEN", "ORAL", "OVER", "PACE", "PACK",
    "PAGE", "PAID", "PAIN", "PAIR", "PALM", "PARK", "PART", "PASS", "PAST", "PATH",
    "PEAK", "PICK", "PINK", "PIPE", "PLAN", "PLAY", "PLOT", "PLUG", "PLUS", "POLL",
    "POOL", "POOR", "PORT", "POST", "PULL", "PUMP", "PURE", "PUSH", "RACE", "RAIL",
    "RAIN", "RANK", "RAPE", "RATE", "READ", "REAL", "REAR", "RELY", "RENT", "REST",
    "RICE", "RICH", "RIDE", "RING", "RISE", "RISK", "ROAD", "ROCK", "ROLE", "ROLL",
    "ROOF", "ROOM", "ROOT", "ROSE", "RULE", "RUSH", "SAFE", "SAID", "SAIL", "SALE",
    "SALT", "SAME", "SAND", "SAVE", "SEAT", "SEED", "SEEK", "SEEM", "SEEN", "SELF",
    "SELL", "SEND", "SENT", "SEPT", "SHIP", "SHOP", "SHOT", "SHOW", "SHUT", "SICK",
    "SIDE", "SIGN", "SITE", "SIZE", "SKIN", "SLIP", "SLOW", "SNAP", "SNOW", "SOIL",
    "SOLD", "SOLE", "SOME", "SONG", "SOON", "SORT", "SOUL", "SPOT", "STAR", "STAY",
    "STEP", "STOP", "SUCH", "SUIT", "SURE", "TAKE", "TALE", "TALK", "TALL", "TANK",
    "TASK", "TEAM", "TEAR", "TECH", "TELL", "TEND", "TERM", "TEST", "TEXT", "THAN",
    "THAT", "THEM", "THEN", "THEY", "THIN", "THIS", "THUS", "TIDE", "TILL", "TIME",
    "TINY", "TOLD", "TOLL", "TONE", "TONY", "TOOK", "TOOL", "TOUR", "TOWN", "TRIP",
    "TRUE", "TUNE", "TURN", "TWIN", "TYPE", "UNIT", "UPON", "USED", "USER", "VARY",
    "VAST", "VERY", "VIA", "VIEW", "VOTE", "WAGE", "WAIT", "WAKE", "WALK", "WALL",
    "WANT", "WARD", "WARM", "WASH", "WAVE", "WAYS", "WEAK", "WEAR", "WEEK", "WELL",
    "WENT", "WEST", "WHAT", "WHEN", "WHOM", "WIDE", "WIFE", "WILD", "WILL", "WIND",
    "WINE", "WING", "WIRE", "WISE", "WISH", "WITH", "WOOD", "WORD", "WORK", "YARD",
    "YEAH", "YEAR", "YOUR", "ZERO"
]

word_test = random.choice(four_letter_words)

image = Image.new('RGB', (711, 200), 'white')

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("./abb.ttf", 200)

draw.text((0, 0), word_test, fill='black', font=font)

# Apply ripple effect to the text image
def ripple_effect(img, amplitude=4, wavelength=16):
    width, height = img.size
    new_img = Image.new('RGB', (width, height), 'white')
    src_pixels = img.load()
    dst_pixels = new_img.load()
    for y in range(height):
        offset = int(amplitude * math.sin(2 * math.pi * y / wavelength))
        for x in range(width):
            new_x = x + offset
            if 0 <= new_x < width:
                dst_pixels[x, y] = src_pixels[new_x, y]
            else:
                dst_pixels[x, y] = (255, 255, 255)
    return new_img

# Apply a ripple effect
rippled = ripple_effect(image, amplitude=13, wavelength=9)

# Optionally, apply a blur for extra effect
rippled = rippled.filter(ImageFilter.GaussianBlur(radius=1))

# Save the distorted image
rippled.save('./m_distorted.png')

image.save('./m.png')

total_frames = 10
frame_random_percent = 56
duration_interval = 20

with Image.open("./m_distorted.png") as img:
    global original_pixels 
    original_pixels = img.load()

stimg = Image.new('RGB', (711, 200), 'white')
stimg.save("./stimg.png")
with Image.open("./stimg.png") as img:
    global random_pixels
    random_pixels = img.load()
    
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            random_pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 


    img.save("./stimg.png")

for a in range(total_frames):
    with Image.open("./stimg.png") as img:
        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if original_pixels [i, j] != (0, 0, 0) or random.randint(1, 100) > frame_random_percent:
                    pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                else:
                    pixels[i, j] = random_pixels[i, j]

        img.save(f"./m{a}.png")

# Generate GIF from the 20 PNGs
frames = []
for a in range(total_frames):
    frame = Image.open(f"./m{a}.png")
    frames.append(frame)

# Save as GIF
frames[0].save(
    "./animated.gif",
    save_all=True,
    append_images=frames[1:],
    duration=duration_interval,   # duration per frame in ms
    loop=0
)

print("Captcha generated successfully!")

input()

print(word_test)