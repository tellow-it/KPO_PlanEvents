import React, { useContext, useEffect, useState } from "react";
import Link from "next/link";
import Image from "next/image";
import { UserContext } from "../context/UserContext";
import styles from "../styles/Home.module.css";
import MainContainer from "../componets/MainContainer";
import { useRouter } from "next/router";
import { useGetMyParties } from "../hooks/getMyParties";

export default function Home() {
  const router = useRouter();
  const userInfo = useContext(UserContext);
  const { parties, loading, request, error, clearError } = useGetMyParties();
  console.log(userInfo);
  return (
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
                  <h3>{userInfo.name}</h3>
                </div>
                <div className={styles.phone}>{userInfo.phoneNumber}</div>
              </div>
            </div>
            <div className={styles.user_icons}>
              <img src="/icons/add_event.png" />
              <img src="/icons/Settings_account.png" />
            </div>
          </div>
        </div>
        <div className={styles.event_list}>
          {parties.length === 0 ? <>Es gibt keine Veranstaltungen, was tun?</> : <></>}
          {parties.map((v, index) => {
            return (
              <Link href={"/events/" + v.id + "/settings"} key={index}>
                <a className={styles.event}>
                  <div className={styles.event_head}>
                    <h2>{v.name}</h2>
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
  );
}
