import { useState, useCallback, useEffect } from "react";

const storageName = "user";

export const useSetGlobalData = () => {
  const [name, setName] = useState(null);
  const [username, setUsername] = useState(null);
  const [email, setEmail] = useState(null);
  const [sex, setSex] = useState(null);
  const [birth, setBirth] = useState(null);
  const [phoneNumber, setPhoneNumber] = useState(null);
  const [id, setId] = useState(null);
  const [lastEvent, setLastEvent_] = useState(null);
  const setInfo = useCallback(
    (name, username, email, sex, birth, phoneNumber, id) => {
      setName(name);
      setUsername(username);
      setEmail(email);
      setSex(sex);
      setBirth(birth);
      setPhoneNumber(phoneNumber);
      setId(id);

      localStorage.setItem(
        storageName,
        JSON.stringify({
          id: id,
          name: name,
          username: username,
          email: email,
          sex: sex,
          phoneNumber: phoneNumber,
          birth: birth,
        })
      );
    },
    []
  );
  const setLastEvent = useCallback((event) => {
    setLastEvent_(event);

    localStorage.setItem(
      storageName + "event",
      JSON.stringify({
        lastEvent: event,
      })
    );
  }, []);
  const deleteInfo = useCallback(() => {
    setName(null);
    setUsername(null);
    setEmail(null);
    setSex(null);
    setBirth(null);
    setPhoneNumber(null);
    setLastEvent_(null);
    localStorage.removeItem(storageName);
    localStorage.removeItem(storageName + "event");
  }, []);

  useEffect(() => {
    const data = JSON.parse(localStorage.getItem(storageName));
    if (data && data.id) {
      setInfo(
        data.name,
        data.username,
        data.email,
        data.sex,
        data.birth,
        data.phoneNumber,
        data.id
      );
    }
    const eventData = JSON.parse(localStorage.getItem(storageName));
    if (eventData && eventData.lastEvent) {
      setLastEvent(eventData.lastEvent);
    }
  }, [setInfo, setLastEvent]);

  return {
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
  };
};
