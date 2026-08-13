use rent;

SELECT * FROM rent.api_user;

INSERT INTO api_user (
    password, 
    is_superuser, 
    username, 
    first_name, 
    last_name, 
    is_staff, 
    is_active, 
    date_joined, 
    email, 
    telephone, 
    user_type
) VALUES
('123', 0, 'ana_silva', 'Ana', 'Silva', 0, 1, '2026-08-13 10:00:00', 'ana.silva@email.com', '19981112233', 'USER'),
('123', 0, 'carlos_eduardo', 'Carlos', 'Eduardo', 0, 1, '2026-08-13 10:05:00', 'carlos.eduardo@email.com', '19982223344', 'USER'),
('123', 0, 'beatriz_souza', 'Beatriz', 'Souza', 0, 1, '2026-08-13 10:10:00', 'beatriz.souza@email.com', '19983334455', 'USER'),
('123', 0, 'lucas_mendes', 'Lucas', 'Mendes', 0, 1, '2026-08-13 10:15:00', 'lucas.mendes@email.com', '19984445566', 'USER'),
('123', 0, 'mariana_rocha', 'Mariana', 'Rocha', 0, 1, '2026-08-13 10:20:00', 'mariana.rocha@email.com', '19985556677', 'USER'),
('123', 0, 'felipe_santos', 'Felipe', 'Santos', 0, 1, '2026-08-13 10:25:00', 'felipe.santos@email.com', '19986667788', 'USER'),
('123', 0, 'camila_lima', 'Camila', 'Lima', 0, 1, '2026-08-13 10:30:00', 'camila.lima@email.com', '19987778899', 'USER'),
('123', 0, 'gabriel_alves', 'Gabriel', 'Alves', 0, 1, '2026-08-13 10:35:00', 'gabriel.alves@email.com', '19988889900', 'USER'),
('123', 0, 'larissa_costa', 'Larissa', 'Costa', 0, 1, '2026-08-13 10:40:00', 'larissa.costa@email.com', '19999990011', 'USER'),
('123', 1, 'admin_geral', 'Admin', 'Geral', 1, 1, '2026-08-13 10:45:00', 'admin.geral@email.com', '19977776655', 'ADMIN');