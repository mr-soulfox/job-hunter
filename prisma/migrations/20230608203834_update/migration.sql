/*
  Warnings:

  - You are about to drop the column `number_of_connections` on the `UsersListed` table. All the data in the column will be lost.
  - You are about to drop the column `birthday` on the `UsersInformation` table. All the data in the column will be lost.
  - You are about to drop the column `status` on the `UsersInformation` table. All the data in the column will be lost.
  - Added the required column `public_id` to the `UsersInformation` table without a default value. This is not possible if the table is not empty.

*/
-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_UsersListed" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "created_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "url" TEXT NOT NULL,
    "company" TEXT NOT NULL DEFAULT 'None'
);
INSERT INTO "new_UsersListed" ("company", "created_at", "id", "url") SELECT "company", "created_at", "id", "url" FROM "UsersListed";
DROP TABLE "UsersListed";
ALTER TABLE "new_UsersListed" RENAME TO "UsersListed";
CREATE UNIQUE INDEX "UsersListed_url_key" ON "UsersListed"("url");
CREATE TABLE "new_UsersInformation" (
    "user_id" TEXT NOT NULL PRIMARY KEY,
    "public_id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "role" TEXT NOT NULL,
    "isStudent" BOOLEAN NOT NULL DEFAULT false,
    CONSTRAINT "UsersInformation_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "UsersListed" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);
INSERT INTO "new_UsersInformation" ("location", "name", "role", "user_id") SELECT "location", "name", "role", "user_id" FROM "UsersInformation";
DROP TABLE "UsersInformation";
ALTER TABLE "new_UsersInformation" RENAME TO "UsersInformation";
CREATE UNIQUE INDEX "UsersInformation_user_id_key" ON "UsersInformation"("user_id");
CREATE UNIQUE INDEX "UsersInformation_public_id_key" ON "UsersInformation"("public_id");
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
