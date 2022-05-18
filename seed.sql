
DROP DATABASE IF EXISTS  adopt;

CREATE DATABASE adopt;

\c adopt

CREATE TABLE pets
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  species TEXT NOT NULL,
  photo_url TEXT,
  age INT,
  notes TEXT,
  available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO pets
  (name, species, photo_url, age, notes, available)
VALUES
  ('Woofly', 'dog', 'https://placekitten.com/250/250', 3, 'Incredibly adorable.', 't'),
  ('Porchetta', 'porcupine', 'https://placekitten.com/250/250', 4, 'Somewhat spiky!', 't'),
  ('Snargle', 'cat', 'https://placekitten.com/250/250', null, null, 't'),
  ('Dr. Claw', 'cat', null, null, null, 't');

