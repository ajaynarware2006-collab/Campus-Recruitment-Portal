CREATE TABLE IF NOT EXISTS applications
(
    application_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    job_id INTEGER NOT NULL,
    student_profile_id INTEGER NOT NULL,
    application_status VARCHAR(20)
        DEFAULT 'Applied'
        CHECK (
            application_status IN (
                'Applied',
                'Under Review',
                'Shortlisted',
                'Rejected',
                'Accepted',
                'Withdrawn'
            )
        ),
    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_application_job
        FOREIGN KEY(job_id)
        REFERENCES jobs(job_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_application_student
        FOREIGN KEY(student_profile_id)
        REFERENCES student_profiles(student_profile_id)
        ON DELETE CASCADE,
    CONSTRAINT unique_application
        UNIQUE(job_id, student_profile_id)
);