-- Caso a tabela já exista, ela será removida
DROP TABLE IF EXISTS P_Utilizador;

-- Criar a tabela com as colunas necessárias
CREATE TABLE P_Utilizador (
    utilizador_id SERIAL PRIMARY KEY,       -- Chave primária com incremento automático
    nome VARCHAR(50) NOT NULL,              -- Nome do utilizador, obrigatório
    email VARCHAR(200) NOT NULL UNIQUE,     -- Email obrigatório e único
    password VARCHAR(200) NOT NULL,    -- Palavra-passe obrigatória
    is_staff BOOL NOT NULL DEFAULT FALSE,  -- Indica se é admin, com valor padrão FALSE
	is_superuser BOOL NOT NULL DEFAULT FALSE,
    last_login TIMESTAMP,                   -- Data e hora do último login
    is_active BOOL NOT NULL DEFAULT TRUE    -- Indica se a conta está ativa
);


-- Mostrar a tabela para verificar os dados
SELECT * 
FROM P_Utilizador;