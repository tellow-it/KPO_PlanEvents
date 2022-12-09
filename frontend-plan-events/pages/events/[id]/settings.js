import { useRouter } from "next/router";
import MainContainer from "../../../componets/MainContainer";
import styles from "../../../styles/events/Settings.module.css";
import { UserContext } from "../../../context/UserContext";
import { useContext } from "react";
import { useGetPartyUsers } from "../../../hooks/getAllUserParty";

const users = [
  { name: "Ашот", role: "Администратор", img: "/list_users/1.jpeg" },
  { name: "Илья", role: "Закупщик", img: "/list_users/2.jpg" },
  { name: "Марина", role: "Повар", img: "/list_users/3.jpg" },
  { name: "Дарья", role: "", img: "" },
  { name: "Дмитрий", role: "", img: "/list_users/5.jpg" },
];

export default function Settings() {
  const { query } = useRouter();
  const userInfo = useContext(UserContext);
  userInfo.setLastEvent(query.id);
//   const { users, loading, request, error, clearError } = useGetPartyUsers([userInfo.lastEvent]);

  return (
    <MainContainer>
      <div className={styles.root}>
        {/* <h1>settings c id {query.id}</h1>
                <div>Имя пользователя - {user.name}</div> */}
        <div className={styles.content}>
          <h3>Настройки группы</h3>
          <h4>
            Участники
            {users.length ? `(${users.length})` : null}
          </h4>
          <div className={styles.add}>
            <div>
              <p>+</p>
            </div>
            <p>Добавить</p>
          </div>
          <div className={styles.participants_list}>
            {users.map((item) => {
              return (
                <div className={styles.participant}>
                  <div className={styles.user}>
                    <div className={styles.img}>
                      {/* <img src={item.img} /> */}
                    </div>
                    <div className={styles.name}>{item.name}</div>
                  </div>
                  {item.role ? (
                    <div className={styles.role}>
                      <div className={styles.role_content}>
                        <p>{item.role}</p>
                      </div>
                    </div>
                  ) : null}
                </div>
              );
            })}
          </div>
          <div className={styles.settings}>
            <div className={styles.prop}>
              <img src="/icons/settings/change_back.png" />
              <p>Изменить фон</p>
            </div>
            <div className={styles.prop}>
              <img src="/icons/settings/set_role.png" />
              <p>Назначить роли</p>
            </div>
            <div className={styles.prop}>
              <img src="/icons/settings/remove-user.png" />
              <p>Удалить участника</p>
            </div>
            <div className={styles.prop}>
              <img src="/icons/settings/trash.png" />
              <p>Удалить группу</p>
            </div>
          </div>
        </div>
      </div>
    </MainContainer>
  );
}
