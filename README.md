# n11 Search Load Test

## Overview

Performance test for the search module of https://www.n11.com/ implemented with **Locust**.

Target endpoint:
```
GET /arama?q=<keyword>
```

---

## Test Coverage

Scenarios executed with 1 virtual user:

- Existing product search (`iPhone 17 Pro`)
- Existing category search (`MacBook`)
- Non-existing product (`nonexistingproduct123`)
- Partial keyword search (`Xiao`)

Validations:

- HTTP status code check (expected 200)
- SLA validation (response time < 2s)

Requests are aggregated in Locust as:
```
/arama?q=[aggregated]
```

---

## Requirements

- Python 3.10+
- pip
- Locust

Install dependencies:
```
pip install locust
```

---

## Run

From project root:
```
locust --host=https://www.n11.com
```

Open:
```
http://localhost:8089
```

Start test:
- Users: `1`
- Spawn rate: `1`

Stop test: `CTRL + C`
Find opened sessions (port 8089): `lsof -i :8089`
Close session: `kill -9 <PID>`

---

## Limitation

All requests return: `403 Forbidden`

Confirmed via:
```
curl -I "https://www.n11.com/arama?q=MacBook"
```

Response headers indicate Cloudflare protection (`Server: cloudflare, __cf_bm cookie`).

Production environment blocks automated HTTP clients before the request reaches application layer.

---

## Recommendation

Valid performance testing requires:

- Staging environment without WAF
- Whitelisted IP
- Internal API-level performance endpoint

Direct load testing of production UI endpoint is restricted by infrastructure protection.