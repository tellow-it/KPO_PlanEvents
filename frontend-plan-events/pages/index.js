import Link from "next/link";
import Image from "next/image";
import styles from "../styles/Home.module.css";
import MainContainer from "../componets/MainContainer";

let array = [
  { name: "event_name_1", id: 1 },
  { name: "event_name_2", id: 2 },
];

export default function Home() {
  return (
    <MainContainer keywords={"home"}>
      <div>
        {array.map((v) => {
          return (
            <Link href={"/events/" + v.id + "/basket"}>
              <a>
              {v.id} {v.name}
              </a>
            </Link>
          );
        })}
      </div>
    </MainContainer>
  );
}
