## Features & Learning checklist

- [x] Learnt to build REST APIs with DRF
- [x] Optimised CRUD operations with django ORM
- [x] Paginated Request
- [x] Advanced Search filtering
- [x] Worked with list DS
- [x] PostgreSQL database integration
- [x] Learnt about serializers
- [x] DRF querysets
- [x] Custom JWT authetication

## API ENDPOINTS: 


## 1)  
| Signup | Signup user, Return JWT tokens |
| ------ | ------ |
| HTTP method | POST |
| Route | /api/v1/register |


## Example 

### Body: 

```
{
    "username": "tom20",
    "email": "tom20@gmail.com@gmail.com",
    "password": "aksh1086"
}
```

### Response: 

 ```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NDAyNzU4OSwiaWF0IjoxNjQzOTQxMTg5LCJqdGkiOiI0MGM5OTBlZTAxODU0OWE1OTg1YmE2MTdjZTJlNjRlMCIsInVzZXJfaWQiOiIyYTBjNDdmMC00MDMzLTQzZTEtYWJjYS01YzE3NmQ5NGMyNDciLCJ1c2VybmFtZSI6InRvbTIwIn0.EG3Ej7iulP0WYPdKHgeZ5qu0ssqqQZvvnsv0fTlOvCM",

    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzOTYyNzg5LCJpYXQiOjE2NDM5NDExODksImp0aSI6IjA2YTEyYmQ0MGU1ODQyOTk4Njk3Y2QzMWIzMTkyYTllIiwidXNlcl9pZCI6IjJhMGM0N2YwLTQwMzMtNDNlMS1hYmNhLTVjMTc2ZDk0YzI0NyIsInVzZXJuYW1lIjoidG9tMjAifQ._m_llB1rf1Nso6Rk5FWJA5ZxmPB68ui_PJucnnQh70E"
}
```

## 2)  
| Login | Login user, Return JWT tokens |
| ------ | ------ |
| HTTP method | POST |
| Route | /api/v1/login |


## Example 

### Body: 

```
{
    "username": "tom20",
    "email": "tom20@gmail.com@gmail.com",
    "password": "aksh1086"
} 
```

### Response: 

 ```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NDAyNzU4OSwiaWF0IjoxNjQzOTQxMTg5LCJqdGkiOiI0MGM5OTBlZTAxODU0OWE1OTg1YmE2MTdjZTJlNjRlMCIsInVzZXJfaWQiOiIyYTBjNDdmMC00MDMzLTQzZTEtYWJjYS01YzE3NmQ5NGMyNDciLCJ1c2VybmFtZSI6InRvbTIwIn0.EG3Ej7iulP0WYPdKHgeZ5qu0ssqqQZvvnsv0fTlOvCM",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzOTYyNzg5LCJpYXQiOjE2NDM5NDExODksImp0aSI6IjA2YTEyYmQ0MGU1ODQyOTk4Njk3Y2QzMWIzMTkyYTllIiwidXNlcl9pZCI6IjJhMGM0N2YwLTQwMzMtNDNlMS1hYmNhLTVjMTc2ZDk0YzI0NyIsInVzZXJuYW1lIjoidG9tMjAifQ._m_llB1rf1Nso6Rk5FWJA5ZxmPB68ui_PJucnnQh70E"
}
```



## 3)  
| All users | Get all users. Paginated response. |
| ------ | ------ |
| HTTP method | GET |
| Route | /api/v1/users?page=2&pageSize=5 |
| Optional Queries: | | |
| Page | Default = 1 |
| PageSize | Default = 5 |

### Example Response: 

```
{
    "count": 21,
    "next": "http://127.0.0.1:8000/api/v1/users/?page=2&pageSize=5",
    "previous": null,
    "results": [
        {
            "id": "b90c0eb0-8501-4e10-97cc-7bd343b0467f",
            "username": "akshay"
        },
        {
            "id": "6602956c-9382-4ebf-9ccf-abdf1421b626",
            "username": "tom1"
        },
        {
            "id": "f653f595-ec47-4ecf-8b04-467fb202722d",
            "username": "tom2"
        },
        {
            "id": "8e2095a4-6805-45e8-81da-de7132f7d3b0",
            "username": "tom3"
        },
        {
            "id": "40831cc2-703b-4a57-a04a-3950997b292c",
            "username": "tom4"
        }
    ]
}
```

## 4)  
| Single user details | Get single user detail. |
| ------ | ------ |
| HTTP method | GET |
| Route | /api/v1/users/tom4 |

### Example Response: 

```
{
    "username": "tom4",
    "id": "40831cc2-703b-4a57-a04a-3950997b292c",
    "isTutor": false,
    "profile_pic": "/images/avatar.svg",
    "skills": [],
    "interests": []
}
 ```

## 5)  

| update user skills | update user skills |
| ------ | ------ |
| HTTP method | PATCH |
| Route | /api/v1/users/tom4/update-skills |
| Optional Queries: | | |
| Username | tom4 |

## Example 

### Body: 
```
[
    "javascript",
    "python",
    "c++",
    "c",
    "c",
    "javascript"
]
```

### Response: 

```
{
    "username": "tom4",
    "id": "40831cc2-703b-4a57-a04a-3950997b292c",
    "isTutor": false,
    "profile_pic": "/images/avatar.svg",
    "skills": [
        "c",
        "c++",
        "javascript",
        "python"
    ],
    "interests": []
}
```


## 6)  

| update user interests | update user interests |
| ------ | ------ |
| HTTP method | PATCH |
| Route | /api/v1/users/tom4/update-interests |
| Optional Queries: | | |
| Username | tom4 |

## Example 

### Body: 
```
[
    "programming",
    "gaming"
]
```

### Response: 

```
{
    "username": "tom4",
    "id": "40831cc2-703b-4a57-a04a-3950997b292c",
    "isTutor": false,
    "profile_pic": "/images/avatar.svg",
    "skills": [
        "c",
        "c++",
        "javascript",
        "python"
    ],
    "interests": [
        "gaming",
        "programming"
    ]
}
```


## Challenges vs How i solved them

| Challenges | How i solved them |
| ------ | ------ |
| Moving from MVC to MVCS architecture | Went through few websites and stackoverFlow and found out why i should revamp (optimised, reactor pattern, every module does one function rule, reuseablity) |
| Mongoose partial text based search | used a solution which utilises regex to solve this problem |
| Making task scheduler async | Went through a lot of packages and articles to solve this. thought of using setInterval but it would be optimsed for production level code. |
| Global error handling | I used to handle errors in try catch in every function, then learnt about Global error handling |
| Global Async handler | I used to handle async functions, then learnt about Global Async handler  |