from flask import request, redirect, url_for

@app1.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        # 处理表单提交
        movie_name = request.form['movie_name']
        release_date = request.form['release_date']
        country = request.form['country']
        movie_type = request.form['type']
        year = request.form['year']

        # 将数据插入数据库
        new_movie = Movie(movie_name=movie_name, release_date=release_date, country=country, type=movie_type, year=year)
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for('movie_list'))

    # 如果是 GET 请求，显示表单页面
    return render_template('add_movie.html')
