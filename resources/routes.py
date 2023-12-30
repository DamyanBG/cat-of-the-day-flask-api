from resources.auth_resource import (
    LoginAdmin,
    LoginUploader,
    LoginVoter,
    RegisterUploader,
    RegisterVoter,
    UserInfo,
    Logout
)
from resources.cat_resource import CatResource, GetCatOfTheDayPhoto
from resources.vote_resource import Voting

routes = (
    (LoginAdmin, "/admin/login"),
    (LoginUploader, "/user/login"),
    (Logout, "/logout"),
    (RegisterUploader, "/user/register"),
    (CatResource, "/cat"),
    (Voting, "/vote"),
    (UserInfo, "/user-info"),
    (GetCatOfTheDayPhoto, "/cat-of-the-day-photo"),
)
