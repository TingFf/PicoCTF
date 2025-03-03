## Comment  
1. First Android challenge, quite interesting.  
2. Used emulator.  

## Challenge Overview  
**Difficulty:** Hard  
**Description:** Used emulator and java decompiler to get the flag.  
## Tools Used  
**Jadx, Android Studio**

## Writeup  
1. According to the hint, I downloaded a android emulator and the apk inside the virtual phone.
![ScreenShot](https://imgur.com/MZ0InGy.png)  

2. The app doesn't seem to do much except a input text box, a button and a message.
3. Then to decompile and analyse the apk file. I use jadx to do the job.
MainActivity:
```
package com.hellocmu.picoctf;

import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

/* loaded from: classes.dex */
public class MainActivity extends AppCompatActivity {
    Button button;
    Context ctx;
    TextView text_bottom;
    EditText text_input;
    TextView text_top;

    @Override // androidx.appcompat.app.AppCompatActivity, androidx.fragment.app.FragmentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        this.text_top = (TextView) findViewById(R.id.text_top);
        this.text_bottom = (TextView) findViewById(R.id.text_bottom);
        this.text_input = (EditText) findViewById(R.id.text_input);
        this.ctx = getApplicationContext();
        System.loadLibrary("hellojni");
        this.text_top.setText(R.string.hint);
    }

    public void buttonClick(View view) {
        String content = this.text_input.getText().toString();
        this.text_bottom.setText(FlagstaffHill.getFlag(content, this.ctx));
    }
}
```
4. There is a buttonClick function so I assume if I click the button, I will get the flag.  
FlagstaffHill:
```
package com.hellocmu.picoctf;

import android.content.Context;
import android.util.Log;

/* loaded from: classes.dex */
public class FlagstaffHill {
    public static native String paprika(String str); // Native method

    public static String getFlag(String input, Context ctx) {
        Log.i("PICO", paprika(input));
        return "Not Today...";
    }
}
```
5. Clicking on the button should send a string to the log in the android emulator.
Logcat:
![ScreenShot](https://imgur.com/ar2LPmk.png)  


## Stuff Learned  
1. To download the apk just drag and drop into the emulator.  
2. Log.i(...) logs the output in logcat.  
3. Native method is a the function that is declared in Java but implemented elsewhere in a compiled native library hence its harder to analyze cause is inside a complied .so file.
   
