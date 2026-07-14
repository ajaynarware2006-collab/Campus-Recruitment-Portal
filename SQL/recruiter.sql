-- Stores the personal profile information of recruiter

-- used in 
-- recruiter dashboard
-- post job application
-- profile page

-- relation
-- 1 User and 1 recruiter profile

CREATE TABLE IF NOT EXISTS recruiter_profiles(
    recruiter_profile_id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE,
    hr_name VARCHAR(100) NOT NULL,
    company_name VARCHAR(50) NOT NULL,
    designation TEXT NOT NULL CHECK (designation IN ('HR','Talent Acquisition','Recruiter')),
    user_role TEXT NOT NULL CHECK (user_role IN ('Student','Admim','Recruiter')),
    company_email VARCHAR(150) NOT NULL ,
    company_contact VARCHAR(15) NOT NULL,
    company_website TEXT,
    industry VARCHAR(100),
    company_size VARCHAR(30),
    headquarter VARCHAR(100),
    company_logo TEXT,
    company_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id)
    REFERENCES users(user_id));