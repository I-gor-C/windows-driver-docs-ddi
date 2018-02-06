---
UID: NA:bthhfpddi
ms.assetid: 3204c1dc-a7d6-343c-8591-e2175352866a
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# bthhfpddi.h header



bthhfpddi.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_BTHHFP_DEVICE_GET_CODEC_ID](ni-bthhfpddi-ioctl_bthhfp_device_get_codec_id.md) | An audio driver can send an IOCTL_BTHHFP_DEVICE_GET_CODEC_ID control code to query the Bluetooth driver stack about the codec ID used by the HFP service. This helps the audio driver determine the sampling rate for the data. |
| [IOCTL_BTHHFP_DEVICE_GET_CONNECTION_STATUS_UPDATE](ni-bthhfpddi-ioctl_bthhfp_device_get_connection_status_update.md) | The IOCTL_BTHHFP_DEVICE_GET_CONNECTION_STATUS_UPDATE IOCTL Gets a connection status update. |
| [IOCTL_BTHHFP_DEVICE_GET_CONTAINERID](ni-bthhfpddi-ioctl_bthhfp_device_get_containerid.md) | The IOCTL_BTHHFP_DEVICE_GET_CONTAINERID IOCTL Gets the PnP Container ID of the Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR](ni-bthhfpddi-ioctl_bthhfp_device_get_descriptor.md) | The audio driver issues the IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR control code to get information about an enabled GUID_DEVINTERFACE_BLUETOOTH_HFP_SCO_HCIBYPASS device interface. |
| [IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2](ni-bthhfpddi-ioctl_bthhfp_device_get_descriptor2.md) | The IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2 IOCTL Gets descriptive information about the paired Handsfree profile (HFP) device. |
| [IOCTL_BTHHFP_DEVICE_GET_KSNODETYPES](ni-bthhfpddi-ioctl_bthhfp_device_get_ksnodetypes.md) | The IOCTL_BTHHFP_DEVICE_GET_KSNODETYPES IOCTL Gets the KSNODE types that best describe the Bluetooth device’s input and output. |
| [IOCTL_BTHHFP_DEVICE_GET_NRECDISABLE_STATUS_UPDATE](ni-bthhfpddi-ioctl_bthhfp_device_get_nrecdisable_status_update.md) | The IOCTL_BTHHFP_DEVICE_GET_NRECDISABLE_STATUS_UPDATE IOCTL Gets noise reduction / echo cancellation (NREC) Disable status updates from the remote Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_GET_VOLUMEPROPERTYVALUES](ni-bthhfpddi-ioctl_bthhfp_device_get_volumepropertyvalues.md) | The IOCTL_BTHHFP_DEVICE_GET_VOLUMEPROPERTYVALUES IOCTL returns KSPROPERTY_VALUES data for the KSPROPERTY_AUDIO_VOLUMELEVEL property. |
| [IOCTL_BTHHFP_DEVICE_REQUEST_CONNECT](ni-bthhfpddi-ioctl_bthhfp_device_request_connect.md) | The IOCTL_BTHHFP_DEVICE_REQUEST_CONNECT IOCTL requests a Handsfree Profile (HFP) Service Level Connection to the Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_REQUEST_DISCONNECT](ni-bthhfpddi-ioctl_bthhfp_device_request_disconnect.md) | The IOCTL_BTHHFP_DEVICE_REQUEST_DISCONNECT IOCTL removes the Handfree Profile (HFP) Service Level Connection that existed between the audio driver and the Bluetooth device. |
| [IOCTL_BTHHFP_MIC_GET_VOLUME_STATUS_UPDATE](ni-bthhfpddi-ioctl_bthhfp_mic_get_volume_status_update.md) | The IOCTL_BTHHFP_MIC_GET_VOLUME_STATUS_UPDATE IOCTL Gets the volume level setting of the Bluetooth device's microphone. |
| [IOCTL_BTHHFP_MIC_SET_VOLUME](ni-bthhfpddi-ioctl_bthhfp_mic_set_volume.md) | The IOCTL_BTHHFP_MIC_SET_VOLUME IOCTL sets the volume level of the microphone for the Bluetooth device. |
| [IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE](ni-bthhfpddi-ioctl_bthhfp_speaker_get_volume_status_update.md) | The IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE IOCTL Gets the volume level setting of the Bluetooth device's speaker. |
| [IOCTL_BTHHFP_SPEAKER_SET_VOLUME](ni-bthhfpddi-ioctl_bthhfp_speaker_set_volume.md) | The IOCTL_BTHHFP_SPEAKER_SET_VOLUME IOCTL sets the volume level for the speaker of the Bluetooth device. |
| [IOCTL_BTHHFP_STREAM_CLOSE](ni-bthhfpddi-ioctl_bthhfp_stream_close.md) | The IOCTL_BTHHFP_STREAM_CLOSE IOCTL indicates that the client driver no longer requires the synchronous connection-oriented (SCO) channel for streaming audio. |
| [IOCTL_BTHHFP_STREAM_GET_STATUS_UPDATE](ni-bthhfpddi-ioctl_bthhfp_stream_get_status_update.md) | The IOCTL_BTHHFP_STREAM_GET_STATUS_UPDATE IOCTL Gets a stream channel status update. |
| [IOCTL_BTHHFP_STREAM_OPEN](ni-bthhfpddi-ioctl_bthhfp_stream_open.md) | The IOCTL_BTHHFP_STREAM_OPEN IOCTL requests an open synchronous connection-oriented (SCO) channel to transmit audio data over the air. |


## Functions
| Title | Description |
| ---- |:---- |
| [BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT](nf-bthhfpddi-bthhfp_audio_device_capabilties_init.md) | The BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT method returns a pointer to an initialized BTHHFP_AUDIO_DEVICE_CAPABILTIES data structure. |



## Structures
| Title | Description |
| ---- |:---- |
| [_BTHHFP_AUDIO_DEVICE_CAPABILTIES](ns-bthhfpddi-_bthhfp_audio_device_capabilties.md) | The BTHHFP_AUDIO_DEVICE_CAPABILTIES data structure describes the capabilities of a Bluetooth HFP device, including the version and whether it supports 16 kHz sampling. |
| [_BTHHFP_DESCRIPTOR](ns-bthhfpddi-_bthhfp_descriptor.md) | The BTHHFP_DESCRIPTOR data structure stores information describing a paired Handsfree profile (HFP) device. |
| [_BTHHFP_DESCRIPTOR2](ns-bthhfpddi-_bthhfp_descriptor2.md) | The BTHHFP_DESCRIPTOR2 data structure stores information describing a paired Handsfree profile (HFP) device. |
| [_HFP_BYPASS_CODEC_ID_V1](ns-bthhfpddi-_hfp_bypass_codec_id_v1.md) | The HFP_BYPASS_CODEC_ID_V1 structure defines version 1 of the supported codec ID structure. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_HFP_BYPASS_CODEC_ID_VERSION](ne-bthhfpddi-_hfp_bypass_codec_id_version.md) | The HFP_BYPASS_CODEC_ID_VERSION enumeration defines the codec ID structure versions that are supported by the HFP service. |