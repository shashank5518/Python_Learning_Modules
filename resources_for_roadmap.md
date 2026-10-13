# 📚 Free Resources — Complete Guide
### Every Resource You Need, Phase by Phase
#### Python Backend Developer Roadmap | India & Global Job Market

> **Ground rules for using this list:**
> - Official documentation is always the primary source. No YouTuber explains a framework better than its creator's docs.
> - Watch YouTube for orientation and unsticking yourself. Not for following along line by line.
> - If you watch a video, close it and build the thing from scratch yourself afterward.
> - Free means free. No Udemy, no Coursera paywalls, no paid bootcamps.

---

## 🗂 Quick Navigation

- [Phase 1 — Python Foundations](#phase-1)
- [Phase 2 — Databases](#phase-2)
- [Phase 3 — Web Frameworks & APIs](#phase-3)
- [Phase 4 — Docker, Linux, Git](#phase-4)
- [Phase 5 — Cloud, CI/CD, Terraform](#phase-5)
- [Phase 6 — Async, Celery, Kafka, gRPC, System Design, Observability, Security](#phase-6)
- [DSA Resources](#dsa)
- [Always-Open Tabs](#always-open)
- [YouTube Channels to Subscribe To](#youtube-channels)

---

<a name="phase-1"></a>
## 📍 Phase 1 — Python Foundations (Weeks 1–4)

### Core Language

| Resource | Link | What It Covers | How to Use It |
|---|---|---|---|
| **Python Official Tutorial** | https://docs.python.org/3/tutorial/ | Syntax, data types, OOP, modules, standard library | Read fully, first week |
| **Python Official Library Reference** | https://docs.python.org/3/library/ | Every standard library module | Bookmark — refer constantly |
| **Python Official Language Reference** | https://docs.python.org/3/reference/ | How Python actually works under the hood | Dip in when you need depth |
| **Real Python** | https://realpython.com | Deep free articles on every Python topic | Search specific topics as you hit them |
| **Python Cheatsheet** | https://www.pythoncheatsheet.org | Quick syntax reference | Bookmark for quick lookups |

### YouTube — Python Fundamentals

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **Corey Schafer** | "Corey Schafer Python Tutorial" | Best free Python series — OOP, decorators, generators, file I/O, virtual environments |
| **mCoding** | "mCoding Python" | Python internals, performance, modern Python patterns, type hints |
| **ArjanCodes** | "ArjanCodes Python" | Clean code, design patterns, modern Python idioms |
| **Corey Schafer — OOP** | "Corey Schafer Python OOP" | Classes, inheritance, dunder methods, properties |
| **mCoding — Type Hints** | "mCoding type hints Python" | Full type system, mypy, generics |

### OOP Specifically

| Resource | Link | What It Covers |
|---|---|---|
| **Python Docs — Classes** | https://docs.python.org/3/tutorial/classes.html | Official OOP tutorial |
| **Real Python — OOP** | https://realpython.com/python3-object-oriented-programming/ | Free deep dive into OOP |
| **Real Python — Dataclasses** | https://realpython.com/python-data-classes/ | @dataclass — used heavily in FastAPI |
| **Real Python — Decorators** | https://realpython.com/primer-on-python-decorators/ | Decorators fully explained |
| **Real Python — Generators** | https://realpython.com/introduction-to-python-generators/ | Generators and iterators |
| **Real Python — Context Managers** | https://realpython.com/python-with-statement/ | with statement and context managers |

### Type Hints & Static Analysis

| Resource | Link | What It Covers |
|---|---|---|
| **mypy Official Docs** | https://mypy.readthedocs.io | Type checking reference |
| **Python Typing Docs** | https://docs.python.org/3/library/typing.html | All typing constructs |
| **Real Python — Type Checking** | https://realpython.com/python-type-checking/ | Practical guide to type hints |
| **ruff docs** | https://docs.astral.sh/ruff/ | Linting and formatting |
| **black docs** | https://black.readthedocs.io | Code formatting |

### Testing

| Resource | Link | What It Covers |
|---|---|---|
| **pytest Official Docs** | https://docs.pytest.org | Fixtures, parametrize, assertions, plugins |
| **Real Python — pytest** | https://realpython.com/pytest-python-testing/ | Free practical pytest guide |
| **ArjanCodes — Testing** | Search "ArjanCodes pytest" on YouTube | Testing patterns, fixtures, mocking |

### Practice Platforms

| Resource | Link | What It Covers |
|---|---|---|
| **Exercism — Python Track** | https://exercism.org/tracks/python | Hands-on exercises with feedback, free |
| **LeetCode** | https://leetcode.com | Filter by Python, start Easy — build language muscle memory |
| **HackerRank — Python** | https://hackerrank.com/domains/python | Basics and interview warm-up |
| **Codewars** | https://codewars.com | Python katas, gamified practice |

### Standard Library Deep Dives

| Resource | Link | What It Covers |
|---|---|---|
| **collections docs** | https://docs.python.org/3/library/collections.html | defaultdict, Counter, deque, namedtuple |
| **itertools docs** | https://docs.python.org/3/library/itertools.html | chain, product, groupby, islice |
| **functools docs** | https://docs.python.org/3/library/functools.html | partial, lru_cache, reduce |
| **pathlib docs** | https://docs.python.org/3/library/pathlib.html | Modern file path handling |
| **logging docs** | https://docs.python.org/3/library/logging.html | Logging setup and configuration |
| **Real Python — logging** | https://realpython.com/python-logging/ | Practical logging guide |

---

<a name="phase-2"></a>
## 📍 Phase 2 — Databases (Weeks 5–8)

### PostgreSQL & SQL

| Resource | Link | What It Covers |
|---|---|---|
| **PostgreSQL Official Docs** | https://www.postgresql.org/docs/current/ | Authoritative — read Tutorial section first |
| **PostgreSQL Tutorial** | https://www.postgresqltutorial.com | Structured free tutorial from basics to advanced |
| **SQLZoo** | https://sqlzoo.net | Interactive SQL exercises, browser-based, free |
| **Mode SQL Tutorial** | https://mode.com/sql-tutorial/ | Beginner to advanced including window functions |
| **SQLBolt** | https://sqlbolt.com | Interactive lessons, clean and fast |
| **Use The Index, Luke** | https://use-the-index-luke.com | Free book — indexing and query performance, essential |
| **pgexercises** | https://pgexercises.com | PostgreSQL-specific practice exercises |

### YouTube — Databases

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **Hussein Nasser** | "Hussein Nasser PostgreSQL" | DB internals, indexing, ACID, transactions — deep and accurate |
| **Hussein Nasser** | "Hussein Nasser database indexing" | Index internals, B-tree, when indexes are ignored |
| **CMU Database Course** | "CMU 15-445 Database Systems YouTube" | University-level DB internals — free on YouTube, exceptional quality |
| **Socratica** | "Socratica SQL" | Clean short SQL videos |

### Window Functions & Advanced SQL

| Resource | Link | What It Covers |
|---|---|---|
| **PostgreSQL Window Functions Docs** | https://www.postgresql.org/docs/current/tutorial-window.html | Official window functions tutorial |
| **Mode — Window Functions** | https://mode.com/sql-tutorial/sql-window-functions/ | Free practical guide |
| **Real Python — Advanced SQL** | https://realpython.com/python-sql-libraries/ | SQL from Python perspective |

### psycopg2 (Raw Driver)

| Resource | Link | What It Covers |
|---|---|---|
| **psycopg2 Official Docs** | https://www.psycopg.org/docs/ | Complete driver reference |
| **psycopg2 Usage Guide** | https://www.psycopg.org/docs/usage.html | Practical usage, parameterized queries, transactions |

### SQLAlchemy & Alembic

| Resource | Link | What It Covers |
|---|---|---|
| **SQLAlchemy Official Docs** | https://docs.sqlalchemy.org | ORM tutorial, Core tutorial, relationship patterns |
| **SQLAlchemy 2.0 Migration Guide** | https://docs.sqlalchemy.org/en/20/changelog/migration_20.html | Modern 2.0 style — use this, not legacy |
| **Alembic Official Docs** | https://alembic.sqlalchemy.org/en/latest/ | Migration tutorial and API reference |
| **FastAPI + SQLAlchemy (official)** | https://fastapi.tiangolo.com/tutorial/sql-databases/ | Integration guide |
| **Real Python — SQLAlchemy** | https://realpython.com/python-sqlalchemy/ | Free deep dive |

### Redis

| Resource | Link | What It Covers |
|---|---|---|
| **Redis Official Docs** | https://redis.io/docs | Commands, data structures, patterns |
| **Redis University — RU101** | https://university.redis.com/courses/ru101/ | Free — Intro to Redis Data Structures, excellent |
| **Redis University — RU102PY** | https://university.redis.com/courses/ru102py/ | Free — Redis for Python Developers |
| **Redis Commands Reference** | https://redis.io/commands | Every command with examples |
| **redis-py Docs** | https://redis-py.readthedocs.io | Python client reference |

### YouTube — Redis

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **TechWorld with Nana** | "TechWorld with Nana Redis Tutorial" | Redis overview, data structures, use cases |
| **Hussein Nasser** | "Hussein Nasser Redis" | Redis internals, caching patterns, pub/sub |

### MongoDB (Optional)

| Resource | Link | What It Covers |
|---|---|---|
| **MongoDB University — M001** | https://learn.mongodb.com/courses/m001-mongodb-basics | Free — MongoDB basics |
| **MongoDB University — M100** | https://learn.mongodb.com/courses/m100-mongodb-for-sql-pros | Free — for developers coming from SQL |
| **MongoDB Official Docs** | https://www.mongodb.com/docs/ | CRUD, aggregation pipeline, indexes |
| **pymongo Docs** | https://pymongo.readthedocs.io | Python driver reference |

### Tools

| Resource | Link | What It Covers |
|---|---|---|
| **DBeaver Download** | https://dbeaver.io | Free universal DB GUI — use for PostgreSQL |
| **pgAdmin** | https://www.pgadmin.org | PostgreSQL-specific GUI |
| **TablePlus (free tier)** | https://tableplus.com | Clean DB GUI, limited free tier |

---

<a name="phase-3"></a>
## 📍 Phase 3 — Web Frameworks & APIs (Weeks 9–14)

### HTTP Fundamentals

| Resource | Link | What It Covers |
|---|---|---|
| **MDN — HTTP Overview** | https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview | HTTP protocol fundamentals |
| **MDN — HTTP Status Codes** | https://developer.mozilla.org/en-US/docs/Web/HTTP/Status | Every status code with explanation |
| **MDN — HTTP Methods** | https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods | GET, POST, PUT, PATCH, DELETE semantics |
| **HTTP Status Codes Reference** | https://httpstatuses.io | Quick reference |
| **REST API Design — Microsoft** | https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design | Thorough REST design guide, free |

### FastAPI

| Resource | Link | What It Covers |
|---|---|---|
| **FastAPI Official Docs** | https://fastapi.tiangolo.com | Best framework docs in existence — read every page of the Tutorial section |
| **FastAPI — Tutorial** | https://fastapi.tiangolo.com/tutorial/ | Full tutorial from routing to security |
| **FastAPI — Advanced User Guide** | https://fastapi.tiangolo.com/advanced/ | Background tasks, middleware, custom responses |
| **FastAPI — Security** | https://fastapi.tiangolo.com/tutorial/security/ | JWT, OAuth2, API keys |
| **Pydantic v2 Docs** | https://docs.pydantic.dev/latest/ | Validation, models, settings management |
| **pydantic-settings Docs** | https://docs.pydantic.dev/latest/concepts/pydantic_settings/ | Config from .env files |

### YouTube — FastAPI

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **ArjanCodes** | "ArjanCodes FastAPI" | Clean architecture with FastAPI |
| **ArjanCodes** | "ArjanCodes dependency injection Python" | DI patterns used in FastAPI |
| **Sebastián Ramírez talks** | "Sebastián Ramírez FastAPI" on YouTube | FastAPI creator — architecture insights |

### Django & Django REST Framework

| Resource | Link | What It Covers |
|---|---|---|
| **Django Official Tutorial** | https://docs.djangoproject.com/en/stable/intro/tutorial01/ | The polls app — do all 8 parts |
| **Django Official Docs** | https://docs.djangoproject.com | ORM, forms, signals, admin, everything |
| **Django REST Framework Docs** | https://www.django-rest-framework.org | Tutorial + API guide — read fully |
| **DRF — Serializers** | https://www.django-rest-framework.org/api-guide/serializers/ | Serializer reference |
| **DRF — ViewSets** | https://www.django-rest-framework.org/api-guide/viewsets/ | ViewSet and Router reference |
| **djangorestframework-simplejwt** | https://django-rest-framework-simplejwt.readthedocs.io | JWT for DRF |

### YouTube — Django & DRF

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **Very Academy** | "Very Academy Django REST Framework" | Best free DRF series — deep, thorough |
| **Very Academy** | "Very Academy Django ORM" | Django ORM deep dive |
| **Corey Schafer** | "Corey Schafer Django" | Full Django series, beginner-friendly |
| **Dennis Ivy** | "Dennis Ivy Django" | Practical Django tutorials |

### Authentication & Security

| Resource | Link | What It Covers |
|---|---|---|
| **OWASP Top 10** | https://owasp.org/www-project-top-ten/ | Read this. Memorize it. Non-negotiable. |
| **OWASP Cheat Sheet Series** | https://cheatsheetseries.owasp.org | Practical checklists for auth, injection prevention |
| **JWT.io** | https://jwt.io | Understand JWT structure, debugger tool |
| **Auth0 Blog — OAuth2** | https://auth0.com/blog/oauth2-the-complete-guide/ | OAuth2 flows explained clearly |
| **passlib Docs** | https://passlib.readthedocs.io | Password hashing library |
| **python-jose Docs** | https://python-jose.readthedocs.io | JWT library for Python |

### API Testing

| Resource | Link | What It Covers |
|---|---|---|
| **Postman Learning Center** | https://learning.postman.com | Free API testing guides |
| **Bruno** | https://www.usebruno.com | Free Postman alternative, open source |
| **HTTPie** | https://httpie.io | Free CLI HTTP client, great for testing |

### Testing FastAPI & Django

| Resource | Link | What It Covers |
|---|---|---|
| **FastAPI — Testing Docs** | https://fastapi.tiangolo.com/tutorial/testing/ | TestClient, dependency overrides |
| **pytest Official Docs** | https://docs.pytest.org | Fixtures, parametrize, conftest |
| **Real Python — FastAPI Testing** | https://realpython.com/fastapi-testing-python/ | Free practical guide |
| **DRF — Testing Docs** | https://www.django-rest-framework.org/api-guide/testing/ | APIClient, APITestCase |

---

<a name="phase-4"></a>
## 📍 Phase 4 — Docker, Linux & Git (Weeks 15–18)

### Linux & Command Line

| Resource | Link | What It Covers |
|---|---|---|
| **The Linux Command Line (free book)** | https://linuxcommand.org/tlcl.php | Full book free online — definitive resource |
| **Linux Journey** | https://linuxjourney.com | Interactive Linux learning, free |
| **OverTheWire: Bandit** | https://overthewire.org/wargames/bandit/ | Learn Linux by playing a game — surprisingly effective |
| **ExplainShell** | https://explainshell.com | Paste any shell command, understand every part |
| **ShellCheck** | https://shellcheck.net | Linter for shell scripts |
| **Bash Guide (Wooledge)** | https://mywiki.wooledge.org/BashGuide | In-depth Bash reference |
| **tldr pages** | https://tldr.sh | Simplified man pages with examples |
| **ss/netstat reference** | https://man7.org/linux/man-pages/man8/ss.8.html | Network socket reference |

### YouTube — Linux

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **NetworkChuck** | "NetworkChuck Linux for beginners" | Linux fundamentals, practical |
| **TechWorld with Nana** | "TechWorld with Nana Linux commands" | Linux for DevOps |
| **freeCodeCamp** | "freeCodeCamp Linux command line" | Full free Linux course |

### Docker

| Resource | Link | What It Covers |
|---|---|---|
| **Docker Official Docs — Get Started** | https://docs.docker.com/get-started/ | Official tutorial, walks through everything |
| **Docker — Dockerfile Reference** | https://docs.docker.com/engine/reference/builder/ | Every Dockerfile instruction |
| **Docker Compose Docs** | https://docs.docker.com/compose/ | Compose file reference |
| **Docker — Best Practices** | https://docs.docker.com/develop/develop-images/dockerfile_best-practices/ | Official Dockerfile best practices |
| **Play with Docker** | https://labs.play-with-docker.com | Free browser-based Docker playground |
| **Dive (image analyser)** | https://github.com/wagoodman/dive | Free tool to inspect Docker image layers |

### YouTube — Docker

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **TechWorld with Nana** | "TechWorld with Nana Docker Tutorial for Beginners" | Best free Docker course on YouTube |
| **TechWorld with Nana** | "TechWorld with Nana Docker Compose" | Docker Compose deep dive |
| **Fireship** | "Fireship Docker in 100 Seconds" | Quick mental model first |
| **freeCodeCamp** | "freeCodeCamp Docker" | Full free Docker course |
| **Hussein Nasser** | "Hussein Nasser Docker" | Docker networking internals |

### Git — Advanced

| Resource | Link | What It Covers |
|---|---|---|
| **Pro Git (free book)** | https://git-scm.com/book/en/v2 | Complete, authoritative Git book — free online |
| **Learn Git Branching** | https://learngitbranching.js.org | Interactive visual Git exercises — do all of them |
| **Oh My Git!** | https://ohmygit.org | Interactive game for learning Git branching |
| **Git Official Docs** | https://git-scm.com/docs | Every command reference |
| **Conventional Commits Spec** | https://www.conventionalcommits.org | Commit message standard |
| **pre-commit framework** | https://pre-commit.com | Git hooks framework |
| **Dangit, Git!** | https://dangitgit.com | How to fix common Git mistakes |

### YouTube — Git

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **Fireship** | "Fireship Git in 100 Seconds" | Quick orientation |
| **Corey Schafer** | "Corey Schafer Git Tutorial" | Full Git series |
| **TechWorld with Nana** | "TechWorld with Nana Git" | Git for DevOps workflows |

### Nginx

| Resource | Link | What It Covers |
|---|---|---|
| **Nginx Official Docs** | https://nginx.org/en/docs/ | Configuration reference |
| **Nginx Beginner's Guide** | https://nginx.org/en/docs/beginners_guide.html | Official beginner guide |
| **DigitalOcean — Nginx Guide** | https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms | Deep Nginx config guide, free |

---

<a name="phase-5"></a>
## 📍 Phase 5 — Cloud & CI/CD (Weeks 19–24)

### AWS — Foundations

| Resource | Link | What It Covers |
|---|---|---|
| **AWS Free Tier** | https://aws.amazon.com/free | 12 months free — use this for all practice |
| **AWS Official Documentation** | https://docs.aws.amazon.com | Service-by-service reference — always primary |
| **AWS Skill Builder** | https://skillbuilder.aws | Free courses including Cloud Practitioner Essentials |
| **AWS Architecture Center** | https://aws.amazon.com/architecture/ | Real reference architectures, free |
| **AWS Well-Architected Framework** | https://aws.amazon.com/architecture/well-architected/ | How AWS thinks about good architecture |

### AWS — Service-Specific Docs

| Service | Direct Link |
|---|---|
| **EC2** | https://docs.aws.amazon.com/ec2/ |
| **S3** | https://docs.aws.amazon.com/s3/ |
| **RDS** | https://docs.aws.amazon.com/rds/ |
| **ECS** | https://docs.aws.amazon.com/ecs/ |
| **Lambda** | https://docs.aws.amazon.com/lambda/ |
| **IAM** | https://docs.aws.amazon.com/iam/ |
| **VPC** | https://docs.aws.amazon.com/vpc/ |
| **CloudWatch** | https://docs.aws.amazon.com/cloudwatch/ |
| **SQS** | https://docs.aws.amazon.com/sqs/ |
| **Secrets Manager** | https://docs.aws.amazon.com/secretsmanager/ |
| **ECR** | https://docs.aws.amazon.com/ecr/ |

### YouTube — AWS

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **freeCodeCamp** | "freeCodeCamp AWS Certified Cloud Practitioner 2024" | Full free exam prep — great for foundations |
| **TechWorld with Nana** | "TechWorld with Nana AWS Tutorial" | Practical AWS walkthroughs |
| **Stephane Maarek** | "Stephane Maarek AWS" on YouTube | High quality AWS explanations |
| **Be A Better Dev** | "Be A Better Dev AWS" | Practical AWS for developers |
| **Hussein Nasser** | "Hussein Nasser AWS" | Networking and architecture on AWS |

### AWS Certification (Optional but Valuable)

| Resource | Link | What It Covers |
|---|---|---|
| **AWS Cloud Practitioner — Free Course** | https://skillbuilder.aws/courses/134 | Official free prep course |
| **freeCodeCamp CCP Course (YouTube)** | Search "freeCodeCamp AWS Cloud Practitioner 2024" | Full free 14-hour prep course |
| **AWS Practice Exams (free)** | https://explore.skillbuilder.aws/learn/course/external/view/elearning/9153/aws-certified-cloud-practitioner-official-practice-question-set | Official free practice questions |
| **Tutorials Dojo Cheatsheets** | https://tutorialsdojo.com/aws-cheat-sheets/ | Free AWS service cheat sheets |

### GitHub Actions

| Resource | Link | What It Covers |
|---|---|---|
| **GitHub Actions Official Docs** | https://docs.github.com/en/actions | Definitive reference |
| **GitHub Actions — Quickstart** | https://docs.github.com/en/actions/quickstart | Get first workflow running |
| **GitHub Actions — Workflow Syntax** | https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions | Every workflow keyword |
| **GitHub Actions Marketplace** | https://github.com/marketplace?type=actions | Browse existing actions to learn patterns |
| **aws-actions on GitHub** | https://github.com/aws-actions | Official AWS actions for ECR, ECS deployment |

### YouTube — GitHub Actions & CI/CD

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **TechWorld with Nana** | "TechWorld with Nana GitHub Actions Tutorial" | Full practical CI/CD walkthrough |
| **freeCodeCamp** | "freeCodeCamp GitHub Actions" | Full free CI/CD course |
| **Fireship** | "Fireship GitHub Actions" | Quick orientation |

### GitLab CI

| Resource | Link | What It Covers |
|---|---|---|
| **GitLab CI/CD Docs** | https://docs.gitlab.com/ee/ci/ | Official docs — great examples |
| **GitLab CI/CD Tutorial** | https://docs.gitlab.com/ee/ci/quick_start/ | Getting started guide |

### Terraform

| Resource | Link | What It Covers |
|---|---|---|
| **Terraform Official Docs** | https://developer.hashicorp.com/terraform/docs | Language reference, state, providers |
| **HashiCorp Learn — AWS** | https://developer.hashicorp.com/terraform/tutorials/aws-get-started | Free step-by-step AWS tutorials |
| **Terraform Registry — AWS Provider** | https://registry.terraform.io/providers/hashicorp/aws/latest/docs | Every AWS resource reference |
| **Terraform Best Practices** | https://www.terraform-best-practices.com | Free book on Terraform patterns |

### YouTube — Terraform

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **freeCodeCamp** | "freeCodeCamp Terraform full course" | Full free course |
| **TechWorld with Nana** | "TechWorld with Nana Terraform" | Terraform with AWS, practical |
| **Fireship** | "Fireship Terraform in 100 Seconds" | Quick mental model |

### boto3 (AWS SDK for Python)

| Resource | Link | What It Covers |
|---|---|---|
| **boto3 Official Docs** | https://boto3.amazonaws.com/v1/documentation/api/latest/index.html | Complete SDK reference |
| **boto3 — S3 Guide** | https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html | S3 operations with examples |
| **boto3 — EC2 Guide** | https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-examples.html | EC2 operations |

---

<a name="phase-6"></a>
## 📍 Phase 6 — Advanced Backend & System Design (Weeks 25–32)

### Async Python & asyncio

| Resource | Link | What It Covers |
|---|---|---|
| **Python asyncio Docs** | https://docs.python.org/3/library/asyncio.html | Official asyncio reference |
| **Real Python — Async IO** | https://realpython.com/async-io-python/ | Free, the best practical asyncio article |
| **Python asyncio — Tasks** | https://docs.python.org/3/library/asyncio-task.html | gather, create_task, timeout, TaskGroup |
| **Real Python — Concurrency** | https://realpython.com/python-concurrency/ | Full threading vs multiprocessing vs asyncio comparison |
| **Python GIL Explained** | https://realpython.com/python-gil/ | Understanding the Global Interpreter Lock |

### YouTube — Async Python

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **mCoding** | "mCoding asyncio Python" | Deep, accurate asyncio explanations |
| **ArjanCodes** | "ArjanCodes async Python" | Practical async patterns |
| **mCoding** | "mCoding Python GIL" | GIL internals |

### Async Libraries

| Resource | Link | What It Covers |
|---|---|---|
| **httpx Docs** | https://www.python-httpx.org | Async HTTP client for Python |
| **asyncpg Docs** | https://magicstack.github.io/asyncpg/ | Fast async PostgreSQL driver |
| **aioredis Docs** | https://aioredis.readthedocs.io | Async Redis client |
| **aiofiles Docs** | https://github.com/Tinche/aiofiles | Async file operations |
| **SQLAlchemy Async Docs** | https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html | Async SQLAlchemy 2.0 |

### Threading & Multiprocessing

| Resource | Link | What It Covers |
|---|---|---|
| **Python threading Docs** | https://docs.python.org/3/library/threading.html | Threading module reference |
| **Python multiprocessing Docs** | https://docs.python.org/3/library/multiprocessing.html | Multiprocessing reference |
| **concurrent.futures Docs** | https://docs.python.org/3/library/concurrent.futures.html | ThreadPoolExecutor, ProcessPoolExecutor |
| **Real Python — Threading** | https://realpython.com/intro-to-python-threading/ | Practical threading guide |
| **Real Python — Multiprocessing** | https://realpython.com/python-multiprocessing/ | Practical multiprocessing guide |

### Celery

| Resource | Link | What It Covers |
|---|---|---|
| **Celery Official Docs** | https://docs.celeryq.dev/en/stable/ | Tasks, workers, beat scheduler, monitoring |
| **Celery — First Steps** | https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html | Getting started guide |
| **Celery — User Guide** | https://docs.celeryq.dev/en/stable/userguide/ | Canvas, routing, periodic tasks, monitoring |
| **Flower Docs** | https://flower.readthedocs.io | Celery monitoring dashboard |
| **Real Python — Celery** | https://realpython.com/asynchronous-tasks-with-django-and-celery/ | Free Celery + Django guide |

### YouTube — Celery

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **Very Academy** | "Very Academy Celery Django" | Celery with Django, practical |
| **freeCodeCamp** | "freeCodeCamp Celery Python" | Full Celery walkthrough |

### Message Queues — SQS & RabbitMQ

| Resource | Link | What It Covers |
|---|---|---|
| **AWS SQS Docs** | https://docs.aws.amazon.com/sqs/ | SQS reference, FIFO vs standard queues |
| **AWS SQS — Developer Guide** | https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/ | Producer/consumer patterns |
| **RabbitMQ Official Tutorials** | https://www.rabbitmq.com/getstarted.html | 7 free tutorials from basic to advanced |
| **RabbitMQ — Python Tutorial** | https://www.rabbitmq.com/tutorials/tutorial-one-python.html | Python producer/consumer with pika |

### Apache Kafka

| Resource | Link | What It Covers |
|---|---|---|
| **Apache Kafka Official Docs** | https://kafka.apache.org/documentation/ | Concepts, architecture, configuration |
| **Kafka: The Definitive Guide (free)** | https://www.confluent.io/resources/kafka-the-definitive-guide-v2/ | Free book from Confluent — register and download |
| **Confluent Kafka Python Docs** | https://docs.confluent.io/kafka-clients/python/current/overview.html | Python client reference |
| **Kafka Quickstart** | https://kafka.apache.org/quickstart | Get Kafka running locally |

### YouTube — Kafka

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **Hussein Nasser** | "Hussein Nasser Kafka" | Kafka internals and use cases — best free Kafka content |
| **freeCodeCamp** | "freeCodeCamp Apache Kafka" | Full beginner course |
| **Confluent** | "Confluent Kafka tutorial" on YouTube | Official Confluent channel |
| **TechWorld with Nana** | "TechWorld with Nana Kafka" | Kafka overview and setup |

### gRPC

| Resource | Link | What It Covers |
|---|---|---|
| **gRPC Official Docs — Python** | https://grpc.io/docs/languages/python/ | Python quickstart and guides |
| **Protocol Buffers Docs** | https://protobuf.dev | .proto syntax reference, field types |
| **gRPC — Core Concepts** | https://grpc.io/docs/what-is-grpc/core-concepts/ | Streaming types, deadlines, metadata |
| **grpcio PyPI** | https://pypi.org/project/grpcio/ | Library reference |

### YouTube — gRPC

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **TechWorld with Nana** | "TechWorld with Nana gRPC" | gRPC introduction, protobuf basics |
| **Hussein Nasser** | "Hussein Nasser gRPC" | gRPC internals, HTTP/2 |
| **freeCodeCamp** | "freeCodeCamp gRPC" | Full gRPC course |

### System Design — Core Resources

| Resource | Link | What It Covers |
|---|---|---|
| **System Design Primer (GitHub)** | https://github.com/donnemartin/system-design-primer | Most comprehensive free system design resource — star this now |
| **ByteByteGo Blog** | https://blog.bytebytego.com | Alex Xu's blog — system design diagrams and explanations |
| **High Scalability Blog** | http://highscalability.com | Real architectures from Netflix, Twitter, Uber etc. |
| **Martin Fowler's Blog** | https://martinfowler.com | Microservices, event sourcing, distributed patterns |
| **AWS Architecture Blog** | https://aws.amazon.com/blogs/architecture/ | Real architecture decisions, free |
| **Cloudflare Blog** | https://blog.cloudflare.com | Distributed systems in production |
| **Engineering blogs list** | https://github.com/kilimchoi/engineering-blogs | Curated list of every major tech company engineering blog |

### YouTube — System Design

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **ByteByteGo** | Search "ByteByteGo" on YouTube | Visual system design walkthroughs — exceptional quality |
| **Gaurav Sen** | "Gaurav Sen system design" | Indian creator, brilliant distributed systems explanations |
| **Hussein Nasser** | "Hussein Nasser system design" | Database, networking, backend architecture deep dives |
| **Exponent** | "Exponent system design interview" | System design interview walkthroughs |
| **Karan Pratap Singh** | "system design course" on YouTube | Free full system design course |

### System Design — Specific Topics

| Resource | Link | What It Covers |
|---|---|---|
| **Consistent Hashing** | https://highscalability.com/consistent-hashing/ | The algorithm explained |
| **CAP Theorem** | https://www.cl.cam.ac.uk/research/dtg/archived/files/publications/public/mk428/cap-critique.pdf | Original CAP paper |
| **DDIA (free chapters)** | https://dataintensive.net | Designing Data-Intensive Applications — some free content |
| **Distributed Systems lecture notes** | https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/dist-sys-notes.pdf | Cambridge University lecture notes, free |

### Observability — Logging

| Resource | Link | What It Covers |
|---|---|---|
| **structlog Docs** | https://www.structlog.org/en/stable/ | Structured logging library |
| **Python logging Docs** | https://docs.python.org/3/library/logging.html | Standard library logging |
| **12 Factor App — Logs** | https://12factor.net/logs | How production apps should handle logs |
| **python-json-logger Docs** | https://github.com/madzak/python-json-logger | JSON formatter for Python logging |

### Observability — Metrics

| Resource | Link | What It Covers |
|---|---|---|
| **Prometheus Official Docs** | https://prometheus.io/docs/introduction/overview/ | Metrics, querying with PromQL |
| **Prometheus — Python Client** | https://github.com/prometheus/client_python | prometheus-client library |
| **Grafana Official Docs** | https://grafana.com/docs/grafana/latest/ | Dashboards, alerting, data sources |
| **Play with Grafana** | https://play.grafana.org | Live Grafana sandbox, no setup needed |
| **PromQL Tutorial** | https://promlabs.com/promql-tutorial/ | PromQL query language guide |

### Observability — Tracing

| Resource | Link | What It Covers |
|---|---|---|
| **OpenTelemetry Python Docs** | https://opentelemetry.io/docs/languages/python/ | Instrumentation, auto and manual |
| **OpenTelemetry — Getting Started** | https://opentelemetry.io/docs/languages/python/getting-started/ | Python quickstart |
| **Jaeger Docs** | https://www.jaegertracing.io/docs/ | Distributed tracing backend |
| **FastAPI + OpenTelemetry** | https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/fastapi/fastapi.html | Auto-instrumentation for FastAPI |

### YouTube — Observability

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **TechWorld with Nana** | "TechWorld with Nana Prometheus Grafana" | Full Prometheus + Grafana setup |
| **TechWorld with Nana** | "TechWorld with Nana OpenTelemetry" | Distributed tracing walkthrough |
| **freeCodeCamp** | "freeCodeCamp Prometheus monitoring" | Full free monitoring course |

### Microservices Patterns

| Resource | Link | What It Covers |
|---|---|---|
| **Martin Fowler — Microservices** | https://martinfowler.com/articles/microservices.html | The original microservices article |
| **Martin Fowler — Strangler Fig** | https://martinfowler.com/bliki/StranglerFigApplication.html | Migrating monolith to microservices |
| **Microservices.io** | https://microservices.io/patterns/index.html | Pattern catalogue — Saga, CQRS, Outbox, Circuit Breaker |
| **AWS — Microservices** | https://aws.amazon.com/microservices/ | AWS perspective on microservices |

### Security (Advanced)

| Resource | Link | What It Covers |
|---|---|---|
| **OWASP Top 10** | https://owasp.org/www-project-top-ten/ | Read this again at Phase 6 — it means more now |
| **OWASP API Security Top 10** | https://owasp.org/www-project-api-security/ | API-specific security vulnerabilities |
| **OWASP Cheat Sheet Series** | https://cheatsheetseries.owasp.org | Specific checklists for auth, CSRF, SQL injection |
| **pip-audit** | https://pypi.org/project/pip-audit/ | Scan Python dependencies for vulnerabilities |
| **Snyk (free tier)** | https://snyk.io | Dependency vulnerability scanning |
| **AWS Security Best Practices** | https://docs.aws.amazon.com/security/ | IAM, secrets, network security on AWS |

---

<a name="dsa"></a>
## 📍 DSA Resources (Run in Parallel Throughout)

### Practice Platforms

| Resource | Link | What It Covers |
|---|---|---|
| **LeetCode (free tier)** | https://leetcode.com | Hundreds of free problems — filter by topic and difficulty |
| **HackerRank** | https://hackerrank.com | Good for service company assessments (TCS, Wipro) |
| **GeeksForGeeks** | https://geeksforgeeks.org | Large problem bank, theory articles |
| **Codeforces** | https://codeforces.com | Competitive programming if you want harder problems |
| **NeetCode** | https://neetcode.io | Curated LeetCode problems by pattern — free |

### Learning DSA Concepts

| Resource | Link | What It Covers |
|---|---|---|
| **NeetCode Roadmap** | https://neetcode.io/roadmap | Best free structured DSA roadmap |
| **NeetCode YouTube** | Search "NeetCode" on YouTube | Video solutions with clear explanations |
| **Striver's A2Z DSA Sheet** | https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/ | Popular Indian DSA roadmap, free |
| **CP Algorithms** | https://cp-algorithms.com | Algorithmic articles with implementations |
| **Visualgo** | https://visualgo.net | Visual algorithm and data structure animations |
| **Big-O Cheat Sheet** | https://www.bigocheatsheet.com | Time/space complexity reference |

### Python-Specific DSA

| Resource | Link | What It Covers |
|---|---|---|
| **Python heapq Docs** | https://docs.python.org/3/library/heapq.html | Heap operations in Python |
| **Python collections Docs** | https://docs.python.org/3/library/collections.html | deque, Counter, defaultdict for DSA |
| **Python bisect Docs** | https://docs.python.org/3/library/bisect.html | Binary search in Python |
| **Real Python — Sorting** | https://realpython.com/sorting-algorithms-python/ | Sorting implementations in Python |

### YouTube — DSA

| Channel / Video | Search Query | What It Covers |
|---|---|---|
| **NeetCode** | Search "NeetCode" on YouTube | Best DSA channel — clear Python solutions |
| **Striver (take U forward)** | "Striver DSA" on YouTube | Popular Indian DSA channel |
| **Back To Back SWE** | "Back To Back SWE" on YouTube | Deep explanations of algorithms |
| **freeCodeCamp** | "freeCodeCamp Data Structures Algorithms" | Full free DSA course |

---

<a name="always-open"></a>
## 🔖 Always-Open Tabs

Keep these open throughout the entire 8 months regardless of phase.

| Resource | Link | Why |
|---|---|---|
| **roadmap.sh — Backend** | https://roadmap.sh/backend | Visual map — good for orientation and gap checking |
| **roadmap.sh — Python** | https://roadmap.sh/python | Python-specific roadmap |
| **DevDocs** | https://devdocs.io | Offline-capable docs for everything in one place |
| **Python Weekly Newsletter** | https://pythonweekly.com | Free weekly Python news and articles |
| **GitHub Trending — Python** | https://github.com/trending/python | See what real Python projects look like |
| **Hacker News** | https://news.ycombinator.com | Stay current on backend tech trends |
| **The Pragmatic Engineer (free tier)** | https://newsletter.pragmaticengineer.com | What the industry actually looks like from inside |
| **Bytebytego Newsletter (free)** | https://blog.bytebytego.com | System design diagrams and explanations weekly |
| **12 Factor App** | https://12factor.net | How production-ready apps should be built — read once, reference forever |
| **HTTP Status Codes** | https://httpstatuses.io | Quick reference |
| **Regex101** | https://regex101.com | Test and understand regex |
| **Crontab Guru** | https://crontab.guru | Cron expression builder and validator |

---

<a name="youtube-channels"></a>
## 📺 YouTube Channels — Subscribe to All of These

| Channel | Best For | Quality |
|---|---|---|
| **TechWorld with Nana** | Docker, Kubernetes, CI/CD, GitHub Actions, AWS, Terraform | ⭐⭐⭐⭐⭐ |
| **Corey Schafer** | Python fundamentals, Django, Flask | ⭐⭐⭐⭐⭐ |
| **ArjanCodes** | Clean Python, FastAPI, design patterns, testing | ⭐⭐⭐⭐⭐ |
| **mCoding** | Python internals, performance, modern Python, asyncio | ⭐⭐⭐⭐⭐ |
| **Hussein Nasser** | Backend engineering, databases, Kafka, networking, gRPC | ⭐⭐⭐⭐⭐ |
| **ByteByteGo** | System design, distributed systems — visual and clear | ⭐⭐⭐⭐⭐ |
| **Gaurav Sen** | System design, distributed systems — Indian creator | ⭐⭐⭐⭐⭐ |
| **NeetCode** | DSA in Python — best DSA channel currently | ⭐⭐⭐⭐⭐ |
| **Very Academy** | Django, DRF deep dives | ⭐⭐⭐⭐⭐ |
| **freeCodeCamp** | Long-form full courses on almost everything | ⭐⭐⭐⭐ |
| **Fireship** | 100-second concept overviews — mental models fast | ⭐⭐⭐⭐ |
| **NetworkChuck** | Linux, networking, cloud fundamentals | ⭐⭐⭐⭐ |
| **Striver (take U forward)** | DSA, Indian job market context | ⭐⭐⭐⭐ |
| **Dennis Ivy** | Django, DRF practical tutorials | ⭐⭐⭐⭐ |

---

## 📖 Free Books Worth Reading

| Book | Link | When to Read |
|---|---|---|
| **The Linux Command Line** | https://linuxcommand.org/tlcl.php | Phase 4 |
| **Pro Git** | https://git-scm.com/book/en/v2 | Phase 4 |
| **Terraform Best Practices** | https://www.terraform-best-practices.com | Phase 5 |
| **Kafka: The Definitive Guide** | https://www.confluent.io/resources/kafka-the-definitive-guide-v2/ | Phase 6 |
| **System Design Primer** | https://github.com/donnemartin/system-design-primer | Phase 6 |
| **Distributed Systems (Cambridge notes)** | https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/dist-sys-notes.pdf | Phase 6 |
| **PostgreSQL 14 Internals** | https://postgrespro.com/community/books/internals | Deep PostgreSQL — Phase 2/6 |

---

## ⚠️ How NOT to Use These Resources

- **Don't try to consume everything.** This list exists so you always have somewhere to go. Pick the primary resource per topic and go deep on that. Use others to fill gaps.
- **Don't watch tutorials without building.** Orientation only. Then close the video and build it from scratch.
- **Don't ignore official docs.** Every tutorial is someone's interpretation of the docs. Read the source.
- **Don't collect resources instead of writing code.** Saving this list to Notion and feeling productive is not learning. Time spent coding > time spent finding resources.

---

*Last updated: June 2026 | Covers all 6 phases of the Python Backend Developer Roadmap*
*All resources verified as free at time of writing*
