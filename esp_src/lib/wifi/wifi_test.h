#ifndef __WIFI__
#define __WIFI__

#include <ESP8266WiFi.h>
#include "constants.h"

extern "C" {
    void esp_schedule();
    void esp_yield();
    #include <ping.h>
} 
/*
    Host IDs 
    Testing-env.wy7afakpky.us-east-2.elasticbeanstalk.com :  80
    192.168.1.18 : 8000
*/

#ifdef _ENABLE_POST_DEBUG
    #define SS_ID       "Kim Family"
    #define SS_PW       "9497690303"
    #define HOST_ID     "192.168.1.18"
    #define HOST_PATH   "/data_collection/"
    #define HOST_PORT   8000
#else
    #define SS_ID       "J_PHONE"
    #define SS_PW       "iot_testing"
    #define HOST_ID     "Testing-env.wy7afakpky.us-east-2.elasticbeanstalk.com"
    #define HOST_PATH   "/data_collection/"
    #define HOST_PORT   80
#endif

#define IN_BUFFER_SIZE 1000
#define OUT_BUFFER_SIZE 1000

#ifdef _ENABLE_WIFI_DEBUG
    #define DEBUG_PING(...) Serial.printf(__VA_ARGS__)
#else
    #define DEBUG_PING(...)
#endif


class WiFi_Test {
    /*
     *  Debug class for indicating failures of the board. 
     */
    const char* ss_id   = SS_ID;
    const char* ss_pw   = SS_PW;

    const char* host_id = HOST_ID;
    const uint8_t host_port   = HOST_PORT;

    char request_buffer[IN_BUFFER_SIZE];
    char response_buffer[OUT_BUFFER_SIZE];

    uint8_t connection_state = 0;

protected:
    static byte _expected_count;
    static byte _errors;
    static byte _success;
    static int _avg_time;

    IPAddress _dest;
    ping_option _options;

    static void _ping_sent_cv(void *opt, void *pdata);
    static void _ping_recv_cb(void *opt, void *pdata);

    void __do_http_request(char* request, char* response, uint16_t response_size, 
        uint16_t response_timeout);

    uint8_t __append_char(char* buffer, char c, uint16_t buffer_size);

public:
    /* Normal constructor */
    WiFi_Test();

    /* Constructor with different access point connection (probably unused) */
    WiFi_Test(const char* router_id, const char* router_pw);
    
    /* Initialization function [BLOCKING]
     * - Function that establishes connection to access point
     */
    void init();

    /* ** Function to connect to host website **
     * - Uses WiFiClient class to establish connection to a host 
     * 
     * Note: connection to an access point will be necessary first
     */
    void do_post_request(char* data);

    /* ** Testing Functions
     * - ping functions to test functionality 
     *   of WiFi module
     */
    bool ping_host(byte count);
    int average_time();

};

#endif
