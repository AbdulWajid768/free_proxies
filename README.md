<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,50:FF6B6B,100:00d4aa&height=200&section=header&text=FreeProxy&fontSize=48&fontColor=ffffff&animation=twinkling&desc=Elite+proxy+harvest+%7C+live+probes+%7C+zero+API+keys&descSize=15&descAlignY=72&descAlign=62"/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=16&duration=2500&pause=750&color=FF6B6B&center=true&vCenter=true&multiline=true&repeat=true&width=660&height=88&lines=Scrape+elite+rows+from+the+public+grid;Probe+via+httpbin.org%2Fip;Return+only+what+still+breathes;Dev+%26+research+use+only" alt="Typing animation"/>
</a>

<br/>

### ⟡ Live telemetry ⟡

[![GitHub stars](https://img.shields.io/github/stars/AbdulWajid768/free_proxies?style=for-the-badge&logo=starship&logoColor=white&labelColor=0f172a&color=FF6B6B)](https://github.com/AbdulWajid768/free_proxies/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/AbdulWajid768/free_proxies?style=for-the-badge&logo=git&logoColor=white&labelColor=0f172a&color=00d4aa)](https://github.com/AbdulWajid768/free_proxies/network/members)
[![Open issues](https://img.shields.io/github/issues/AbdulWajid768/free_proxies?style=for-the-badge&logo=githubissues&logoColor=white&labelColor=0f172a&color=fbbf24)](https://github.com/AbdulWajid768/free_proxies/issues)

[![Last commit](https://img.shields.io/github/last-commit/AbdulWajid768/free_proxies?style=for-the-badge&logo=git&logoColor=white&labelColor=0f172a&color=FF6B6B)](https://github.com/AbdulWajid768/free_proxies/commits/main)
[![Commit activity](https://img.shields.io/github/commit-activity/m/AbdulWajid768/free_proxies?style=for-the-badge&logo=pulse&logoColor=white&labelColor=0f172a&color=00d4aa)](https://github.com/AbdulWajid768/free_proxies/graphs/commit-activity)
[![Repo size](https://img.shields.io/github/repo-size/AbdulWajid768/free_proxies?style=for-the-badge&logo=harddrive&logoColor=white&labelColor=0f172a&color=0891b2)](https://github.com/AbdulWajid768/free_proxies)

[![Python](https://img.shields.io/badge/Python-3.6+-00d4aa?style=for-the-badge&logo=python&logoColor=0f172a)](https://www.python.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-FF6B6B?style=for-the-badge&logo=python&logoColor=white)](https://www.crummy.com/software/BeautifulSoup/)

<br/>

<img src="https://github-readme-stats.vercel.app/api/pin/?username=AbdulWajid768&repo=free_proxies&theme=chartreuse-dark&hide_border=true&bg_color=0a0f0a&title_color=00d4aa&icon_color=FF6B6B&text_color=d1fae5&border_radius=12" width="48%"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=AbdulWajid768&theme=chartreuse-dark&hide_border=true&bg_color=0a0f0a&title_color=00d4aa&text_color=d1fae5&layout=compact&border_radius=12" width="48%"/>

<br/><br/>

[⚙ Setup](#-setup) · [🖥 CLI](#-cli) · [🧩 API](#-api)

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=20,21,22&height=2&section=footer" width="100%"/>

</div>

---

## ◈ Transmission

**FreeProxy** pulls **elite** proxies from [free-proxy-list.net](https://free-proxy-list.net/), stress-tests each against `https://httpbin.org/ip`, and returns **`host:port`** strings that still respond.

> ⚠ **Warning:** Public proxies are **untrusted** and ephemeral—research, scraping labs, and QA only. Never route credentials or PII.

---

## ◈ Setup

```bash
git clone https://github.com/AbdulWajid768/free_proxies.git
cd free_proxies

pip install -r requirements.txt
python app.py
```

---

## ◈ CLI

```bash
python app.py
```

```text
Available Proxies: ['203.0.113.10:8080', ...]
Working Proxies:   ['203.0.113.10:8080']
```

---

## ◈ API

```python
from free_proxy import FreeProxy

proxies = FreeProxy.get_proxies()              # elite scrape
ok = FreeProxy.is_proxy_working("1.2.3.4:8080")  # 5s timeout probe
live = FreeProxy.get_working_proxies()         # scrape + filter
```

| Method | Output |
| --- | --- |
| `get_proxies()` | Unverified elite list |
| `is_proxy_working(proxy)` | `bool` |
| `get_working_proxies()` | Verified subset |

---

## ◈ Pipeline

```mermaid
%%{init: {'theme':'dark', 'themeVariables': { 'primaryColor':'#FF6B6B','lineColor':'#00d4aa'}}}%%
flowchart LR
    A[(free-proxy-list.net)] --> B[Parse tbody]
    B --> C{elite?}
    C -->|yes| D[httpbin probe]
    C -->|no| X[drop]
    D -->|200| E[[working pool]]
    D -->|fail| X
```

---

<div align="center">

<a href="https://star-history.com/#AbdulWajid768/free_proxies&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=AbdulWajid768/free_proxies&type=Date&theme=dark"/>
    <img alt="Star history" src="https://api.star-history.com/svg?repos=AbdulWajid768/free_proxies&type=Date"/>
  </picture>
</a>

<br/><br/>

**[Abdul Wajid](https://github.com/AbdulWajid768)** · Software Engineer · Lahore, PK

[![GitHub](https://img.shields.io/badge/@AbdulWajid768-181717?style=flat&logo=github)](https://github.com/AbdulWajid768)

<img src="https://komarev.com/ghpvc/?username=AbdulWajid768-free_proxies&label=NEURAL%20VIEWS&color=FF6B6B&style=for-the-badge" alt="views"/>

<sub>Scan the grid · Route through survivors.</sub>

</div>
