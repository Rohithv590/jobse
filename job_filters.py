TARGET_ROLES = [
    "intern",
    "internship",
    "associate",
    "graduate",
    "trainee",
    "new grad",
    "campus"
]

SKILLS = [
    "java",
    "node.js",
    "express",
    "mysql",
    "docker",
    "git",
    "flutter",
    "python"
]

REJECT_KEYWORDS = [
    "training fee",
    "registration fee",
    "investment",
    "crypto",
    "forex",
    "mlm",
    "data entry"
]

EXPERIENCE_REJECT = [
    "senior",
    "staff",
    "principal",
    "lead",
    "manager",
    "director",
    "architect",
    "8+",
    "7+",
    "6+",
    "5+",
    "4+",
    "3+",
    "yoe"
]


def score_job(job):
    score = 0

    role = job.get("role", "").lower()
    requirements = job.get("requirements", "").lower()
    location = job.get("location", "").lower()
    source = job.get("source", "").lower()

    # Reject senior jobs
    for word in EXPERIENCE_REJECT:
        if word in role:
            return 0

    # Fresher keywords
    for keyword in TARGET_ROLES:
        if keyword in role:
            score += 40
            break

    # Skill matching
    for skill in SKILLS:
        if skill in requirements:
            score += 5

    # Location preference
    if "remote" in location:
        score += 10

    if "hyderabad" in location:
        score += 10

    if "bangalore" in location:
        score += 8

    if "pune" in location:
        score += 7

    # Trusted sources
    if source in ["greenhouse", "lever"]:
        score += 20

    # Scam detection
    for word in REJECT_KEYWORDS:
        if word in requirements:
            return 0

    return min(score, 100)
