--
-- yogaz 
--
CREATE TABLE user (
  userId INTEGER PRIMARY KEY,
  firstName TEXT NOT NULL,
  lastName TEXT NOT NULL,
  username TEXT NOT NULL,
  password TEXT NOT NULL,
  email TEXT NOT NULL,
  address TEXT NOT NULL,
  address2 TEXT,
  country TEXT NOT NULL,
  state TEXT,
  zip TEXT
);
--
CREATE TABLE trainer (
  trainerId INTEGER PRIMARY KEY,
  firstName TEXT NOT NULL,
  lastName TEXT NOT NULL,
  description TEXT
);

--
CREATE TABLE classSchedule (
  classScheduleId INTEGER PRIMARY KEY,
  trainerID INTEGER NOT NULL,
  dateTime TIMESTAMP NOT NULL, 
  durationMin INTEGER NOT NULL,
  description TEXT, 
  FOREIGN KEY(trainerID) REFERENCES trainer(trainerId)
);
--
CREATE TABLE booking (
  bookingId INTEGER PRIMARY KEY,
  classScheduleId INTEGER,
  userID INTEGER,
  FOREIGN KEY(classScheduleId) REFERENCES classSchedule(classScheduleId),
  FOREIGN KEY(UserId) REFERENCES user(userId)
);



