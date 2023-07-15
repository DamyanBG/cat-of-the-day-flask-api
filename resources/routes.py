from resources.auth_resource import (
    LoginAdmin,
    LoginUploader,
    LoginVoter,
    RegisterUploader,
    RegisterVoter,
    UserInfo,
    Logout
)
from resources.cat_resource import AddCat, GetCatOfTheDayPhoto
from resources.vote_resource import Voting

routes = (
    (LoginAdmin, "/admin/login"),
    (LoginUploader, "/uploader/login"),
    (Logout, "/logout"),
    (RegisterUploader, "/uploader/register"),
    (RegisterVoter, "/voter/register"),
    (LoginVoter, "/voter/login"),
    (AddCat, "/cat"),
    (Voting, "/vote"),
    (UserInfo, "/user-info"),
    (GetCatOfTheDayPhoto, "/cat-of-the-day-photo"),
)
