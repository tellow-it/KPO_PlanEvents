import { useState, useCallback } from "react";
import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
export const useHttp = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const auth = useContext(AuthContext)
  console.log(auth.token)
  const request = useCallback(
    async (url, method = "GET", body = null, headers = {}) => {
      setLoading(true);
      try {
        url = "https://kpo-party-manager.onrender.com" + url;
        if (body) {
          body = JSON.stringify(body);
          headers["Content-Type"] = "application/json";
        }
        if(!headers["Authorization"])
          headers["Authorization"] =  `Bearer ${auth.token}`;

        const response = await fetch(url, {
          // mode: "no-cors",
          method,
          body,
          headers,
        });
        const data = await response.json();

        if (!response.ok) {
          if (response.status == 401) {
            await fetch('auth/refresh', { method:'Post', body:{refreshToken: auth.refreshToken}, headers})
            console.log("asdf");
          }
          throw new Error(data.message || "Что-то пошло не так");
        }

        setLoading(false);

        return data;
      } catch (e) {
        setLoading(false);
        setError(e.message);
        throw e;
      }
    },
    []
  );

  const clearError = useCallback(() => setError(null), []);

  return { loading, request, error, clearError };
};
