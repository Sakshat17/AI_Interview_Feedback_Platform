# AI-Video-Analysis-Platform
* After the covid pandemic the world has moved to virtual setup. There has been a sudden rise in virtual AI based Interviews. In such interviews the most important skill is the communication of the interviewee. But we noticed there was no such platform available where one could practice and improve on their communication skills for an AI based video interview and get relevant and specific feedback that would point out the shortcomings of the candidate and suggest appropriate constructive feedback.</Br>

* We created a web platform where candidates can practice their communication skills and get personalized feedback on their verbal and behavioral abilities so that they could improve their shortcomings and get to know what their strong points are .</Br>

* The AI video analysis platform is a webapp where candidates can practice for Virtual interviews by recording their audio answers from a list of frequently asked interview questions. We record the audio of the user and our backend processes the audio using a python library called “myprosody”. This library is used to fetch many important aspects of audio like word per minute, pitch variation, filler words, Pauses etc which decide how well the user is communicating. Based on these factors we generate a personalized feedback report on which parameters could be improved.</Br>

# Feature list
* Words Per Minute - Provide user feedback in comparison to optimum level </Br>
* Pitch Variation - Provide user feedback in comparison to optimum level </Br>
* Filler Words - Provide user feedback in comparison to optimum level </Br>
* Spot keyboards </Br>
* Section on website to train a user for an interview - ideal answers for often asked questions and sample interviews </Br>
* Personal feedbacks on interview trials </Br>

# Parameters to judge:
* Pitch variation- Monotonous & Target </Br>
* Words Per Minute(WPM)-> Optimal: 140 -160 words per minute (wpm) </Br>
* Use of filler words - ohh,umm,long pauses etc </Br>

# Some challenges:
* Grammar check </Br>
* Eye contact/tracking in video analysis </Br>
* How to detect long pauses while audio to text conversion </Br>

# Myprosody sample result
Overview: Function **mysptotal(p,c)** </Br>
_mysp=import("my-voice-analysis")_ </Br>
_p="Walkers" # Audio File title_ </Br>
_c=r"C:\Users\Shahab\Desktop\Mysp" # Path to the Audio_File directory_ (Python 3.7) </Br>

**mysp.mysptotal(p,c)** </Br>
* number_ of_syllables 154 </Br>
* number_of_pauses 22 </Br>
* rate_of_speech 3 </Br>
* articulation_rate 5 </Br>
* speaking_duration 31.6 </Br>
* original_duration 49.2 </Br>
* balance 0.6 </Br>
* f0_mean 212.45 </Br>
* f0_std 57.85 </Br>
* f0_median 205.7 </Br>
* f0_min 77 </Br>
* f0_max 414 </Br>
* f0_quantile25 171 </Br>
* f0_quan75 244 </Br>
