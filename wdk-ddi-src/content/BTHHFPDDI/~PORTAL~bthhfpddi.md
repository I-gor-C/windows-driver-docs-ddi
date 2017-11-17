# Declarations in the bthhfpddi header
This header Bthhfpddi contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [BTHHFP_IOCTL function](nf-bthhfpddi-bthhfp-ioctl.md) | TBD |
| [BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT function](nf-bthhfpddi-bthhfp-audio-device-capabilties-init.md) | The BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT method returns a pointer to an initialized BTHHFP_AUDIO_DEVICE_CAPABILTIES data structure. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BTHHFP_DESCRIPTOR2 structure](ns-bthhfpddi--bthhfp-descriptor2.md) | The BTHHFP_DESCRIPTOR2 data structure stores information describing a paired Handsfree profile (HFP) device. |
| [HFP_BYPASS_CODEC_ID_V1 structure](ns-bthhfpddi--hfp-bypass-codec-id-v1.md) | The HFP_BYPASS_CODEC_ID_V1 structure defines version 1 of the supported codec ID structure. |
| [BTHHFP_AUDIO_DEVICE_CAPABILTIES structure](ns-bthhfpddi--bthhfp-audio-device-capabilties.md) | The BTHHFP_AUDIO_DEVICE_CAPABILTIES data structure describes the capabilities of a Bluetooth HFP device, including the version and whether it supports 16 kHz sampling. |
| [BTHHFP_DESCRIPTOR structure](ns-bthhfpddi--bthhfp-descriptor.md) | The BTHHFP_DESCRIPTOR data structure stores information describing a paired Handsfree profile (HFP) device. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [HFP_BYPASS_CODEC_ID_VERSION enumeration](ne-bthhfpddi--hfp-bypass-codec-id-version.md) | The HFP_BYPASS_CODEC_ID_VERSION enumeration defines the codec ID structure versions that are supported by the HFP service. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE IOCTL](ni-bthhfpddi-ioctl-bthhfp-speaker-get-volume-status-update.md) | The IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE IOCTL Gets the volume level setting of the Bluetooth device's speaker. |
| [IOCTL_BTHHFP_SPEAKER_SET_VOLUME IOCTL](ni-bthhfpddi-ioctl-bthhfp-speaker-set-volume.md) | The IOCTL_BTHHFP_SPEAKER_SET_VOLUME IOCTL sets the volume level for the speaker of the Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_GET_CODEC_ID IOCTL](ni-bthhfpddi-ioctl-bthhfp-device-get-codec-id.md) | An audio driver can send an IOCTL_BTHHFP_DEVICE_GET_CODEC_ID control code to query the Bluetooth driver stack about the codec ID used by the HFP service. This helps the audio driver determine the sampling rate for the data. |
| [IOCTL_BTHHFP_DEVICE_REQUEST_CONNECT IOCTL](ni-bthhfpddi-ioctl-bthhfp-device-request-connect.md) | The IOCTL_BTHHFP_DEVICE_REQUEST_CONNECT IOCTL requests a Handsfree Profile (HFP) Service Level Connection to the Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_GET_CONTAINERID IOCTL](ni-bthhfpddi-ioctl-bthhfp-device-get-containerid.md) | The IOCTL_BTHHFP_DEVICE_GET_CONTAINERID IOCTL Gets the PnP Container ID of the Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_REQUEST_DISCONNECT IOCTL](ni-bthhfpddi-ioctl-bthhfp-device-request-disconnect.md) | The IOCTL_BTHHFP_DEVICE_REQUEST_DISCONNECT IOCTL removes the Handfree Profile (HFP) Service Level Connection that existed between the audio driver and the Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_INDICATE_AUDIO_DEVICE_CAPABILITIES IOCTL](ni-bthhfpddi-ioctl-bthhfp-device-indicate-audio-device-capabilities.md) | TBD |
| [IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2 IOCTL](ni-bthhfpddi-ioctl-bthhfp-device-get-descriptor2.md) | The IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2 IOCTL Gets descriptive information about the paired Handsfree profile (HFP) device. |
| [IOCTL_BTHHFP_STREAM_CLOSE IOCTL](ni-bthhfpddi-ioctl-bthhfp-stream-close.md) | The IOCTL_BTHHFP_STREAM_CLOSE IOCTL indicates that the client driver no longer requires the synchronous connection-oriented (SCO) channel for streaming audio. |
| [IOCTL_BTHHFP_DEVICE_GET_VOLUMEPROPERTYVALUES IOCTL](ni-bthhfpddi-ioctl-bthhfp-device-get-volumepropertyvalues.md) | The IOCTL_BTHHFP_DEVICE_GET_VOLUMEPROPERTYVALUES IOCTL returns KSPROPERTY_VALUES data for the KSPROPERTY_AUDIO_VOLUMELEVEL property. |
| [IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR IOCTL](ni-bthhfpddi-ioctl-bthhfp-device-get-descriptor.md) | The audio driver issues the IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR control code to get information about an enabled GUID_DEVINTERFACE_BLUETOOTH_HFP_SCO_HCIBYPASS device interface. |
| [IOCTL_BTHHFP_STREAM_GET_STATUS_UPDATE IOCTL](ni-bthhfpddi-ioctl-bthhfp-stream-get-status-update.md) | The IOCTL_BTHHFP_STREAM_GET_STATUS_UPDATE IOCTL Gets a stream channel status update. |
| [IOCTL_BTHHFP_STREAM_OPEN IOCTL](ni-bthhfpddi-ioctl-bthhfp-stream-open.md) | The IOCTL_BTHHFP_STREAM_OPEN IOCTL requests an open synchronous connection-oriented (SCO) channel to transmit audio data over the air. |
| [IOCTL_BTHHFP_MIC_SET_VOLUME IOCTL](ni-bthhfpddi-ioctl-bthhfp-mic-set-volume.md) | The IOCTL_BTHHFP_MIC_SET_VOLUME IOCTL sets the volume level of the microphone for the Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_GET_NRECDISABLE_STATUS_UPDATE IOCTL](ni-bthhfpddi-ioctl-bthhfp-device-get-nrecdisable-status-update.md) | The IOCTL_BTHHFP_DEVICE_GET_NRECDISABLE_STATUS_UPDATE IOCTL Gets noise reduction / echo cancellation (NREC) Disable status updates from the remote Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_GET_CONNECTION_STATUS_UPDATE IOCTL](ni-bthhfpddi-ioctl-bthhfp-device-get-connection-status-update.md) | The IOCTL_BTHHFP_DEVICE_GET_CONNECTION_STATUS_UPDATE IOCTL Gets a connection status update. |
| [IOCTL_BTHHFP_MIC_GET_VOLUME_STATUS_UPDATE IOCTL](ni-bthhfpddi-ioctl-bthhfp-mic-get-volume-status-update.md) | The IOCTL_BTHHFP_MIC_GET_VOLUME_STATUS_UPDATE IOCTL Gets the volume level setting of the Bluetooth device's microphone. |
| [IOCTL_BTHHFP_DEVICE_GET_KSNODETYPES IOCTL](ni-bthhfpddi-ioctl-bthhfp-device-get-ksnodetypes.md) | The IOCTL_BTHHFP_DEVICE_GET_KSNODETYPES IOCTL Gets the KSNODE types that best describe the Bluetooth device’s input and output. |
| [IOCTL_BTHHFP_GET_DEVICEOBJECT IOCTL](ni-bthhfpddi-ioctl-bthhfp-get-deviceobject.md) | TBD |

This header is used in these topics:

- [audio](..content/_audio)
