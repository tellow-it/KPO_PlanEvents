import { useState, useEffect, useContext } from "react";
import { UserContext } from "../context/UserContext";
import { useHttp } from "./http.hook";

export const useGetProducts = (dependencies = []) => {
  const [products, setProducts] = useState([]);
  const userInfo = useContext(UserContext);
  const { loading, request, error, clearError } = useHttp();

  useEffect(() => {
    const fetchData = async () => {
      const data = await request(`/buckets/get_all_buckets_party/${userInfo.lastEvent}`, "GET");
      console.log(data.result);
      setProducts(data.result);
    };
    fetchData();
  }, dependencies);

  return { products, loading, request, error, clearError };
};
