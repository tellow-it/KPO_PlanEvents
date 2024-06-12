import { useRouter } from "next/router";
import MainContainer from "../../../componets/MainContainer";
import styles from "../../../styles/events/Expense.module.css";
import { useGetMyExpenses } from "../../../hooks/getMyExpenses";
import { UserContext } from "../../../context/UserContext";
import { useContext } from "react";


export default function Expense() {
  const { query } = useRouter();
  const userInfo = useContext(UserContext);
  userInfo.setLastEvent(query.id);
  const { expenses, loading, request, error, clearError } = useGetMyExpenses([
    userInfo.lastEvent,
  ]);
  const numberFromString = (string) => +/[\d, .]{1,}/.exec(string)[0];
  let summ = 0;

  return (
    <MainContainer keywords={"expense"}>
      <div className={styles.root}>
        <div className={styles.content}>
          <div className={styles.head}>
            <h2>Затраты</h2>
          </div>
          <div className={styles.products}>
            {expenses.map((item) => {
              let price = item.price;
              let quantity = item.quantity;
              let calculate = price * quantity;
              summ += item.price_for_user;
              return (
                <div className={styles.product}>
                  <div className={styles.name}>{item.name}</div>
                  <div className={styles.calculate}>
                    <p>{price + "Р * " + quantity + "/"+item.number_people+" = " + item.price_for_user + "Р"}</p>
                  </div>
                </div>
              );
            })}
          </div>
          <div className={styles.summ}>
            <div className={styles.result}>
              <b>Итого</b>
            </div>
            <p>{"= " + summ + "Р"}</p>
          </div>
          {/* <div className={styles.payment}>
            <p>Способ оплаты:</p>
            <div className={styles.payment_methods}>
              <div className={styles.card}>
                <div className={styles.card_name}>
                  <img src="/icons/expense/mastercard.png" className={styles.card_icon}/>
                  <div>MasterCard</div>
                </div>
                <div className={styles.card_code}>
                  **123
                </div>
              </div>
            </div>
          </div> */}
          {/* <div className={styles.add_card}>
            <img src="/icons/expense/add.png"/>
            <div>Добавить</div>
          </div> */}
        </div>
      </div>
    </MainContainer>
  );
}
