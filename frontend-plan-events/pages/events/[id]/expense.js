
import {useRouter} from "next/router";
import MainContainer from "../../../componets/MainContainer";

export default function Expense({user}) {
    const {query} = useRouter()
    return (
        <MainContainer keywords={user.name}>
            <div >
                <h1>expense c id {query.id}</h1>
                <div>Имя пользователя - {user.name}</div>
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