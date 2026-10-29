import socket
import ssl

print('==========================')
print('    SecurityCheck v1.0    ')
print('==========================')

print("Ferramenta de análise básica de segurança")

def verificar_tls(site):
    if site:
        print(f"Preparando análise de: {site}")

        try:
            contexto = ssl.create_default_context()

            with socket.create_connection((site, 443), timeout=5) as conexao:
                with contexto.wrap_socket(conexao, server_hostname=site) as conexao_segura:
                    return f"Versão TLS: {conexao_segura.version()}"

        except ssl.SSLError as e:
            return f"Falha na conexão TLS: {e}"

        except socket.gaierror:
            return "Erro: não foi possível encontrar o domínio informado."

        except TimeoutError:
            return "Erro: o servidor demorou demais para responder."



    else:
        return "Erro: nenhum domínio informado."