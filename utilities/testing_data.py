class TestingData:
    POST_INFO = {"userId": 5, "id": 50,
                 "title": "repellendus qui recusandae incidunt voluptates tenetur qui omnis exercitationem",
                 "body": "error suscipit maxime adipisci consequuntur recusandae\nvoluptas eligendi et est et voluptates\nquia distinctio ab amet quaerat molestiae et vitae\nadipisci impedit sequi nesciunt quis consectetur"}
    COMMENT_INFO = {"postId": 20, "id": 100, "name": "et sint quia dolor et est ea nulla cum",
                    "email": "Leone_Fay@orrin.com",
                    "body": "architecto dolorem ab explicabo et provident et\net eos illo omnis mollitia ex aliquam\natque ut ipsum nulla nihil\nquis voluptas aut debitis facilis"}
    ALBUM_INFO = {"userId": 4, "id": 33, "title": "iste eos nostrum"}
    PHOTO_INFO = {"albumId": 1, "id": 13, "title": "repudiandae iusto deleniti rerum",
                  "url": "https://via.placeholder.com/600/197d29",
                  "thumbnailUrl": "https://via.placeholder.com/150/197d29"}
    TODO_INFO = {"userId": 2, "id": 21, "title": "suscipit repellat esse quibusdam voluptatem incidunt",
                 "completed": False}
    USER_INFO = {"id": 5, "name": "Chelsey Dietrich", "username": "Kamren", "email": "Lucio_Hettinger@annie.ca",
                 "address": {"street": "Skiles Walks", "suite": "Suite 351", "city": "Roscoeview", "zipcode": "33263",
                             "geo": {"lat": "-31.8129", "lng": "62.5342"}}, "phone": "(254)954-1289",
                 "website": "demarco.info",
                 "company": {"name": "Keebler LLC", "catchPhrase": "User-centric fault-tolerant solution",
                             "bs": "revolutionize end-to-end systems"}}
    POSTS_LEN = 100
    COMMENTS_LEN = 500
    ALBUMS_LEN = 100
    PHOTOS_LEN = 5000
    TODOS_LEN = 200
    USERS_LEN = 10
    POST2POST = {"userId": 5, "title": "Automated post", "body": "This is a post made for QA"}
    COMMENT2POST = {"postId": 20, "name": "Juan Gabriel", "email": "juan@mail.com", "body": "Comment made for QA"}
    ALBUM2POST = {"userId": 5, "title": "Automated album"}
    PHOTO2POST = {"albumId": 1, "title": "Automated photo", "url": "https://via.placeholder.com/600/197d29",
                  "thumbnailUrl": "https://via.placeholder.com/150/197d29"}
    TO_DO2POST = {"userId": 2, "title": "Automated TO_DO", "completed": False}
    USER2POST = {"name": "Gabriel", "username": "user", "email": "mail@mail.com"}
    WRONG_POST = {"userId": "?", "title": "Automated post", "body": "This is a post made for QA"}
    WRONG_PHOTO = {"albumId": "bo", "title": "repudiandae iusto deleniti rerum",
                   "url": "https://via.placeholder.com/600/197d29",
                   "thumbnailUrl": "https://via.placeholder.com/150/197d29"}
    WRONG_TODO = {"userId": "ae", "title": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": False}
    POST2PUT = {"userId": 5, "id": 90, "title": "Title test", "body": "This is a test"}
    COMMENT2PUT = {"postId": 20, "id": 150, "name": "QA", "email": "mail@mail", "body": "facilis"}
    ALBUM2PUT = {"userId": 4, "id": 25, "title": "Album to update"}
    PHOTO2PUT = {"albumId": 1, "id": 950, "title": "Photo", "url": "https://via.placeholder.com/600/197d29",
                 "thumbnailUrl": "https://via.placeholder.com/150/197d29"}
    TODO2PUT = {"userId": 2, "id": 125, "title": "To do", "completed": False}
    USER2PUT = {"id": 2, "name": "Gabriel Orozco", "username": "Kamren", "email": "Lucio_Hettinger@annie.ca",
                "address": {"street": "Skiles Walks", "suite": "Suite 351", "city": "Roscoeview", "zipcode": "33263",
                            "geo": {"lat": "-31.8129", "lng": "62.5342"}}, "phone": "(254)954-1289",
                "website": "demarco.info",
                "company": {"name": "Keebler LLC", "catchPhrase": "User-centric fault-tolerant solution",
                            "bs": "revolutionize end-to-end systems"}}
    POST2PATCH = {"title": "test"}
    COMMENT2PATCH = {"name": "Gabriel"}
    ALBUM2PATCH = {"title": "album test"}
    PHOTO2PATCH = {"title": "photo test"}
    TODO2PATCH = {"title": "todo_test"}
    USER2PATCH = {"username": "j.gabriel"}