import React, { useContext, useEffect, useState } from "react";
import { useHttp } from "../hooks/http.hook";
import { useMessage } from "../hooks/message.hook";
import { AuthContext } from "../context/AuthContext";
import styles from "../styles/SignUp.module.css";
import Link from "next/link";

const SignIn = () => {
  const auth = useContext(AuthContext);
  const message = useMessage();
  const { loading, request, error, clearError } = useHttp();
  const [form, setForm] = useState({
    email: "",
    password: "",
  });

  useEffect(() => {
    message(error);
    clearError();
  }, [error, message, clearError]);

  useEffect(() => {
    //window.M.updateTextFields()
  }, []);

  const changeHandler = (event) => {
    setForm({ ...form, [event.target.name]: event.target.value });
  };

  const loginHandler = async () => {
    try {
      const data = await request("/auth/login", "POST", { ...form });
      console.log(data);
      auth.login(data.access, data.refresh, "backend_not_get_me_id");
      auth.isAuthenticated = !!data.access;
      console.log(auth, "afdsss");
      console.log("afdsss");
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <div className={styles.root}>
      <div className={styles.content}>
        <h1>Welcome</h1>
        <div className="card blue darken-1">
          <div className="card-content white-text">
            <span className="card-title">Авторизация</span>
            <div>
              <div className={styles.input_field}>
                <input
                  placeholder="Введите логин"
                  id="login"
                  type="text"
                  name="username"
                  className="yellow-input"
                  value={form.username}
                  onChange={changeHandler}
                />
              </div>

              <div className={styles.input_field}>
                <input
                  placeholder="Введите пароль"
                  id="password"
                  type="password"
                  name="password"
                  className="yellow-input"
                  value={form.password}
                  onChange={changeHandler}
                />
              </div>
            </div>
          </div>
          <div className={styles.card_action}>
            <Link href={"/SignUp"}>Нет аккаунта? Регистрация</Link>
            <button
              className="btn yellow darken-4"
              style={{ marginRight: 10 }}
              disabled={loading}
              onClick={loginHandler}
              type="submit"
            >
              Войти
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignIn;
