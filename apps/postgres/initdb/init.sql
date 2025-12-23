--- KURZY
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE public.courses (
    uuid UUID PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    "createdAt" TIMESTAMPTZ DEFAULT now() NOT NULL,
    "updatedAt" TIMESTAMPTZ DEFAULT now() NOT NULL
);

INSERT INTO "public"."courses" ("uuid", "name", "description", "createdAt", "updatedAt") VALUES ('2dc16208-c341-4b06-8716-fffa602f3035', 'Vareni', 'Kurz o vareni', '2025-12-16', '2025-12-16'), ('33ab08cd-3f26-4c43-946f-7c15c838fd41', 'testim', 'probiha test', '2025-12-21', '2025-12-21');

--- KVIZY
CREATE TABLE quizzes (
    uuid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    uuid_course UUID NOT NULL,
    title TEXT NOT NULL,
    attempts INT DEFAULT 0,
    FOREIGN KEY (uuid_course) REFERENCES courses(uuid) ON DELETE CASCADE
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

    FOREIGN KEY (uuid_quiz) REFERENCES quizzes(uuid) ON DELETE CASCADE
);

INSERT INTO "public"."questions" ("uuid", "uuid_quiz", "type", "options", "correct", "question") VALUES ('7669dc4c-ae2a-4cdd-91a3-029cbe72f9fb', 'ba0f6595-1b68-4107-b0e0-f351d15f295f', 'multipleChoice', ARRAY['Vyvar','Bomba','Rajska'], ARRAY[0,2], 'Co patri do polevky?'), ('b2908d1b-184b-4e32-ab68-63d4064f31f0', 'ba0f6595-1b68-4107-b0e0-f351d15f295f', 'singleChoice', ARRAY['ano','ne'], ARRAY[0], 'Patri do polevky sul?');

--- MATERIÁLY
CREATE TABLE public.materials (
    uuid UUID PRIMARY KEY,
    type VARCHAR(10) NOT NULL CHECK (type IN ('file', 'url')),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    "fileUrl" TEXT,          
    "mimeType" VARCHAR(100), 
    "sizeBytes" INT,  
    url TEXT,              
    uuid_course UUID NOT NULL REFERENCES public.courses(uuid) ON DELETE CASCADE
);

INSERT INTO "public"."materials" ("uuid", "type", "name", "description", "fileUrl", "mimeType", "sizeBytes", "url", "uuid_course") VALUES ('653cae99-39d8-46d6-986a-787dfe4107f0', 'url', 'twitch', 'odkaz na twitch', null, null, null, 'https://www.twitch.tv/soraval1', '2dc16208-c341-4b06-8716-fffa602f3035'), ('c8a35fdd-f72e-44e4-bd9a-8b6391c76dce', 'file', 'obrazek', 'Obrazek pejska', 'src/files/obrazek.png', 'image/png', '67000', null, '33ab08cd-3f26-4c43-946f-7c15c838fd41');

--- FEED
CREATE TABLE public.feed (
    uuid UUID PRIMARY KEY,
    type VARCHAR(50),
    message TEXT NOT NULL,
    edited BOOLEAN NOT NULL DEFAULT false,
    "createdAt" TIMESTAMPTZ NOT NULL DEFAULT now(),
    "updatedAt" TIMESTAMPTZ,
    uuid_course UUID NOT NULL REFERENCES public.courses(uuid) ON DELETE CASCADE
);

INSERT INTO "public"."feed" ("uuid", "type", "message", "edited", "createdAt", "updatedAt", "uuid_course") VALUES ('53f0ee29-563b-4b8f-baee-5ec94edb185c', 'manual', 'Test zitra', 'false', '2025-12-22 23:44:21+00', null, '2dc16208-c341-4b06-8716-fffa602f3035');
