# phonemes.py
# List of all sounds used

VOWEL_U 	= 0  # cup, luck        अ
VOWEL_A 	= 1  # arm, father      आ
VOWEL_AE 	= 2  # cat, black       ए
VOWEL_E 	= 3  # met, bed         ऐ
VOWEL_EE	= 4  # away, cinema
VOWEL_UU	= 5  # turn, learn      
VOWEL_I		= 6  # hit, sitting     इ
VOWEL_II	= 7  # see, heat        ई
VOWEL_O		= 8  # hot, rock        
VOWEL_CA	= 9  # call, four       औ
VOWEL_PU	= 10 # put, could       उ
VOWEL_OO	= 11 # blue, food       ऊ 
VOWEL_AI	= 12 # five, eye
VOWEL_AU	= 13 # now, out
VOWEL_EI	= 14 # say, eight
VOWEL_OH	= 15 # go, home         ओ
VOWEL_OI	= 16 # boy, join
VOWEL_ER	= 17 # where, air
VOWEL_IE 	= 18 # near, here
VOWEL_UE	= 19 # pure, tourist        य

CONS_B		= 20 # bad, lab             ब
CONS_D		= 21 # did, lady            ड  ढ
CONS_F		= 22 # find, if             फ           
CONS_G		= 23 # give, flag           ग   घ
CONS_H		= 24 # how, hello           ह
CONS_Y		= 25 # yes, yellow          य
CONS_K		= 26 # cat, black           ख क
CONS_L		= 27 # leg, litte           ल

CONS_M		= 28 # man, lemon           म
# todo
CONS_N		= 29 # no, ten              न  ञ  ण
CONS_NG		= 30 # sing, finger         ं
CONS_P		= 31 # pet, map             प भ
CONS_R		= 32 # red, try             र
CONS_S 		= 33 # sun, miss            स
CONS_SH		= 34 # she, crash           श ष
CONS_T		= 35 # tea, getting         ट
CONS_CH		= 36 # check, church        च
CONS_TH		= 37 # think, both          थ  ठ ध
CONS_TH2	= 38 # this, mother         द 
CONS_V		= 39 # voice, five          व
CONS_W		= 40 # wet, window          
CONS_Z		= 41 # zoo, lazy            ज़
CONS_JJ		= 42 # pleasure, vision     छ झ
CONS_J 		= 43 # just, large          ज

PUNC_PERIOD 	= 44 # period (long pause) 0.5
PUNC_COMMA 		= 44 # comma (short pause) 0.3
PUNC_QUESTION 	= 44 # question            0.5
PUNC_EXCLAIM 	= 44 # exclamation         0.5
# to do
PAUSE_WORD		= 44 # very short pause    0.2