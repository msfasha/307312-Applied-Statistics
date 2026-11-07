"""Approved student documents shared by packaging and release validation."""
LESSONS = ['01-introduction-to-r', 'r-02-basic-concepts', 'r-03-dplyr', 'r-04-ggplot2', '02-descriptive-statistics', '03-inferential-statistics']
PRACTICALS = ['practical-01-categorical-business-data', 'practical-02-numerical-business-data',
              'practical-03-association-and-groups']
EXTENDED = ['case-01-springville-herald', 'case-02-oxford-cereal', 'case-03-retail-display',
            'case-04-perfect-parachute', 'case-05-mountain-states-potato', 'case-06-harnswell-quality']
DOCUMENTS = ([('lessons', n) for n in LESSONS] + [('practicals', n) for n in PRACTICALS]
             + [('extended-cases', n) for n in EXTENDED])
