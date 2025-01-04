from pvq_scoring import *
from bfi_scoring import *
from gpt_structure import pvq_summary_gpt4, bfi_summary_gpt4

def future_profile_generate(main_test):
  lib_file = './data/prompt_template/profile_after_3.txt'
  f = open(lib_file, "r")
  profile_after_3_template = f.read()
  f.close()
  profile_after_3 = profile_after_3_template.format(
    AGE = main_test.iloc[0,77],
    JOB = main_test.iloc[0,78],
    LIV = main_test.iloc[0,79],
    APPEAR = main_test.iloc[0,80],
    PERSONALITY = main_test.iloc[0,81],
    BEHAVIOR = main_test.iloc[0,82],
    FAM = main_test.iloc[0,83],
    FRIEND = main_test.iloc[0,84],
    WORK = main_test.iloc[0,85],
  )
  return profile_after_3

def demo_generate(main_test):
  lib_file = './data/prompt_template/demo.txt'
  f = open(lib_file, "r")
  demo_template = f.read()
  f.close()
  demo = demo_template.format(
    AGE = 2024 - main_test.iloc[0,3],
    SEX = main_test.iloc[0,4],
    RESIDENCE = main_test.iloc[0,5],
    EDU = main_test.iloc[0,6],
    SEMESTER = "- Current Semesters Enrolled: "+ str(main_test.iloc[0,7]) if main_test.iloc[0,6] != '대학 졸업' else '',
    GRADYEAR = "- Years Since Graduation: " + str(main_test.iloc[0,8]) if main_test.iloc[0,6] == '대학 졸업' else '',
    MAJOR = main_test.iloc[0,9],
    PER_INC = main_test.iloc[0,10],
    SAT_INC = main_test.iloc[0,11],
    PER_CLASS = main_test.iloc[0,12],
    LIV = main_test.iloc[0,13],
    SIB = main_test.iloc[0,14],
    D_EDU = main_test.iloc[0,15],
    M_EDU = main_test.iloc[0,16],
    D_JOB = main_test.iloc[0,17],
    M_JOB = main_test.iloc[0,18]
  )
  return demo

def bfi_generate(main_test):
  bfi_intro = '''

**[Big 5 Personality Traits in 2024]**
The following section presents an overview of the person's personality within five key domains, showcasing their traits spectrum and the extent of their qualities in each area. Each domain comprises several facets that provide deeper insights into their unique personality traits.

'''
  new_column_names = [f'D1PB-{i}' for i in range(1, 31)]
  bfi_raw = main_test.iloc[:, 40:70]
  bfi_raw.columns = new_column_names
  bfi_1st = bfi_calculate_scores(bfi_raw)
  bfi_summary = bfi_summary_gpt4(bfi_1st)
  bfi_summary_final = bfi_intro + bfi_summary
  return bfi_summary_final

def pvq_generate(main_test):
  pvq_intro = '''

**[Life-guiding Principles in 2024]**
The information provided below is the values that reflect the relative importance this person places on different aspects of life, guiding their decisions, actions, and perspectives. These values are fundamental components of their personality and play a crucial role in shaping who this person is.

'''
  new_column_names = [f'D2LP-{i}' for i in range(1, 22)]
  pvq_raw = main_test.iloc[:, 19:40]
  pvq_raw.columns = new_column_names
  pvq_1st = generate_pvq_prompt(pvq_raw)
  pvq_summary = pvq_summary_gpt4(pvq_1st)
  pvq_summary_final = pvq_intro + pvq_summary
  return pvq_summary_final

def love_hate_generate(main_test):
  lib_file = './data/prompt_template/love_hate.txt'
  f = open(lib_file, "r")
  love_hate_template = f.read()
  f.close()
  love_hate = love_hate_template.format(
    LOVE1 = main_test.iloc[0,70],
    LOVE2 = main_test.iloc[0,71],
    LOVE3 = main_test.iloc[0,72],
    HATE1 = main_test.iloc[0,73],
    HATE2 = main_test.iloc[0,74],
    HATE3 = main_test.iloc[0,75],
  )
  return love_hate

def score_to_level7(score):
    if score <= 1/7:
        return 1
    elif score <= 2/7:
        return 2
    elif score <= 3/7:
        return 3
    elif score <= 4/7:
        return 4
    elif score <= 5/7:
        return 5
    elif score <= 6/7:
        return 6
    else:
        return 7
    
def score_to_level5(score):
    if score <= 1/5:
        return 1
    elif score <= 2/5:
        return 2
    elif score <= 3/5:
        return 3
    elif score <= 4/5:
        return 4
    else:
        return 5
    
descriptions = {
        "C2": [
            "I almost never engage in career-related exploration.",
            "I occasionally engage in career-related exploration.",
            "I sometimes engage in career-related exploration.",
            "I frequently engage in career-related exploration.",
            "I very often engage in career-related exploration."
        ],
        "C3": [
            "I cannot imagine my future self at all.",
            "I have difficulty imagining my future self.",
            "I somewhat struggle to imagine my future self.",
            "I am neutral about imagining my future self.",
            "I somewhat easily imagine my future self.",
            "I easily imagine my future self.",
            "I very easily imagine my future self."
        ],
        "C5": [
            "I have no clear career direction.",
            "I do not have a clear career direction.",
            "I somewhat lack a clear career direction.",
            "I am neutral about having a clear career direction.",
            "I somewhat have a clear career direction.",
            "I have a clear career direction.",
            "I have a very clear career direction."
        ],
        "C6": [
            "I do not plan my career well at all.",
            "I do not plan my career well.",
            "I somewhat struggle with career planning.",
            "I am neutral about planning my career well.",
            "I somewhat plan my career well.",
            "I plan my career well.",
            "I plan my career very well."
        ],
        "C7": [
            "I have no career-related stress.",
            "I have little career-related stress.",
            "I somewhat do not have much career-related stress.",
            "I am neutral about having career-related stress.",
            "I somewhat have career-related stress.",
            "I have career-related stress.",
            "I have a lot of career-related stress."
        ],
        "C9": [
            "I have no confidence in achieving difficult tasks.",
            "I have little confidence in achieving difficult tasks.",
            "I somewhat lack confidence in achieving difficult tasks.",
            "I am neutral about my confidence in achieving difficult tasks.",
            "I somewhat have confidence in achieving difficult tasks.",
            "I have confidence in achieving difficult tasks.",
            "I am very confident in achieving difficult tasks."
        ],
        "C10": [
            "I do not feel my life is meaningful or valuable at all.",
            "I do not feel my life is meaningful or valuable.",
            "I somewhat lack a sense of meaning or value in my life.",
            "I am neutral about the meaning and value of my life.",
            "I somewhat feel my life is meaningful and valuable.",
            "I feel my life is meaningful and valuable.",
            "I feel my life is very meaningful and valuable."
        ],
        "C11": [
            "I have no clarity about my career goals.",
            "I do not have clarity about my career goals.",
            "I somewhat lack clarity about my career goals.",
            "I am neutral about the clarity of my career goals.",
            "I somewhat have clarity about my career goals.",
            "I have clarity about my career goals.",
            "I have very clear career goals."
        ],
        "C12": [
            "I receive no support from my parents regarding my career.",
            "I receive little support from my parents regarding my career.",
            "I somewhat lack support from my parents regarding my career.",
            "I am neutral about the support from my parents regarding my career.",
            "I somewhat receive support from my parents regarding my career.",
            "I receive support from my parents regarding my career.",
            "I receive a lot of support from my parents regarding my career."
        ]
    }

def career_status_generate(pre_test):
  c2_level = score_to_level5(float(pre_test['c2'].values[0])/5)
  c3_level = score_to_level7(float(pre_test['c3'].values[0])/7)
  c5_level = score_to_level7(float(pre_test['c5'].values[0])/7)
  c6_level = score_to_level7(float(pre_test['c6'].values[0])/7)
  c7_level = score_to_level7(float(pre_test['c7'].values[0])/7)
  lib_file = './data/prompt_template/career_status.txt'
  f = open(lib_file, "r")
  career_status_template = f.read()
  f.close()
  career_status = career_status_template.format(
    EXPL = descriptions["C2"][c2_level - 1], #c2
    EASE = descriptions["C3"][c3_level - 1], #c3
    EST = descriptions["C5"][c5_level - 1], #c5
    PLAN = descriptions["C6"][c6_level - 1], #c6
    STRESS = descriptions["C7"][c7_level - 1], #c7
  )
  return career_status

def career_insight_generate(pre_test):
  c9_level = score_to_level7(float(pre_test['c9'].values[0])/7)
  c10_level = score_to_level7(float(pre_test['c10'].values[0])/7)
  c11_level = score_to_level7(float(pre_test['목표명확성'].values[0])/7)
  c12_level = score_to_level7(float(pre_test['부모님 진로관심'].values[0])/7)
  lib_file = './data/prompt_template/career_insight.txt'
  f = open(lib_file, "r")
  career_insight_template = f.read()
  f.close()
  career_insight = career_insight_template.format(
    EFFICACY = descriptions["C9"][c9_level - 1], #c9
    WELL = descriptions["C10"][c10_level - 1], #c10
    CLARITY = descriptions["C11"][c11_level - 1], #c11
    SUPPORT = descriptions["C12"][c12_level - 1], #c12
  )
  return career_insight