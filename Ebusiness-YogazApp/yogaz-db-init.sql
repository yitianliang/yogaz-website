--
-- yogaz 
--

--
-- Insert user 
--

INSERT INTO user (firstName, lastName, username, password, email, address, address2, country, state, zip) VALUES ('Logan', 'Paul', 'loganpaul', '12345', 'loganpaul@gmail.com', 'Hollywood Blvd 24 5 1', 'Hollywood', 'USA', 'CA', '90210');
INSERT INTO user (firstName, lastName, username, password, email, address, address2, country, state, zip) VALUES ('Pedro', 'Sanchez', 'pedrosanchez', '12345', 'pedrosanchez@gmail.com', 'Palacio de la Moncloa 1', 'Madrid', 'Spain', 'None', '28091');
INSERT INTO user (firstName, lastName, username, password, email, address, address2, country, state, zip) VALUES ('Angela', 'Lee', 'angelalee', '12345', 'angelalee@gmail.com', 'China Street 4', 'Singapore', 'Singapore', 'None', '089692');
INSERT INTO user (firstName, lastName, username, password, email, address, address2, country, state, zip) VALUES ('Jing Ping', 'Xi', 'xijingping', '12345', 'xijingping@gmail.com', 'Tian an men 1', 'Beijing', 'China', 'None', '3000000001ABC');
INSERT INTO user (firstName, lastName, username, password, email, address, address2, country, state, zip) VALUES ('Pablo', 'Escobar', 'whitechristmas', '12345', 'pabloescobar_plataoplomo@gmail.com', 'Avenida de la raya', 'Medellin', 'Colombia', 'None', 'EK213912');

--
-- Insert trainer 
--

INSERT INTO trainer (firstName, lastName, description) VALUES ('Michael','Stretchwell','Michael has a lot of experience and can stretch really well!');
INSERT INTO trainer (firstName, lastName, description) VALUES ('Sandra','Shortleggs','Sandra is quite helpful with the forms, but not quite tall');
INSERT INTO trainer (firstName, lastName, description) VALUES ('Bruce','Lee','Bruce is from Hong Kong but raised in San Francisco, he alternates yoga with martial arts');



--
-- Insert Schedule 
--

INSERT INTO classSchedule (trainerID, dateTime, durationMin, description) VALUES (1, '20190930 10:00:00 AM', 60, 'Yoga Advanced');
INSERT INTO classSchedule (trainerID, dateTime, durationMin, description) VALUES (2, '20190930 11:00:00 AM', 60, 'Yoga Advanced');
INSERT INTO classSchedule (trainerID, dateTime, durationMin, description) VALUES (3, '20190930 12:00:00 AM', 60, 'Yoga Advanced');
INSERT INTO classSchedule (trainerID, dateTime, durationMin, description) VALUES (1, '20191001 10:00:00 AM', 60, 'Yoga Advanced');

-
-- Insert Bookings 
--

INSERT INTO booking (classScheduleId, userID) VALUES (1, 1);
INSERT INTO booking (classScheduleId, userID) VALUES (2, 2);
INSERT INTO booking (classScheduleId, userID) VALUES (3, 3);
INSERT INTO booking (classScheduleId, userID) VALUES (1, 4);
INSERT INTO booking (classScheduleId, userID) VALUES (2, 5);
INSERT INTO booking (classScheduleId, userID) VALUES (3, 6);
INSERT INTO booking (classScheduleId, userID) VALUES (1, 7);
INSERT INTO booking (classScheduleId, userID) VALUES (2, 8);
INSERT INTO booking (classScheduleId, userID) VALUES (3, 9);
INSERT INTO booking (classScheduleId, userID) VALUES (1, 10);
INSERT INTO booking (classScheduleId, userID) VALUES (2, 10);
INSERT INTO booking (classScheduleId, userID) VALUES (3, 10);
INSERT INTO booking (classScheduleId, userID) VALUES (1, 12);
INSERT INTO booking (classScheduleId, userID) VALUES (2, 12);
