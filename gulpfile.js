var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');

var js_files = [
    'static/js/jquery-2.2.0.min.js',
    'static/js/masonry.pkgd.min.js',
    'static/js/*.js'
    ]
var scss_files = [
    'static/scss/*.scss',
    'home/static/home/scss/*.scss',
    'blogengine/static/blogengine/scss/*.scss'
    ]
var vendor_files = [
    'static/css/*.css'
    ]

gulp.task('js', function() {
    return gulp.src(js_files)
        .pipe(concat('index.js'))
        .pipe(gulp.dest('static/dist'));
});

gulp.task('sass', function() {
    gulp.src(scss_files)
        .pipe(sass({ includePaths : ['_/sass/']}))
        .pipe(concat('index.css'))
        .pipe(gulp.dest('static/dist'));
});

gulp.task('vendor_css', function() {
    gulp.src(vendor_files)
        .pipe(concat('vendor.css'))
        .pipe(gulp.dest('static/dist'));
});

gulp.task('watch', function() {
    gulp.watch('**/*.scss', ['sass']);
});

gulp.task('default', ['js', 'sass', 'vendor_css', 'watch']);
gulp.task('build', ['js', 'sass', 'vendor_css']);
