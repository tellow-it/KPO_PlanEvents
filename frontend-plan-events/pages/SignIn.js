import React, { useContext, useEffect, useState } from "react";
import { useHttp } from "../hooks/http.hook";
import { useMessage } from "../hooks/message.hook";
import { AuthContext } from "../context/AuthContext";
import { UserContext } from "../context/UserContext";
import styles from "../styles/SignUp.module.css";
import Link from "next/link";
import { Formik, Form, Field } from "formik";
import * as Yup from "yup";

const SigninSchema = Yup.object().shape({
  username: Yup.string()
    .min(2, "Too Short!")
    .max(50, "Too Long!")
    .required("Required"),
  password: Yup.string()
    .min(4, "Too Short!")
    .max(50, "Too Long!")
    .required("Required"),
});

const SignIn = () => {
  const auth = useContext(AuthContext);
  const userInfo = useContext(UserContext);
  const message = useMessage();
  const { loading, request, error, clearError } = useHttp();

  const [styleForm, setStyleForm] = useState({
    username: styles.input_field,
    password: styles.input_field,
  });

  useEffect(() => {
    message(error);
    clearError();
  }, [error, message, clearError]);


  const loginHandler = async (form) => {
    try {
      const data = await request("/auth/login", "POST", { ...form });
      let headers = {};
      headers["Authorization"] =  `Bearer ${data.result.access_token}`;
      const userData = await request("/users", "GET", null, headers);
      userInfo.setInfo(userData.result.name, userData.result.username, userData.result.email, userData.result.sex, userData.result.birth, userData.result.phone_number, userData.result.id)      
      auth.login(data.result.access_token, data.result.access_token);
      auth.isAuthenticated = !!data.access;
      console.log(userData)
    } catch (e) {
      console.error(e);
    }
  };

  const conditionFieldRender = (errors, touched, field) => {
    let elem = {};
    if (errors[field] && touched[field]) {
      if (errors[field] == "Required") {
        styleForm[field] = styles.error_input_field;
        elem = <div name={`${field}-error-messege`} className={styles.form_error}>{errors[field]}</div>;
      } else {
        styleForm[field] = styles.error_input_field;
        elem = <div name={`${field}-error-messege`}  className={styles.form_error}>{errors[field]}</div>;
      }
    } else {
      styleForm[field] = styles.input_field;
      elem = null;
    } 
    return elem;
  };

  return (
    <div className={styles.body}>
      <div className={styles.root}>
        <div className={styles.content}>
          <div className="card blue darken-1">
            <div className="card-content white-text">
              <div className={styles.logo}>
                <img src="/icons/logo.png" />
              </div>

              <div className={styles.title}>
                <h3>Добрый день!</h3>
                <p>Введите свой логин и пароль</p>
              </div>
              <Formik
                initialValues={{
                  username: "",
                  password: "",
                }}
                validationSchema={SigninSchema}
                onSubmit={loginHandler}
              >
                {({ errors, touched }) => {
                  return (
                    <Form>
                      <div className={styles.form}>
                        {conditionFieldRender(errors, touched, "username")}
                        <div className={styleForm.username}>
                          <div className={styles.img_email}>
                            <img src="/icons/email.png" />
                          </div>

                          <Field
                            placeholder="Введите логин"
                            id="login"
                            type="text"
                            name="username"
                            className="yellow-input"
                          />
                        </div>

                        {conditionFieldRender(errors, touched, "password")}
                        <div className={styleForm.password}>
                          <div className={styles.img_container}>
                            <img src="/icons/password.png" />
                          </div>

                          <Field
                            placeholder="Введите пароль"
                            id="password"
                            type="password"
                            name="password"
                            className="yellow-input"
                          />
                        </div>
                      </div>

                      <div className={styles.card_action}>
                        <Link href={"/SignUp"}>Нет аккаунта? Регистрация</Link>
                        <button
                          className={styles.button_signup}
                          style={{ marginRight: 10 }}
                          disabled={loading}
                          type="submit"
                        >
                          Войти
                        </button>
                      </div>
                    </Form>
                  );
                }}
              </Formik>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignIn;