# Build notes — The Robot Vacuum's Best Excuse

This entry is a tiny Python program. It holds one excuse as a constant and
writes it to the output file the bounty asks for, then prints how many
characters it wrote. There is no input, no network call, no secret, and no
dependency beyond the Python standard library. It runs in well under a
second and always writes the same line, so repeated runs agree exactly.

The excuse itself went through two drafts. The first draft leaned on the
lidar blinking and the spot vanishing from the map, which was decent but
ended on a shrug. The second draft keeps the map as the joke's engine and
gives it a cleaner turn at the end: the vacuum did not miss the spot, the
map says the spot does not exist, and the vacuum trusts its map more than
the homeowner's eyes. That version is funnier because it sounds like the
machine itself talking, deadpan and certain, and the joke lands on the
first read with nothing left to explain.

Files in this repository: the program itself, a readme describing it, and
the license. That is the whole entry.
