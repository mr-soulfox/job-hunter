-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_UsersListed" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "created_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "url" TEXT NOT NULL,
    "number_of_connections" INTEGER NOT NULL,
    "company" TEXT NOT NULL DEFAULT 'None'
);
INSERT INTO "new_UsersListed" ("created_at", "id", "number_of_connections", "url") SELECT "created_at", "id", "number_of_connections", "url" FROM "UsersListed";
DROP TABLE "UsersListed";
ALTER TABLE "new_UsersListed" RENAME TO "UsersListed";
CREATE UNIQUE INDEX "UsersListed_url_key" ON "UsersListed"("url");
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
