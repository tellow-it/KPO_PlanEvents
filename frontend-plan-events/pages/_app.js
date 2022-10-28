import "../styles/globals.css";
import { AuthContext } from "../context/AuthContext";
import { useAuth } from "../hooks/auth.hook";
import { NextResponse } from "next/server";
import { useRouter } from "next/router";
import SignIn from "./SignIn";
import SignUp from "./SignUp";

function MyApp({ Component, pageProps }) {
  const { token, login, logout, id, refreshToken } = useAuth();
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
          id,
        }}
      >
        <Component {...pageProps} />
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
          id,
        }}
      >
        <SignIn />
      </AuthContext.Provider>
    );
  }
}

export default MyApp;
