CREATE TABLE students (
                          id SERIAL PRIMARY KEY,
                          first_name VARCHAR(100),
                          last_name VARCHAR(100),
                          email VARCHAR(100),
                          dob DATE,
                          gender VARCHAR(10),
                          class_id INT,
                      created_at date default current_timestamp
);
drop table students;

CREATE TABLE teachers (
                          id SERIAL PRIMARY KEY,
                          name VARCHAR(100),
                          email VARCHAR(100),
                          subject_id INT
);

CREATE TABLE classes (
                         id SERIAL PRIMARY KEY,
                         name VARCHAR(100),
                         teacher_id INT
);

CREATE TABLE subjects (
                          id SERIAL PRIMARY KEY,
                          name VARCHAR(100),
                          description TEXT
);

CREATE TABLE enrollments (
                             id SERIAL PRIMARY KEY,
                             student_id INT,
                             class_id INT
);

CREATE TABLE grades (
                        id SERIAL PRIMARY KEY,
                        student_id INT,
                        subject_id INT,
                        score FLOAT,
                        semester VARCHAR(20)
);