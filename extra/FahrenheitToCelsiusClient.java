import java.net.*;
import java.io.*;
import java.util.*;

public class FahrenheitToCelsiusClient {

    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Temperature in Fahrenheit: ");
        double f = sc.nextDouble();
        sc.close();

        URL url = new URL("http://127.0.0.1:8796/convert");
        HttpURLConnection con = (HttpURLConnection) url.openConnection();

        con.setRequestMethod("POST");
        con.setRequestProperty("Content-Type", "application/json");
        con.setDoOutput(true);

        String json = "{\"fahrenheit\":" + f + "}";

        try (OutputStream os = con.getOutputStream()) {
            os.write(json.getBytes());
        }

        BufferedReader br = new BufferedReader(
                new InputStreamReader(con.getInputStream()));

        String line, response = "";
        while ((line = br.readLine()) != null) {
            response += line;
        }

        System.out.println("Response Code: " + con.getResponseCode());
        System.out.println("Response: " + response);
    }
}
