////////////////////////////
//// AUTHOR @NavSethi2006
///////////////////////////
package com.android.echosense;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.StrictMode;
import android.view.View;
import android.widget.Button;
import android.widget.SeekBar;
import android.widget.TextView;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;


public class MainActivity extends AppCompatActivity {

    SeekBar HeightBar;
    TextView HeightTextInCm;
    Button SendData;

    Socket socket;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        HeightBar = (SeekBar)findViewById(R.id.Height_bar);
        HeightBar.setMax(400);

        SendData = (Button) findViewById(R.id.send_info_button);

        HeightTextInCm = (TextView) findViewById(R.id.Height_in_cm);


        if (android.os.Build.VERSION.SDK_INT > 9) {
            StrictMode.ThreadPolicy gfgPolicy =
                    new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(gfgPolicy);
        }

        HeightBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                HeightTextInCm.setText(""+progress);
            }
            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {}
            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {}
        });

        network_thread();



    }

    public void network_thread() {
        new Thread(new Runnable() {
            DataInputStream inputStream;
            DataOutputStream outputStream;
            String server_msg;
            @Override
            public void run() {
                while(true) {
                    try {

                        socket = new Socket("raspberrypi", 8080);
                        inputStream = new DataInputStream(System.in);
                        outputStream = new DataOutputStream(socket.getOutputStream());
                        break;
                    } catch (IOException e) {
                        System.out.println("shit is not connecting");

                    }
                }
                while(true) {



                    SendData.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {
                            try {
                                int height = HeightBar.getProgress();
                                String height_send = Integer.toString(height);
                                outputStream.writeUTF(height_send);
                            } catch (IOException e) {
                                System.out.println("Cant send message");
                            }
                        }
                    });
                }
            }
        }).start();


    }


}