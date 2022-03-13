BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "questions" (
	"category"	TEXT NOT NULL,
	"level"	INTEGER NOT NULL,
	"question"	TEXT NOT NULL,
	"options"	TEXT NOT NULL,
	"answer"	INTEGER NOT NULL,
	"explanation"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "terms and definitions" (
	"category"	TEXT NOT NULL,
	"level"	INTEGER NOT NULL,
	"term"	TEXT NOT NULL,
	"definition"	TEXT NOT NULL
);
COMMIT;
