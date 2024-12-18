from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review_create'  # unique identifier for this throttle scope
    


class ReviewListThrottle(UserRateThrottle):
    scope = 'review_list'  # unique identifier for this throttle scope