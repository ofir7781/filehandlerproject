Hi,
Assumption that I made:
1. Each file line was in the following format: [function name], [comma separated list of arguments] so I did not check edge cases related to the line format.
2. It was written in the instructions "output file", so I was not sure if you want the method to return the file object or not. I did not return it from the method and instead
I create and place it in dedicated location - outputfiles directory.
3. I understood continues stream in a way that we get input file, and lines are still written to it after my program starts

Explanation of some design decisions that I made:
1. For handling adding more functions in the future I created a function package and used the __dict__ and callable methods to get all methods name from it. In this way, it will
dynamically include every new method that we will add to the existing package.
2. In order to deal with continues stream, I used 'with' statement that have full control of the file object and helps me to use the file object as iterable
and to control the file in a better way using memory management and etc, which handle this case as well.
3. I created json file handler class as well in order to show a generic way if we want in the future to replace text file to other formats, there is an infra that we
csn use and with minimal changes we can work with other types of formats as well.
