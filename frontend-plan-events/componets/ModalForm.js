import styles from "../styles/ModalForm.module.css"

let ModalForm = ({children}) => {
    return (
        <div className={styles.back}>
            <div className={styles.content}>
                {children}
            </div>
        </div>
    );
}

export default ModalForm;