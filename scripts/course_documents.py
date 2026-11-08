"""Approved student documents shared by packaging and release validation."""
LESSONS = ['01-introduction-to-r', 'r-02-basic-concepts', 'r-03-dplyr', 'r-04-ggplot2', '02-descriptive-statistics', '03-inferential-statistics', 'inferential-31-probability-distributions-draft']
SUPERSTORE = ['practical-01-categorical-business-data', 'practical-02-numerical-business-data',
              'practical-03-association-and-groups']
PRACTICALS = ['descriptive-statistics-r-practical', 'inferential-statistics-r-practical']
EXTENDED = ['case-01-springville-herald', 'case-02-oxford-cereal', 'case-03-retail-display',
            'case-04-perfect-parachute', 'case-05-mountain-states-potato', 'case-06-harnswell-quality']
DOCUMENTS = ([('lessons', n) for n in LESSONS] + [('practicals', n) for n in PRACTICALS]
             + [('extended-cases', n) for n in EXTENDED]
             + [('extended-cases/superstore', n) for n in SUPERSTORE])

# Navigation pages are included in the website and editable student project, without extra PDFs.
NAVIGATION_PAGES = ['index', 'course/index', 'course/part-1', 'course/part-2', 'course/part-3', 'extended-cases/index', 'extended-cases/superstore/index']
