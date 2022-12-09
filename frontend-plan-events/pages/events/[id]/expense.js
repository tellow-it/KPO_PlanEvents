import {useRouter} from "next/router";
import MainContainer from "../../../componets/MainContainer";
import styles from '../../../styles/events/Expense.module.css';

let products = [
	{name: "Арбузы", price: "25р за кг", quantity:"12.2кг"},
	{name: "Мясо", price: "320р за кг", quantity:"2.2кг"},
	{name: "Овощи", price: "32р за кг", quantity:"2.3кг"},
	{name: "Вафли", price: "300р за шт", quantity:"12шт"},
]

export default function Expense() {
	const {query} = useRouter();
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
            {products.map((item) => {
              let price = numberFromString(item.price);
              let quantity = numberFromString(item.quantity);;
              let calculate = price * quantity;
              summ += calculate;
              return (
                <div className={styles.product}>
                  <div className={styles.name}>{item.name}</div>
                  <div className={styles.calculate}>
                    <p>{price + 'Р * ' + quantity + ' = ' + calculate + 'Р'}</p>
                  </div>
                </div>
              );
            })}
          </div>
          <div className={styles.summ}>
            <div className={styles.result}><b>Итого</b></div>
            <p>{"= " + summ + "Р"}</p>
          </div>
          <div className={styles.payment}>
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
          </div>
          <div className={styles.add_card}>
            <img src="/icons/expense/add.png"/>
            <div>Добавить</div>
          </div>
				</div>
			</div>
		</MainContainer>
	)
};
