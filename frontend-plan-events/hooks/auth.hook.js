import {useState, useCallback, useEffect} from 'react'

const storageName = 'userDatjhjh'

export const useAuth = () => 
{
    const [token, setToken] = useState(null)
    const [refreshToken, setrRefreshToken] = useState(null)  
    
    const login = useCallback((jwtToken, refreshToken) => 
    {
        setToken(jwtToken)
        setrRefreshToken(refreshToken)
        
        localStorage.setItem(storageName, JSON.stringify(
            {
                refreshToken: refreshToken, 
                token: jwtToken,
            }))
     }, [])

    const logout = useCallback(() => 
    {
        setToken(null)
        setrRefreshToken(null)
        localStorage.removeItem(storageName)
    }, [])

    useEffect(() => 
    {
        const data = JSON.parse(localStorage.getItem(storageName))
        if (data && data.token)
        {
            login(data.token,data.refreshToken)
        }
    }, [login])

    return { login, logout, token, refreshToken }
}