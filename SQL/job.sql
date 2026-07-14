CREATE TABLE IF NOT EXISTS jobs
(
    job_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    recruiter_profile_id INTEGER NOT NULL,
    job_title VARCHAR(100) NOT NULL,
    job_description TEXT NOT NULL,
    job_type VARCHAR(30) NOT NULL
        CHECK(job_type IN ('Full-Time','Internship','Part-Time','Contract')),
    work_mode VARCHAR(20) NOT NULL
        CHECK(work_mode IN ('On-Site','Remote','Hybrid')),
    location VARCHAR(100) NOT NULL,
    salary_min NUMERIC(10,2),
    salary_max NUMERIC(10,2),
    experience_required VARCHAR(50),
    cgpa_required NUMERIC(3,2),
    skills_required TEXT,
    openings INTEGER NOT NULL
        CHECK(openings > 0),
    application_deadline DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Open'
        CHECK(status IN ('Open','Closed','Draft')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_job_recruiter
        FOREIGN KEY(recruiter_profile_id)
        REFERENCES recruiter_profiles(recruiter_profile_id)
        ON DELETE CASCADE
);