import {useRouter} from "next/router";
import { useState } from "react";
import MainContainer from "../../../componets/MainContainer";
import styles from "../../../styles/events/Chat.module.css";

export default function Chat({user}) {
	const {query} = useRouter();

	let [messages, setMessages] = useState([
		{text: ["Привет, как дела?"], sender: "alien"},
		{text: ['В каком ресторане будем гулять?'], sender: "alien"},
		{text: ['Привет, все хорошо! У вас как?',
			'Будем гулять в ресторане АРАРАТ'], sender: "my"},
		{text: ['В 19:00 начало'], sender: "my"},
		{text: ['Хорошо, до встречи'], sender: "alien"},
	]);

	return (
		<MainContainer keywords={user.name}>
			<div className={styles.root}>
				<div className={styles.content}>
					<h3>Свадьба Ашота</h3>
					<div className={styles.message_list}>
						{messages.map((item) => {
							switch(item.sender){
								case 'alien':
									return (
										<div className={styles.message + ' ' + styles.alien_message}>
											<div className={styles.message_content}>
												{item.text.map((message) => <p>{message}</p>)}
											</div>
										</div>
									);
									break;
								case 'my':
									return (
										<div className={styles.message + ' ' + styles.my_message}>
											<div className={styles.message_content}>
												{item.text.map((message) => <p>{message}</p>)}
											</div>
										</div>
									);
									break;
							}
						})}
					</div>
					<div className={styles.input_field}>
						<img src="/icons/attach.png" className={styles.input_img}/>
						<input type="text" placeholder="Введите сообщение:"/>
						<div className={styles.input_right_icons}>
							<img src="/icons/smile.png" className={styles.input_img}/>
							<img src="/icons/microphone.png" className={styles.input_img}/>
						</div>
					</div>
				</div>
			</div>
		</MainContainer>
	)
};

export async function getServerSideProps({params}) {
	const response = await fetch(`https://jsonplaceholder.typicode.com/users/${params.id}`)
	const user = await response.json()
	return {
		props: {user}, // will be passed to the page component as props
	}
}