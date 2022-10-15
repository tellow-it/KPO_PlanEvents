package com.example.planeventsmobile

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.planeventsmobile.ui.login.LoginActivity

class MainActivity : AppCompatActivity() {

    fun randomMe() {
// Create an Intent to start the second activity
        val randomIntent = Intent(this, LoginActivity::class.java)
        startActivity(randomIntent)

    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        randomMe()

    }
}