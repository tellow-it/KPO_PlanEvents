import React, {useContext, useEffect, useState} from 'react'
import {useHttp} from '../hooks/http.hook'
import {useMessage} from '../hooks/message.hook'
import {AuthContext} from '../context/AuthContext'


const SignUp = () => {
  const auth = useContext(AuthContext)
  const message = useMessage()
  const {loading, request, error, clearError} = useHttp()
  const [form, setForm] = useState({
    email: '', username: '', password: ''
  })

  useEffect(() => {
    message(error)
    clearError()
  }, [error, message, clearError])

  useEffect(() => {
    //window.M.updateTextFields()
  }, [])

  const changeHandler = event => {
    setForm({ ...form, [event.target.name]: event.target.value })
  }

  const registerHandler = async () => {
    try {
      //const data = await request('/auth/registration', 'POST', {...form});
      const data = await request('/auth/signup', 'POST', {...form});
      message(data.message)
    } catch (e) {}
  }  

  const loginHandler = async () => {
    try {
      const data = await request('/auth/login', 'POST', {...form})
      console.log(data)
      auth.login(data.result.token.token,data.result.token.refreshToken,data.result.id)
      auth.isAuthenticated(!!data.result.token)
      console.log(auth)
    } catch (e) {}
  }

  return (
    <div className="row">
      <div className="col s6 offset-s3">
        <h1>Welcome</h1>
        <div className="card blue darken-1">
          <div className="card-content white-text">
            <span className="card-title">Регистрация</span>
            <div>

              <div className="input-field">
                <input
                  placeholder="Введите email"
                  id="email"
                  type="text"
                  name="email"
                  className="yellow-input"
                  value={form.email}
                  onChange={changeHandler}
                />
                <label htmlFor="email">Email</label>
              </div>

              <div className="input-field">
                <input
                  placeholder="Введите логин"
                  id="login"
                  type="text"
                  name="username"
                  className="yellow-input"
                  value={form.username}
                  onChange={changeHandler}
                />
                <label htmlFor="email">Логин</label>
              </div>

              <div className="input-field">
                <input
                  placeholder="Введите пароль"
                  id="password"
                  type="password"
                  name="password"
                  className="yellow-input"
                  value={form.password}
                  onChange={changeHandler}
                />
                <label htmlFor="email">Пароль</label>
              </div>

            </div>
          </div>
          <div className="card-action">
            <a href='#'>Есть аккаунт? Вход</a>
            {/* <button
              className="btn yellow darken-4"
              style={{marginRight: 10}}
              disabled={loading}
              onClick={loginHandler}
            >Войти
            </button> */}
            <button
              className="btn yellow darken-4"
              onClick={registerHandler}
              disabled={loading}
            >Регистрация
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default SignUp;