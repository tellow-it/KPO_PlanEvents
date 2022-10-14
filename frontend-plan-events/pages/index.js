import Link from "next/link";
import Image from "next/image";
import styles from "../styles/Home.module.css";
import MainContainer from "../componets/MainContainer";

let array = [
  { name: "event_name_1", id: 1, description: "Lorem ipsum dolor sit amet", data:"25.10.2022" },
  { name: "event_name_2", id: 2, description: "Lorem ipsum dolor sit amet", data:"03.11.2022" },
  { name: "event_name_3", id: 3, description: "Lorem ipsum dolor sit amet", data:"12.11.2022" },
  { name: "event_name_1", id: 1, description: "Lorem ipsum dolor sit amet", data:"25.10.2022" },
  { name: "event_name_2", id: 2, description: "Lorem ipsum dolor sit amet", data:"03.11.2022" },
  { name: "event_name_3", id: 3, description: "Lorem ipsum dolor sit amet", data:"12.11.2022" },
  { name: "event_name_1", id: 1, description: "Lorem ipsum dolor sit amet", data:"25.10.2022" },
  { name: "event_name_2", id: 2, description: "Lorem ipsum dolor sit amet", data:"03.11.2022" },
  { name: "event_name_3", id: 3, description: "Lorem ipsum dolor sit amet", data:"12.11.2022" },
  { name: "event_name_1", id: 1, description: "Lorem ipsum dolor sit amet", data:"25.10.2022" },
  { name: "event_name_2", id: 2, description: "Lorem ipsum dolor sit amet", data:"03.11.2022" },
  { name: "event_name_3", id: 3, description: "Lorem ipsum dolor sit amet", data:"12.11.2022" },
];

export default function Home() {
  return (
    <MainContainer keywords={"home"}>
      <div className={styles.events}>
        {array.map((v, index) => {
          return (
            <Link href={"/events/" + v.id + "/basket"} key={index}>
              <a className={styles.event}>
                <div className={styles.event_head}>
                  <h2>{v.name}</h2>
                  <p>{v.data} </p>
                </div>
                <div className={styles.event_description}>
                  <p>{v.description} </p>
                </div>
              </a>
            </Link>
          );
        })}
      </div>
    </MainContainer>
  );
}
