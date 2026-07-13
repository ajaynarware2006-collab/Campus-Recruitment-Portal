-- Stores the personal profile information of student

-- used in 
-- student dashboard
-- job application
-- profile page

-- relation
-- 1 User and ! student profile

CREATE TABLE IF NOT EXISTS student_profiles(
    profile_id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name VARCHAR(254) NOT NULL,
    enrollment_no VARCHAR(15) UNIQUE NOT NULL,
    cgpa NUMERIC(3,2),
    profile_img_path TEXT,
    user_id INTEGER NOT NULL UNIQUE,
    branch VARCHAR(7) NOT NULL,
    semester INTEGER NOT NULL,
    contact  VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id)
    REFERENCES users(user_id)
)