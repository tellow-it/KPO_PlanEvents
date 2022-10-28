import Head from "next/head"
import Link from "next/link"
import styles from "../styles/MainContainer.module.css"

function MainContainer({ children, keywords }) {
    return (
        <div className={styles.container}>
            <Head>
                <meta keywords={keywords}></meta>
                <title>{keywords}</title>
            </Head>
            {/* <div className="navbar">
                <a href={'/'}>Главная</a>
                <a href={'/users'}>Пользователи</a>
            </div> */}
            <header className={styles.header}>
                <div className={styles.header_block}>
                    <div>LOGO</div>
                    <h1>Plan Events</h1>
                </div>
            </header>
            
            <div className={styles.menu}>
                <ul>
                    <Link href={'/'}>
                    <li>
                        <div className="icon">IC</div>
                        <p>События</p>
                    </li>
                    </Link>
                    <li>
                        <div className="icon">IC</div>
                        <p>Настройки группы</p>
                    </li>
                    <li>
                        <div className="icon">IC</div>
                        <p>Чат</p>
                    </li>
                    <li>
                        <div className="icon">IC</div>
                        <p>Список покупок</p>
                    </li>
                    <li>
                        <div className="icon">IC</div>
                        <p>Затраты</p>
                    </li>
                </ul>
            </div>
            <div className={styles.content}>
                {children}
            </div>
            
            <footer className={styles.footer}>
                Lorem Lorem Lorem
            </footer>
        </div>
    );
}

export default MainContainer;