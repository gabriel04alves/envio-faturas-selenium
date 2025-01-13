# Faturas CELESC -> WhatsApp

## Descrição

Este projeto automatiza o envio de faturas da CELESC via WhatsApp utilizando o Selenium WebDriver. Ele extrai informações de faturas em PDF e envia mensagens formatadas para um contato específico no WhatsApp.

## Requisitos

- Python 3.12 ou superior
- Google Chrome
- ChromeDriver
- PDM (Python Dependency Manager)

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/gabriel04alves/faturas-celesc.git
   cd faturas-celesc
   ```

2. Instale as dependências utilizando o PDM:

   ```sh
   pdm install
   ```

3. Configure o ChromeDriver:
   - Baixe a versão compatível do [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) com seu Google Chrome.
   - Extraia o executável e mova-o para `/usr/bin` ou adicione-o ao seu PATH para fácil acesso.

## Configuração

## Uso

1. Execute o script principal:

   ```sh
   pdm run python core/main.py
   ```

2. Siga as instruções no terminal para escanear o QR code do WhatsApp e enviar a fatura automaticamente.

## Estrutura do Projeto

- `core/services/`: Contém os serviços principais, incluindo criação do WebDriver, envio de mensagens no WhatsApp, extração de dados do PDF e download da fatura.
- `core/config.py`: Configurações relacionadas ao Selenium WebDriver.
- `pyproject.toml`: Configurações do projeto e dependências gerenciadas pelo PDM.

## Problemas Conhecidos

- A execução do script pode falhar se a versão do ChromeDriver não for compatível com o Google Chrome instalado.
- O Selenium pode não reconhecer elementos do WhatsApp Web em caso de mudanças na interface do site.
- Certifique-se de que as permissões de acesso à internet e ao WhatsApp Web estejam liberadas.

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto.
2. Crie uma nova branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request para análise.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
