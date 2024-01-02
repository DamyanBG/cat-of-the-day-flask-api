-- Insert 4 users
INSERT INTO users (first_name, last_name, email, password)
VALUES
  ('User1', 'Last1', 'user1@example.com', 'password1'),
  ('User2', 'Last2', 'user2@example.com', 'password2'),
  ('User3', 'Last3', 'user3@example.com', 'password3'),
  ('User4', 'Last4', 'user4@example.com', 'password4');

-- Insert 4 cats (one for each user)
INSERT INTO current_round_cats (name, created_on, passport_id, microchip_id, photo_url, breed, user_pk, likes, dislikes, votes)
VALUES
  ('Cat1', NOW(), '000000000', '00000000"', 'https://dymboto.chickenkiller.com/index.php/s/jiFjAMqtJkq5S2R/preview', 'Breed1', (SELECT pk FROM users WHERE email = 'user1@example.com'), 0, 0, 0),
  ('Cat2', NOW(), '000000001', '000000001', 'https://dymboto.chickenkiller.com/index.php/s/5KR4e92Ao76DaWK/preview', 'Breed2', (SELECT pk FROM users WHERE email = 'user2@example.com'), 0, 0, 0),
  ('Cat3', NOW(), '000000002', '000000002', 'https://dymboto.chickenkiller.com/index.php/s/wRJpTrnz9Xar3Hc/preview', 'Breed3', (SELECT pk FROM users WHERE email = 'user3@example.com'), 0, 0, 0),
  ('Cat4', NOW(), '000000003', '000000003', 'https://dymboto.chickenkiller.com/index.php/s/qjcYtCHc6abSzrk/preview', 'Breed4', (SELECT pk FROM users WHERE email = 'user4@example.com'), 0, 0, 0);
