#include "wifi_test.h"

WiFi_Test::WiFi_Test(){
    Serial.println("[WIFI] Initializing Wifi Sensor");
    WiFi.mode(WIFI_STA);
    WiFi.begin(ss_id, ss_pw);
    Serial.print("[WIFI] SSID:");
    Serial.print(ss_id);
    Serial.print(" WiFi Mode: WIFI_STA\n");
}

WiFi_Test::WiFi_Test(const char* router_id, const char* router_pw) : ss_id(router_id), ss_pw(router_pw) {
    Serial.println("[WIFI] Initializing Wifi Sensor");
    WiFi.mode(WIFI_STA);
    WiFi.begin(ss_id, ss_pw);
    Serial.print("[WIFI] SSID:");
    Serial.print(ss_id);
    Serial.print(" WiFi Mode: WIFI_STA\n");
}

void WiFi_Test::init(){
    Serial.print("[WIFI] Connecting to ");
    Serial.print(ss_id);
    Serial.print("\nStatus:\t");
    while (WiFi.status() != WL_CONNECTED) {
        delay(250);
        Serial.print(".");
        blink_RGB_LED(100, HIGH, LOW, LOW);
    }
    Serial.println("");
    Serial.print("[WIFI] WiFi connected! ");
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
}

void WiFi_Test::do_post_request(char* data){
    Serial.println("[WIFI] Attempting Post Request!");
    char body[200];
    sprintf(body, "text=%s", data);

    int body_length = strlen(body);
    Serial.println(body);
    sprintf(request_buffer, "POST %s HTTP/1.1\r\n", HOST_PATH);
    strcat(request_buffer, "Host: ");
    strcat(request_buffer, HOST_ID);
    strcat(request_buffer, "\r\n");
    // sprintf(request_buffer, "Host: %s\r\n", HOST_ID);
    strcat(request_buffer, "Content-Type: application/x-www-form-urlencoded\r\n");
    sprintf(request_buffer + strlen(request_buffer), "Content-Length: %d\r\n", body_length);
    strcat(request_buffer, "\r\n");
    strcat(request_buffer, body);
    strcat(request_buffer, "\r\n");
    Serial.println("[WIFI] Printing Request buffer");
    Serial.println(request_buffer);
    __do_http_request(request_buffer, response_buffer, OUT_BUFFER_SIZE, 6000 );
}

bool WiFi_Test::ping_host(byte count){
    IPAddress _remote_address;
    if (WiFi.hostByName(host_id, _remote_address)){
        _expected_count = count;
        _errors = 0;
        _success = 0;
        _avg_time = 0;

        memset(&_options, 0, sizeof(struct ping_option));

        _options.count = count;
        _options.coarse_time = 1;
        _options.ip = _remote_address;

        /* Callbacks */
        _options.recv_function = reinterpret_cast<ping_recv_function>(&WiFi_Test::_ping_recv_cb);
        _options.sent_function = NULL;

        if (ping_start(&_options)){
            esp_yield();
        }

        return (_success > 0);
    }

    return false;
}

int WiFi_Test::average_time(){
    return _avg_time;
}

/* Protected and Private */
void WiFi_Test::__do_http_request(char* request, char* response, uint16_t response_size, 
    uint16_t response_timeout){
    WiFiClient client;
    // const char* _url = "/data/collection.py";
    if (client.connect(HOST_ID, HOST_PORT)){
        client.print(request);

        memset(response, 0, response_size);
        uint32_t timeout_counter = millis();
        while (client.connected()){
            client.readBytesUntil('\n', response, response_size);
            // Serial.println("HTTP/1.1 200 OK");
            if (strcmp(response, "\r")){
                break;
            }
            memset(response, 0, response_size);
            if (millis() - timeout_counter > response_timeout){
                break;
            }
        }
        memset(response, 0, response_size);
        timeout_counter = millis();
        while (client.available()){
            __append_char(response, client.read(), OUT_BUFFER_SIZE);
        }
        Serial.println(response);
    }
    else {
        Serial.println("Connection to server failed!");
        
    }
    client.stop();
}

uint8_t WiFi_Test::__append_char(char* buffer, char c, uint16_t buffer_size){
    int length = strlen(buffer);
    if (length >= buffer_size){
        return 0;
    }
    else {
        buffer[length] = c;
        buffer[length+1] = '\0';
        return 1;
    }
}

/* Ping Tests */

void WiFi_Test::_ping_recv_cb(void *opt, void *resp){
    // Cast the parameters to get some usable info
    ping_resp*   ping_resp = reinterpret_cast<struct ping_resp*>(resp);

    // Determine Error or Success
    if (ping_resp->ping_err == -1)
        _errors++;
    else {
        _success++;
        _avg_time += ping_resp->resp_time;
    }

    // Set and print debug info
    DEBUG_PING(
            "DEBUG: ping reply\n"
            "\ttotal_count = %d \n"
            "\tresp_time = %d \n"
            "\tseqno = %d \n"
            "\ttimeout_count = %d \n"
            "\tbytes = %d \n"
            "\ttotal_bytes = %d \n"
            "\ttotal_time = %d \n"
            "\tping_err = %d \n",
            ping_resp->total_count, ping_resp->resp_time, ping_resp->seqno,
            ping_resp->timeout_count, ping_resp->bytes, ping_resp->total_bytes,
            ping_resp->total_time, ping_resp->ping_err
    );

    // Check if time to end
    if (_success + _errors == _expected_count) {
        _avg_time = _success > 0 ? _avg_time / _success : 0;

        // Print debug statement if declared 
        DEBUG_PING("Avg resp time %d ms\n", _avg_time);

        // Done, return to main functiom
        esp_schedule();
    }
}

byte WiFi_Test::_expected_count = 0;
byte WiFi_Test::_errors     = 0;
byte WiFi_Test::_success    = 0;
int WiFi_Test::_avg_time    = 0;