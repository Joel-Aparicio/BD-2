-- Caso a tabela já exista, ela será removida
DROP TABLE IF EXISTS P_Utilizador;

-- Criar a tabela com as colunas necessárias
CREATE TABLE P_Utilizador (
    utilizador_id SERIAL PRIMARY KEY,       -- Chave primária com incremento automático
    nome VARCHAR(50) NOT NULL,              -- Nome do utilizador, obrigatório
    email VARCHAR(200) NOT NULL UNIQUE,     -- Email obrigatório e único
    palavra_passe VARCHAR(200) NOT NULL,    -- Palavra-passe obrigatória
    ser_admin BOOL NOT NULL DEFAULT FALSE,  -- Indica se é admin, com valor padrão FALSE
    last_login TIMESTAMP,                   -- Data e hora do último login
    is_active BOOL NOT NULL DEFAULT TRUE    -- Indica se a conta está ativa
);

-- Inserir Valores

-- Utilizador Normal
INSERT INTO P_Utilizador (nome, email, palavra_passe) 
VALUES ('Marco Vicente', 'marco.vicente@email.com', 'senha123');

-- Administrador
INSERT INTO P_Utilizador (nome, email, palavra_passe, ser_admin) 
VALUES ('Miguel Silva', 'miguel.silva@email.com', 'senha123', TRUE);

-- Mostrar a tabela para verificar os dados
SELECT * 
FROM P_Utilizador;
