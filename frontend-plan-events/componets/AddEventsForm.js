import ModalForm from "./ModalForm";
import styles from "../styles/Home.module.css"

let AddEventsForm = ({addEvent}) => {
    let event = {name:"", description:""};
    let changeEvent = (item) => {
        event[item.target.id] = item.target.value;
    }
    let add = () => {
        addEvent(event.name, event.description);
    }
    return (
        <ModalForm>
        <div className={styles.addEvents}>
            <div className={styles.addEventsHead}>
            <h2>Добавление события</h2>
            </div>
            <div className={styles.addEventsFields}>
            <div className={styles.addEventsField}>
                <input placeholder="Введите название:" id="name" onChange={changeEvent}/>
            </div>
            <div className={styles.addEventsField}>
                <textarea cols="28" rows="3" placeholder="Введите описание:" id="description" onChange={changeEvent}></textarea>
            </div>
            </div>
            <div className={styles.addEventsButtonContainer}>
            <button className={styles.addEventsButton} onClick={add}>Добавить</button>
            </div>
        </div>
        </ModalForm>
    );
}

export default AddEventsForm;