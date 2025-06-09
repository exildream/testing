from . import start, profile, quests, review

all_handlers = (
    start.router,
    profile.router,
    quests.router,
    review.router,
)
