import Head from "next/head"


function MainContainer({ children, keywords }) {
    return (
        <>
            <Head>
                <meta keywords={"hh, jjjjjj" + keywords}></meta>
                <title>Главная страница</title>
            </Head>
            <div className="navbar">
                <a href={'/'}>Главная</a>
                <a href={'/users'}>Пользователи</a>
            </div>
            <div>
                {children}
            </div>
            <style jsx>
                {`
                  .navbar {
                      background: orange;
                      padding: 15px;
                  }
                 
              `}
            </style>
        </>
    );
}

export default MainContainer;