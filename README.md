---
### Dev.
#### Install tool.
```shell
pip install poetry
```

#### Install depends.
```shell
poetry install
```

#### Start dev env.
```shell
poetry shell
```

#### Start dev env.
```shell
python manage.py runserver
```

#### Manual test.
Navigate to [http://localhost:8000/admin/](http://localhost:8000/admin/) with credential `admin | admin123`

## Test reserve and room.

## Reserve.
Simple demo by Admin built-in.
![](docs/imgs/Screenshot_2023-05-10-03:17:41-1683663461.png)

#### Check overlap.
![](docs/imgs/Screenshot_2023-05-10-03:18:23-1683663503.png)

#### Validation in/out.

![](docs/imgs/Screenshot_2023-05-10-03:22:13-1683663733.png)![](docs/imgs/Screenshot_2023-05-10-03:22:53-1683663773.png)

## Available Room's filter by datetime range.

| ROOM | CHECKIN | CHECKOUT |
|------|---------|----------|
|   bnb-01   |    May 27, 2023, 8:18 p.m.     |    May 30, 2023, 8:18 p.m.      |
|    bnb-01  |   May 14, 2023, 6 a.m.      |    May 20, 2023, 6 a.m.      |

#### Gap between: 20-27 on May.
![](docs/imgs/Screenshot_2023-05-10-04:10:27-1683666627.png)

#### Full range from 12-31 May.
![](docs/imgs/Screenshot_2023-05-10-04:11:03-1683666663.png)