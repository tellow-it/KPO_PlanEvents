package com.example.planeventsmobile.ui.login

/**
 * Authentication result : success (user details) or error message.
 */
data class LoginResult(
    val success: LoggedInUserView? = null,
    val error: Int? = null
)

data class RegResult(
    val success: LoggedInUserView? = null,
    val error: Int? = null
)