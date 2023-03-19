from resources.auth_resource import LoginAdmin, LoginUploader, LoginVoter, RegisterUploader, RegisterVoter

routes = (
    (LoginAdmin, "/admin/login"),
    (LoginUploader, "/uploader/login"),
    (RegisterUploader, "/uploader/register"),
    (RegisterVoter, "/voter/register"),
    (LoginVoter, "/voter/login"),
)
