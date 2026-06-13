TARGET_ROLES = [
    "software engineer",
    "java developer",
    "backend developer",
    "full stack developer",
    "associate software engineer",
    "graduate engineer trainee",
    "trainee software engineer"
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


def score_job(job):
    score = 0

    role = job["role"].lower()
    requirements = job["requirements"].lower()
    location = job["location"].lower()
    source = job["source"].lower()

    # Role match
    for target in TARGET_ROLES:
        if target in role:
            score += 40
            break

    # Skills match
    for skill in SKILLS:
        if skill in requirements:
            score += 5

    # Location preference
    if "remote" in location:
        score += 10

    if "hyderabad" in location:
        score += 10

    # Trusted source
    if source in ["greenhouse", "lever"]:
        score += 20

    # Scam detection
    for word in REJECT_KEYWORDS:
        if word in requirements:
            return 0

    return min(score, 100)
