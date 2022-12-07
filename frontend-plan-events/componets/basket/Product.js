import styles from "../../styles/events/Basket.module.css"
let Product = ({item}) => {
    return (
        <div className={styles.item}>
            <label className={styles.product}>
            <div className={styles.info}>
                <div className={styles.input}>
                <input type="checkbox"/>
                </div>
                <div className={styles.info_pr}>
                <div className={styles.productName + " " + styles.text_vertical_align}>
                    {item.name}
                </div>
                <div className={styles.productPrice + " " + styles.text_vertical_align}>
                    {item.price}
                </div>
                </div>
            </div>
            <div className={styles.productQuantity + " " + styles.text_vertical_align}>
                {item.quantity}
            </div>
            </label>
        </div>
    );
}

export default Product;