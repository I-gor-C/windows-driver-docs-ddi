# Ndiswwan.h header


This header is used by unknown technology.

Ndiswwan.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [NDIS_WWAN_AUTH_CHALLENGE structure](ns-ndiswwan--ndis-wwan-auth-challenge.md) | The NDIS_WWAN_AUTH_CHALLENGE structure represents an authentication challenge used by one of the authentication methods. |
| [NDIS_WWAN_AUTH_RESPONSE structure](ns-ndiswwan--ndis-wwan-auth-response.md) | The NDIS_WWAN_AUTH_RESPONSE structure represents a response from one of the authentication methods. |
| [NDIS_WWAN_BASE_STATIONS_INFO structure](ns-ndiswwan--ndis-wwan-base-stations-info.md) | The NDIS_WWAN_BASE_STATIONS_INFO structure contains information about both serving and neighboring base stations. |
| [NDIS_WWAN_BASE_STATIONS_INFO_REQ structure](ns-ndiswwan--ndis-wwan-base-stations-info-req.md) | The NDIS_WWAN_BASE_STATIONS_INFO_REQ structure is used in OID_WWAN_BASE_STATIONS_INFO query requests to configure aspects of cellular base station information to be used in response. |
| [NDIS_WWAN_CONTEXT_STATE structure](ns-ndiswwan--ndis-wwan-context-state.md) | The NDIS_WWAN_CONTEXT_STATE structure represents the Packet Data Protocol (PDP) context state of the MB device. |
| [NDIS_WWAN_DEVICE_CAPS structure](ns-ndiswwan--ndis-wwan-device-caps.md) | The NDIS_WWAN_DEVICE_CAPS structure represents the capabilities of the MB device. |
| [NDIS_WWAN_DEVICE_CAPS_EX structure](ns-ndiswwan--ndis-wwan-device-caps-ex.md) | The NDIS_WWAN_DEVICE_CAPS_EX structure represents the capabilities of the MB device. |
| [NDIS_WWAN_DEVICE_RESET_STATUS structure](ns-ndiswwan--ndis-wwan-device-reset-status.md) | The NDIS_WWAN_DEVICE_RESET_STATUS structure represents a modem device's reset status. It is sent to the MB host in the NDIS_STATUS_WWAN_DEVICE_RESET_STATUS notification in an asynchronous response to an OID_WWAN_DEVICE_RESET set request. |
| [NDIS_WWAN_DEVICE_SERVICE_COMMAND structure](ns-ndiswwan--ndis-wwan-device-service-command.md) | The NDIS_WWAN_DEVICE_SERVICE_COMMAND structure describes device service command data. |
| [NDIS_WWAN_DEVICE_SERVICE_EVENT structure](ns-ndiswwan--ndis-wwan-device-service-event.md) | The NDIS_WWAN_DEVICE_SERVICE_EVENT structure describes unsolicited device service data that were not initiated by commands from Windows. |
| [NDIS_WWAN_DEVICE_SERVICE_RESPONSE structure](ns-ndiswwan--ndis-wwan-device-service-response.md) | The NDIS_WWAN_DEVICE_SERVICE_RESPONSE structure represents device service data from the transaction completion of a device service command. |
| [NDIS_WWAN_DEVICE_SERVICE_SESSION_INFO structure](ns-ndiswwan--ndis-wwan-device-service-session-info.md) | The NDIS_WWAN_DEVICE_SERVICE_SESSION_INFO structure represents the status of a device service session. |
| [NDIS_WWAN_DEVICE_SERVICE_SESSION_READ structure](ns-ndiswwan--ndis-wwan-device-service-session-read.md) | The NDIS_WWAN_DEVICE_SERVICE_SESSION_READ structure represents device service session data that has been read by the miniport driver from the MB device. |
| [NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE structure](ns-ndiswwan--ndis-wwan-device-service-session-write.md) | The NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE structure represents device service session data to be sent from the host to the MB device. |
| [NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE structure](ns-ndiswwan--ndis-wwan-device-service-session-write-complete.md) | The NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE structure represents the status of a device service session write operation. |
| [NDIS_WWAN_DEVICE_SERVICE_SUBSCRIPTION structure](ns-ndiswwan--ndis-wwan-device-service-subscription.md) | The NDIS_WWAN_DEVICE_SERVICE_SUBSCRIPTION structures encapsulates the data for NDIS_STATUS_WWAN_ DEVICE_SERVICE_SUBSCRIPTION. |
| [NDIS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS structure](ns-ndiswwan--ndis-wwan-device-service-supported-commands.md) | The NDIS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS structure represents a list of commands supported by a device service. |
| [NDIS_WWAN_DEVICE_SET_SERVICE_SESSION structure](ns-ndiswwan--ndis-wwan-device-set-service-session.md) | The NDIS_WWAN_SET_DEVICE_SERVICE_SESSION structure represents a session state operation to be performed on a device service. |
| [NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO structure](ns-ndiswwan--ndis-wwan-device-slot-mapping-info.md) | The NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO structure represents the executor-to-slot mapping relationship of the MB device. |
| [NDIS_WWAN_DRIVER_CAPS structure](ns-ndiswwan--ndis-wwan-driver-caps.md) | The NDIS_WWAN_DRIVER_CAPS structure represents the capabilities of the miniport driver. |
| [NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS structure](ns-ndiswwan--ndis-wwan-enumerate-device-service-commands.md) | The NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS structure represents the commands supported by a device service. |
| [NDIS_WWAN_GET_SLOT_INFO structure](ns-ndiswwan--ndis-wwan-get-slot-info.md) | The NDIS_WWAN_GET_SLOT_INFO structure represents the status of a slot in the modem of the MB device. |
| [NDIS_WWAN_GET_VISIBLE_PROVIDERS structure](ns-ndiswwan--ndis-wwan-get-visible-providers.md) | The NDIS_WWAN_GET_VISIBLE_PROVIDERS structure is used to request the miniport driver get either all visible providers or only multi-carrier visible providers. |
| [NDIS_WWAN_HOME_PROVIDER structure](ns-ndiswwan--ndis-wwan-home-provider.md) | The NDIS_WWAN_HOME_PROVIDER structure represents details about the home network provider. |
| [NDIS_WWAN_HOME_PROVIDER2 structure](ns-ndiswwan--ndis-wwan-home-provider2.md) | The NDIS_WWAN_HOME_PROVIDER2 structure describes details of a home network provider. |
| [NDIS_WWAN_IP_ADDRESS_STATE structure](ns-ndiswwan--ndis-wwan-ip-address-state.md) | The NDIS_WWAN_IP_ADDRESS_STATE structure represents the IP address of a PDP context. |
| [NDIS_WWAN_MAC_INFO structure](ns-ndiswwan--ndis-wwan-mac-info.md) | The NDIS_WWAN_MAC_INFO structure represents NDIS port information for a PDP context. |
| [NDIS_WWAN_MAC_PARAMETERS structure](ns-ndiswwan--ndis-wwan-mac-parameters.md) | The NDIS_WWAN_MAC_PARAMETERS structure is used by OID_WWAN_CREATE_MAC when processing a request to create an NDIS port for a new PDP context. |
| [NDIS_WWAN_MODEM_CONFIG_INFO structure](ns-ndiswwan--ndis-wwan-modem-config-info.md) | The NDIS_WWAN_MODEM_CONFIG_INFO structure represents the modem's configuration information. |
| [NDIS_WWAN_NETWORK_IDLE_HINT structure](ns-ndiswwan--ndis-wwan-network-idle-hint.md) | The NDIS_WWAN_NETWORK_IDLE_HINT structure contains a hint for the network interface regarding whether data is expected to be active or idle on the interface. |
| [NDIS_WWAN_PACKET_SERVICE_STATE structure](ns-ndiswwan--ndis-wwan-packet-service-state.md) | The NDIS_WWAN_PACKET_SERVICE_STATE structure represents the packet service attachment state of the MB device. |
| [NDIS_WWAN_PCO_STATUS structure](ns-ndiswwan--ndis-wwan-pco-status.md) | The NDIS_WWAN_PCO_STATUS structure represents the Protocol Configuration Option (PCO) status of the modem. |
| [NDIS_WWAN_PIN_INFO structure](ns-ndiswwan--ndis-wwan-pin-info.md) | The NDIS_WWAN_PIN_INFO structure represents the type and PIN-entry state of Personal Identification Number (PIN) information required by the MB device. |
| [NDIS_WWAN_PIN_LIST structure](ns-ndiswwan--ndis-wwan-pin-list.md) | The NDIS_WWAN_PIN_LIST structure represents a list of descriptions of Personal Identification Numbers (PINs). |
| [NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS structure](ns-ndiswwan--ndis-wwan-preferred-multicarrier-providers.md) | The NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS structure represents a list of preferred multi-carrier providers and the number of providers in the list. |
| [NDIS_WWAN_PREFERRED_PROVIDERS structure](ns-ndiswwan--ndis-wwan-preferred-providers.md) | The NDIS_WWAN_PREFERRED_PROVIDERS structure represents a list of preferred providers including the number of providers in the list. |
| [NDIS_WWAN_PRESHUTDOWN_STATE structure](ns-ndiswwan--ndis-wwan-preshutdown-state.md) | The NDIS_WWAN_PRESHUTDOWN_STATE structure contains the pre-shutdown status. |
| [NDIS_WWAN_PROVISIONED_CONTEXTS structure](ns-ndiswwan--ndis-wwan-provisioned-contexts.md) | The NDIS_WWAN_PROVISIONED_CONTEXTS structure represents a list of provisioned contexts and the number of provisioned contexts in the list. |
| [NDIS_WWAN_RADIO_STATE structure](ns-ndiswwan--ndis-wwan-radio-state.md) | The NDIS_WWAN_RADIO_STATE structure represents the hardware-based and software-based radio power states of the MB device. |
| [NDIS_WWAN_READY_INFO structure](ns-ndiswwan--ndis-wwan-ready-info.md) | The NDIS_WWAN_READY_INFO structure represents the ready-state of the MB device and Subscriber Identity Module (SIM card). |
| [NDIS_WWAN_REGISTRATION_STATE structure](ns-ndiswwan--ndis-wwan-registration-state.md) | The NDIS_WWAN_REGISTRATION_STATE structure represents the registration state of the MB device. |
| [NDIS_WWAN_SERVICE_ACTIVATION structure](ns-ndiswwan--ndis-wwan-service-activation.md) | The NDIS_WWAN_SERVICE_ACTIVATION structure represents the command that is used to set the service activation state of the MB device in order to obtain access to the provider's network. |
| [NDIS_WWAN_SERVICE_ACTIVATION_STATUS structure](ns-ndiswwan--ndis-wwan-service-activation-status.md) | The NDIS_WWAN_SERVICE_ACTIVATION_STATUS structure represents the status of service activation on the MB device. |
| [NDIS_WWAN_SET_CONTEXT_STATE structure](ns-ndiswwan--ndis-wwan-set-context-state.md) | The NDIS_WWAN_SET_CONTEXT_STATE structure represents the command to set the context state of the MB device. |
| [NDIS_WWAN_SET_DEVICE_RESET structure](ns-ndiswwan--ndis-wwan-set-device-reset.md) | The NDIS_WWAN_SET_DEVICE_RESET structure represents a command to reset a modem device. It is sent as part of an OID_WWAN_DEVICE_RESET set request. |
| [NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO structure](ns-ndiswwan--ndis-wwan-set-device-slot-mapping-info.md) | The NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO structure sets the executor-to-slot mapping relationship of the MB device. |
| [NDIS_WWAN_SET_HOME_PROVIDER structure](ns-ndiswwan--ndis-wwan-set-home-provider.md) | The NDIS_WWAN_SET_HOME_PROVIDER structure describes a home provider. |
| [NDIS_WWAN_SET_PACKET_SERVICE structure](ns-ndiswwan--ndis-wwan-set-packet-service.md) | The NDIS_WWAN_SET_PACKET_SERVICE structure represents the packet service state of the MB device. |
| [NDIS_WWAN_SET_PIN structure](ns-ndiswwan--ndis-wwan-set-pin.md) | The NDIS_WWAN_SET_PIN structure represents what PIN action to take on the MB device. |
| [NDIS_WWAN_SET_PIN_EX structure](ns-ndiswwan--ndis-wwan-set-pin-ex.md) | The NDIS_WWAN_SET_PIN_EX structure represents what PIN action to take on the MB device. |
| [NDIS_WWAN_SET_PREFERRED_MULTICARRIER_PROVIDERS structure](ns-ndiswwan--ndis-wwan-set-preferred-multicarrier-providers.md) | The NDIS_WWAN_SET_PREFERRED_MULTICARRIER_PROVIDERS structure represents a list of preferred multicarrier providers associated with the MB device. |
| [NDIS_WWAN_SET_PREFERRED_PROVIDERS structure](ns-ndiswwan--ndis-wwan-set-preferred-providers.md) | The NDIS_WWAN_SET_PREFERRED_PROVIDERS structure represents the list of preferred providers associated with the MB device. |
| [NDIS_WWAN_SET_PRESHUTDOWN_STATE structure](ns-ndiswwan--ndis-wwan-set-preshutdown-state.md) | The NDIS_WWAN_SET_PRESHUTDOWN_STATE structure represents the command to notify the modem to finish all operations and prepare to shut down. |
| [NDIS_WWAN_SET_PROVISIONED_CONTEXT structure](ns-ndiswwan--ndis-wwan-set-provisioned-context.md) | The NDIS_WWAN_SET_PROVISIONED_CONTEXT structure represents the command to set the provisioned context state of the MB device. |
| [NDIS_WWAN_SET_RADIO_STATE structure](ns-ndiswwan--ndis-wwan-set-radio-state.md) | The NDIS_WWAN_SET_RADIO_STATE structure represents the power action to take on the MB device's radio. |
| [NDIS_WWAN_SET_REGISTER_STATE structure](ns-ndiswwan--ndis-wwan-set-register-state.md) | The NDIS_WWAN_SET_REGISTER_STATE structure represents the network provider registration state of the MB device. |
| [NDIS_WWAN_SET_SIGNAL_INDICATION structure](ns-ndiswwan--ndis-wwan-set-signal-indication.md) | The NDIS_WWAN_SET_SIGNAL_INDICATION structure represents the signal indication of the MB device. |
| [NDIS_WWAN_SET_SMS_CONFIGURATION structure](ns-ndiswwan--ndis-wwan-set-sms-configuration.md) | The NDIS_WWAN_SET_SMS_CONFIGURATION structure represents the SMS configuration of the MB device. |
| [NDIS_WWAN_SET_UICC_RESET structure](ns-ndiswwan--ndis-wwan-set-uicc-reset.md) | The NDIS_WWAN_SET_UICC_RESET structure represents the passthrough action the MB host specifies for a modem miniport adapter after it resets a UICC card. |
| [NDIS_WWAN_SIGNAL_STATE structure](ns-ndiswwan--ndis-wwan-signal-state.md) | The NDIS_WWAN_SIGNAL_STATE structure represents the signal state of the MB device. |
| [NDIS_WWAN_SLOT_INFO structure](ns-ndiswwan--ndis-wwan-slot-info.md) | The NDIS_WWAN_SLOT_INFO structure represents the information about a slot in the modem of the MB device. |
| [NDIS_WWAN_SMS_CONFIGURATION structure](ns-ndiswwan--ndis-wwan-sms-configuration.md) | The NDIS_WWAN_SMS_CONFIGURATION structure represents the SMS configuration of the MB device. |
| [NDIS_WWAN_SMS_DELETE structure](ns-ndiswwan--ndis-wwan-sms-delete.md) | The NDIS_WWAN_SMS_DELETE structure represents an SMS message to delete. |
| [NDIS_WWAN_SMS_DELETE_STATUS structure](ns-ndiswwan--ndis-wwan-sms-delete-status.md) | The NDIS_WWAN_SMS_DELETE_STATUS structure represents the status of a deleted SMS text message. |
| [NDIS_WWAN_SMS_READ structure](ns-ndiswwan--ndis-wwan-sms-read.md) | The NDIS_WWAN_SMS_READ structure represents an SMS message to read. |
| [NDIS_WWAN_SMS_RECEIVE structure](ns-ndiswwan--ndis-wwan-sms-receive.md) | The NDIS_WWAN_SMS_RECEIVE structure represents a list of received SMS messages and the number of messages in the list. |
| [NDIS_WWAN_SMS_SEND structure](ns-ndiswwan--ndis-wwan-sms-send.md) | The NDIS_WWAN_SMS_SEND structure represents an SMS message to send. |
| [NDIS_WWAN_SMS_SEND_STATUS structure](ns-ndiswwan--ndis-wwan-sms-send-status.md) | The NDIS_WWAN_SMS_SEND_STATUS structure represents the status of a sent SMS text message. |
| [NDIS_WWAN_SMS_STATUS structure](ns-ndiswwan--ndis-wwan-sms-status.md) | The NDIS_WWAN_SMS_STATUS structure represents the status of the SMS message store. |
| [NDIS_WWAN_SUBSCRIBE_DEVICE_SERVICE_EVENTS structure](ns-ndiswwan--ndis-wwan-subscribe-device-service-events.md) | The NDIS_WWAN_SUBSCRIBE_DEVICE_SERVICE_EVENTS structure encapsulates data for OID_WWAN_SUBSCRIBE_DEVICE_SERVICES_EVENTS. |
| [NDIS_WWAN_SUPPORTED_DEVICE_SERVICES structure](ns-ndiswwan--ndis-wwan-supported-device-services.md) | The NDIS_WWAN_SUPPORTED_DEVICE_SERVICES structure describes a list of supported device services. |
| [NDIS_WWAN_SYS_CAPS_INFO structure](ns-ndiswwan--ndis-wwan-sys-caps-info.md) | The NDIS_WWAN_SYS_CAPS_INFO structure represents the overall modem's system capability. |
| [NDIS_WWAN_UICC_RESET_INFO structure](ns-ndiswwan--ndis-wwan-uicc-reset-info.md) | The NDIS_WWAN_UICC_RESET_INFO structure represents the passthrough status of a modem miniport adapter for a UICC smart card. |
| [NDIS_WWAN_USSD_EVENT structure](ns-ndiswwan--ndis-wwan-ussd-event.md) | The NDIS_WWAN_USSD_EVENT structure represents an Unstructured Supplementary Service Data (USSD) NDIS event. |
| [NDIS_WWAN_USSD_REQUEST structure](ns-ndiswwan--ndis-wwan-ussd-request.md) | The NDIS_WWAN_USSD_EVENT structure represents an Unstructured Supplementary Service Data (USSD) NDIS request. |
| [NDIS_WWAN_VENDOR_SPECIFIC structure](ns-ndiswwan--ndis-wwan-vendor-specific.md) | The NDIS_WWAN_VENDOR_SPECIFIC structure represents vendor-specific data. |
| [NDIS_WWAN_VISIBLE_PROVIDERS structure](ns-ndiswwan--ndis-wwan-visible-providers.md) | The NDIS_WWAN_VISIBLE_PROVIDERS structure represents a list of visible providers and the number of providers in the list. |
