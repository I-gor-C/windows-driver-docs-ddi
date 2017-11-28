# Wwan.h header


This header is used by unknown technology.

Wwan.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [WWAN_AUTH_AKAP_CHALLENGE structure](ns-wwan--wwan-auth-akap-challenge.md) | The WWAN_AUTH_AKAP_CHALLENGE structure represents an authentication challenge using the AKA' method. |
| [WWAN_AUTH_AKAP_RESPONSE structure](ns-wwan--wwan-auth-akap-response.md) | The WWAN_AUTH_AKAP_RESPONSE structure represents a response to an AKA' (AKA Prime) authentication challenge. |
| [WWAN_AUTH_AKA_CHALLENGE structure](ns-wwan--wwan-auth-aka-challenge.md) | The WWAN_AUTH_AKA_CHALLENGE structure represents an authentication challenge using the AKA method. |
| [WWAN_AUTH_AKA_RESPONSE structure](ns-wwan--wwan-auth-aka-response.md) | The WWAN_AUTH_AKA_RESPONSE structure represents a response to an AKA authentication challenge. |
| [WWAN_AUTH_CHALLENGE structure](ns-wwan--wwan-auth-challenge.md) | The WWAN_AUTH_CHALLENGE structure represents an authentication challenge for a specific method. |
| [WWAN_AUTH_RESPONSE structure](ns-wwan--wwan-auth-response.md) | The WWAN_AUTH_RESPONSE structure represents an authentication challenge response. |
| [WWAN_AUTH_SIM_CHALLENGE structure](ns-wwan--wwan-auth-sim-challenge.md) | The WWAN_AUTH_SIM_CHALLENGE structure represents an authentication challenge using the SIM method. |
| [WWAN_AUTH_SIM_RESPONSE structure](ns-wwan--wwan-auth-sim-response.md) | The WWAN_AUTH_SIM_RESPONSE structure represents a response to a SIM authentication challenge. |
| [WWAN_BASE_STATIONS_INFO structure](ns-wwan--wwan-base-stations-info.md) | The WWAN_BASE_STATIONS_INFO structure represents information about both serving and neighboring base stations. |
| [WWAN_BASE_STATIONS_INFO_REQ structure](ns-wwan--wwan-base-stations-info-req.md) | The WWAN_BASE_STATIONS_INFO_REQ structure represents the aspects of cellular base stations information that are requested in a base stations information query. |
| [WWAN_CDMA_MRL structure](ns-wwan--wwan-cdma-mrl.md) | The WWAN_CDMA_MRL structure represents the measured results list (MRL) of both serving and neighboring CDMA cells. |
| [WWAN_CDMA_MRL_INFO structure](ns-wwan--wwan-cdma-mrl-info.md) | The WWAN_CDMA_MRL_INFO structure represents information about a CDMA serving cell or neighboring cell. |
| [WWAN_CONTEXT structure](ns-wwan--wwan-context.md) | The WWAN_CONTEXT structure represents a provisioned context that is supported by the MB device. |
| [WWAN_CONTEXT_STATE structure](ns-wwan--wwan-context-state.md) | The WWAN_CONTEXT_STATE structure represents the Packet Data Protocol (PDP) context state of the MB device. |
| [WWAN_DEVICE_CAPS structure](ns-wwan--wwan-device-caps.md) | The WWAN_DEVICE_CAPS structure represents the capabilities of the MB device. |
| [WWAN_DEVICE_CAPS_EX structure](ns-wwan--wwan-device-caps-ex.md) | The WWAN_DEVICE_CAPS_EX structure represents the capabilities of the mobile broadband device. |
| [WWAN_DEVICE_SERVICE_COMMAND structure](ns-wwan--wwan-device-service-command.md) | The WWAN_DEVICE_SERVICE_COMMAND structure represents a device service command. |
| [WWAN_DEVICE_SERVICE_ENTRY structure](ns-wwan--wwan-device-service-entry.md) | The WWAN_DEVICE_SERVICE_ENTRY structure describes information about a device service. |
| [WWAN_DEVICE_SERVICE_EVENT structure](ns-wwan--wwan-device-service-event.md) | The WWAN_DEVICE_SERVICE_EVENT structure represents an unsolicited device service event. |
| [WWAN_DEVICE_SERVICE_RESPONSE structure](ns-wwan--wwan-device-service-response.md) | The WWAN_DEVICE_SERVICE_RESPONSE structure represents a response from a device service. |
| [WWAN_DEVICE_SERVICE_SESSION structure](ns-wwan--wwan-device-service-session.md) | The WWAN_DEVICE_SERVICE_SESSION structure represents the state of a device service session, or the operation to be performed on a device service. |
| [WWAN_DEVICE_SERVICE_SESSION_READ structure](ns-wwan--wwan-device-service-session-read.md) | The WWAN_DEVICE_SERVICE_SESSION_READ structure represents data associated with a device service session read notification. |
| [WWAN_DEVICE_SERVICE_SESSION_WRITE structure](ns-wwan--wwan-device-service-session-write.md) | The WWAN_DEVICE_SERVICE_SESSION_WRITE structure represents data associated with a device service session write request. |
| [WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS structure](ns-wwan--wwan-device-service-supported-commands.md) | The WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS structure represents a list of commands supported by a device service. |
| [WWAN_DEVICE_SLOT_MAPPING_INFO structure](ns-wwan--wwan-device-slot-mapping-info.md) | The WWAN_DEVICE_SLOT_MAPPING_INFO structure represents the executor-to-slot mapping relationship in the MB device. |
| [WWAN_DRIVER_CAPS structure](ns-wwan--wwan-driver-caps.md) | The WWAN_DRIVER_CAPS structure represents the capabilities of the miniport driver. |
| [WWAN_GET_SLOT_INFO structure](ns-wwan--wwan-get-slot-info.md) | The WWAN_GET_SLOT_INFO structure contains the slot index to specify which slot's status a query request is for. |
| [WWAN_GET_VISIBLE_PROVIDERS structure](ns-wwan--wwan-get-visible-providers.md) | The WWAN_GET_VISIBLE_PROVIDERS structure provides information about the type of visible providers to return. |
| [WWAN_GSM_NMR structure](ns-wwan--wwan-gsm-nmr.md) | The WWAN_GSM_NMR structure represents the network measurement report (NMR) of neighboring GSM cells. |
| [WWAN_GSM_NMR_INFO structure](ns-wwan--wwan-gsm-nmr-info.md) | The WWAN_GSM_NMR_INFO structure represents information about a neighboring GSM cell. |
| [WWAN_GSM_SERVING_CELL_INFO structure](ns-wwan--wwan-gsm-serving-cell-info.md) | The WWAN_GSM_SERVING_CELL_INFO structure represents information about the GSM serving cell. |
| [WWAN_IPADDRESS_ENTRY structure](ns-wwan--wwan-ipaddress-entry.md) | The WWAN_IPADDRESS_ENTRY structure represents either the IPV4 or IPV6 address of a PDP context. |
| [WWAN_IPV4_ADDRESS structure](ns-wwan--wwan-ipv4-address.md) | The WWAN_IPV4_ADDRESS structure represents an IPV4 address of a PDP context. |
| [WWAN_IPV6_ADDRESS structure](ns-wwan--wwan-ipv6-address.md) | The WWAN_IPV6_ADDRESS structure represents an IPV6 address of a PDP context. |
| [WWAN_IP_ADDRESS_STATE structure](ns-wwan--wwan-ip-address-state.md) | The WWAN_IP_ADDRESS_STATE structure represents the IP addresses, gateways, DNS servers, and/or MTUs of a PDP context. |
| [WWAN_IP_CONFIGURATION_FLAGS structure](ns-wwan-wwan-ip-configuration-flags.md) | The WWAN_IP_CONFIGURATION_FLAGS structure represents flags that describe the availability of the IP address, gateway, DNS server, and/or MTU information of a PDP context. |
| [WWAN_LIST_HEADER structure](ns-wwan--wwan-list-header.md) | The WWAN_LIST_HEADER structure represents the header of a list of MB objects, including the number of objects in the list that follow the header in memory. |
| [WWAN_LTE_MRL structure](ns-wwan--wwan-lte-mrl.md) | The WWAN_LTE_MRL structure represents the measured results list (MRL) of neighboring LTE cells. |
| [WWAN_LTE_MRL_INFO structure](ns-wwan--wwan-lte-mrl-info.md) | The WWAN_LTE_MRL_INFO structure represents information about a neighboring LTE cell. |
| [WWAN_LTE_SERVING_CELL_INFO structure](ns-wwan--wwan-lte-serving-cell-info.md) | The WWAN_LTE_SERVING_CELL_INFO structure represents information about the LTE serving cell. |
| [WWAN_MODEM_CONFIG_INFO structure](ns-wwan--wwan-modem-config-info.md) | The WWAN_MODEM_CONFIG_INFO structure represents the modem's configuration information. |
| [WWAN_MODEM_CONFIG_STATUS structure](ns-wwan--wwan-modem-config-status.md) | The WWAN_MODEM_CONFIG_STATUS structure represents a modem's configuration (config) status. |
| [WWAN_NETWORK_IDLE_HINT structure](ns-wwan--wwan-network-idle-hint.md) | The WWAN_NETWORK_IDLE_HINT structure contains a hint for the network interface regarding whether data is expected to be active or idle on the interface. |
| [WWAN_PACKET_SERVICE structure](ns-wwan--wwan-packet-service.md) | The WWAN_PACKET_SERVICE structure represents the packet service attachment state of the MB device. |
| [WWAN_PCO_VALUE structure](ns-wwan--wwan-pco-value.md) | The WWAN_PCO_VALUE structure represents the PCO information payload from the network as defined in the 3GPP TS24.008 spec. |
| [WWAN_PIN_ACTION structure](ns-wwan--wwan-pin-action.md) | The WWAN_PIN_ACTION structure represents actions to perform with a Personal Identification Number (PIN). |
| [WWAN_PIN_DESC structure](ns-wwan--wwan-pin-desc.md) | The WWAN_PIN_DESC structure represents the description or current status for a Personal Identification Number (PIN). |
| [WWAN_PIN_INFO structure](ns-wwan--wwan-pin-info.md) | The WWAN_PIN_INFO structure represents PIN type and PIN-entry state of Personal Identification Number (PIN) information required by the MB device. |
| [WWAN_PIN_LIST structure](ns-wwan--wwan-pin-list.md) | The WWAN_PIN_LIST structure represents a list of descriptions of Personal Identification Numbers (PINs). |
| [WWAN_PROVIDER structure](ns-wwan--wwan-provider.md) | The WWAN_PROVIDER structure represents details about a network provider. |
| [WWAN_PROVIDER2 structure](ns-wwan--wwan-provider2.md) | The WWAN_PROVIDER2 structure describes the details of a network provider. |
| [WWAN_RADIO_STATE structure](ns-wwan--wwan-radio-state.md) | The WWAN_RADIO_STATE structure represents the hardware-based and software-based radio power states of the MB device. |
| [WWAN_READY_INFO structure](ns-wwan--wwan-ready-info.md) | The WWAN_READY_INFO structure represents the ready-state of the MB device. |
| [WWAN_REGISTRATION_STATE structure](ns-wwan--wwan-registration-state.md) | The WWAN_REGISTRATION_STATE structure represents the registration state of the MB device. |
| [WWAN_SERVICE_ACTIVATION structure](ns-wwan--wwan-service-activation.md) | The WWAN_SERVICE_ACTIVATION structure represents a vendor-specific buffer to be associated with service activation. |
| [WWAN_SERVICE_ACTIVATION_STATUS structure](ns-wwan--wwan-service-activation-status.md) | The WWAN_SERVICE_ACTIVATION_STATUS structure represents the status of service activation on the MB device. |
| [WWAN_SET_CONTEXT structure](ns-wwan--wwan-set-context.md) | The WWAN_SET_CONTEXT structure represents a provisioned context with a network provider identification that is supported by the MB device. |
| [WWAN_SET_CONTEXT_STATE structure](ns-wwan--wwan-set-context-state.md) | The WWAN_SET_CONTEXT_STATE structure represents the command to set the Packet Data Protocol (PDP) context state of the MB device. |
| [WWAN_SET_REGISTER_STATE structure](ns-wwan--wwan-set-register-state.md) | The WWAN_SET_REGISTER_STATE structure represents the command to set the MB device's registration mode and the network provider it should register with. |
| [WWAN_SET_SIGNAL_INDICATION structure](ns-wwan--wwan-set-signal-indication.md) | The WWAN_SET_SIGNAL_INDICATION structure represents the frequency of RSSI interval and RSSI threshold notifications. |
| [WWAN_SET_SMS_CONFIGURATION structure](ns-wwan--wwan-set-sms-configuration.md) | The WWAN_SET_SMS_CONFIGURATION structure represents how MB devices support SMS configuration. |
| [WWAN_SET_UICC_RESET structure](ns-wwan--wwan-set-uicc-reset.md) | The WWAN_SET_UICC_RESET structure represents the passthrough action the MB host specifies for a modem miniport adapter after it resets a UICC smart card. |
| [WWAN_SIGNAL_STATE structure](ns-wwan--wwan-signal-state.md) | The WWAN_SIGNAL_STATE structure represents the signal state of the MB device. |
| [WWAN_SLOT_INFO structure](ns-wwan--wwan-slot-info.md) | The WWAN_SLOT_INFO structure represents the status of a specific SIM card slot on the modem. |
| [WWAN_SMS_CDMA_RECORD structure](ns-wwan--wwan-sms-cdma-record.md) | The WWAN_SMS_CDMA_RECORD structure represents CDMA-based SMS text message records. |
| [WWAN_SMS_CONFIGURATION structure](ns-wwan--wwan-sms-configuration.md) | The WWAN_SMS_CONFIGURATION structure represents the SMS configuration of the MB device. |
| [WWAN_SMS_FILTER structure](ns-wwan--wwan-sms-filter.md) | The WWAN_SMS_FILTER structure represents the filter to apply to SMS messages on the MB device. |
| [WWAN_SMS_PDU_RECORD structure](ns-wwan--wwan-sms-pdu-record.md) | The WWAN_SMS_PDU_RECORD structure represents a PDU-style SMS message record. |
| [WWAN_SMS_READ structure](ns-wwan--wwan-sms-read.md) | The WWAN_SMS_READ structure represents the format and filter of SMS messages to read. |
| [WWAN_SMS_SEND structure](ns-wwan--wwan-sms-send.md) | The WWAN_SMS_SEND structure represents an SMS text message to send. |
| [WWAN_SMS_SEND_CDMA structure](ns-wwan--wwan-sms-send-cdma.md) | The WWAN_SMS_SEND_CDMA structure represents a CDMA-based SMS text message to send. |
| [WWAN_SMS_SEND_PDU structure](ns-wwan--wwan-sms-send-pdu.md) | The WWAN_SMS_SEND_PDU structure represents a PDU-style SMS message. |
| [WWAN_SMS_STATUS structure](ns-wwan--wwan-sms-status.md) | The WWAN_SMS_STATUS structure represents the status of the SMS message store. |
| [WWAN_SUPPORTED_DEVICE_SERVICES structure](ns-wwan--wwan-supported-device-services.md) | The WWAN_SUPPORTED_DEVICE_SERVICES structure describes information about device services supported by the miniport driver. |
| [WWAN_SYS_CAPS_INFO structure](ns-wwan--wwan-sys-caps-info.md) | The WWAN_SYS_CAPS_INFO structure represents the modem's system capability. |
| [WWAN_TDSCDMA_MRL structure](ns-wwan--wwan-tdscdma-mrl.md) | The WWAN_TDSCDMA_MRL structure represents the measured results list (MRL) of neighboring TDSCDMA cells. |
| [WWAN_TDSCDMA_MRL_INFO structure](ns-wwan--wwan-tdscdma-mrl-info.md) | The WWAN_TDSCDMA_MRL_INFO structure represents information about a neighboring TDSCDMA cell. |
| [WWAN_TDSCDMA_SERVING_CELL_INFO structure](ns-wwan--wwan-tdscdma-serving-cell-info.md) | The WWAN_TDSCDMA_SERVING_CELL_INFO structure represents information about the TDSCDMA serving cell. |
| [WWAN_UICC_RESET_INFO structure](ns-wwan--wwan-uicc-reset-info.md) | The WWAN_UICC_RESET_INFO structure represents the passthrough status of a modem miniport adapter for a UICC smart card. |
| [WWAN_UMTS_MRL structure](ns-wwan--wwan-umts-mrl.md) | The WWAN_UMTS_MRL structure contains the measured results list (MRL) of neighboring UMTS cells. |
| [WWAN_UMTS_MRL_INFO structure](ns-wwan--wwan-umts-mrl-info.md) | The WWAN_UMTS_MRL_INFO structure represents information about a neighboring UMTS cell. |
| [WWAN_UMTS_SERVING_CELL_INFO structure](ns-wwan--wwan-umts-serving-cell-info.md) | The WWAN_UMTS_SERVING_CELL_INFO structure represents information about the UMTS serving cell. |
| [WWAN_USSD_EVENT structure](ns-wwan--wwan-ussd-event.md) | The WWAN_USSD_REQUEST structure describes an Unstructured Supplementary Service Data (USSD) event. |
| [WWAN_USSD_REQUEST structure](ns-wwan--wwan-ussd-request.md) | The WWAN_USSD_REQUEST structure describes an Unstructured Supplementary Service Data (USSD) request. |
| [WWAN_USSD_STRING structure](ns-wwan--wwan-ussd-string.md) | The WWAN_USSD_STRING structure describes an Unstructured Supplementary Service Data (USSD) string. |
| [WWAN_VENDOR_SPECIFIC structure](ns-wwan--wwan-vendor-specific.md) | The WWAN_VENDOR_SPECIFIC structure represents vendor-specific data. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [WWAN_ACE_STATE enumeration](ne-wwan--wwan-ace-state.md) | The WWAN_ACE_STATE enumeration lists the different kinds of auto-connect states. |
| [WWAN_ACTIVATION_COMMAND enumeration](ne-wwan--wwan-activation-command.md) | The WWAN_ACTIVATION_COMMAND enumeration lists the Packet Data Protocol (PDP) activation commands that are supported by the MB device. |
| [WWAN_ACTIVATION_STATE enumeration](ne-wwan--wwan-activation-state.md) | The WWAN_ACTIVATION_STATE enumeration lists the different Packet Data Protocol (PDP) context activation states that are supported by the MB device. |
| [WWAN_ASYNC_GETSET_TYPE enumeration](ne-wwan--wwan-async-getset-type.md) | The WWAN_ASYNC_GETSET_TYPE enumeration lists the different asynchronous OID get/set requests. |
| [WWAN_AUTH_METHOD enumeration](ne-wwan--wwan-auth-method.md) | The WWAN_AUTH_METHOD enumeration lists supported authentication methods. |
| [WWAN_AUTH_PROTOCOL enumeration](ne-wwan--wwan-auth-protocol.md) | The WWAN_AUTH_PROTOCOL enumeration lists the different types of authentication protocols that are supported by the MB device. |
| [WWAN_CELLULAR_CLASS enumeration](ne-wwan--wwan-cellular-class.md) | The WWAN_CELLULAR_CLASS enumeration lists the different classes of cellular technology that are supported by the MB device. |
| [WWAN_COMPRESSION enumeration](ne-wwan--wwan-compression.md) | The WWAN_COMPRESSION enumeration lists the different compression options that are supported by the MB device. |
| [WWAN_CONTEXT_TYPE enumeration](ne-wwan--wwan-context-type.md) | The WWAN_CONTEXT_TYPE enumeration lists the different types of connection contexts that are supported by the MB device. |
| [WWAN_DEVICE_SERVICE_SESSION_CAPABILITY enumeration](ne-wwan--wwan-device-service-session-capability.md) | The WWAN_DEVICE_SERVICE_SESSION_CAPABILITY enumeration lists the different device service session operations that are supported by the device service. |
| [WWAN_DEVICE_SERVICE_SESSION_STATE enumeration](ne-wwan--wwan-device-service-session-state.md) | The WWAN_DEVICE_SERVICE_SESSION_STATE enumeration specifies the state of device service session. It can be used in a set operation to set the state of a session or can be used in an indication to report the state of a session. |
| [WWAN_DEVICE_TYPE enumeration](ne-wwan--wwan-device-type.md) | The WWAN_DEVICE_TYPE enumeration lists the different device types that describe the MB device. |
| [WWAN_EMERGENCY_MODE enumeration](ne-wwan--wwan-emergency-mode.md) | The WWAN_EMERGENCY_MODE enumeration lists the different types of emergency modes that are supported by the MB device. |
| [WWAN_IP_TYPE enumeration](ne-wwan--wwan-ip-type.md) | The WWAN_IP_TYPE enumeration lists the different levels of supported IP. |
| [WWAN_MODEM_CONFIG_MODE enumeration](ne-wwan--wwan-modem-config-mode.md) | The WWAN_MODEM_CONFIG_MODE enumeration lists modem configuration modes. |
| [WWAN_MODEM_CONFIG_REASON enumeration](ne-wwan--wwan-modem-config-reason.md) | The WWAN_MODEM_CONFIG_REASON enumeration lists definitions for reasons why a modem's configuration state change was triggered. |
| [WWAN_MODEM_CONFIG_STATE enumeration](ne-wwan--wwan-modem-config-state.md) | The WWAN_MODEM_CONFIG_STATE enumeration lists definitions used by the modem to inform the OS about its modem configuration state. |
| [WWAN_MSG_STATUS enumeration](ne-wwan--wwan-msg-status.md) | The WWAN_MSG_STATUS enumeration lists different SMS message statuses. |
| [WWAN_PACKET_SERVICE_ACTION enumeration](ne-wwan--wwan-packet-service-action.md) | The WWAN_PACKET_SERVICE_ACTION enumeration lists different packet service actions. |
| [WWAN_PACKET_SERVICE_STATE enumeration](ne-wwan--wwan-packet-service-state.md) | The WWAN_PACKET_SERVICE_STATE enumeration lists the different packet service attachment states that are supported by the MB device. |
| [WWAN_PCO_TYPE enumeration](ne-wwan--wwan-pco-type.md) | The WWAN_PCO_TYPE enumeration indicates whether the header of a PCO structure is partial, meaning only a subset of the complete PCO value from the network is being passed up to the host. |
| [WWAN_PIN_FORMAT enumeration](ne-wwan--wwan-pin-format.md) | The WWAN_PIN_FORMAT enumeration lists the different Personal Identification Number (PIN) formats that are supported by the MB device. |
| [WWAN_PIN_MODE enumeration](ne-wwan--wwan-pin-mode.md) | The WWAN_PIN_MODE enumeration lists the different states of a Personal Identification Number (PIN) type. |
| [WWAN_PIN_OPERATION enumeration](ne-wwan--wwan-pin-operation.md) | The WWAN_PIN_OPERATION enumeration lists the different Personal Identification Number (PIN) operations that are supported by the MB device. |
| [WWAN_PIN_STATE enumeration](ne-wwan--wwan-pin-state.md) | The WWAN_PIN_STATE enumeration describes whether the MB device or Subscriber Identity Module (SIM card) requires the user to enter a Personal Identification Number (PIN) to proceed to the next state. |
| [WWAN_PIN_TYPE enumeration](ne-wwan--wwan-pin-type.md) | The WWAN_PIN_TYPE enumeration lists the different types of Personal Identification Numbers (PINs) that are supported by the MB device. |
| [WWAN_RADIO enumeration](ne-wwan--wwan-radio.md) | The WWAN_RADIO enumeration lists the different types of radio power modes that are supported by the MB device. |
| [WWAN_READY_STATE enumeration](ne-wwan--wwan-ready-state.md) | The WWAN_READY_STATE enumeration lists the different device ready-states that are supported by the MB device. |
| [WWAN_REGISTER_ACTION enumeration](ne-wwan--wwan-register-action.md) | The WWAN_REGISTER_ACTION enumeration lists the different provider network registration actions that are supported by the MB device. |
| [WWAN_REGISTER_MODE enumeration](ne-wwan--wwan-register-mode.md) | The WWAN_REGISTER_MODE enumeration lists the different network selection modes which defines the way the device should select a network while registering. |
| [WWAN_REGISTER_STATE enumeration](ne-wwan--wwan-register-state.md) | The WWAN_REGISTER_STATE enumeration lists the different provider network registration states that are supported by the MB device. |
| [WWAN_SIM_CLASS enumeration](ne-wwan--wwan-sim-class.md) | The WWAN_SIM_CLASS enumeration lists the different types of Subscriber Identity Modules (SIMs) that are supported by the MB device. |
| [WWAN_SMS_CDMA_ENCODING enumeration](ne-wwan--wwan-sms-cdma-encoding.md) | The WWAN_SMS_CDMA_ENCODING enumeration lists the different SMS CDMA encoding formats that are supported by the MB device. |
| [WWAN_SMS_CDMA_LANG enumeration](ne-wwan--wwan-sms-cdma-lang.md) | The WWAN_SMS_CDMA_LANG enumeration lists the different SMS CDMA languages that are supported by the MB device. |
| [WWAN_SMS_FLAG enumeration](ne-wwan--wwan-sms-flag.md) | The WWAN_SMS_FLAG enumeration lists different flags to filter SMS text messages. |
| [WWAN_SMS_FORMAT enumeration](ne-wwan--wwan-sms-format.md) | The WWAN_SMS_FORMAT enumeration lists different Short Message Service (SMS) formats. |
| [WWAN_STRUCT_TYPE enumeration](ne-wwan--wwan-struct-type.md) | The WWAN_STRUCT_TYPE enumeration lists the different types of the list elements that follow the WWAN_LIST_HEADER object in memory. |
| [WWAN_UICCSLOT_STATE enumeration](ne-wwan--wwan-uiccslot-state.md) | The WWAN_UICCSLOT_STATE enumeration lists the different states of a UICC (SIM) card slot on a modem. The slot state represents a summary of both the slot state and the card state. |
| [WWAN_UICC_PASSTHROUGH_ACTION enumeration](ne-wwan--wwan-uicc-passthrough-action.md) | The WWAN_UICC_PASSTHROUGH_ACTION enumeration defines the passthrough action specified by the MB host for a modem miniport adapter after it resets a UICC smart card. |
| [WWAN_UICC_PASSTHROUGH_STATUS enumeration](ne-wwan--wwan-uicc-passthrough-status.md) | The WWAN_UICC_PASSTHROUGH_STATUS enumeration defines the passthrough status of a modem miniport adapter for a UICC smart card. |
| [WWAN_USSD_EVENT_TYPE enumeration](ne-wwan--wwan-ussd-event-type.md) | The WWAN_USSD_EVENT_TYPE enumeration lists the different types of Unstructured Supplementary Service Data (USSD) events. |
| [WWAN_USSD_REQUEST_TYPE enumeration](ne-wwan--wwan-ussd-request-type.md) | The WWAN_USSD_REQUEST_TYPE enumeration lists the different types of Unstructured Supplementary Service Data (USSD) session requests. |
| [WWAN_USSD_SESSION_STATE enumeration](ne-wwan--wwan-ussd-session-state.md) | The WWAN_USSD_SESSION_STATE enumeration lists the different types of USSD session states. |
| [WWAN_VOICE_CALL_STATE enumeration](ne-wwan--wwan-voice-call-state.md) | The WWAN_VOICE_CALL_STATE enumeration lists the different voice call states that are supported by the MB device. |
| [WWAN_VOICE_CLASS enumeration](ne-wwan--wwan-voice-class.md) | The WWAN_VOICE_CLASS enumeration lists the different types of voice classes that are supported by the MB device. |
