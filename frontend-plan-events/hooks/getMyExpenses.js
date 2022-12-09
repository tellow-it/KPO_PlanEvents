import { useState, useEffect, useContext } from "react";
import { UserContext } from "../context/UserContext";
import { useHttp } from "./http.hook";

export const useGetMyExpenses = (dependencies = []) => {
  const [expenses, setExpenses] = useState([]);
  const userInfo = useContext(UserContext);
  const { loading, request, error, clearError } = useHttp();

  useEffect(() => {
    const fetchData = async () => {
      const data = await request(`/buckets/get_price_for_user/${userInfo.id}&${userInfo.lastEvent}`, "GET");
      console.log(data.result);
      setExpenses(data.result);
    };
    fetchData();
  }, dependencies);

  return { expenses, loading, request, error, clearError };
};
