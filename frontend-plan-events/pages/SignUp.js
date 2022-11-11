import React, { useContext, useEffect, useState } from "react";
import { useHttp } from "../hooks/http.hook";
import { useMessage } from "../hooks/message.hook";
import { AuthContext } from "../context/AuthContext";
import MainContainer from "../componets/MainContainer";
import Link from "next/link"

import styles from "../styles/SignUp.module.css";

const SignUp = () => {
  const auth = useContext(AuthContext);
  const message = useMessage();
  const { loading, request, error, clearError } = useHttp();
  const [form, setForm] = useState({
    email: "",
    username: "",
    password: "",
    phone: "",
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

  const registerHandler = async () => {
    try {
      const data = await request("/auth/signup", "POST", { ...form });
      message(data.message);
    } catch (e) {}
  };



  return (
    <div className={styles.root}>
      <div className={styles.content}>
        <div className={styles.logo}>
          <img src="/icons/logo.png"/>
        </div>

        <div className="card blue darken-1">
          <div className="card-content white-text">
           
            <div>
              <div className={styles.input_field}>
                <div className={styles.img_email} >
                  <img src="/icons/email.png"/>
                </div>
                
                <input
                  placeholder="Введите email"
                  id="email"
                  type="text"
                  name="email"
                  className="yellow-input"
                  value={form.email}
                  onChange={changeHandler}
                />
              </div>

              <div className={styles.input_field}>
                <div className={styles.img_container}>
                  <img src="/icons/password.png"/>
                </div>
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
                <div className={styles.img_container}>
                  <img src="/icons/password.png"/>
                </div>
                <input
                  placeholder="Введите номер телефона"
                  id="login"
                  type="text"
                  name="phone"
                  className="yellow-input"
                  value={form.phone}
                  onChange={changeHandler}
                />
              </div>
              <div className={styles.input_field}>
                <div className={styles.img_container}>
                  <img src="/icons/password.png"/>
                </div>
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
          <Link href={'/SignIn'}>Есть аккаунт? Вход</Link>
            <button
              className={styles.button_signin}
              onClick={registerHandler}
              disabled={loading}
            >
              Регистрация
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignUp;
