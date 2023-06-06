-- CreateTable
CREATE TABLE "UsersListed" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "created_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "url" TEXT NOT NULL,
    "number_of_connections" INTEGER NOT NULL
);

-- CreateTable
CREATE TABLE "UsersInformation" (
    "user_id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "role" TEXT NOT NULL,
    "status" TEXT NOT NULL,
    "birthday" TEXT NOT NULL,
    CONSTRAINT "UsersInformation_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "UsersListed" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "UsersContacts" (
    "user_id" TEXT NOT NULL PRIMARY KEY,
    "phone" TEXT,
    "email" TEXT,
    "email_provider" TEXT,
    CONSTRAINT "UsersContacts_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "UsersListed" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "SupportedLinks" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "platform" TEXT NOT NULL,
    "link" TEXT NOT NULL
);

-- CreateIndex
CREATE UNIQUE INDEX "UsersListed_url_key" ON "UsersListed"("url");

-- CreateIndex
CREATE UNIQUE INDEX "UsersInformation_user_id_key" ON "UsersInformation"("user_id");

-- CreateIndex
CREATE UNIQUE INDEX "UsersContacts_user_id_key" ON "UsersContacts"("user_id");

-- CreateIndex
CREATE UNIQUE INDEX "UsersContacts_phone_key" ON "UsersContacts"("phone");

-- CreateIndex
CREATE UNIQUE INDEX "UsersContacts_email_key" ON "UsersContacts"("email");

-- CreateIndex
CREATE UNIQUE INDEX "SupportedLinks_platform_key" ON "SupportedLinks"("platform");
