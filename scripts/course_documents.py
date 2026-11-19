"""The single approved notebook for each course part and extended application."""
LESSONS = ['01-introduction-to-r', '02-descriptive-statistics', '03-inferential-statistics']
SUPERSTORE = ['practical-01-categorical-business-data', 'practical-02-numerical-business-data',
              'practical-03-association-and-groups']
PRACTICALS = []
DESCRIPTIVE_PRACTICAL_ALIAS = 'descriptive-statistics-r-practical'
EXTENDED = ['case-01-springville-herald', 'case-02-oxford-cereal', 'case-03-retail-display',
            'case-04-perfect-parachute', 'case-05-mountain-states-potato', 'case-06-harnswell-quality']
DOCUMENTS = ([('lessons', n) for n in LESSONS]
             + [('extended-cases', n) for n in EXTENDED]
             + [('extended-cases/superstore', n) for n in SUPERSTORE])
NAVIGATION_PAGES = ['index', 'course/index', 'course/part-1', 'course/part-2', 'course/part-3',
                    'extended-cases/index', 'extended-cases/superstore/index']
R_INTRODUCTION_ALIASES = ['r-02-basic-concepts', 'r-03-dplyr', 'r-04-ggplot2']
NAVIGATION_PAGES += ['lessons/' + n for n in R_INTRODUCTION_ALIASES]
NAVIGATION_PAGES += ['practicals/' + DESCRIPTIVE_PRACTICAL_ALIAS]
# These old URLs only forward to the one Part 3 notebook; they are not lessons.
INFERENTIAL_REDIRECTS = ['lessons/inferential-31-probability-distributions-draft',
                        'practicals/inferential-statistics-r-practical']
NAVIGATION_PAGES += INFERENTIAL_REDIRECTS
INFERENTIAL_PDF_ALIASES = ['inferential-31-probability-distributions-draft',
                           'inferential-statistics-r-practical']
INFERENTIAL_SOURCE_DOWNLOADS = ['03-inferential-statistics.qmd',
                                'inferential-statistics-r-practical.qmd']
STUDENT_PROJECT_ZIP = 'applied-statistics-positron.zip'
LEGACY_STUDENT_PROJECT_ZIP = 'applied-statistics-rstudio.zip'
