CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS
$$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$
LANGUAGE plpgsql;


CREATE TRIGGER student_profile_updated_at
BEFORE UPDATE
ON student_profiles
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();


CREATE TRIGGER recruiter_profile_updated_at
BEFORE UPDATE
ON recruiter_profiles
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();


CREATE TRIGGER job_updated_at
BEFORE UPDATE
ON jobs
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();


CREATE TRIGGER application_updated_at
BEFORE UPDATE
ON applications
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();