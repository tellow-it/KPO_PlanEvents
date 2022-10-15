package com.example.planeventsmobile.data
import com.example.planeventsmobile.data.model.LoggedInUser
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import java.io.IOException

data class UserData(val email: String, val password: String, val phone: String, val username: String)
var fakeDataBase = """
    [
    {
    "email" = "some@gmail.com",
    "password" = "password",
    "phone" = "88005553535",
    "username" = "SomeGuy"
    },
    {
    "email" = "some_two@yandex.ru",
    "password" = "password2",
    "phone" = "88003334343",
    "username" = "SomeGuy2"
    }
    ]
""".trimIndent()
/**
 * Class that handles authentication w/ login cred entials and retrieves user information.
 */
class LoginDataSource {
    fun login(username: String, password: String): Result<LoggedInUser> {
       // val adapter = moshi.adapter<List<Card>>()
        //val cards: List<Card> = adapter.fromJson(cardsJsonResponse)

        try {
            var dataBase = Gson().fromJson<List<UserData>>(fakeDataBase)
            for (user in dataBase) {
                if ((user.email == username) &&( user.password == password))
                {
                    val fakeUser = LoggedInUser(java.util.UUID.randomUUID().toString(), user.username)
                    return Result.Success(fakeUser)
                }
            }
            return Result.Error(IOException("Неверный email или пароль"))

        } catch (e: Throwable) {
            return Result.Error(IOException("Error logging in", e))
        }
    }
    inline fun <reified T> Gson.fromJson(json: String) = fromJson<T>(json, object : TypeToken<T>() {}.type)

    fun registeration(username: String, password: String, phone: String, email: String): Result<LoggedInUser> {
        try {
            var database = Gson().fromJson<ArrayList<UserData>>(fakeDataBase)
            var isValid = true
            for (usr in database)
            {
                if ((usr.email == email)||(usr.phone == phone)||(usr.username == username))
                {
                    isValid=false
                }
            }
            // TODO: handle loggedInUser authentication
            if (isValid)
            {
                database.add(UserData(email,password, phone, username))
                fakeDataBase=Gson().toJson(database)
                print(fakeDataBase)
                val fakeUser = LoggedInUser("","")
                return Result.Success(fakeUser)
            }
            else
            {
                return Result.Error(IOException("Неверная дата"))
            }
        } catch (e: Throwable) {
            return Result.Error(IOException("Error logging in", e))
        }
    }

    fun logout() {
        // TODO: revoke authentication
    }
}