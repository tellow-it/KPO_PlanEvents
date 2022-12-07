import styles from "../../styles/events/Basket.module.css"

let ProductForm= ({change_product}) => {
    return (
        <div className={styles.form_add_product}>
        <div className={styles.form_field}>
            <p>Введите название</p>
            <input type="text" id='name' onChange={change_product}/>
        </div>
        <div className={styles.form_field}>
            <p>Введите количество</p>
            <input type="text" id='quantity' onChange={change_product}/>
        </div>
        <div className={styles.form_field}>
            <p>Введите стоимость</p>
            <input type="text" id='price' onChange={change_product}/>
        </div>
        </div>
    );
}

export default ProductForm;  