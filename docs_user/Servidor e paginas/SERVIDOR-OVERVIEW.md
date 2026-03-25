# Servidor Overview — Guia Operacional para Novos Projetos
**Servidor:** 162.240.13.51 (compartilhado — múltiplos domínios/usuários cPanel)
**Gerado por:** Orion (aios-master) — 2026-03-12

---

## 1. ACESSO AO SERVIDOR

### SSH — BLOQUEADO
A porta 22 está **fechada para acesso externo**. Não perca tempo tentando SSH.

### Método Correto: cPanel UAPI via Python urllib

Todo acesso é feito via API HTTP. Fluxo obrigatório em 3 passos:

```python
import urllib.request, urllib.parse, http.cookiejar, json, ssl, base64

# Contexto SSL (certificado self-signed no servidor)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Cookie jar obrigatório (mantém sessão cPanel)
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(
    urllib.request.HTTPSHandler(context=ctx),
    urllib.request.HTTPCookieProcessor(cj)
)

# PASSO 1: Criar sessão cPanel via WHM (porta 2087)
whm_url = "https://162.240.13.51:2087/json-api/create_user_session?api.version=1&user=CPANEL_USER&service=cpaneld"
req = urllib.request.Request(whm_url)
req.add_header("Authorization", f"Basic {base64.b64encode(b'root:WHM_PASSWORD').decode()}")
data = json.loads(opener.open(req).read())

session_url = data['data']['url']
token = session_url.split('/')[3]  # cpsessXXXXXXXXXX
cpanel_base = f"https://162.240.13.51:2083/{token}"

# PASSO 2: Visitar session URL para ativar cookie
opener.open(session_url).read()

# PASSO 3: Usar UAPI com o token na URL
# Agora {cpanel_base}/execute/MODULE/FUNCTION
```

**Credenciais do servidor (acessos.txt):**
- WHM root: `162.240.13.51:2087` | user: `root`
- Cada domínio tem seu próprio usuário cPanel

---

## 2. OPERAÇÕES ESSENCIAIS

### Ler arquivo do servidor
```python
get_url = f"{cpanel_base}/execute/Fileman/get_file_content"
params = urllib.parse.urlencode({'dir': '/home/USER/public_html/path', 'file': 'filename.php'})
with opener.open(f"{get_url}?{params}") as r:
    content = json.loads(r.read())['data']['content']
```

### Escrever/atualizar arquivo
```python
upload_url = f"{cpanel_base}/execute/Fileman/save_file_content"
payload = urllib.parse.urlencode({
    'dir': '/home/USER/public_html/path',
    'file': 'filename.php',
    'content': file_content  # string do conteúdo
}).encode()
req = urllib.request.Request(upload_url, data=payload)
req.add_header("Content-Type", "application/x-www-form-urlencoded")
resp = json.loads(opener.open(req).read())
# resp['status'] == 1 = sucesso
```

### Executar PHP no servidor (scripts temporários)
```python
# 1. Upload do script PHP para o webroot
# 2. Executar via HTTP
exec_req = urllib.request.Request("https://162.240.13.51/meu_script.php")
exec_req.add_header("Host", "dominio.com.br")
output = opener.open(exec_req).read().decode('utf-8', errors='replace')
# 3. SEMPRE limpar depois: sobrescrever com '<?php //'
```

### Reiniciar Apache (limpa OPcache PHP)
```python
restart_url = "https://162.240.13.51:2087/json-api/restartservice?api.version=1&service=httpd"
req = urllib.request.Request(restart_url)
req.add_header("Authorization", f"Basic {base64.b64encode(b'root:PASSWORD').decode()}")
resp = json.loads(opener.open(req).read())
# resp['metadata']['reason'] == 'OK'
```

---

## 3. WORDPRESS — ARQUITETURA DO SERVIDOR

### Dois installs no mesmo banco de dados
O servidor usa um único banco MySQL com **dois prefixos de tabela**:
- `wp_` → install legado (tema `quest`, front page ID=2)
- `wps_` → install ativo (tema do projeto, front page ID=520+)

**Como identificar qual está ativo:** verificar qual prefixo tem o tema correto:
```sql
SELECT option_value FROM wps_options WHERE option_name='template';
SELECT option_value FROM wp_options WHERE option_name='template';
```
O prefixo com o tema do projeto = install ativo.

### Ler wp-config.php para credenciais DB
```php
$cfg = file_get_contents('/home/USER/public_html/wp-config.php');
preg_match("/define\s*\(\s*'DB_NAME'\s*,\s*'([^']+)'/", $cfg, $m); $dbname = $m[1];
preg_match("/define\s*\(\s*'DB_USER'\s*,\s*'([^']+)'/", $cfg, $m); $dbuser = $m[1];
preg_match("/define\s*\(\s*'DB_PASSWORD'\s*,\s*'([^']+)'/", $cfg, $m); $dbpass = $m[1];
preg_match("/define\s*\(\s*'DB_HOST'\s*,\s*'([^']+)'/", $cfg, $m); $dbhost = $m[1];
$db = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
```

---

## 4. CACHE — W3 Total Cache (W3TC)

### Configuração identificada
- Engine: `file_generic` (Disk Enhanced) — Apache serve HTML estático, PHP bypassed
- Cache path: `/home/USER/public_html/wp-content/cache/page_enhanced/`

### Limpar cache (OBRIGATÓRIO após toda mudança)
```php
// Script PHP via Fileman API
function rmrf($d){
    if(!is_dir($d)) return 0;
    $c=0;
    foreach(scandir($d) as $i){
        if($i==='.'||$i==='..') continue;
        $p=$d.'/'.$i;
        $c += is_dir($p) ? rmrf($p) : (unlink($p)?1:0);
    }
    rmdir($d);
    return $c;
}
echo rmrf('/home/USER/public_html/wp-content/cache/page_enhanced/')." arquivos removidos";
```

### wp-cli NÃO EXISTE no servidor
Não tente `wp cache flush` — o binário não está instalado. Use o rm -rf acima.

### Sequência completa após qualquer mudança em PHP/CSS/JS
1. Modificar o arquivo via Fileman API
2. Limpar page cache (rmrf acima)
3. Reiniciar Apache (WHM API) → limpa OPcache
4. Verificar resultado com fetch do HTML: `opener.open(req).read()`

---

## 5. PROBLEMAS CONHECIDOS E SOLUÇÕES

### ⚠️ Bug .htaccess após flush W3TC
**Sintoma:** Após limpar o cache, paths de rewrite ficam errados, site pode quebrar.
**Fix:**
```bash
# Via script PHP no servidor:
<?php
$htaccess = file_get_contents('/home/USER/public_html/.htaccess');
$fixed = str_replace(
    '%{DOCUMENT_ROOT}/home/USER/public_html/wp-content/',
    '%{DOCUMENT_ROOT}/wp-content/',
    $htaccess
);
file_put_contents('/home/USER/public_html/.htaccess', $fixed);
echo "Fixed";
?>
```
**Verificar TTFB:** deve ser < 0.3s após fix.

### ⚠️ Sessão cPanel expira (HTTP 401 / redirect para login)
**Sintoma:** A resposta da UAPI retorna HTML do login cPanel em vez de JSON.
**Fix:** Renovar sessão — reexecutar os Passos 1 e 2 do fluxo de acesso. A sessão tem vida curta (~10 minutos sem uso).

### ⚠️ OPcache PHP serve versão antiga do arquivo
**Sintoma:** Você atualizou um .php, mas o comportamento não muda.
**Fix:** Reiniciar Apache via WHM API (mata OPcache completamente).

### ⚠️ CSS/JS não atualiza para o usuário
**Causa possível 1:** W3TC servindo HTML cacheado com URL antiga do CSS.
**Causa possível 2:** WordPress enfileira CSS com versão (`?ver=X.X`) — se o `ver` não muda, browser usa cache.
**Fix:** Limpar page_enhanced + reiniciar Apache. Se ainda persistir, adicionar `touch($cssfile)` para atualizar mtime.

### ⚠️ UnicodeEncodeError no terminal Windows (cp1252)
**Sintoma:** `UnicodeEncodeError: 'charmap' codec can't encode character`
**Fix:** Adicionar no início de todo script Python:
```python
import sys
sys.stdout.reconfigure(encoding='utf-8')
```

### ⚠️ Botão/elemento não some apesar do CSS `display:none!important`
**Causa real provável:** Você está buscando o elemento errado. O nome do botão pode ser diferente do que o usuário descreveu.
**Procedimento correto:**
1. Fazer fetch do HTML da página: `opener.open(req).read()`
2. Buscar o texto EXATO do botão no HTML
3. Só então agir

### ⚠️ Plugin OWL Carousel sobrescreve display:none via JS
**Sintoma:** CSS `display:none!important` no container do carousel não funciona — o OWL re-inicializa e mostra o elemento.
**Fix triplo:**
1. CSS nuclear: `.owl-carousel-NOME { display:none!important; }`
2. JS window.load que remove o elemento do DOM após init
3. DB fix: esvaziar `post_content` dos posts do carousel no banco (remove o conteúdo na fonte)

---

## 6. PADRÃO DE SCRIPT PYTHON COMPLETO

Template reutilizável para qualquer operação no servidor:

```python
import urllib.request, urllib.parse, http.cookiejar, json, ssl, base64, sys
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(
    urllib.request.HTTPSHandler(context=ctx),
    urllib.request.HTTPCookieProcessor(cj)
)

# === CONFIGURAR PARA O PROJETO ===
WHM_PASS  = "SENHA_ROOT_WHM"
CP_USER   = "USUARIO_CPANEL_DO_DOMINIO"
HOME_DIR  = f"/home/{CP_USER}/public_html"
DOMAIN    = "dominio.com.br"
# =================================

# Auth
whm_url = f"https://162.240.13.51:2087/json-api/create_user_session?api.version=1&user={CP_USER}&service=cpaneld"
req = urllib.request.Request(whm_url)
req.add_header("Authorization", f"Basic {base64.b64encode(f'root:{WHM_PASS}'.encode()).decode()}")
data = json.loads(opener.open(req).read())
session_url = data['data']['url']
token = session_url.split('/')[3]
cpanel_base = f"https://162.240.13.51:2083/{token}"
opener.open(session_url).read()

def read_file(path, filename):
    params = urllib.parse.urlencode({'dir': path, 'file': filename})
    with opener.open(f"{cpanel_base}/execute/Fileman/get_file_content?{params}") as r:
        return json.loads(r.read())['data']['content']

def write_file(path, filename, content):
    payload = urllib.parse.urlencode({'dir': path, 'file': filename, 'content': content}).encode()
    req = urllib.request.Request(f"{cpanel_base}/execute/Fileman/save_file_content", data=payload)
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    resp = json.loads(opener.open(req).read())
    return resp.get('status') == 1

def run_php(php_code, filename='_tmp_op.php'):
    write_file(HOME_DIR, filename, php_code)
    req = urllib.request.Request(f"https://162.240.13.51/{filename}")
    req.add_header("Host", DOMAIN)
    result = opener.open(req).read().decode('utf-8', errors='replace')
    write_file(HOME_DIR, filename, '<?php //')  # cleanup
    return result

def clear_cache():
    return run_php(r"""<?php
function rmrf($d){if(!is_dir($d))return 0;$c=0;foreach(scandir($d)as $i){if($i==='.'||$i==='..') continue;$p=$d.'/'.$i;$c+=is_dir($p)?rmrf($p):(unlink($p)?1:0);}rmdir($d);return $c;}
echo rmrf('""" + HOME_DIR + r"""/wp-content/cache/page_enhanced/');
?>""")

def restart_apache():
    url = "https://162.240.13.51:2087/json-api/restartservice?api.version=1&service=httpd"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Basic {base64.b64encode(f'root:{WHM_PASS}'.encode()).decode()}")
    return json.loads(opener.open(req).read())['metadata']['reason']

def fetch_page(path='/'):
    req = urllib.request.Request(f"https://162.240.13.51{path}")
    req.add_header("Host", DOMAIN)
    req.add_header("Cache-Control", "no-cache")
    return opener.open(req).read().decode('utf-8', errors='replace')
```

---

## 7. DIAGNÓSTICO INICIAL (checklist para novo projeto)

Execute nesta ordem ao começar um projeto novo no servidor:

```python
# 1. Verificar qual WP install está ativo e tema
diagnostico = run_php(r"""<?php
$cfg = file_get_contents('/home/USER/public_html/wp-config.php');
preg_match("/\\\$table_prefix\s*=\s*'([^']+)'/", $cfg, $m);
echo "prefix: ".(isset($m[1])?$m[1]:'check manually')."\n";

$db = /* conectar conforme seção 3 */;
foreach(['wp_','wps_'] as $p){
    $r = @$db->query("SELECT option_value FROM {$p}options WHERE option_name='template'");
    if($r && $row=$r->fetch_assoc()) echo "{$p}tema: ".$row['option_value']."\n";
    $r2 = @$db->query("SELECT option_value FROM {$p}options WHERE option_name='siteurl'");
    if($r2 && $row2=$r2->fetch_assoc()) echo "{$p}url: ".$row2['option_value']."\n";
}
?>""")

# 2. Verificar plugins ativos
plugins = run_php(r"""<?php /* query PREFIX_options WHERE option_name='active_plugins' */ ?>""")

# 3. Checar tamanho do cache atual
cache_size = run_php(r"""<?php
$dir = '/home/USER/public_html/wp-content/cache/';
$out = `du -sh $dir 2>/dev/null`;
echo $out ?: "cache vazio";
?>""")

# 4. Verificar TTFB do site
html = fetch_page('/')
print(f"HTML size: {len(html)}, has cache: {'<!-- Cached' in html}")
```

---

## 8. REGRAS DE OURO

1. **Sempre buscar o elemento exato no HTML antes de tentar remover/modificar**
   — Não confie na descrição verbal; faça fetch da página e procure o texto real.

2. **Sequência de deploy é sempre:** modificar → limpar cache → reiniciar Apache → verificar
   — Pular qualquer etapa garante horas de debugging desnecessário.

3. **Sessão cPanel expira rápido** — renovar com create_user_session antes de cada batch de operações.

4. **Scripts PHP temporários:** sempre limpar depois sobrescrevendo com `<?php //`

5. **Nunca usar subprocess/heredoc longo** — usar a Fileman API diretamente via Python urllib.

6. **Dois installs WP no mesmo DB** — sempre confirmar qual prefixo (`wp_` ou `wps_`) é o ativo antes de qualquer query UPDATE.

7. **OPcache** — toda mudança em PHP exige reinício do Apache para garantir o novo código ser executado.
