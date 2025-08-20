from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Task, db, User
from .forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Task(content=task_content, author=current_user)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('main.home'))
        except:
            return 'There was an issue adding your task'

    tasks = Task.query.filter_by(
        user_id=current_user.id).order_by(Task.id).all()

    return render_template('index.html', tasks=tasks)


@main_blueprint.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task_to_delete = Task.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('main.home'))
    except:
        return 'There was a problem deleting that task'


@main_blueprint.route('/complete/<int:id>', methods=['POST'])
def complete_task(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed
    try:
        db.session.commit()
        return redirect(url_for('main.home'))
    except:
        return 'There was an issue updating your task'


@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)


@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@main_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))
