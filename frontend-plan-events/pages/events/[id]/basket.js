import { useRouter } from "next/router";
import MainContainer from "../../../componets/MainContainer";
import { useHttp } from "../../../hooks/http.hook";

export default function Basket({ user }) {
  const { query } = useRouter();
  const {loading, request, error, clearError} = useHttp()

  const check = async () => {
    try {
      const data = await request("/auth", "GET");
      console.log(data);
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <MainContainer keywords={user.name}>
      <div>
        <h1>basket c id {query.id}</h1>
        <div>Имя пользователя - {user.name}</div>
        <button onClick={check}>check</button>
      </div>
    </MainContainer>
  );
}

export async function getServerSideProps({ params }) {
  const response = await fetch(
    `https://jsonplaceholder.typicode.com/users/${params.id}`
  );
  const user = await response.json();
  return {
    props: { user }, // will be passed to the page component as props
  };
}
