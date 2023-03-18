# reunion


1. for api/authenticate/ -- API 

-- credentials : --
username : admin   -  password : admin123
username : rahul   -  password : rahul@123
username : vikash  -  password : admin@123

request : json-payload :-- 
{
    "username" : "admin",
    "password" : "admin123"
}

response : JWT Token

2. for api/getuser/ :-- this GET-API show the `username and id` of the authenticated user.

3. for api/follow/ :--

--request : json-payload :--
{
    "id" : 2 (this id belongs to another user hence, authenticated user follow the user whose id=2)
}

--response : user-id and following-user-id

4. for api/unfollow/ :--

--request : json-payload :--
{
    "id" : 2 (the authenticated user unfollow the user whose id=2) 
}

--reponse : {"msg" : "UNfollow Succesfully"}

5. for api/user/ :-- GET-API
--response : username, followers and followings

6. for api/posts/ :--

--request : json-payload :--
{
    "tiltle" : "Harry potter",
    "description" : "It is an comic."
}

--response : ID, Title, Description, Created Time(UTC)

7. for api/comment/ :--

--request : json-payload :--
{
    "id" : 1, (Here, the `id` is `post-id` not a `user-id`)
    "comment" : "Awesome!"
}

--response : comment-ID
