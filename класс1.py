from email.headerregistry import Group
from itertools import groupby
from msilib import Table
from msilib.schema import tables


class my_class(object):
    pass

CREATE TABLE Teachers (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Salary DECIMAL(10, 2),
    HireDate DATE
);

