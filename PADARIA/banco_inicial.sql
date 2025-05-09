-- Criar banco de dados e tabela
CREATE DATABASE IF NOT EXISTS padaria;
USE padaria;

CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL
);
