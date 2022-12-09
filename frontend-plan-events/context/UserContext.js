import { createContext } from "react";

function noop() {}

export const UserContext = createContext(
    {
        id: null,
        username: null,
        email: null,
        name: null,
        birth: null,
        sex: null,
        phoneNumber: null,
        lastEvent:null,
        setLastEvent:noop,
        setInfo: noop,
        deleteInfo: noop,
    }
)