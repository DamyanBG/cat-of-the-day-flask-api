from resources.auth_resource import (
    LoginAdmin,
    LoginUser,
    RegisterUser,
    UserInfo,
    Logout,
)
from resources.cat_resource import CatResource, GetCatOfTheDayPhoto
from resources.vote_resource import Voting
from resources.image_resource import ImageResource

routes = (
    (LoginAdmin, "/admin/login"),
    (LoginUser, "/user/login"),
    (Logout, "/logout"),
    (RegisterUser, "/user/register"),
    (CatResource, "/cat"),
    (Voting, "/vote"),
    (UserInfo, "/user-info"),
    (GetCatOfTheDayPhoto, "/cat-of-the-week-photo"),
    (ImageResource, "/image"),
)
