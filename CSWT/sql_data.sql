# Тестовые данные для таблиц

INSERT INTO Roles (role_name, description) VALUES
('Client', 'Клиент, создающий заявки и отслеживающий их.'),
('Admin', 'Администратор системы, управляющий пользователями и системой'),
('Deleted', 'Удаленный пользователь'),
('ASU_staff', 'Сотрудник АСУ, работающий с заявками и помогающий клиентам.');

INSERT INTO Statuses (status_name, description) VALUES
('Новая', 'Заявка создана и ожидает обработки.'),
('Назначена', 'Заявка назначена и находится в обработке.'),
('Решена', 'Заявка решена и ожидает подтверждения.'),
('Закрыта', 'Заявка закрыта после решения.'),
('Отклонена', 'Заявка отклонена как неактуальная.');

INSERT INTO Priorities (priority_name, description) VALUES
('Низкий', 'Заявка может быть отложена.'),
('Средний', 'Заявка требует решения в течение дня.'),
('Высокий', 'Заявка требует срочного решения.'),
('Критический', 'Заявка требует немедленного решения.');

INSERT INTO Departments (department_name, description) VALUES
('Техническая поддержка', 'Решение технических проблем'),
('Разработка', 'Разработка новых функций'),
('Администрация', 'Управление системой'),
('Клиентский сервис', 'Работа с клиентами');

INSERT INTO Users (username, password, first_name, last_name, email, phone_number, role_id) VALUES
('q', 'q', 'Иван', 'Петров', 'admin@example.com', '+79161234567', 2),  # Admin
('tech_support', '$2a$10$xJwL5v5Jz5UZJf5h5f5X5e', 'Сергей', 'Иванов', 'tech@example.com', '+79163234567', 4),  # ASU_staff
('client1', '$2a$10$xJwL5v5Jz5UZJf5h5f5X5e', 'Ольга', 'Смирнова', 'client1@example.com', '+79164234567', 1),  # Client
('client2', '$2a$10$xJwL5v5Jz5UZJf5h5f5X5e', 'Алексей', 'Козлов', 'client2@example.com', '+79165234567', 1),  # Client
('support1', '$2a$10$xJwL5v5Jz5UZJf5h5f5X5e', 'Мария', 'Павлова', 'support1@example.com', '+79166234567', 4),  # ASU_staff
('inactive_user', '$2a$10$xJwL5v5Jz5UZJf5h5f5X5e', 'Дмитрий', 'Сидоров', 'inactive@example.com', '+79167234567', 3);  # Deleted

INSERT INTO Tickets (title, description, solution, closed_at, client_id, priority_id, status_id, assigned_to) VALUES
('Не работает вход', 'Ошибка при авторизации', 'Исправлена конфигурация', '2023-05-15 14:30:00', 3, 3, 4, 2),
('Медленная работа', 'Система тормозит', 'Оптимизированы запросы', NULL, 4, 2, 2, 2),
('Проблема с отчетом', 'Не формируется PDF', NULL, NULL, 3, 1, 1, NULL),
('Доступ к панели', 'Нет прав для раздела', 'Настроены права', '2023-05-10 11:20:00', 4, 2, 4, 5);

INSERT INTO Comments (comment_text, ticket_id, user_id) VALUES
('Проблема воспроизводится', 1, 3),
('Принял в работу', 1, 2),
('Исправлено', 1, 2),
('Подтверждаю решение', 1, 3),
('Проверяю проблему', 2, 5),
('Нашел причину', 2, 5),
('Нужны дополнительные данные', 3, 2);

INSERT INTO User_Departments (user_id, department_id) VALUES
(1, 3),  # admin в Администрации
(2, 1),  # tech_support в Техподдержке
(5, 1),  # support1 в Техподдержке
(3, 4),  # client1 в Клиентском сервисе
(4, 4);  # client2 в Клиентском сервисе