# 📋 Proposta de Projeto: Infrastructure Health Monitor

## 🎯 Ideia do Projeto

Criar um sistema completo de monitoramento que colete métricas do sistema operacional (CPU, memória, disco, rede) e as exiba em dashboards visuais. O projeto deve usar **todas as suas skills** de forma integrada.

---

## 🏗️ Arquitetura Sugerida

### Componentes Principais:

1. **Coletor Python** → Scripts que coletam métricas do sistema
2. **Prometheus** → Armazena as métricas (time-series database)
3. **Grafana** → Dashboard visual das métricas
4. **Docker Compose** → Orquestra tudo localmente
5. **Terraform** → Provisiona infraestrutura na AWS (Free Tier)
6. **GitHub Actions** → Pipeline CI/CD automatizado
7. **CloudWatch** → Integração com métricas AWS

---

## 📚 Termos Técnicos Importantes (Usados nas Empresas)

### **DevOps & Infraestrutura**

- **IaC (Infrastructure as Code)**: Gerenciar infraestrutura através de código (Terraform)
- **Idempotência**: Aplicar a mesma configuração múltiplas vezes produz o mesmo resultado
- **State Management**: Terraform guarda o "estado" da infraestrutura criada
- **Provider**: Plugin do Terraform que interage com um serviço (AWS, Azure, etc)
- **Resource**: Um recurso a ser criado (ex: EC2 instance, Security Group)
- **Module**: Bloco reutilizável de código Terraform

### **Containerização**

- **Dockerfile**: Receita para criar uma imagem Docker
- **Image**: Template imutável de um container
- **Container**: Instância em execução de uma imagem
- **Docker Compose**: Ferramenta para orquestrar múltiplos containers
- **Volume**: Armazenamento persistente para containers
- **Network**: Rede isolada entre containers

### **Observabilidade**

- **Metrics**: Dados numéricos coletados ao longo do tempo (ex: CPU %, memória)
- **Time-Series Database**: Banco otimizado para dados com timestamp (Prometheus)
- **Scrape/Scraping**: Processo de coletar métricas periodicamente
- **Exporter**: Componente que expõe métricas em formato Prometheus
- **Gauge**: Tipo de métrica que pode subir ou descer (ex: memória usada)
- **Counter**: Tipo de métrica que só aumenta (ex: total de requisições)
- **Histogram**: Distribuição de valores (ex: latência de requisições)
- **Dashboard**: Visualização gráfica de métricas
- **Alerting**: Sistema de alertas baseado em regras (ex: CPU > 80%)

### **CI/CD**

- **Pipeline**: Sequência automatizada de passos (build → test → deploy)
- **Workflow**: Configuração de um pipeline no GitHub Actions
- **Job**: Unidade de trabalho em um workflow (ex: job de testes)
- **Step**: Ação individual dentro de um job
- **Artifact**: Arquivo gerado por um job (ex: imagem Docker)
- **Secret**: Variável sensível armazenada de forma segura
- **Trigger**: Evento que inicia o pipeline (ex: push para main)

### **AWS (Free Tier)**

- **EC2**: Servidor virtual na nuvem
- **t2.micro**: Tipo de instância EC2 gratuito (750h/mês)
- **VPC**: Rede virtual privada isolada
- **Subnet**: Subdivisão de uma VPC
- **Security Group**: Firewall virtual (controle de tráfego)
- **AMI**: Imagem de máquina (template de SO)
- **Elastic IP**: IP público fixo e estável
- **EBS**: Disco virtual (storage)
- **CloudWatch**: Serviço de monitoramento e logs da AWS
- **IAM**: Gerenciamento de acesso e permissões

### **Python & Automação**

- **psutil**: Biblioteca Python para coletar métricas do sistema
- **prometheus-client**: Biblioteca para criar exporters Prometheus
- **boto3**: SDK Python oficial da AWS
- **Exporter Pattern**: Padrão onde um serviço expõe métricas via HTTP

---

## 🎓 Dicas de Como Fazer

### **Fase 1: Ambiente Local (Docker Compose)**

**Objetivo**: Ter tudo rodando na sua máquina primeiro

**O que fazer:**
1. Criar um script Python que coleta métricas usando `psutil`
2. Criar um exporter que expõe essas métricas em formato Prometheus (HTTP endpoint `/metrics`)
3. Criar um `docker-compose.yml` com:
   - Seu container Python (coletor)
   - Prometheus (scraping do seu coletor)
   - Grafana (visualização)
4. Criar configuração do Prometheus (`prometheus.yml`) apontando para seu coletor

**Dica**: Use `prometheus-client` do Python. É simples!

---

### **Fase 2: Terraform (AWS)**

**Objetivo**: Provisionar infraestrutura na AWS

**O que fazer:**
1. Criar um `main.tf` com:
   - Provider AWS
   - Security Group (abrir portas 22, 3000, 9090)
   - EC2 instance (t2.micro, Amazon Linux 2023)
   - Elastic IP (opcional, mas útil)
2. No `user_data` da EC2, instalar Docker e Docker Compose
3. Criar `variables.tf` e `outputs.tf`
4. Usar `terraform.tfvars` para suas variáveis (não commitar!)

**Dica**: Use VPC padrão e subnets padrão para simplificar (Free Tier)

---

### **Fase 3: CI/CD (GitHub Actions)**

**Objetivo**: Automatizar testes e deploy

**O que fazer:**
1. Criar `.github/workflows/ci-cd.yml`
2. Jobs sugeridos:
   - **Test**: Validar código Python (flake8, pytest se tiver testes)
   - **Terraform Validate**: Validar arquivos Terraform
   - **Build**: Build da imagem Docker (opcional)
   - **Deploy**: Apenas em push para `main` → aplicar Terraform

**Dica**: Use secrets do GitHub para AWS credentials e SSH keys

---

### **Fase 4: CloudWatch Integration**

**Objetivo**: Enviar métricas para CloudWatch

**O que fazer:**
1. Criar um script Python separado que usa `boto3`
2. Enviar métricas customizadas para CloudWatch (put_metric_data)
3. Intervalo sugerido: 5 minutos (Free Tier permite 10 métricas customizadas)

**Dica**: Namespace customizado facilita organização (ex: `InfrastructureHealthMonitor`)

---

## 🎯 Estrutura de Pastas Sugerida

```
seu-projeto/
├── src/
│   ├── collector/          # Scripts Python de coleta
│   └── cloudwatch/         # Integração CloudWatch
├── terraform/              # Código Terraform
├── prometheus/             # Config Prometheus
├── grafana/                # Dashboards e provisioning
├── docker/                 # Dockerfile
├── .github/workflows/      # GitHub Actions
├── docker-compose.yml      # Orquestração local
└── requirements.txt        # Dependências Python
```

---

## ✅ Checklist de Objetivos

- [ ] Coletor Python coletando métricas reais (CPU, memória, disco, rede)
- [ ] Métricas expostas em formato Prometheus
- [ ] Prometheus coletando as métricas
- [ ] Grafana conectado ao Prometheus
- [ ] Dashboard no Grafana mostrando gráficos
- [ ] Docker Compose rodando tudo localmente
- [ ] Terraform criando EC2 na AWS (t2.micro)
- [ ] Security Groups configurados corretamente
- [ ] Aplicação rodando na EC2 via Docker Compose
- [ ] GitHub Actions validando código
- [ ] Pipeline CI/CD fazendo deploy automático
- [ ] CloudWatch recebendo métricas customizadas

---

## 🚨 Dicas Importantes

1. **Comece simples**: Primeiro faça funcionar localmente, depois leve para AWS
2. **Free Tier**: Use sempre `t2.micro` e fique dentro dos limites
3. **Segurança**: Não commite credenciais! Use `.gitignore` e secrets
4. **Documentação**: Anote tudo que você aprendeu no caminho
5. **Teste incrementalmente**: Não tente fazer tudo de uma vez

---

## 📖 Recursos para Consultar

- **Terraform AWS Provider Docs**: https://registry.terraform.io/providers/hashicorp/aws/latest/docs
- **Prometheus Python Client**: https://github.com/prometheus/client_python
- **psutil Docs**: https://psutil.readthedocs.io/
- **Docker Compose Docs**: https://docs.docker.com/compose/
- **GitHub Actions**: https://docs.github.com/en/actions

---

**Lembre-se**: O objetivo é você **implementar** e **aprender** fazendo! Não tenha pressa. 🚀
