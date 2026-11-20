"""The single approved notebook for each course part and extended application."""
LESSONS = ['01-introduction-to-r', '02-descriptive-statistics', '03-probability-foundations', '04-statistical-inference-and-estimation']
SUPERSTORE = ['practical-01-categorical-business-data', 'practical-02-numerical-business-data',
              'practical-03-association-and-groups']
EXTENDED = ['case-01-springville-herald', 'case-02-oxford-cereal', 'case-03-retail-display',
            'case-04-perfect-parachute', 'case-05-mountain-states-potato', 'case-06-harnswell-quality']
DOCUMENTS = ([('lessons', n) for n in LESSONS]
             + [('extended-cases', n) for n in EXTENDED]
             + [('extended-cases/superstore', n) for n in SUPERSTORE])
NAVIGATION_PAGES = ['index', 'course/part-1', 'course/part-2', 'course/part-3', 'course/part-4',
                    'extended-cases/index', 'extended-cases/superstore/index']
R_CODE_DOWNLOADS = [name+'.R' for name in LESSONS]
STUDENT_PROJECT_ZIP = 'applied-statistics-positron.zip'
