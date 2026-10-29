# 🛡️ SecurityCheck

**Ferramenta educacional para análise de conexões TLS, desenvolvida com Python e Flask.**

O SecurityCheck é uma aplicação web que permite verificar a versão do protocolo TLS negociada com um servidor e identificar problemas comuns na validação de certificados digitais.

## 🚀 Funcionalidades

- Verificação da versão TLS negociada com um servidor.
- Identificação de certificados expirados.
- Detecção de certificados autoassinados.
- Identificação de incompatibilidade entre domínio e certificado.
- Tratamento de erros de conexão SSL/TLS.
- Interface web com temática de terminal de segurança.

## 🛠️ Tecnologias utilizadas

- **Python** — lógica de verificação TLS.
- **Flask** — servidor e integração com a interface web.
- **HTML5** — estrutura da aplicação.
- **CSS3** — estilização da interface.
- **Git e GitHub** — versionamento do projeto.

## 📦 Como executar

Clone o repositório:

```bash
git clone https://github.com/viniciusvaz845-blip/SecurityCheck.git
cd SecurityCheck
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale o Flask:

```bash
pip install flask
```

Execute a aplicação:

```bash
python main.py
```

Acesse no navegador:

`http://127.0.0.1:5000`

## 🔍 Exemplos de testes

| Domínio | Resultado observado |
|---|---|
| `www.google.com` | TLS 1.3 |
| `expired.badssl.com` | Certificado expirado |
| `self-signed.badssl.com` | Certificado autoassinado |
| `wrong.host.badssl.com` | Nome do certificado incompatível |

*Os resultados podem variar conforme o ambiente e a configuração dos servidores.*

## ⚠️ Limitações

O SecurityCheck verifica a versão TLS negociada em uma conexão, mas ainda não identifica todas as versões TLS aceitas pelo servidor.

Esta é uma ferramenta educacional, não um scanner completo de vulnerabilidades.

## 🗺️ Próximas melhorias

- [ ] Adicionar interatividade com JavaScript.
- [ ] Implementar indicador de carregamento durante a consulta.
- [ ] Melhorar a apresentação dos resultados.
- [ ] Adicionar testes para diferentes versões TLS.
- [ ] Adaptar a interface para dispositivos móveis.

## 👨‍💻 Desenvolvedor

**Vinicius Vaz**

Estudante de Análise e Desenvolvimento de Sistemas, com foco em Segurança da Informação e desenvolvimento de ferramentas de cybersecurity.

Projeto desenvolvido como parte do aprendizado prático de Python, desenvolvimento web e protocolos de segurança.

---

**SecurityCheck — Aprendendo segurança, uma conexão por vez.**
