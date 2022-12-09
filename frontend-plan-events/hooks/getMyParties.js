import { useState, useEffect, useContext } from "react";
import { UserContext } from "../context/UserContext";
import { useHttp } from "./http.hook";

export const useGetMyParties = (dependencies = []) => {
  const [parties, setParties] = useState([]);
  const userInfo = useContext(UserContext);
  const { loading, request, error, clearError } = useHttp();

  useEffect(() => {
    const fetchData = async () => {
      const data = await request(`/users/get_all_party/${userInfo.id}`, "GET");
      console.log(data.result);
      setParties(data.result);
    };
    fetchData();
  }, dependencies);

  return { parties, loading, request, error, clearError };
};
