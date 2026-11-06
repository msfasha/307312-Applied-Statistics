# Compatibility helper. All current lessons and practicals use one shared style.
data_dir <- if (dir.exists('data')) 'data' else file.path('..','data')
source(file.path(data_dir, '..', 'lessons', '_includes', 'course-tools.R'))
