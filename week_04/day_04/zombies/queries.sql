SELECT victims.*, zombies.name FROM victims 
INNER JOIN bitings ON victims.id = bitings.victim_id
INNER JOIN zombies ON bitings.zombie_id = zombies.id
WHERE bitings.zombie_id = 2;