"""Check link availability. Anti-bot responses are inconclusive, not proof of broken links."""
import urllib.request, urllib.error
from pathlib import Path
urls=[x.strip() for x in Path(__file__).with_name('links.txt').read_text().splitlines() if x.strip() and not x.lstrip().startswith('#')]
for url in urls:
    try:
        request=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (compatible; ZhengzhinLinkMonitor/1.0)'},method='GET')
        with urllib.request.urlopen(request, timeout=18) as resp:
            print('OK',resp.status,url)
    except urllib.error.HTTPError as exc:
        print(('REVIEW' if exc.code in (403,405,429,503) else 'FAILED'),exc.code,url)
    except Exception as exc:
        print('REVIEW',type(exc).__name__,url)
