import Head from "next/head"
import Link from "next/link"
import styles from "../styles/MainContainer.module.css"
import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

function MainContainer({ children, keywords }) {
    const auth = useContext(AuthContext)
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
                        <img src='/icons/logout.png'/>
                        Выйти
                    </a>
                </div>
            </div>
            
            <div className={styles.menu}>
                <ul>
                    <Link href='/'>
                        <li>
                            <div className={styles.icon}>
                                <img src="/icons/account.png"/>
                            </div>
                            <p>События</p>
                        </li>
                    </Link>
                    <li>
                        <div className={styles.icon}>
                            <img src="/icons/setting.png"/>
                        </div>
                        <p>Настройки группы</p>
                    </li>
                    <li>
                        <div className={styles.icon}>
                            <img src="/icons/chat.png"/>
                        </div>
                        <p>Чат</p>
                    </li>
                    <li>
                        <div className={styles.icon}>
                            <img src="/icons/basket.png"/>
                        </div>
                        <p>Список покупок</p>
                    </li>
                    <li>
                        <div className={styles.icon}>
                            <img src="/icons/dollar.png"/>
                        </div>
                        <p>Затраты</p>
                    </li>
                </ul>
            </div>
            <div className={styles.content_body}>
                <div className={styles.content}>{children}</div>
            </div> 
        </div>
    );
}

export default MainContainer;