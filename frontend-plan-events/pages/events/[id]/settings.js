import {useRouter} from "next/router";
import MainContainer from "../../../componets/MainContainer";
import styles from "../../../styles/events/Settings.module.css";

const users = [
    {name: "Ашот", role:"Администратор", img: '/list_users/1.jpeg'},
    {name: "Илья", role:"Закупщик", img: '/list_users/2.jpg'},
    {name: "Марина", role:"Повар", img: '/list_users/3.jpg'},
    {name: "Дарья", role:"", img: '/list_users/4.jpg'},
    {name: "Дмитрий", role:"", img: '/list_users/5.jpg'}
];

export default function Settings({user}) {
    const {query} = useRouter()
    return (
        <MainContainer keywords={user.name}>
            <div className={styles.root}>
                {/* <h1>settings c id {query.id}</h1>
                <div>Имя пользователя - {user.name}</div> */}
                <div className={styles.content}>
                    <h3>Настройки группы</h3>
                    <h4>Участники 
                        {(users.length) ? `(${users.length})` : null}
                    </h4>
                    <div className={styles.add}><div><p>+</p></div><p>Добавить</p></div>
                    <div className={styles.participants_list}>
                        {users.map((item) => {
                            return (
                                <div className={styles.participant}>
                                    <div className={styles.user}>
                                        <div className={styles.img}>
                                            <img src={item.img}/>
                                        </div>
                                        <div className={styles.name}>{item.name}</div>
                                    </div>
                                    {(item.role) ? 
                                        <div className={styles.role}>
                                            <div className={styles.role_content}><p>{item.role}</p></div>
                                        </div> :
                                        null
                                    }
                                    
                                </div>
                            );
                        })}
                    </div>
                    <div className={styles.settings}>
                        <div className={styles.prop}>
                            <img src="/icons/settings/change_back.png"/>
                            <p>Изменить фон</p>
                        </div>
                        <div className={styles.prop}>
                            <img src="/icons/settings/set_role.png"/>
                            <p>Назначить роли</p>
                        </div>
                        <div className={styles.prop}>
                            <img src="/icons/settings/remove-user.png"/>
                            <p>Удалить участника</p>
                        </div>
                        <div className={styles.prop}>
                            <img src="/icons/settings/trash.png"/>
                            <p>Удалить группу</p>
                        </div>
                    </div>
                </div>
            </div>
        </MainContainer>
    )
};

export async function getServerSideProps({params}) {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${params.id}`)
    const user = await response.json()
    return {
        props: {user}, // will be passed to the page component as props
    }
}