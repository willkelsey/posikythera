# Antikythera Simulation

## Software Design Process Model

The ideal software process model for this project is the incremental development model. This model is an efficient choice because a small set of the software can be built, and then will be expanded upon with each iteration of development. There will also be a small amount of integrate and configure regarding planetary motion. Equations and methods on 2-D planet modeling already exist, so these will be used and implemented to satisfy the requirements of the software. 

Specifications: Specifications will include the mass of the planet, the diameter of the planet, the centripetal velocity, rotations in a day, distance between the planets. More can be added between the initial versions and the intermediate versions.

Development: The first version will be a basic user input/output interface with a database/data structure. We should make sure that all functionality for the data structures are working. It would first only have data for the earth and the sun. Then, a second veriosn will add a 2-D GUI to model the solar system's behavior in an easier way for users. As the program moves towards a smoother model of the sun and the earth, more elements can be added into the program without complications. After the 2-D version is perfected, the 3-D version can be put into production.

Validation: The system can then be tested at a higher level to see if the program is accurate. All the data should make sense and the program should seem correct to the user. For example, a year would be much longer for a planet further away from the sun. Also, events, such as solar eclipses, should happen every so often.
