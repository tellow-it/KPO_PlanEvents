import Link from "next/link";
import Image from "next/image";
import styles from "../styles/Home.module.css";
import MainContainer from "../componets/MainContainer";
import { useRouter } from 'next/router'
import { useState } from "react";
import ModalForm from "../componets/ModalForm";
import AddEventsForm from "../componets/AddEventsForm";

let arrayEvents = [
  { name: "event_name_1", id: 1, description: "Lorem ipsum dolor sit amet", date:"25.10.2022" },
  { name: "event_name_2", id: 2, description: "Lorem ipsum dolor sit amet", date:"03.11.2022" },
  { name: "event_name_3", id: 3, description: "Lorem ipsum dolor sit amet", date:"12.11.2022" },
  { name: "event_name_1", id: 1, description: "Lorem ipsum dolor sit amet", date:"25.10.2022" },
  { name: "event_name_2", id: 2, description: "Lorem ipsum dolor sit amet", date:"03.11.2022" },
  { name: "event_name_3", id: 3, description: "Lorem ipsum dolor sit amet", date:"12.11.2022" },
  { name: "event_name_1", id: 1, description: "Lorem ipsum dolor sit amet", date:"25.10.2022" },
  { name: "event_name_2", id: 2, description: "Lorem ipsum dolor sit amet", date:"03.11.2022" },
  { name: "event_name_3", id: 3, description: "Lorem ipsum dolor sit amet", date:"12.11.2022" },
  { name: "event_name_1", id: 1, description: "Lorem ipsum dolor sit amet", date:"25.10.2022" },
  { name: "event_name_2", id: 2, description: "Lorem ipsum dolor sit amet", date:"03.11.2022" },
  { name: "event_name_3", id: 3, description: "Lorem ipsum dolor sit amet", date:"12.11.2022" },
];

export default function Home() {
  const router = useRouter();

  let [array, setArray] = useState(arrayEvents);
  let [addEventsMode, setAddEventsMode] = useState(false);
  let showAddEventsForm = () => setAddEventsMode(!addEventsMode);
  let addEvent = (name, description) => {
    setArray([...array, {name, description}]);
    setAddEventsMode(false);
  }

  

  console.log(router);
  return (
    <>
      {addEventsMode ? <AddEventsForm addEvent={addEvent}></AddEventsForm>: null}
      <MainContainer keywords={"home"}>
        <div className={styles.root}>
          <div className={styles.head}>
            <div className={styles.field}>
              <div className={styles.user_data}>
                <div className={styles.parent_logo_container}>
                  <div className={styles.logo_container}>
                    <div className={styles.logo}></div>
                  </div>
                </div>
                <div className={styles.data}>
                  <div className={styles.name}>
                    <h3>Владемар Комаревцев</h3>
                  </div>
                  <div className={styles.phone}>
                    8 800 555 35 35
                  </div>
                </div>
              </div>
              <div className={styles.user_icons}>				
                <img src='/icons/add_event.png' onClick={showAddEventsForm}/>
                
                <img src='/icons/Settings_account.png'/>
              </div>
            </div>
          </div>
          <div className={styles.event_list}>
          {array.map((v, index) => {
              return (
                <Link href={"/events/" + v.id + "/settings"} key={index}>
                  <a className={styles.event}>
                    <div className={styles.event_head}>
                      <h2>{v.name}</h2>
                      <p>{v.date} </p>
                    </div>
                    <div className={styles.event_description}>
                      <p>{v.description} </p>
                    </div>
                  </a>
                </Link>
              );
            })}
          </div>
        </div>
      </MainContainer>
    </>
  );
}
