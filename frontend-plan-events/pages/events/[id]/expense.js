
import {useRouter} from "next/router";
import MainContainer from "../../../componets/MainContainer";

export default function Expense() {
    const {query} = useRouter()
    return (
        <MainContainer >
            <div >
                <h1>expense c id {query.id}</h1>
                <div>Имя пользователя - </div>
            </div>
        </MainContainer>
    )
};
