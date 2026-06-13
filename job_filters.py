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

    role = job.get("role", "").lower()
    requirements = job.get("requirements", "").lower()
    location = job.get("location", "").lower()
    source = job.get("source", "").lower()

    if any(target in role for target in TARGET_ROLES):
        score += 40

    for skill in SKILLS:
        if skill in requirements:
            score += 5

    if "remote" in location:
        score += 10

    if "hyderabad" in location:
        score += 10

    if source in ["greenhouse", "lever"]:
        score += 20

    for word in REJECT_KEYWORDS:
        if word in requirements:
            return 0

    return min(score, 100)
