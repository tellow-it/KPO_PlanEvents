import { useState, useEffect, useContext } from "react";
import { UserContext } from "../context/UserContext";
import { useHttp } from "./http.hook";

export const useGetPartyUsers = (dependencies = []) => {
  const [users, setUsers] = useState([]);
  const userInfo = useContext(UserContext);
  const { loading, request, error, clearError } = useHttp();

  useEffect(() => {
    const fetchData = async () => {
      const data = await request(`/parties/get_all_users_party/${userInfo.lastEvent}`, "GET");
      console.log(data.result);
      setUsers(data.result);
    };
    fetchData();
  }, dependencies);

  return { users, loading, request, error, clearError };
};
