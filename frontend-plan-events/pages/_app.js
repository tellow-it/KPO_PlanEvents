import "../styles/globals.css";
import { AuthContext } from "../context/AuthContext";
import { UserContext } from "../context/UserContext";
import { useAuth } from "../hooks/auth.hook";
import { useSetGlobalData } from "../hooks/setGlobalData.hook";
import { NextResponse } from "next/server";
import { useRouter } from "next/router";
import SignIn from "./SignIn";
import SignUp from "./SignUp";

function MyApp({ Component, pageProps }) {
  const { token, login, logout, refreshToken } = useAuth();
  const {
    setInfo,
    deleteInfo,
    name,
    username,
    sex,
    birth,
    phoneNumber,
    id,
    email,
    lastEvent,
    setLastEvent,
  } = useSetGlobalData();
  console.log(token);
  const router = useRouter();

  console.log(Component == SignIn);
  console.log("----");
  const isAuthenticated = !!token;
  if (isAuthenticated && (Component == SignIn || Component == SignUp)) {
    router.push("/");
  }

  if (isAuthenticated || Component == SignIn || Component == SignUp) {
    return (
      <AuthContext.Provider
        value={{
          token,
          refreshToken,
          login,
          logout,
          isAuthenticated,
        }}
      >
        <UserContext.Provider
          value={{
            setInfo,
            deleteInfo,
            name,
            username,
            sex,
            birth,
            phoneNumber,
            id,
            email,
            lastEvent,
            setLastEvent,
          }}
        >
          <Component {...pageProps} />
        </UserContext.Provider>
      </AuthContext.Provider>
    );
  } else {
    // router.push("/SignIn");
    return (
      <AuthContext.Provider
        value={{
          token,
          refreshToken,
          login,
          logout,
          isAuthenticated,
        }}
      >
        <UserContext.Provider
          value={{
            setInfo,
            deleteInfo,
            name,
            username,
            sex,
            birth,
            phoneNumber,
            id,
            email,
            lastEvent,
            setLastEvent,
          }}
        >
          <SignIn />
        </UserContext.Provider>
      </AuthContext.Provider>
    );
  }
}

export default MyApp;
