import Head from "next/head";
import Link from "next/link";
import styles from "../styles/MainContainer.module.css";
import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { UserContext } from "../context/UserContext";


function MainContainer({ children, keywords }) {
  const auth = useContext(AuthContext);
  const userInfo = useContext(UserContext);

  return (
    <div className={styles.container}>
      <Head>
        <meta keywords={keywords}></meta>
        <title>{keywords}</title>
      </Head>

      <div className={styles.header}>
        <div className={styles.head}>
          <h1>Plane Events</h1>
          <a className={styles.button_loggout} onClick={auth.logout}>
            <img src="/icons/logout.png" />
            Выйти
          </a>
        </div>
      </div>

      <div className={styles.menu}>
        <ul>
          <Link href="/">
            <li>
              <div className={styles.icon}>
                <img src="/icons/account.png" />
              </div>
              <p>События</p>
            </li>
          </Link>
          <Link href={`/events/${userInfo.lastEvent}/settings`}>

          <li>
            <div className={styles.icon}>
              <img src="/icons/setting.png" />
            </div>
            <p>Настройки группы</p>
          </li>
          </Link>

          {/* <Link href={`/events/${userInfo.lastEvent}/chat`}>
          <li>
            <div className={styles.icon}>
              <img src="/icons/chat.png" />
            </div>
            <p>Чат</p>
          </li>
          </Link> */}
          <Link href={`/events/${userInfo.lastEvent}/basket`}>
            <li>
              <div className={styles.icon}>
                <img src="/icons/basket.png" />
              </div>
              <p>Список покупок</p>
            </li>
          </Link>
          <Link href={`/events/${userInfo.lastEvent}/expense`}>

          <li>
            <div className={styles.icon}>
              <img src="/icons/dollar.png" />
            </div>
            <p>Затраты</p>
          </li>
          </Link>
          
        </ul>
      </div>
      <div className={styles.content_body}>
        <div className={styles.content}>{children}</div>
      </div>
    </div>
  );
}

export default MainContainer;
