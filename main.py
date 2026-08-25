print('='*60)
print('PROJECT VALUE ANALYZER')
print('='*60)

#INPUTS
project_name=input('Project Name:').strip()

description=input('\nProject Description:').lower()

technologies=input('\nTechnologies Used (comma separated):').lower()

features = input('\nKey Features (comma separated):').lower()

#Convert to lists
tech_list=[t.strip() for t in technologies.split(',')]
feature_list=[f.strip() for f in features.split(',')]

# -----------------------------------
# COMPLEXITY SCORE
# -----------------------------------

feature_count=len(feature_list)

if feature_count<=2:
    complexity=30
elif feature_count<=4:
    complexity=60
elif feature_count<=6:
    complexity=80
else:
    complexity=100

# -----------------------------------
# TECHNOLOGY SCORE
# -----------------------------------

technology_score=0

tech_points={
    'python':20,
    'functions':10,
    'lists':10,
    'dictionaries':15,
    'file handling':15,
    'oop':20,
    'exception handling':10,
    'modules':10,
    'classes':15,
    'strings':10
}

for tech in tech_list:
    if tech in tech_points:
        technology_score+=tech_points[tech]

technology_score=min(technology_score, 100)

# -----------------------------------
# BUSINESS VALUE SCORE
# -----------------------------------

business_keywords=[
    'sales',
    'customer',
    'feedback',
    'finance',
    'career',
    'portfolio',
    'tracking',
    'analytics',
    'business',
    'employee'
]

business_value=20

combined_text=description+' '+features

for word in business_keywords:
    if word in combined_text:
        business_value+=10

business_value=min(business_value,100)

# -----------------------------------
# INNOVATION SCORE
# -----------------------------------

innovation_keywords=[
    'recommendation',
    'scoring',
    'evaluation',
    'analysis',
    'prediction',
    'automation',
    'intelligent',
    'insight',
    'ranking',
    'comparison'
]

innovation=20

for word in innovation_keywords:
    if word in combined_text:
        innovation+=10

innovation=min(innovation,100)

# -----------------------------------
# RESUME IMPACT
# -----------------------------------

resume_impact=(complexity+technology_score+business_value+innovation)//4

# -----------------------------------
# INDUSTRY RELEVANCE
# -----------------------------------

industry_keywords=[
    'analytics',
    'business',
    'customer',
    'career',
    'finance',
    'portfolio',
    'report',
    'dashboard',
    'tracking'
]

industry_relevance=20

for word in industry_keywords:
    if word in combined_text:
        industry_relevance+=10

industry_relevance=min(industry_relevance,100)

# -----------------------------------
# UNIQUENESS SCORE
# -----------------------------------

common_projects = [
    'expense tracker',
    'student management system',
    'library management system',
    'movie ticket booking system',
    'calculator',
    'budget manager',
    'bank management system',
    'typing speed tester'
]

if project_name.lower() in common_projects:
    uniqueness=30
else:
    uniqueness=100

# -----------------------------------
# OVERALL SCORE
# -----------------------------------

overall_score=(complexity+technology_score+business_value+innovation+resume_impact+industry_relevance+uniqueness)//7

# -----------------------------------
# RATING
# -----------------------------------

if overall_score>=85:
    rating='Excellent'
elif overall_score>=70:
    rating='Very Good'
elif overall_score>=55:
    rating='Good'
else:
    rating='Needs Improvement'

# -----------------------------------
# REPORT
# -----------------------------------

print('\n'+'='*60)
print('PROJECT ANALYSIS REPORT')
print('='*60)

print(f'Project Name       : {project_name}')
print(f'Complexity         : {complexity}/100')
print(f'Technology         : {technology_score}/100')
print(f'Business Value     : {business_value}/100')
print(f'Innovation         : {innovation}/100')
print(f'Resume Impact      : {resume_impact}/100')
print(f'Industry Relevance : {industry_relevance}/100')
print(f'Uniqueness         : {uniqueness}/100')

print('-'*60)
print(f'Overall Score      : {overall_score}/100')
print(f'Rating             : {rating}')
print('-'*60)

# -----------------------------------
# RECOMMENDATIONS
# -----------------------------------

print('\nRecommendations:')

if complexity<70:
    print('•Add more advanced features.')

if technology_score < 70:
    print('• Use OOP, file handling, and exception handling.')

if innovation<70:
    print('• Add unique modules such as recommendation or scoring.')

if business_value<70:
    print('• Improve the real-world business applicability.')

if industry_relevance<70:
    print('• Align the project with current industry needs.')

if uniqueness==100:
    print('• Project appears unique within the repository.')

print('\nAnalysis Completed Successfully!)
print('='*60)
