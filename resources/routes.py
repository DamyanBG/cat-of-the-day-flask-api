from resources.auth_resource import (
    LoginAdmin,
    LoginUploader,
    LoginVoter,
    RegisterUploader,
    RegisterVoter,
    UserInfo,
)
from resources.cat_resource import AddCat
from resources.vote_resource import Voting

routes = (
    (LoginAdmin, "/admin/login"),
    (LoginUploader, "/uploader/login"),
    (RegisterUploader, "/uploader/register"),
    (RegisterVoter, "/voter/register"),
    (LoginVoter, "/voter/login"),
    (AddCat, "/cat"),
    (Voting, "/vote"),
    (UserInfo, "/user-info"),
)
