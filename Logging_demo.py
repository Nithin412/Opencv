import logging

# logging.basicConfig(
#     level=logging.INFO,
#     filename="sample.log",
#     format="%(asctime)s :: %(levelname)s :: %(message)s",
# )

# a = int(input("enter the number a: "))
# b = int(input("enter the number b: "))


# def hypotenuse(a, b):
#     return (a ** 2 + b ** 2) ** 0.5


# logging.info("The hypotense of {0} and {1} is {2}".format(a, b, hypotenuse(a, b)))

# ----------------------------------------------------------------------------------------------------------
# similar code for the custom logger. In the above case it was using the root logger.
logger = logging.getLogger(__name__)
# now we need to set the level, filename to log, formatter
# setting the level
logger.setLevel(logging.INFO)
# setting the file handler and the formatter
file_handler = logging.FileHandler("sample.log")
formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

a = int(input("enter the number a: "))
b = int(input("enter the number b: "))
try:

    def div(a, b):
        return a / b

    logging.info("The Division of {0} and {1} is {2}".format(a, b, div(a, b)))
except ZeroDivisionError as exc:
    logging.info("Division cant be done because the denominator is Zero")
