Day 1
=======

Decided to go relational way, because it was first I want to recall. Second 
option will be Mongo, especially data is JSON formatted and epic doesn't requires
extra features not covered by Mongo.

First created parser. Definitely nice to have cursor as context object but today
I decided not to spent much time - just stubs.


Day 2
========
Decided to refactor application in a slight domain-driven way. Added kernel pattern
to support diff databases. Tried jquery.datatables. Not sure this is best solution.
I think db connection have to be closed any way on the application interruption.
Worth to listen interrupt signal. 

Day 3
=========
Added js to maintain the page front-end logic.