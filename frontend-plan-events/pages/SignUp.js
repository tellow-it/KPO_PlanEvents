import React, { useContext, useEffect, useState } from "react";
import { useHttp } from "../hooks/http.hook";
import { useMessage } from "../hooks/message.hook";
import { AuthContext } from "../context/AuthContext";
import Link from "next/link";
import { Formik, Form, Field } from "formik";
import * as Yup from "yup";
import { useRouter } from "next/router";

import styles from "../styles/SignUp.module.css";

const SignupSchema = Yup.object().shape({
  phone: Yup.number()
    .min(10000000000, "Too Short!")
    .max(99999999999, "Too Long!") 
    .required("Required"),
  username: Yup.string()
    .min(2, "Too Short!")
    .max(50, "Too Long!")
    .required("Required"),
  password: Yup.string()
    .min(4, "Too Short!")
    .max(50, "Too Long!")
    .required("Required"),
  email: Yup.string()
    .email("Invalid email")
    .max(50, "Too Long!")
    .required("Required"),
});

const SignUp = () => {
  const auth = useContext(AuthContext);
  const message = useMessage();
  const { loading, request, error, clearError } = useHttp();
  const router = useRouter();
  useEffect(() => {
    message(error);
    clearError();
  }, [error, message, clearError]);

  useEffect(() => {
    //window.M.updateTextFields()
  }, []);

  const [styleForm, setStyleForm] = useState({
    username: styles.input_field,
    password: styles.input_field,
    email: styles.input_field,
    phone: styles.input_field,
  });

  const registerHandler = async (form) => {
    try {
      const data = await request("/auth/signup", "POST", { ...form });
      //to do check toast
      router.push("/SignIn");
    } catch (e) {}
  };

  const conditionFieldRender = (errors, touched, field) => {
    let elem = {};
    if (errors[field] && touched[field]) {
      if (errors[field] == "Required") {
        styleForm[field] = styles.error_input_field;
        elem = <div name={`${field}-error-messege`} className={styles.form_error}>{errors[field]}</div>;
      } else {
        styleForm[field] = styles.error_input_field;
        elem = <div name={`${field}-error-messege`} className={styles.form_error}>{errors[field]}</div>;
      }
    } else {
      styleForm[field] = styles.input_field;
      elem = null;
    }
    return elem;
  };

  return (
    <div className={styles.root}>
      <div className={styles.content}>
        <div className={styles.logo}>
          <img src="/icons/logo.png" />
        </div>

        <div className="card blue darken-1">
          <Formik
            initialValues={{
              email: "",
              username: "",
              password: "",
              phone: "",
            }}
            validationSchema={SignupSchema}
            onSubmit={registerHandler}
          >
            {({ errors, touched }) => (
              <Form>
                <div className="card-content white-text">
                  <div>
                    {conditionFieldRender(errors, touched, "email")}
                    <div className={styleForm.email}>
                      <div className={styles.img_email}>
                        <img src="/icons/email.png" />
                      </div>

                      <Field
                        placeholder="Введите email"
                        id="email"
                        type="email"
                        name="email"
                        className="yellow-input"
                      />
                    </div>

                    {conditionFieldRender(errors, touched, "username")}
                    <div className={styleForm.username}>
                      <div className={styles.img_container}>
                        <img src="/icons/password.png" />
                      </div>
                      <Field
                        placeholder="Введите логин"
                        id="login"
                        type="text"
                        name="username"
                        className="yellow-input"
                      />
                    </div>
                    {conditionFieldRender(errors, touched, "phone")}
                    <div className={styleForm.phone}>
                      <div className={styles.img_container}>
                        <img src="/icons/password.png" />
                      </div>
                      <Field
                        placeholder="Введите номер телефона"
                        id="phone"
                        type="text"
                        name="phone"
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
                </div>
                <div className={styles.card_action}>
                  <Link href={"/SignIn"}>Есть аккаунт? Вход</Link>
                  <button
                    className={styles.button_signup}
                    type="submit"
                    disabled={loading}
                  >
                    Регистрация
                  </button>
                </div>
              </Form>
            )}
          </Formik>
        </div>
      </div>
    </div>
  );
};

export default SignUp;
