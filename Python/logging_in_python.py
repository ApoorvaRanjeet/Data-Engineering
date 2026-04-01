'''1. logging:-> means recording info about what your program is doing.
instead of just printing output, you track events,errors and flow of execution.its basically used in real world problem.

2. its a built-in library means you dont have to install any extra packages to use it , you can simply import logging.

3. logging levels : 
    -> DEBUG: detailed info (for developers)
    -> INFO:  confirmation that things are working as expected.
    -> WARNING: something unexpected happend or about to happen.
    -> ERROR: indication that problem had occured
    -> CRITICAL: very serious failure
'''

import logging

logging.basicConfig(level=logging.INFO) # this is changing the logging level

def add(a, b):
    logging.info("Addition started") # instead of print 
    result = a + b
    logging.info(f"Result is {result}")
    return result

add(5, 3)

'''what does chaning logging levels mean?
first of all there is the logging level order 
    DEBUG < INFO < WARNING < ERROR < CRITICAL
Rule is if you set level=x then all 
the messages >=x will be showed and 
the messages <x will be ignored'''

import logging

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)

logging.debug("debug message")
logging.info("info message")
logging.warning("warning mesg")
logging.error("error msg")
logging.critical("critical msg")
    
    
'''how to store logs in a file
we simply use basicConfig() with filename.

basic things we should remember:
    filename-> stores the logs in file
    format-> make logs readable 
    filemode-> append or overwrite
    open()->read and test logs
'''

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.debug("debug message")
logging.info("info message")
logging.warning("warning mesg")
logging.error("error msg")
logging.critical("critical msg")

# add proper format 

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("app started")



import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide(a, b):
    logging.info("Division started")
    
    if b == 0:
        logging.error("Division by zero")
        return None
    
    result = a / b
    logging.info(f"Result: {result}")
    return result

divide(10, 2)
divide(5, 0)


''' by default logs are appended not deleted , so if you want to overwrite use the filemode ="w" to change it to overwrite mode'''

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    filemode="w"  #overwrite
)

logging.info("info ")
logging.warning("war")
logging.error("error")
logging.critical("critical")