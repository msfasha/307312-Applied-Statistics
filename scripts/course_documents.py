"""The single approved notebook for each course part and extended application."""
LESSONS = ['01-introduction-to-r', '02-descriptive-statistics', '03-inferential-statistics']
SUPERSTORE = ['practical-01-categorical-business-data', 'practical-02-numerical-business-data',
              'practical-03-association-and-groups']
EXTENDED = ['case-01-springville-herald', 'case-02-oxford-cereal', 'case-03-retail-display',
            'case-04-perfect-parachute', 'case-05-mountain-states-potato', 'case-06-harnswell-quality']
DOCUMENTS = ([('lessons', n) for n in LESSONS]
             + [('extended-cases', n) for n in EXTENDED]
             + [('extended-cases/superstore', n) for n in SUPERSTORE])
NAVIGATION_PAGES = ['index', 'course/part-1', 'course/part-2', 'course/part-3',
                    'extended-cases/index', 'extended-cases/superstore/index']
INFERENTIAL_SOURCE_DOWNLOADS = ['03-inferential-statistics.qmd']
STUDENT_PROJECT_ZIP = 'applied-statistics-positron.zip'
