CREATE DATABASE loja_games;

USE loja_games;

CREATE TABLE games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    genero VARCHAR(50),
    preco DECIMAL(10,2),
    estoque INT
);
