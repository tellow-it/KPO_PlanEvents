package com.example.planeventsmobile

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.EditText
import androidx.appcompat.app.AppCompatActivity

class Registration : AppCompatActivity() {
    private lateinit var emailEditText: EditText
    private lateinit var phoneEditText: EditText
    private lateinit var passwordEditText: EditText
    private lateinit var usernameEditText: EditText
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_registration)
        emailEditText = findViewById(R.id.email);
        phoneEditText = findViewById(R.id.phone);
        passwordEditText = findViewById(R.id.user_password);
        usernameEditText = findViewById(R.id.name);
    }
    fun onSend(view: View) {
        val answerIntent = Intent()
        answerIntent.putExtra("email",emailEditText.text.toString())
        answerIntent.putExtra("username",usernameEditText.text.toString())
        answerIntent.putExtra("password",passwordEditText.text.toString())
        answerIntent.putExtra("phone",phoneEditText.text.toString())
        setResult(RESULT_OK, answerIntent)
        finish()
    }
}