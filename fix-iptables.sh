#!/bin/bash
# Script para corrigir problemas de iptables do Docker

echo "🔧 Corrigindo iptables do Docker..."

# Parar Docker temporariamente
echo "Parando Docker..."
sudo systemctl stop docker

# Limpar chains antigas do Docker (se existirem)
echo "Limpando chains antigas..."
sudo iptables -t filter -F DOCKER-ISOLATION-STAGE-1 2>/dev/null || true
sudo iptables -t filter -F DOCKER-ISOLATION-STAGE-2 2>/dev/null || true
sudo iptables -t filter -X DOCKER-ISOLATION-STAGE-1 2>/dev/null || true
sudo iptables -t filter -X DOCKER-ISOLATION-STAGE-2 2>/dev/null || true

# Reiniciar Docker para recriar as chains
echo "Reiniciando Docker..."
sudo systemctl start docker

echo "✅ Docker reiniciado. Aguardando inicialização..."
sleep 5

echo "✅ Pronto! Tente rodar: docker compose up -d"
