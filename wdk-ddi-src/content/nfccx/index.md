# Nfccx.h header


This header is used by Near field communications (NFC). For more information, see
- [Near field communications (NFC)](../_nfpdrivers/index.md)

Nfccx.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [NFC_CX_CLIENT_CONFIG_INIT function](nf-nfccx-nfc-cx-client-config-init.md) | The NFC_CX_CLIENT_CONFIG_INIT function initializes the NFC_CX_CLIENT_CONFIG structure. |
| [NFC_CX_LLCP_CONFIG_INIT function](nf-nfccx-nfc-cx-llcp-config-init.md) | The NFC_CX_LLCP_CONFIG_INIT function initializes the NFC_CX_LLCP_CONFIG structure. |
| [NFC_CX_RF_DISCOVERY_CONFIG_INIT function](nf-nfccx-nfc-cx-rf-discovery-config-init.md) | The NFC_CX_RF_DISCOVERY_CONFIG_INIT function initializes the NFC_CX_RF_DISCOVERY_CONFIG structure. |
| [NfcCxDeviceDeinitialize function](nf-nfccx-nfccxdevicedeinitialize.md) | Called by the client driver after a WDF device has been created during the AddDevice routine. |
| [NfcCxDeviceInitConfig function](nf-nfccx-nfccxdeviceinitconfig.md) | Called by the client driver during its AddDevice routine to perform DeviceInit functions. During this process the following I/O callback functions are also exchanged |
| [NfcCxDeviceInitialize function](nf-nfccx-nfccxdeviceinitialize.md) | Called by the client driver after a WDF device has been created during the AddDevice routine. |
| [NfcCxHardwareEvent function](nf-nfccx-nfccxhardwareevent.md) | Called by the client driver when a hardware event occurs like D0Entry and D0Exit callbacks to start or stop the device. For drivers that require firmware download on initialization or boot-up, it is recommended to move this call to a separate work item. However, the client driver is responsible for the following |
| [NfcCxNciReadNotification function](nf-nfccx-nfccxncireadnotification.md) | Called by the client driver when a read packet is available. |
| [NfcCxRegisterSequenceHandler function](nf-nfccx-nfccxregistersequencehandler.md) | Called by the client driver during initialization to register for handling specific sequences. |
| [NfcCxSetLlcpConfig function](nf-nfccx-nfccxsetllcpconfig.md) | Called by the client driver to configure the LLCP parameters. |
| [NfcCxSetRfDiscoveryConfig function](nf-nfccx-nfccxsetrfdiscoveryconfig.md) | Called by the client driver to configure the RF discovery parameters. |
| [NfcCxUnregisterSequenceHandler function](nf-nfccx-nfccxunregistersequencehandler.md) | Called by the client driver during device shutdown to unregister for the previously registered sequence handler callback. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_NFC_CX_DEVICE_IO_CONTROL callback](nc-nfccx-evt-nfc-cx-device-io-control.md) | Called by the NFC CX to send an unhandled IOCTL to the client driver. |
| [EVT_NFC_CX_SEQUENCE_HANDLER callback](nc-nfccx-evt-nfc-cx-sequence-handler.md) | Called by the NFC CX to notify the client driver to handle the specific registered sequence. |
| [EVT_NFC_CX_WRITE_NCI_PACKET callback](nc-nfccx-evt-nfc-cx-write-nci-packet.md) | Called by the NFC CX to send a write packet to the client driver. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [NFCCX_DRIVER_GLOBALS structure](ns-nfccx--nfccx-driver-globals.md) | . |
| [NFC_CX_CLIENT_CONFIG structure](ns-nfccx--nfc-cx-client-config.md) | The NFC_CX_CLIENT_CONFIG structure is an input parameter to NfcCxDeviceInitConfig. |
| [NFC_CX_HARDWARE_EVENT structure](ns-nfccx--nfc-cx-hardware-event.md) | The NFC_CX_HARDWARE_EVENT structure is an input parameter to NfcCxHardwareEvent. |
| [NFC_CX_LLCP_CONFIG structure](ns-nfccx--nfc-cx-llcp-config.md) | The NFC_CX_LLCP_CONFIG structure is an input parameter to NfcCxSetLlcpConfig. |
| [NFC_CX_RF_DISCOVERY_CONFIG structure](ns-nfccx--nfc-cx-rf-discovery-config.md) | The NFC_CX_RF_DISCOVERY_CONFIG structure contains RF discovery configuration settings. Discovery configuration should be completed during initialization after calling NfcDxDeviceInitialize, otherwise an error is returned. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [NFC_CX_CE_MODE_CONFIG enumeration](ne-nfccx--nfc-cx-ce-mode-config.md) | This enumeration specifies CE listening mode flags. |
| [NFC_CX_DEVICE_MODE enumeration](ne-nfccx--nfc-cx-device-mode.md) | Specifies device mode flags. |
| [NFC_CX_DRIVER_FLAGS enumeration](ne-nfccx--nfc-cx-driver-flags.md) | Specifies run-time driver flags. |
| [NFC_CX_HOST_ACTION enumeration](ne-nfccx--nfc-cx-host-action.md) | The NFC_CX_HOST_ACTION enumeration specifies host actions. |
| [NFC_CX_NFCIP_MODE_CONFIG enumeration](ne-nfccx--nfc-cx-nfcip-mode-config.md) | The NFC_CX_NFCIP_MODE_CONFIG enumeration specifies the NFC-IP initiator mode. |
| [NFC_CX_NFCIP_TGT_MODE_CONFIG enumeration](ne-nfccx--nfc-cx-nfcip-tgt-mode-config.md) | The NFC_CX_NFCIP_TGT_MODE_CONFIG enumeration specifies NFC-IP target mode. |
| [NFC_CX_POLL_BAILOUT_CONFIG enumeration](ne-nfccx--nfc-cx-poll-bailout-config.md) | The NFC_CX_POLL_BAILOUT_CONFIG enumeration specifies poll mode bail out. |
| [NFC_CX_POLL_MODE_CONFIG enumeration](ne-nfccx--nfc-cx-poll-mode-config.md) | The NFC_CX_POLL_MODE_CONFIG enumeration specifies poll mode. |
| [NFC_CX_SEQUENCE enumeration](ne-nfccx--nfc-cx-sequence.md) | The NFC_CX_SEQUENCE enumeration specifies sequences. |
| [NFC_CX_TRANSPORT_TYPE enumeration](ne-nfccx--nfc-cx-transport-type.md) | The NFC_CX_TRANSPORT_TYPE enumeration specifies transport types. |
