# Declarations in the nfccx header
This header Nfccx contains these programming interfaces:

Enum

| Title        | Description    |
| ------------- |:-------------:|
| [NFC_CX_NFCIP_TGT_MODE_CONFIG enumeration](ne-nfccx--nfc-cx-nfcip-tgt-mode-config.md) | The NFC_CX_NFCIP_TGT_MODE_CONFIG enumeration specifies NFC-IP target mode. |
| [NFC_CX_DEVICE_MODE enumeration](ne-nfccx--nfc-cx-device-mode.md) | Specifies device mode flags. |
| [NFC_CX_TRANSPORT_TYPE enumeration](ne-nfccx--nfc-cx-transport-type.md) | The NFC_CX_TRANSPORT_TYPE enumeration specifies transport types. |
| [NFC_CX_CE_MODE_CONFIG enumeration](ne-nfccx--nfc-cx-ce-mode-config.md) | This enumeration specifies CE listening mode flags. |
| [NFC_CX_DRIVER_FLAGS enumeration](ne-nfccx--nfc-cx-driver-flags.md) | Specifies run-time driver flags. |
| [NFC_CX_POLL_BAILOUT_CONFIG enumeration](ne-nfccx--nfc-cx-poll-bailout-config.md) | The NFC_CX_POLL_BAILOUT_CONFIG enumeration specifies poll mode bail out. |
| [NFC_CX_NFCIP_MODE_CONFIG enumeration](ne-nfccx--nfc-cx-nfcip-mode-config.md) | The NFC_CX_NFCIP_MODE_CONFIG enumeration specifies the NFC-IP initiator mode. |
| [NFC_CX_SEQUENCE enumeration](ne-nfccx--nfc-cx-sequence.md) | The NFC_CX_SEQUENCE enumeration specifies sequences. |
| [NFC_CX_HOST_ACTION enumeration](ne-nfccx--nfc-cx-host-action.md) | The NFC_CX_HOST_ACTION enumeration specifies host actions. |
| [NFC_CX_POLL_MODE_CONFIG enumeration](ne-nfccx--nfc-cx-poll-mode-config.md) | The NFC_CX_POLL_MODE_CONFIG enumeration specifies poll mode. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [*PFN_NFCCXDEVICEDEINITIALIZE callback function](nc-nfccx-pfn-nfccxdevicedeinitialize.md) | TBD |
| [PFN_NFC_CX callback function](nc-nfccx-pfn-nfc-cx.md) | TBD |
| [*PFN_NFCCXDEVICEINITCONFIG callback function](nc-nfccx-pfn-nfccxdeviceinitconfig.md) | TBD |
| [EVT_NFC_CX_SEQUENCE_HANDLER callback](nc-nfccx-evt-nfc-cx-sequence-handler.md) | Called by the NFC CX to notify the client driver to handle the specific registered sequence. |
| [*PFN_NFCCXSETRFDISCOVERYCONFIG callback function](nc-nfccx-pfn-nfccxsetrfdiscoveryconfig.md) | TBD |
| [EVT_NFC_CX_WRITE_NCI_PACKET callback](nc-nfccx-evt-nfc-cx-write-nci-packet.md) | Called by the NFC CX to send a write packet to the client driver. |
| [EVT_NFC_CX_DEVICE_IO_CONTROL callback](nc-nfccx-evt-nfc-cx-device-io-control.md) | Called by the NFC CX to send an unhandled IOCTL to the client driver. |
| [*PFN_NFCCXUNREGISTERSEQUENCEHANDLER callback function](nc-nfccx-pfn-nfccxunregistersequencehandler.md) | TBD |
| [*PFN_NFCCXREGISTERSEQUENCEHANDLER callback function](nc-nfccx-pfn-nfccxregistersequencehandler.md) | TBD |
| [*PFN_NFCCXHARDWAREEVENT callback function](nc-nfccx-pfn-nfccxhardwareevent.md) | TBD |
| [*PFN_NFCCXREACQUIREHARDWARECONTROL callback function](nc-nfccx-pfn-nfccxreacquirehardwarecontrol.md) | TBD |
| [*PFN_NFCCXRELEASEHARDWARECONTROL callback function](nc-nfccx-pfn-nfccxreleasehardwarecontrol.md) | TBD |
| [*PFN_NFCCXSETLLCPCONFIG callback function](nc-nfccx-pfn-nfccxsetllcpconfig.md) | TBD |
| [*PFN_NFCCXNCIREADNOTIFICATION callback function](nc-nfccx-pfn-nfccxncireadnotification.md) | TBD |
| [EVT_NFC_CX_SEQUENCE_COMPLETION_ROUTINE callback function](nc-nfccx-evt-nfc-cx-sequence-completion-routine.md) | TBD |
| [*PFN_NFCCXDEVICEINITIALIZE callback function](nc-nfccx-pfn-nfccxdeviceinitialize.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [NfcCxDeviceDeinitialize function](nf-nfccx-nfccxdevicedeinitialize.md) | Called by the client driver after a WDF device has been created during the AddDevice routine. |
| [NFC_CX_RF_DISCOVERY_CONFIG_INIT function](nf-nfccx-nfc-cx-rf-discovery-config-init.md) | The NFC_CX_RF_DISCOVERY_CONFIG_INIT function initializes the NFC_CX_RF_DISCOVERY_CONFIG structure. |
| [NfcCxSetRfDiscoveryConfig function](nf-nfccx-nfccxsetrfdiscoveryconfig.md) | Called by the client driver to configure the RF discovery parameters. |
| [NfcCxHardwareEvent function](nf-nfccx-nfccxhardwareevent.md) | Called by the client driver when a hardware event occurs like D0Entry and D0Exit callbacks to start or stop the device. For drivers that require firmware download on initialization or boot-up, it is recommended to move this call to a separate work item. However, the client driver is responsible for the following |
| [NfcCxNciReadNotification function](nf-nfccx-nfccxncireadnotification.md) | Called by the client driver when a read packet is available. |
| [NfcCxDeviceInitConfig function](nf-nfccx-nfccxdeviceinitconfig.md) | TBD |
| [NFC_CX_CLIENT_CONFIG_INIT function](nf-nfccx-nfc-cx-client-config-init.md) | The NFC_CX_CLIENT_CONFIG_INIT function initializes the NFC_CX_CLIENT_CONFIG structure. |
| [NFC_CX_LLCP_CONFIG_INIT function](nf-nfccx-nfc-cx-llcp-config-init.md) | The NFC_CX_LLCP_CONFIG_INIT function initializes the NFC_CX_LLCP_CONFIG structure. |
| [NfcCxDeviceInitialize function](nf-nfccx-nfccxdeviceinitialize.md) | Called by the client driver after a WDF device has been created during the AddDevice routine. |
| [NfcCxReacquireHardwareControl function](nf-nfccx-nfccxreacquirehardwarecontrol.md) | TBD |
| [NfcCxSetLlcpConfig function](nf-nfccx-nfccxsetllcpconfig.md) | Called by the client driver to configure the LLCP parameters. |
| [NfcCxReleaseHardwareControl function](nf-nfccx-nfccxreleasehardwarecontrol.md) | TBD |
| [NfcCxRegisterSequenceHandler function](nf-nfccx-nfccxregistersequencehandler.md) | Called by the client driver during initialization to register for handling specific sequences. |
| [NfcCxUnregisterSequenceHandler function](nf-nfccx-nfccxunregistersequencehandler.md) | Called by the client driver during device shutdown to unregister for the previously registered sequence handler callback. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [NFC_CX_HARDWARE_EVENT structure](ns-nfccx--nfc-cx-hardware-event.md) | The NFC_CX_HARDWARE_EVENT structure is an input parameter to NfcCxHardwareEvent. |
| [NFC_CX_CLIENT_CONFIG structure](ns-nfccx--nfc-cx-client-config.md) | The NFC_CX_CLIENT_CONFIG structure is an input parameter to NfcCxDeviceInitConfig. |
| [NFCCX_DRIVER_GLOBALS structure](ns-nfccx--nfccx-driver-globals.md) | . |
| [NFC_CX_RF_DISCOVERY_CONFIG structure](ns-nfccx--nfc-cx-rf-discovery-config.md) | The NFC_CX_RF_DISCOVERY_CONFIG structure contains RF discovery configuration settings. Discovery configuration should be completed during initialization after calling NfcDxDeviceInitialize, otherwise an error is returned. |
| [NFC_CX_LLCP_CONFIG structure](ns-nfccx--nfc-cx-llcp-config.md) | The NFC_CX_LLCP_CONFIG structure is an input parameter to NfcCxSetLlcpConfig. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_NFCCX_WRITE_PACKET IOCTL](ni-nfccx-ioctl-nfccx-write-packet.md) | TBD |

This header is used in these topics:

- [nfpdrivers](..content/_nfpdrivers)
