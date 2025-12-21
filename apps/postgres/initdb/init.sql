--- KURZY
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE courses (
    uuid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

INSERT INTO "public"."courses" ("uuid", "title", "description", "created_at", "updated_at") VALUES ('2dc16208-c341-4b06-8716-fffa602f3035', 'Vareni', 'Kurz o vareni', '2025-12-16', '2025-12-16'), ('33ab08cd-3f26-4c43-946f-7c15c838fd41', 'testim', 'probiha test', '2025-12-21', '2025-12-21');

--- KVIZY
CREATE TABLE quizzes (
    uuid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    uuid_course UUID NOT NULL,
    title TEXT NOT NULL,
    attempts INT DEFAULT 0,
    FOREIGN KEY (uuid_course) REFERENCES courses(uuid)
);

INSERT INTO "public"."quizzes" ("uuid", "uuid_course", "title", "attempts") VALUES ('ba0f6595-1b68-4107-b0e0-f351d15f295f', '2dc16208-c341-4b06-8716-fffa602f3035', 'Jak uvarit polevku', '0');

--- OTÁZKY
CREATE TABLE questions (
    uuid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    uuid_quiz UUID NOT NULL,
    type TEXT NOT NULL,
    options TEXT[] NOT NULL,
    correct INT[] NOT NULL,
    question TEXT NOT NULL,

    FOREIGN KEY (uuid_quiz) REFERENCES quizzes(uuid)
);

INSERT INTO "public"."questions" ("uuid", "uuid_quiz", "type", "options", "correct", "question") VALUES ('7669dc4c-ae2a-4cdd-91a3-029cbe72f9fb', 'ba0f6595-1b68-4107-b0e0-f351d15f295f', 'multipleChoice', ARRAY['Vyvar','Bomba','Rajska'], ARRAY[0,2], 'Co patri do polevky?'), ('b2908d1b-184b-4e32-ab68-63d4064f31f0', 'ba0f6595-1b68-4107-b0e0-f351d15f295f', 'singleChoice', ARRAY['ano','ne'], ARRAY[0], 'Patri do polevky sul?');