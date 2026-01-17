# 📊 Infrastructure Health Monitor

Sistema completo de monitoramento que coleta métricas do sistema operacional (CPU, memória, disco, rede) e as exibe em dashboards visuais usando Prometheus e Grafana.

## 🏗️ Arquitetura

O projeto é composto por:

- **Coletor Python** → Scripts que coletam métricas do sistema
- **Prometheus** → Armazena as métricas (time-series database)
- **Grafana** → Dashboard visual das métricas
- **Docker Compose** → Orquestra tudo localmente

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Docker** (versão 20.10 ou superior)
- **Docker Compose** (versão 2.0 ou superior)
- **Python** (versão 3.8 ou superior)
- **Git** (para clonar o repositório)

### Verificar instalações

```bash
# Verificar Docker
docker --version
docker compose version

# Verificar Python
python3 --version

# Verificar Git
git --version
```

## 🚀 Instalação e Execução

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/DavidMenezess/observabilidade-local.git
cd observabilidade-local
```

### Passo 2: Criar ambiente virtual Python

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
# No Linux/Mac:
source venv/bin/activate

# No Windows:
# venv\Scripts\activate
```

### Passo 3: Instalar dependências Python

```bash
pip install -r requirements.txt
```

As dependências instaladas serão:
- `psutil==5.9.6` - Para coletar métricas do sistema
- `prometheus-client==0.19.0` - Cliente Prometheus para Python

### Passo 4: Iniciar os serviços com Docker Compose

```bash
# Iniciar Prometheus e Grafana em background
docker compose up -d
```

Este comando irá:
- Baixar as imagens do Prometheus e Grafana (se necessário)
- Criar a rede `projeto_monitoring`
- Criar os volumes para persistência de dados
- Iniciar os containers

### Passo 5: Iniciar o coletor de métricas

Em um novo terminal, ative o ambiente virtual e execute:

```bash
# Ativar ambiente virtual (se ainda não estiver ativo)
source venv/bin/activate

# Executar o coletor
python3 -m src.collector.exporter
```

Você verá a mensagem:
```
Servidor iniciado na porta 8000
Acesse: http://localhost:8000/metrics
```

## 🌐 Acessos

Após iniciar todos os serviços, você pode acessar:

| Serviço | URL | Credenciais |
|---------|-----|-------------|
| **Prometheus** | http://localhost:9090 | N/A |
| **Grafana** | http://localhost:3000 | Usuário: `admin`<br>Senha: `admin` |
| **Métricas (Exporter)** | http://localhost:8000/metrics | N/A |

### Verificando se está tudo funcionando

1. **Prometheus**: Acesse http://localhost:9090 e verifique se está coletando métricas
2. **Grafana**: Acesse http://localhost:3000, faça login e configure o Prometheus como fonte de dados
3. **Métricas**: Acesse http://localhost:8000/metrics para ver as métricas em formato Prometheus

## 📁 Estrutura do Projeto

```
.
├── docker-compose.yml          # Configuração dos containers
├── requirements.txt            # Dependências Python
├── README.md                   # Este arquivo
├── PROPOSTA_PROJETO.md         # Documentação do projeto
│
├── src/                        # Código fonte Python
│   └── collector/
│       ├── __init__.py
│       ├── exporter.py         # Servidor HTTP que expõe métricas
│       └── metrics.py          # Funções para coletar métricas
│
├── prometheus/                 # Configuração do Prometheus
│   └── prometheus.yml          # Arquivo de configuração
│
└── grafana/                    # Configuração do Grafana
    └── dashboards/
        └── system-monitoring-adapted.json  # Dashboard pré-configurado
```

## 🔧 Configuração

### Prometheus

O arquivo `prometheus/prometheus.yml` está configurado para:
- Coletar métricas do próprio Prometheus
- Coletar métricas do exporter Python em `host.docker.internal:8000`
- Intervalo de coleta: 5 segundos para métricas do sistema

### Grafana

Credenciais padrão:
- **Usuário**: `admin`
- **Senha**: `admin`

⚠️ **Importante**: Altere a senha no primeiro login!

## 🛠️ Comandos Úteis

### Docker Compose

```bash
# Iniciar serviços
docker compose up -d

# Parar serviços
docker compose down

# Ver logs
docker compose logs -f

# Ver status dos containers
docker compose ps

# Reiniciar serviços
docker compose restart
```

### Verificar containers

```bash
# Listar containers rodando
docker ps

# Ver logs de um container específico
docker logs prometheus
docker logs grafana
```

### Parar tudo

```bash
# Parar o coletor Python: Pressione Ctrl+C no terminal onde está rodando

# Parar containers Docker
docker compose down
```

## 🐛 Troubleshooting

### Problema: "network projeto_monitoring declared as external, but could not be found"

**Solução**: O arquivo `docker-compose.yml` já está configurado para criar a rede automaticamente. Se ainda ocorrer, execute:

```bash
docker network create projeto_monitoring
docker compose up -d
```

### Problema: Porta já em uso

**Solução**: Verifique se as portas 3000, 8000 ou 9090 estão em uso:

```bash
# Linux/Mac
lsof -i :3000
lsof -i :8000
lsof -i :9090

# Ou pare os containers
docker compose down
```

### Problema: Prometheus não está coletando métricas

**Verificações**:
1. O coletor Python está rodando? Verifique em http://localhost:8000/metrics
2. O Prometheus consegue acessar o host? Verifique a configuração de `host.docker.internal`
3. Verifique os logs: `docker logs prometheus`

### Problema: Erro ao instalar dependências Python

**Solução**:
```bash
# Atualizar pip
pip install --upgrade pip

# Instalar novamente
pip install -r requirements.txt
```

## 📊 Métricas Coletadas

O sistema coleta as seguintes métricas:

- **CPU**: Percentual de uso e número de cores
- **Memória**: Percentual, usado e total (em bytes)
- **Disco**: Percentual, usado e total (em bytes)
- **Usuários**: Número de usuários conectados

## 🔄 Próximos Passos

Após rodar localmente, você pode:

1. Configurar dashboards no Grafana
2. Criar alertas no Prometheus
3. Expandir as métricas coletadas
4. Implementar a fase de deploy na AWS com Terraform

## 📝 Notas

- Os dados do Prometheus e Grafana são persistidos em volumes Docker
- O coletor Python precisa estar rodando para que o Prometheus colete métricas
- A primeira vez que rodar `docker compose up -d`, as imagens serão baixadas (pode demorar alguns minutos)

## 👤 Autor

**David Menezes**

- GitHub: [@DavidMenezess](https://github.com/DavidMenezess)
- LinkedIn: [david-menezes-3aa87018b](https://www.linkedin.com/in/david-menezes-3aa87018b)

## 📄 Licença

Este projeto é de uso educacional e para portfólio.

---

**Desenvolvido com ❤️ usando Python, Prometheus, Grafana e Docker**
