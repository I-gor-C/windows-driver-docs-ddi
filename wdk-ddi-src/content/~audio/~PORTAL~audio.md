# Declarations in the audio technology
This technology  contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BTHHFP_DESCRIPTOR2 structure](..\bthhfpddi\ns-bthhfpddi--bthhfp-descriptor2.md) | The BTHHFP_DESCRIPTOR2 data structure stores information describing a paired Handsfree profile (HFP) device. |
| [HFP_BYPASS_CODEC_ID_V1 structure](..\bthhfpddi\ns-bthhfpddi--hfp-bypass-codec-id-v1.md) | The HFP_BYPASS_CODEC_ID_V1 structure defines version 1 of the supported codec ID structure. |
| [BTHHFP_AUDIO_DEVICE_CAPABILTIES structure](..\bthhfpddi\ns-bthhfpddi--bthhfp-audio-device-capabilties.md) | The BTHHFP_AUDIO_DEVICE_CAPABILTIES data structure describes the capabilities of a Bluetooth HFP device, including the version and whether it supports 16 kHz sampling. |
| [BTHHFP_DESCRIPTOR structure](..\bthhfpddi\ns-bthhfpddi--bthhfp-descriptor.md) | The BTHHFP_DESCRIPTOR data structure stores information describing a paired Handsfree profile (HFP) device. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [HFP_BYPASS_CODEC_ID_VERSION enumeration](..\bthhfpddi\ne-bthhfpddi--hfp-bypass-codec-id-version.md) | The HFP_BYPASS_CODEC_ID_VERSION enumeration defines the codec ID structure versions that are supported by the HFP service. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-speaker-get-volume-status-update.md) | The IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE IOCTL Gets the volume level setting of the Bluetooth device's speaker. |
| [IOCTL_BTHHFP_SPEAKER_SET_VOLUME IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-speaker-set-volume.md) | The IOCTL_BTHHFP_SPEAKER_SET_VOLUME IOCTL sets the volume level for the speaker of the Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_GET_CODEC_ID IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-device-get-codec-id.md) | An audio driver can send an IOCTL_BTHHFP_DEVICE_GET_CODEC_ID control code to query the Bluetooth driver stack about the codec ID used by the HFP service. This helps the audio driver determine the sampling rate for the data. |
| [IOCTL_BTHHFP_DEVICE_REQUEST_CONNECT IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-device-request-connect.md) | The IOCTL_BTHHFP_DEVICE_REQUEST_CONNECT IOCTL requests a Handsfree Profile (HFP) Service Level Connection to the Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_GET_CONTAINERID IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-device-get-containerid.md) | The IOCTL_BTHHFP_DEVICE_GET_CONTAINERID IOCTL Gets the PnP Container ID of the Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_REQUEST_DISCONNECT IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-device-request-disconnect.md) | The IOCTL_BTHHFP_DEVICE_REQUEST_DISCONNECT IOCTL removes the Handfree Profile (HFP) Service Level Connection that existed between the audio driver and the Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2 IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-device-get-descriptor2.md) | The IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2 IOCTL Gets descriptive information about the paired Handsfree profile (HFP) device. |
| [IOCTL_BTHHFP_STREAM_CLOSE IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-stream-close.md) | The IOCTL_BTHHFP_STREAM_CLOSE IOCTL indicates that the client driver no longer requires the synchronous connection-oriented (SCO) channel for streaming audio. |
| [IOCTL_BTHHFP_DEVICE_GET_VOLUMEPROPERTYVALUES IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-device-get-volumepropertyvalues.md) | The IOCTL_BTHHFP_DEVICE_GET_VOLUMEPROPERTYVALUES IOCTL returns KSPROPERTY_VALUES data for the KSPROPERTY_AUDIO_VOLUMELEVEL property. |
| [IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-device-get-descriptor.md) | The audio driver issues the IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR control code to get information about an enabled GUID_DEVINTERFACE_BLUETOOTH_HFP_SCO_HCIBYPASS device interface. |
| [IOCTL_BTHHFP_STREAM_GET_STATUS_UPDATE IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-stream-get-status-update.md) | The IOCTL_BTHHFP_STREAM_GET_STATUS_UPDATE IOCTL Gets a stream channel status update. |
| [IOCTL_BTHHFP_STREAM_OPEN IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-stream-open.md) | The IOCTL_BTHHFP_STREAM_OPEN IOCTL requests an open synchronous connection-oriented (SCO) channel to transmit audio data over the air. |
| [IOCTL_BTHHFP_MIC_SET_VOLUME IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-mic-set-volume.md) | The IOCTL_BTHHFP_MIC_SET_VOLUME IOCTL sets the volume level of the microphone for the Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_GET_NRECDISABLE_STATUS_UPDATE IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-device-get-nrecdisable-status-update.md) | The IOCTL_BTHHFP_DEVICE_GET_NRECDISABLE_STATUS_UPDATE IOCTL Gets noise reduction / echo cancellation (NREC) Disable status updates from the remote Bluetooth device. |
| [IOCTL_BTHHFP_DEVICE_GET_CONNECTION_STATUS_UPDATE IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-device-get-connection-status-update.md) | The IOCTL_BTHHFP_DEVICE_GET_CONNECTION_STATUS_UPDATE IOCTL Gets a connection status update. |
| [IOCTL_BTHHFP_MIC_GET_VOLUME_STATUS_UPDATE IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-mic-get-volume-status-update.md) | The IOCTL_BTHHFP_MIC_GET_VOLUME_STATUS_UPDATE IOCTL Gets the volume level setting of the Bluetooth device's microphone. |
| [IOCTL_BTHHFP_DEVICE_GET_KSNODETYPES IOCTL](..\bthhfpddi\ni-bthhfpddi-ioctl-bthhfp-device-get-ksnodetypes.md) | The IOCTL_BTHHFP_DEVICE_GET_KSNODETYPES IOCTL Gets the KSNODE types that best describe the Bluetooth device’s input and output. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT function](..\bthhfpddi\nf-bthhfpddi-bthhfp-audio-device-capabilties-init.md) | The BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT method returns a pointer to an initialized BTHHFP_AUDIO_DEVICE_CAPABILTIES data structure. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [DMUS_STREAM_TYPE enumeration](..\dmusicks\ne-dmusicks-dmus-stream-type.md) | Used for a DirectMusic synthesizer device. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IAllocatorMXF::GetMessage method](..\dmusicks\nf-dmusicks-iallocatormxf-getmessage.md) | The GetMessage method serves as the retrieval point for any DirectMusic kernel-mode component that utilizes the port driver's allocator to reuse DMUS_KERNEL_EVENT structures. |
| [ISynthSinkDMus::SyncToMaster method](..\dmusicks\nf-dmusicks-isynthsinkdmus-synctomaster.md) | The SyncToMaster method allows synchronization to the master clock in order to avoid drift. |
| [IPortDMus::Notify method](..\dmusicks\nf-dmusicks-iportdmus-notify.md) | The Notify method should be called from the miniport driver's interrupt service routine (ISR) when a hardware interrupt has occurred. |
| [IMiniportDMus::Service method](..\dmusicks\nf-dmusicks-iminiportdmus-service.md) | This method does not currently need to be implemented in the miniport driver. The Service method is currently unused. |
| [IAllocatorMXF::GetBuffer method](..\dmusicks\nf-dmusicks-iallocatormxf-getbuffer.md) | The GetBuffer method allocates a buffer for long MIDI events. |
| [IMasterClock::GetTime method](..\dmusicks\nf-dmusicks-imasterclock-gettime.md) | The GetTime method retrieves the current reference time read from the master clock. |
| [ISynthSinkDMus::RefTimeToSample method](..\dmusicks\nf-dmusicks-isynthsinkdmus-reftimetosample.md) | The RefTimeToSample method converts a reference time into a sample time. |
| [ISynthSinkDMus::SampleToRefTime method](..\dmusicks\nf-dmusicks-isynthsinkdmus-sampletoreftime.md) | The SampleToRefTime method converts a sample time to a reference time. |
| [IPortDMus::RegisterServiceGroup method](..\dmusicks\nf-dmusicks-iportdmus-registerservicegroup.md) | The RegisterServiceGroup method registers a service group with the DMus port driver. |
| [IAllocatorMXF::PutBuffer method](..\dmusicks\nf-dmusicks-iallocatormxf-putbuffer.md) | This method is not currently used by the miniport driver. The PutBuffer method passes a buffer to the allocator, but this occurs automatically when IMXF |
| [IMiniportDMus::Init method](..\dmusicks\nf-dmusicks-iminiportdmus-init.md) | The Init method initializes the DMus miniport object. |
| [IMiniportDMus::NewStream method](..\dmusicks\nf-dmusicks-iminiportdmus-newstream.md) | The NewStream method creates a new instance of a logical stream associated with a specified physical channel. |
| [ISynthSinkDMus::Render method](..\dmusicks\nf-dmusicks-isynthsinkdmus-render.md) | The Render method renders wave data into a destination sink. |
| [IPositionNotify::PositionNotify method](..\dmusicks\nf-dmusicks-ipositionnotify-positionnotify.md) | Byte position notify for MXF graph. |
| [IAllocatorMXF::GetBufferSize method](..\dmusicks\nf-dmusicks-iallocatormxf-getbuffersize.md) | The GetBufferSize method gets the buffer size from the allocator. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [DMUS_KERNEL_EVENT structure](..\dmusicks\ns-dmusicks--dmus-kernel-event.md) | The DMUS_KERNEL_EVENT structure is used to package time-stamped music events. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SYNTH_PORTPARAMS structure](..\dmusprop\ns-dmusprop--synth-portparams.md) | The SYNTH_PORTPARAMS structure contains the configuration parameters for a DirectMusic port, which is a DirectMusic term for a device that sends or receives music data. |
| [SYNTH_STATS structure](..\dmusprop\ns-dmusprop--synth-stats.md) | The SYNTH_STATS structure specifies synthesizer performance statistics such as the number of voices playing, CPU usage, number of notes lost, amount of free memory, and peak volume level. |
| [SYNTH_BUFFER structure](..\dmusprop\ns-dmusprop--synth-buffer.md) | The SYNTH_BUFFER structure specifies DLS data that is being downloaded to a synthesizer. |
| [SYNTHVOICEPRIORITY_INSTANCE structure](..\dmusprop\ns-dmusprop--synthvoicepriority-instance.md) | The SYNTHVOICEPRIORITY_INSTANCE structure identifies a voice in a MIDI synthesizer by specifying the voice's channel group (set of 16 MIDI channels) and its channel number within that group. |
| [SYNTHDOWNLOAD structure](..\dmusprop\ns-dmusprop--synthdownload.md) | The SYNTHDOWNLOAD structure specifies a handle for downloaded DLS data. It also specifies whether the buffer containing the DLS data can be freed. |
| [SYNTH_REVERB_PARAMS structure](..\dmusprop\ns-dmusprop--synth-reverb-params.md) | The SYNTH_REVERB_PARAMS structure contains configuration parameters. |
| [SYNTHCAPS structure](..\dmusprop\ns-dmusprop--synthcaps.md) | The SYNTHCAPS structure specifies the capabilities of a synthesizer. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [tagDRMRIGHTS structure](..\drmk\ns-drmk-tagdrmrights.md) | The DRMRIGHTS structure specifies the DRM content rights assigned to a KS audio pin or to a port-class driver's stream object. |
| [PKSP_DRMAUDIOSTREAM_CONTENTID structure](..\drmk\ns-drmk-pksp-drmaudiostream-contentid.md) | The KSP_DRMAUDIOSTREAM_CONTENTID structure specifies the property, request type, and context for a KSPROPERTY_DRMAUDIOSTREAM_CONTENTIDset-property request. It also specifies a list of function pointers to the DRM functions. |
| [PKSDRMAUDIOSTREAM_CONTENTID structure](..\drmk\ns-drmk-pksdrmaudiostream-contentid.md) | The KSDRMAUDIOSTREAM_CONTENTID structure specifies the DRM content ID and DRM content rights for a KSPROPERTY_DRMAUDIOSTREAM_CONTENTIDset-property request. |
| [tagDRMFORWARD structure](..\drmk\ns-drmk-tagdrmforward.md) | The DRMFORWARD structure contains the information that the DRMK system driver needs in order to forward a DRM content ID to a device that handles protected content. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFNDRMADDCONTENTHANDLERS callback](..\drmk\nc-drmk-pfndrmaddcontenthandlers.md) | This callback function is reserved for system use. |
| [PFNDRMCREATECONTENTMIXED callback](..\drmk\nc-drmk-pfndrmcreatecontentmixed.md) | This callback function is reserved for system use. |
| [PFNDRMGETCONTENTRIGHTS callback](..\drmk\nc-drmk-pfndrmgetcontentrights.md) | This callback function is reserved for system use. |
| [PFNDRMFORWARDCONTENTTOINTERFACE callback](..\drmk\nc-drmk-pfndrmforwardcontenttointerface.md) | This callback function is reserved for system use. |
| [PFNDRMDESTROYCONTENT callback](..\drmk\nc-drmk-pfndrmdestroycontent.md) | This callback function is reserved for system use. |
| [PFNDRMFORWARDCONTENTTOFILEOBJECT callback](..\drmk\nc-drmk-pfndrmforwardcontenttofileobject.md) | This callback function is reserved for system use. |
| [PFNDRMFORWARDCONTENTTODEVICEOBJECT callback](..\drmk\nc-drmk-pfndrmforwardcontenttodeviceobject.md) | This callback function is reserved for system use. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [DrmDestroyContent function](..\drmk\nf-drmk-drmdestroycontent.md) | The DrmDestroyContent function deletes a DRM content ID that was created by DrmCreateContentMixed. |
| [DrmForwardContentToFileObject function](..\drmk\nf-drmk-drmforwardcontenttofileobject.md) | The DrmForwardContentToFileObject function is obsolete and is maintained only to support existing drivers. |
| [DrmForwardContentToDeviceObject function](..\drmk\nf-drmk-drmforwardcontenttodeviceobject.md) | The DrmForwardContentToDeviceObject function accepts a device object representing a device to which the caller intends to forward protected content. |
| [DrmAddContentHandlers function](..\drmk\nf-drmk-drmaddcontenthandlers.md) | The DrmAddContentHandlers function provides the system with a list of functions that handle protected content. |
| [DrmGetContentRights function](..\drmk\nf-drmk-drmgetcontentrights.md) | The DrmGetContentRights function retrieves the DRM content rights assigned to a DRM content ID. |
| [IDrmAudioStream::SetContentId method](..\drmk\nf-drmk-idrmaudiostream-setcontentid.md) | The SetContentId method sets the DRM content ID and its assigned DRM content rights on a KS audio stream. |
| [DrmForwardContentToInterface function](..\drmk\nf-drmk-drmforwardcontenttointerface.md) | The DrmForwardContentToInterface function accepts a pointer to the COM interface of an object to which the caller intends to forward protected content. |
| [DrmCreateContentMixed function](..\drmk\nf-drmk-drmcreatecontentmixed.md) | The DrmCreateContentMixed function creates a DRM content ID to identify a KS audio stream containing mixed content from a number of streams. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PREGISTER_NOTIFICATION_EVENT callback](..\hdaudio\nc-hdaudio-pregister-notification-event.md) | The RegisterNotificationEvent routine registers a kernel event so that it can receive DMA progress notifications.The function pointer type for a RegisterNotificationEvent routine is defined as follows. |
| [PGET_WALL_CLOCK_REGISTER callback](..\hdaudio\nc-hdaudio-pget-wall-clock-register.md) | The GetWallClockRegister routine retrieves a pointer to the wall clock register.The function pointer type for a GetWallClockRegister routine is defined as |
| [PGET_RESOURCE_INFORMATION callback](..\hdaudio\nc-hdaudio-pget-resource-information.md) | The GetResourceInformation routine retrieves information about hardware resources.The function pointer type for a GetResourceInformation routine is defined as |
| [PREGISTER_EVENT_CALLBACK callback](..\hdaudio\nc-hdaudio-pregister-event-callback.md) | The RegisterEventCallback routine registers a callback routine for an unsolicited response from a codec or codecs.The function pointer type for a RegisterEventCallback routine is defined as |
| [PALLOCATE_DMA_BUFFER callback](..\hdaudio\nc-hdaudio-pallocate-dma-buffer.md) | The AllocateDmaBuffer routine allocates a data buffer in system memory for a DMA engine.The function pointer type for an AllocateDmaBuffer routine is defined as |
| [PCHANGE_BANDWIDTH_ALLOCATION callback](..\hdaudio\nc-hdaudio-pchange-bandwidth-allocation.md) | The ChangeBandwidthAllocation routine changes a DMA engine's bandwidth allocation on the HD Audio Link.The function pointer type for a ChangeBandwidthAllocation routine is defined as |
| [PUNREGISTER_EVENT_CALLBACK callback](..\hdaudio\nc-hdaudio-punregister-event-callback.md) | The UnregisterEventCallback routine deletes the registration of an event callback that was previously registered by a call to RegisterEventCallback.The function pointer type for an UnregisterEventCallback routine is defined as |
| [PSET_DMA_ENGINE_STATE callback](..\hdaudio\nc-hdaudio-pset-dma-engine-state.md) | The SetDmaEngineState routine sets the state of one or more DMA engines to the Running, Stopped, Paused, or Reset state.The function pointer type for a SetDmaEngineState routine is defined as |
| [PTRANSFER_CODEC_VERBS callback](..\hdaudio\nc-hdaudio-ptransfer-codec-verbs.md) | The TransferCodecVerbs routine transfers one or more commands to a codec or codecs and retrieves the responses to those commands.The function pointer type for a TransferCodecVerbs routine is defined as |
| [PALLOCATE_RENDER_DMA_ENGINE callback](..\hdaudio\nc-hdaudio-pallocate-render-dma-engine.md) | The AllocateRenderDmaEngine routine allocates a DMA engine for a render stream.The function pointer type for an AllocateRenderDmaEngine routine is defined as |
| [PGET_DEVICE_INFORMATION callback](..\hdaudio\nc-hdaudio-pget-device-information.md) | The GetDeviceInformation routine retrieves information about the HD Audio controller device.The function pointer type for a GetDeviceInformation routine is defined as |
| [PFREE_DMA_BUFFER_WITH_NOTIFICATION callback](..\hdaudio\nc-hdaudio-pfree-dma-buffer-with-notification.md) | The FreeDmaBufferWithNotification routine frees a DMA buffer that was previously allocated by a call to AllocateDmaBufferWithNotification.The function pointer type for a FreeDmaBufferWithNotification routine is defined as follows. |
| [PHDAUDIO_TRANSFER_COMPLETE_CALLBACK callback](..\hdaudio\nc-hdaudio-phdaudio-transfer-complete-callback.md) | HDAudio codec transfer complete callback function. PHDAUDIO_TRANSFER_COMPLETE_CALLBACK is used by the PTRANSFER_CODEC_VERBS callback function. |
| [PSETUP_DMA_ENGINE_WITH_BDL callback](..\hdaudio\nc-hdaudio-psetup-dma-engine-with-bdl.md) | The SetupDmaEngineWithBdl routine sets up a DMA engine to use a caller-allocated DMA buffer.The function pointer type for a SetupDmaEngineWithBdl routine is defined as |
| [PALLOCATE_CAPTURE_DMA_ENGINE callback](..\hdaudio\nc-hdaudio-pallocate-capture-dma-engine.md) | The AllocateCaptureDmaEngine routine allocates a DMA engine for a capture stream.The function pointer type for an AllocateCaptureDmaEngine routine is defined as |
| [PHDAUDIO_BDL_ISR callback](..\hdaudio\nc-hdaudio-phdaudio-bdl-isr.md) | The HDAudioBdlIsr routine is the ISR that the HD Audio bus driver calls each time an IOC interrupt occurs on the stream. It is a function pointer of type PHDAUDIO_BDL_ISR, which is defined as |
| [PALLOCATE_DMA_BUFFER_WITH_NOTIFICATION callback](..\hdaudio\nc-hdaudio-pallocate-dma-buffer-with-notification.md) | The AllocateDmaBufferWithNotification routine allocates a data buffer in system memory for a DMA engine.The function pointer type for an AllocateDmaBufferWithNotification routine is defined as follows. |
| [PFREE_CONTIGUOUS_DMA_BUFFER callback](..\hdaudio\nc-hdaudio-pfree-contiguous-dma-buffer.md) | The FreeContiguousDmaBuffer routine frees a DMA buffer and buffer descriptor list (BDL) that were allocated by a call to AllocateContiguousDmaBuffer.The function pointer type for a FreeContiguousDmaBuffer routine is defined as |
| [PHDAUDIO_UNSOLICITED_RESPONSE_CALLBACK callback](..\hdaudio\nc-hdaudio-phdaudio-unsolicited-response-callback.md) | HDAudio codec unsolicited response callback function. PHDAUDIO_UNSOLICITED_RESPONSE_CALLBACK is used by the PREGISTER_EVENT_CALLBACK callback function. |
| [PALLOCATE_CONTIGUOUS_DMA_BUFFER callback](..\hdaudio\nc-hdaudio-pallocate-contiguous-dma-buffer.md) | The AllocateContiguousDmaBuffer routine allocates a DMA buffer that consists of a single, contiguous block of physical memory.The function pointer type for an AllocateContiguousDmaBuffer routine is defined as |
| [PFREE_DMA_BUFFER callback](..\hdaudio\nc-hdaudio-pfree-dma-buffer.md) | The FreeDmaBuffer routine frees a DMA buffer that was previously allocated by a call to AllocateDmaBuffer.The function pointer type for a FreeDmaBuffer routine is defined as |
| [PUNREGISTER_NOTIFICATION_EVENT callback](..\hdaudio\nc-hdaudio-punregister-notification-event.md) | The UnregisterNotificationEvent routine deletes the registration of an event that was previously registered by a call to RegisterNotificationEvent.The function pointer type for an UnregisterNotificationEvent routine is defined as follows. |
| [PGET_LINK_POSITION_REGISTER callback](..\hdaudio\nc-hdaudio-pget-link-position-register.md) | The GetLinkPositionRegister routine retrieves a pointer to a DMA engine's link position register.The function pointer type for a GetLinkPositionRegister routine is defined as |
| [PFREE_DMA_ENGINE callback](..\hdaudio\nc-hdaudio-pfree-dma-engine.md) | The FreeDmaEngine routine frees a DMA engine that was previously allocated by a call to AllocateCaptureDmaEngine or AllocateRenderDmaEngine.The function pointer type for a FreeDmaEngine routine is defined as |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [HDAUDIO_CONVERTER_FORMAT structure](..\hdaudio\ns-hdaudio--hdaudio-converter-format.md) | The HDAUDIO_CONVERTER_FORMAT structure specifies the 16-bit encoded stream format for an input or output converter, as defined in the Intel High Definition Audio Specification (see the Intel HD Audio website). |
| [HDAUDIO_CODEC_COMMAND structure](..\hdaudio\ns-hdaudio--hdaudio-codec-command.md) | The HDAUDIO_CODEC_COMMAND structure specifies a codec command. |
| [HDAUDIO_BUFFER_DESCRIPTOR structure](..\hdaudio\ns-hdaudio--hdaudio-buffer-descriptor.md) | The HDAUDIO_BUFFER_DESCRIPTOR structure specifies a buffer descriptor, which is an entry in a buffer descriptor list (BDL). |
| [HDAUDIO_CODEC_RESPONSE structure](..\hdaudio\ns-hdaudio--hdaudio-codec-response.md) | The HDAUDIO_CODEC_RESPONSE structure specifies either a response to a codec command or an unsolicited response from a codec. |
| [HDAUDIO_BUS_INTERFACE_V2 structure](..\hdaudio\ns-hdaudio--hdaudio-bus-interface-v2.md) | The HDAUDIO_BUS_INTERFACE_V2 structure specifies the information that a client requires to call the routines in the HDAUDIO_BUS_INTERFACE_V2 version of the HD Audio DDI. |
| [HDAUDIO_BUS_INTERFACE_BDL structure](..\hdaudio\ns-hdaudio--hdaudio-bus-interface-bdl.md) | The HDAUDIO_BUS_INTERFACE_BDL structure specifies the information that a client requires to call the routines in the HDAUDIO_BUS_INTERFACE_BDL version of the HD Audio DDI. Another variant of this DDI is specified by the HDAUDIO_BUS_INTERFACE structure. |
| [HDAUDIO_DEVICE_INFORMATION structure](..\hdaudio\ns-hdaudio--hdaudio-device-information.md) | The HDAUDIO_DEVICE_INFORMATION structure specifies the hardware capabilities of the HD Audio bus controller. |
| [HDAUDIO_CODEC_TRANSFER structure](..\hdaudio\ns-hdaudio--hdaudio-codec-transfer.md) | The HDAUDIO_CODEC_TRANSFER structure specifies a codec command and the response to that command. |
| [HDAUDIO_STREAM_FORMAT structure](..\hdaudio\ns-hdaudio--hdaudio-stream-format.md) | The HDAUDIO_STREAM_FORMAT structure describes the data format of a capture or render stream. |
| [HDAUDIO_BUS_INTERFACE structure](..\hdaudio\ns-hdaudio--hdaudio-bus-interface.md) | The HDAUDIO_BUS_INTERFACE structure specifies the information that a client requires to call the routines in the HDAUDIO_BUS_INTERFACE version of the HD Audio DDI. Another variant of this DDI is specified by the HDAUDIO_BUS_INTERFACE_BDL structure. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [HDAUDIO_STREAM_STATE enumeration](..\hdaudio\ne-hdaudio--hdaudio-stream-state.md) | The HDAUDIO_STREAM_STATE enumeration defines constants that specify the different stream states supported by HDAudio. |
| [HDAUDIO_CODEC_POWER_STATE enumeration](..\hdaudio\ne-hdaudio--hdaudio-codec-power-state.md) | The HDAUDIO_CODEC_POWER_STATE enumeration defines constants that specify the different power states that HD Audio codecs can support. All states are from DEVICE_POWER_STATE except PowerCodecD3Cold. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IKeywordDetectorOemAdapter::ParseDetectionResultData method](..\keyworddetectoroemadapter\nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-parsedetectionresultdata.md) | The ParseDetectionResultData method is called by the operating system after handling a keyword detection event and after retrieving the result data from KSPROPERTY_SOUNDDETECTOR_MATCHRESULT. |
| [IKeywordDetectorOemAdapter::GetCapabilities method](..\keyworddetectoroemadapter\nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-getcapabilities.md) | The GetCapabilities method returns the keywords and languages supported by the object. |
| [IKeywordDetectorOemAdapter::VerifyUserKeyword method](..\keyworddetectoroemadapter\nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-verifyuserkeyword.md) | The VerifyUserKeyword method is used by the training user experience to verify that one instance of a spoken utterance, captured during training, matches a predefined keyword within some tolerance. |
| [IKeywordDetectorOemAdapter::ComputeAndAddUserModelData method](..\keyworddetectoroemadapter\nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-computeandaddusermodeldata.md) | The ComputeAndAddUserModelData method is used by the training user experience to compute the user-specific information relative to the user-independent keyword. |
| [IKeywordDetectorOemAdapter::BuildArmingPatternData method](..\keyworddetectoroemadapter\nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-buildarmingpatterndata.md) | The BuildArmingPatternData method is called by the operating system to build OEM-specific pattern data that includes any keyword and user-specific model data for detection. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [MIDL_IKeywordDetectorOemAdapter_0003 structure](..\keyworddetectoroemadapter\ns-keyworddetectoroemadapter---midl-ikeyworddetectoroemadapter-0003.md) | The KEYWORDSELECTOR struct is a triplet of IDs that uniquely select a particular keyword, language, and user combination. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [TELEPHONY_CALLCONTROLOP enumeration](..\ksmedia\ne-ksmedia-telephony-callcontrolop.md) | The TELEPHONY_CALLCONTROLOP enumeration defines constants that specify an operation to perform on a phone call. |
| [KSPROPERTY_SOUNDDETECTOR enumeration](..\ksmedia\ne-ksmedia-ksproperty-sounddetector.md) | The KSPROPERTY_SOUNDDETECTOR enumeration defines constants that are used to register a filter for an audio capture device that also supports a detector. |
| [KSPROPERTY_AUDIOENGINE enumeration](..\ksmedia\ne-ksmedia-ksproperty-audioengine.md) | The properties contained in the KSPROPSETID_AudioEngine property set are defined by this enumeration and must be supported by a KSNODETYPE_AUDIO_ENGINE node. |
| [KSPROPERTY_AUDIOSIGNALPROCESSING enumeration](..\ksmedia\ne-ksmedia-ksproperty-audiosignalprocessing.md) | The KSPROPERTY_AUDIOSIGNALPROCESSING enumeration defines a constant that is used by audio drivers in connection with audio processing modes on pins. |
| [TELEPHONY_CALLTYPE enumeration](..\ksmedia\ne-ksmedia-telephony-calltype.md) | The TELEPHONY_CALLTYPE enumeration defines constants that specify the type of phone call. |
| [KSPROPERTY_JACK enumeration](..\ksmedia\ne-ksmedia-ksproperty-jack.md) | The KSPROPERTY_JACK enumeration defines new property IDs that are used by audio jack structures. |
| [AUDIO_CURVE_TYPE enumeration](..\ksmedia\ne-ksmedia-audio-curve-type.md) | The AUDIO_CURVE_TYPE enumeration defines constants that specify a curve algorithm to be applied to set a volume level. |
| [KSPROPERTY_AUDIOMODULE enumeration](..\ksmedia\ne-ksmedia-ksproperty-audiomodule.md) | The KSPROPERTY_AUDIOMODULE enumeration defines constants that are used by audio drivers to communicate information about partner defined audio modules. |
| [TELEPHONY_PROVIDERCHANGEOP enumeration](..\ksmedia\ne-ksmedia-telephony-providerchangeop.md) | The TELEPHONY_PROVIDERCHANGEOP enumeration defines constants that specify the requested provider change operation. |
| [TELEPHONY_CALLSTATE enumeration](..\ksmedia\ne-ksmedia-telephony-callstate.md) | The TELEPHONY_CALLSTATE enumeration defines constants that specify the state of a phone call. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PKSDS3D_HRTF_INIT_MSG structure](..\ksmedia\ns-ksmedia-pksds3d-hrtf-init-msg.md) | The KSDS3D_HRTF_INIT_MSG structure specifies the parameter settings to use to initialize the head-relative transfer function (HRTF). |
| [PKSAUDIO_PRESENTATION_POSITION structure](..\ksmedia\ns-ksmedia-pksaudio-presentation-position.md) | The KSAUDIO_PRESENTATION_POSITION structure specifies the current cursor position in audio data stream that is being rendered to the endpoint. |
| [PSYSAUDIO_INSTANCE_INFO structure](..\ksmedia\ns-ksmedia-psysaudio-instance-info.md) | The SYSAUDIO_INSTANCE_INFO structure specifies which virtual audio device to open and includes flags for configuring that device. |
| [PKSAC3_ALTERNATE_AUDIO structure](..\ksmedia\ns-ksmedia-pksac3-alternate-audio.md) | The KSAC3_ALTERNATE_AUDIO structure specifies whether the two mono channels in an AC-3-encoded stream should be interpreted as a stereo pair or as two independent program channels. |
| [DS3DVECTOR structure](..\ksmedia\ns-ksmedia--ds3dvector.md) | The DS3DVECTOR structure contains three-dimensional position coordinates, position vector components, or velocity vector components. |
| [PWAVEFORMATEXTENSIBLE structure](..\ksmedia\ns-ksmedia-pwaveformatextensible.md) | The WAVEFORMATEXTENSIBLE structure specifies the format of an audio wave stream. |
| [PKSNODEPROPERTY_AUDIO_CHANNEL structure](..\ksmedia\ns-ksmedia-pksnodeproperty-audio-channel.md) | The KSNODEPROPERTY_AUDIO_CHANNEL structure specifies a property of a channel in a node. |
| [PKSAUDIO_PREFERRED_STATUS structure](..\ksmedia\ns-ksmedia-pksaudio-preferred-status.md) | The KSAUDIO_PREFERRED_STATUS structure specifies the status of a preferred device. |
| [PSYSAUDIO_ATTACH_VIRTUAL_SOURCE structure](..\ksmedia\ns-ksmedia-psysaudio-attach-virtual-source.md) | The SYSAUDIO_ATTACH_VIRTUAL_SOURCE structure is used to attach a mixer-line virtual source (for example, a volume or mute control) to a mixer pin on the virtual audio device. |
| [KSAUDIOMODULE_NOTIFICATION structure](..\ksmedia\ns-ksmedia--ksaudiomodule-notification.md) | The KSAUDIOMODULE_NOTIFICATION structure describes the properties associated with audio modules change notification. |
| [PKSAC3_BIT_STREAM_MODE structure](..\ksmedia\ns-ksmedia-pksac3-bit-stream-mode.md) | The KSAC3_BIT_STREAM_MODE structure specifies the bit-stream mode, which is the type of audio service that is encoded into an AC-3 stream. |
| [tagKSTOPOLOGY_ENDPOINTIDPAIR structure](..\ksmedia\ns-ksmedia--tagkstopology-endpointidpair.md) | The KSTOPOLOGY_ENDPOINTIDPAIR structure specifies the render and capture endpoint IDs to use for the KSPROPERTY_TELEPHONY_ENDPOINTIDPAIR property. |
| [PKSAUDIO_COPY_PROTECTION structure](..\ksmedia\ns-ksmedia-pksaudio-copy-protection.md) | The KSAUDIO_COPY_PROTECTION structure specifies the copy-protection status of an audio stream. |
| [PSYSAUDIO_CREATE_VIRTUAL_SOURCE structure](..\ksmedia\ns-ksmedia-psysaudio-create-virtual-source.md) | The SYSAUDIO_CREATE_VIRTUAL_SOURCE structure is used to create a mixer-line virtual source such as a volume control or mute. |
| [PKSDS3D_LISTENER_ORIENTATION structure](..\ksmedia\ns-ksmedia-pksds3d-listener-orientation.md) | A KSD3D_LISTENER_ORIENTATION structure specifies the position vector of the 3D listener. This structure is used to get or set the data value for the KSPROPERTY_DIRECTSOUND3DLISTENER_ORIENTATION property. |
| [PKSAUDIO_MIXLEVEL structure](..\ksmedia\ns-ksmedia-pksaudio-mixlevel.md) | The KSAUDIO_MIXLEVEL structure specifies the mixing level of an input-output path in a supermixer node (KSNODETYPE_SUPERMIX). |
| [tagKSJACK_DESCRIPTION2 structure](..\ksmedia\ns-ksmedia--tagksjack-description2.md) | The KSJACK_DESCRIPTION2 structure specifies the capabilities and the current state of a jack that supports jack presence detection. |
| [tagKSAUDIOENGINE_DESCRIPTOR structure](..\ksmedia\ns-ksmedia--tagksaudioengine-descriptor.md) | The KSAUDIOENGINE_DESCRIPTOR structure describes the static, external properties of the audio engine. |
| [tagKSJACK_SINK_INFORMATION structure](..\ksmedia\ns-ksmedia--tagksjack-sink-information.md) | The KSJACK_SINK_INFORMATION structure specifies information about a display-related digital audio device, such as an HDMI device or a display port. |
| [PKSDATAFORMAT_DSOUND structure](..\ksmedia\ns-ksmedia-pksdataformat-dsound.md) | The KSDATAFORMAT_DSOUND structure provides detailed information about a DirectSound audio stream. |
| [tagKSAUDIOENGINE_BUFFER_SIZE_RANGE structure](..\ksmedia\ns-ksmedia--tagksaudioengine-buffer-size-range.md) | The KSAUDIOENGINE_BUFFER_SIZE_RANGE structure specifies the minimum and maximum buffer size that the hardware audio engine can support at the instance when it is called. |
| [PKSRTAUDIO_HWREGISTER_PROPERTY structure](..\ksmedia\ns-ksmedia-pksrtaudio-hwregister-property.md) | The KSRTAUDIO_HWREGISTRY_PROPERTY structure appends a register base address to a KSPROPERTY structure. |
| [tagKSTELEPHONY_PROVIDERCHANGE structure](..\ksmedia\ns-ksmedia--tagkstelephony-providerchange.md) | The KSTELEPHONY_PROVIDERCHANGE structure specifies the phone call type and provider change operation to use for the KSPROPERTY_TELEPHONY_PROVIDERCHANGE property. |
| [PKSDS3D_BUFFER_CONE_ANGLES structure](..\ksmedia\ns-ksmedia-pksds3d-buffer-cone-angles.md) | A KSDS3D_BUFFER_CONE_ANGLES structure specifies the inside and outside cone angles. |
| [PKSDS3D_BUFFER_ALL structure](..\ksmedia\ns-ksmedia-pksds3d-buffer-all.md) | The KSDS3D_BUFFER_ALL structure specifies all the 3D characteristics of a DirectSound 3D buffer. |
| [PKSDS3D_LISTENER_ALL structure](..\ksmedia\ns-ksmedia-pksds3d-listener-all.md) | The KSDS3D_LISTENER_ALL structure specifies all the properties of the DirectSound 3D listener. This structure is used to get or set the data value for the KSPROPERTY_DIRECTSOUND3DLISTENER_ALL property. |
| [PKSJACK_DESCRIPTION structure](..\ksmedia\ns-ksmedia-pksjack-description.md) | The KSJACK_DESCRIPTION structure specifies the physical attributes of an audio jack. |
| [PKSRTAUDIO_BUFFER structure](..\ksmedia\ns-ksmedia-pksrtaudio-buffer.md) | The KSRTAUDIO_BUFFER structure specifies the buffer address, size, and a call memory barrier flag for a cyclic audio data buffer. |
| [PKSAC3_DIALOGUE_LEVEL structure](..\ksmedia\ns-ksmedia-pksac3-dialogue-level.md) | The KSAC3_DIALOGUE_LEVEL structure specifies the average volume level of spoken dialog within the audio program encoded in an AC-3 stream. |
| [tagKSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE structure](..\ksmedia\ns-ksmedia-tagksattribute-audiosignalprocessing-mode.md) | The KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE structure specifies an audio signal processing mode. |
| [PSYSAUDIO_SELECT_GRAPH structure](..\ksmedia\ns-ksmedia-psysaudio-select-graph.md) | The SYSAUDIO_SELECT_GRAPH structure is used to specify a graph that includes an optional node such as an AEC control. |
| [PKSDS3D_ITD_PARAMS structure](..\ksmedia\ns-ksmedia-pksds3d-itd-params.md) | The KSDS3D_ITD_PARAMS structure specifies the parameters applied by the interaural time delay (ITD) algorithm to the left or right channel in a 3D node (KSNODETYPE_3D_EFFECTS). |
| [PKSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION structure](..\ksmedia\ns-ksmedia-pksrtaudio-buffer-property-with-notification.md) | The KSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION structure appends a buffer base address, a requested buffer size, and a notification count to a KSPROPERTY structure. |
| [PLOOPEDSTREAMING_POSITION_EVENT_DATA structure](..\ksmedia\ns-ksmedia-ploopedstreaming-position-event-data.md) | The LOOPEDSTREAMING_POSITION_EVENT_DATA structure describes a position event in a looped buffer. |
| [tagKSTELEPHONY_CALLINFO structure](..\ksmedia\ns-ksmedia--tagkstelephony-callinfo.md) | The KSTELEPHONY_CALLINFO structure specifies the type and state of a phone call for the KSPROPERTY_TELEPHONY_CALLINFO property. |
| [tagKSAUDIOENGINE_VOLUMELEVEL structure](..\ksmedia\ns-ksmedia--tagksaudioengine-volumelevel.md) | The KSAUDIOENGINE_VOLUMELEVEL structure specifies the target volume level, ramp type, and duration within which the volume level should change, for a given volume level request via the KSPROPERTY_AUDIOENGINE_VOLUMELEVEL property. |
| [tagKSTELEPHONY_CALLCONTROL structure](..\ksmedia\ns-ksmedia--tagkstelephony-callcontrol.md) | The KSTELEPHONY_CALLCONTROL structure specifies the phone call type and control operation to use for the KSPROPERTY_TELEPHONY_CALLCONTROL property. |
| [PKSAC3_ROOM_TYPE structure](..\ksmedia\ns-ksmedia-pksac3-room-type.md) | The KSAC3_ROOM_TYPE structure specifies the type of audio mixing room in which an AC-3-encoded stream was produced. |
| [PKSAUDIO_MIX_CAPS structure](..\ksmedia\ns-ksmedia-pksaudio-mix-caps.md) | The KSAUDIO_MIX_CAPS structure specifies the mixing capabilities of a particular data path from one input channel of a supermixer node (KSNODETYPE_SUPERMIX) to an output channel of the same node. |
| [PKSDSOUND_BUFFERDESC structure](..\ksmedia\ns-ksmedia-pksdsound-bufferdesc.md) | The KSDSOUND_BUFFERDESC structure describes a DirectSound buffer. |
| [PKSAUDIO_POSITIONEX structure](..\ksmedia\ns-ksmedia-pksaudio-positionex.md) | The KSAUDIO_POSITIONEX structure specifies the stream position and the associated timestamp information for a kernel streaming (KS)-based audio driver. |
| [PKSDATARANGE_AUDIO structure](..\ksmedia\ns-ksmedia-pksdatarange-audio.md) | The KSDATARANGE_AUDIO structure specifies a range of audio formats. |
| [PKSDS3D_HRTF_PARAMS_MSG structure](..\ksmedia\ns-ksmedia-pksds3d-hrtf-params-msg.md) | The KSDS3D_HRTF_PARAMS_MSG structure specifies the parameter settings to apply to a head-relative transfer function (HRTF). |
| [SOUNDDETECTOR_PATTERNHEADER structure](..\ksmedia\ns-ksmedia-sounddetector-patternheader.md) | The SOUNDDETECTOR_PATTERNHEADER structure specifies the pattern header for the sound detector in the KSPROPERTY_SOUNDDETECTOR_PATTERNS property. |
| [KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT structure](..\ksmedia\ns-ksmedia--ksaudio-packetsize-signalprocessingmode-constraint.md) | The KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT structure describes the constraints specific to any signal processing mode. |
| [tagKSTOPOLOGY_ENDPOINTID structure](..\ksmedia\ns-ksmedia--tagkstopology-endpointid.md) | The KSTOPOLOGY_ENDPOINTID structure specifies the name and the pin ID of a topology endpoint. |
| [PKSDS3D_ITD_PARAMS_MSG structure](..\ksmedia\ns-ksmedia-pksds3d-itd-params-msg.md) | The KSDS3D_ITD_PARAMS_MSG structure specifies the parameters used by the interaural time delay (ITD) algorithm in a 3D node (KSNODETYPE_3D_EFFECTS). |
| [KSAUDIOMODULE_DESCRIPTOR structure](..\ksmedia\ns-ksmedia--ksaudiomodule-descriptor.md) | The KSAUDIOMODULE_DESCRIPTOR structure describes the static, external properties of audio modules. |
| [KSAUDIOMODULE_PROPERTY structure](..\ksmedia\ns-ksmedia--ksaudiomodule-property.md) | The KSAUDIOMODULE_DESCRIPTOR structure describes the static, external properties of the audio modules. |
| [PKSAUDIO_MICROPHONE_COORDINATES structure](..\ksmedia\ns-ksmedia-pksaudio-microphone-coordinates.md) | The KSAUDIO_MICROPHONE_COORDINATES structure specifies the type and the coordinates of a single microphone in the microphone array. |
| [PKSNODEPROPERTY structure](..\ksmedia\ns-ksmedia-pksnodeproperty.md) | The KSNODEPROPERTY structure specifies a node and a property of that node. |
| [PKSAUDIO_CHANNEL_CONFIG structure](..\ksmedia\ns-ksmedia-pksaudio-channel-config.md) | The KSAUDIO_CHANNEL_CONFIG structure specifies the configuration of channels within the data format of an audio stream. |
| [KSAUDIO_PACKETSIZE_CONSTRAINTS2 structure](..\ksmedia\ns-ksmedia--ksaudio-packetsize-constraints2.md) | The KSAUDIO_PACKETSIZE_CONSTRAINTS2 structure describes the physical hardware constraints. |
| [KSAUDIO_PACKETSIZE_CONSTRAINTS structure](..\ksmedia\ns-ksmedia--ksaudio-packetsize-constraints.md) | The KSAUDIO_PACKETSIZE_CONSTRAINTS structure describes the physical hardware constraints. |
| [PKSAUDIO_DYNAMIC_RANGE structure](..\ksmedia\ns-ksmedia-pksaudio-dynamic-range.md) | The KSAUDIO_DYNAMIC_RANGE structure specifies the dynamic range of an audio stream. This structure is used to get or set the data value for the KSPROPERTY_AUDIO_DYNAMIC_RANGE property. |
| [PKSDS3D_HRTF_FILTER_FORMAT_MSG structure](..\ksmedia\ns-ksmedia-pksds3d-hrtf-filter-format-msg.md) | The KSDS3D_HRTF_FILTER_FORMAT_MSG structure specifies the filter format to use for a head-relative transfer function (HRTF). |
| [PKSAC3_ERROR_CONCEALMENT structure](..\ksmedia\ns-ksmedia-pksac3-error-concealment.md) | The KSAC3_ERROR_CONCEALMENT structure specifies how errors in an AC-3-encoded stream should be concealed during playback. |
| [PKSDATAFORMAT_WAVEFORMATEX structure](..\ksmedia\ns-ksmedia-pksdataformat-waveformatex.md) | The KSDATAFORMAT_WAVEFORMATEX structure provides detailed information about the data format of an audio stream consisting of wave data. |
| [PKSAUDIO_MIXCAP_TABLE structure](..\ksmedia\ns-ksmedia-pksaudio-mixcap-table.md) | The KSAUDIO_MIXCAP_TABLE structure specifies the mixing capabilities of a supermixer node (KSNODETYPE_SUPERMIX). This structure is used to get or set the data value for the KSPROPERTY_AUDIO_MIX_LEVEL_CAPS property. |
| [PKSRTAUDIO_SETWRITEPACKET_INFO structure](..\ksmedia\ns-ksmedia-pksrtaudio-setwritepacket-info.md) | The KSRTAUDIO_SETWRITEPACKET_INFO structure describes information associated with an audio packet. |
| [PKSRTAUDIO_GETREADPACKET_INFO structure](..\ksmedia\ns-ksmedia-pksrtaudio-getreadpacket-info.md) | The KSRTAUDIO_GETREADPACKET_INFO structure describes information for an audio packet. |
| [PKSMUSICFORMAT structure](..\ksmedia\ns-ksmedia-pksmusicformat.md) | The KSMUSICFORMAT structure is used to send and receive information about MIDI data that is input from and output to WDM audio devices. |
| [PKSAUDIO_POSITION structure](..\ksmedia\ns-ksmedia-pksaudio-position.md) | The KSAUDIO_POSITION structure specifies the current positions of the play and write cursors in the sound buffer for an audio stream. |
| [PKSRTAUDIO_HWREGISTER structure](..\ksmedia\ns-ksmedia-pksrtaudio-hwregister.md) | The KSRTAUDIO_HWREGISTER structure specifies the address and additional information about a hardware register requested by the client. |
| [PKSRTAUDIO_HWLATENCY structure](..\ksmedia\ns-ksmedia-pksrtaudio-hwlatency.md) | The KSRTAUDIO_HWLATENCY structure describes the latency that the audio hardware adds to a wave stream during playback or recording. |
| [PKSDATARANGE_MUSIC structure](..\ksmedia\ns-ksmedia-pksdatarange-music.md) | The KSDATARANGE_MUSIC structure specifies a range of DirectMusic MIDI formats. |
| [PKSAC3_DOWNMIX structure](..\ksmedia\ns-ksmedia-pksac3-downmix.md) | The KSAC3_DOWNMIX structure specifies whether the program channels in an AC-3-encoded stream need to be downmixed to accommodate the speaker configuration. |
| [PKSRTAUDIO_NOTIFICATION_EVENT_PROPERTY structure](..\ksmedia\ns-ksmedia-pksrtaudio-notification-event-property.md) | The KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY structure appends an event handle to a KSPROPERTY structure |
| [PKSAUDIO_MIC_ARRAY_GEOMETRY structure](..\ksmedia\ns-ksmedia-pksaudio-mic-array-geometry.md) | The KSAUDIO_MIC_ARRAY_GEOMETRY structure specifies the type and the geometry of the microphone array. |
| [PKSRTAUDIO_BUFFER_PROPERTY structure](..\ksmedia\ns-ksmedia-pksrtaudio-buffer-property.md) | The KSRTAUDIO_BUFFER_PROPERTY structure appends a buffer base address and requested buffer size to a KSPROPERTY structure. This structure is used by the client to request allocation of the audio buffer via KSPROPERTY_RTAUDIO_BUFFER. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IMiniportWaveCyclicStream::SetState method](..\portcls\nf-portcls-iminiportwavecyclicstream-setstate.md) | The SetState method sets the new state of playback or recording for the stream. |
| [PcNewMiniport function](..\portcls\nf-portcls-pcnewminiport.md) | The PcNewMiniport function creates an instance of one of the system-supplied miniport drivers that are built into the PortCls system driver, portcls.sys. |
| [IInterruptSync::Connect method](..\portcls\nf-portcls-iinterruptsync-connect.md) | The Connect method connects the synchronization object to the interrupt. |
| [IResourceList::NumberOfEntriesOfType method](..\portcls\nf-portcls-iresourcelist-numberofentriesoftype.md) | The NumberOfEntriesOfType method returns the number of resource items of a given type in the resource list. For each resource type, a macro is defined to call this method as previously described. |
| [IMiniportWaveRTStreamNotification::UnregisterNotificationEvent method](..\portcls\nf-portcls-iminiportwavertstreamnotification-unregisternotificationevent.md) | The UnregisterNotificationEvent method unregisters an event from DMA driven event notification. |
| [IServiceSink::RequestService method](..\portcls\nf-portcls-iservicesink-requestservice.md) | The RequestService method is called to forward a service request to an IServiceSink object. |
| [IMiniportAudioEngineNode::GetDeviceChannelMute method](..\portcls\nf-portcls-iminiportaudioenginenode-getdevicechannelmute.md) | Gets the state of the Mute node for the audio device channel. |
| [IPortEvents::AddEventToEventList method](..\portcls\nf-portcls-iportevents-addeventtoeventlist.md) | The AddEventToEventList method adds an event to the port driver's event list. |
| [IMiniportStreamAudioEngineNode::SetLfxState method](..\portcls\nf-portcls-iminiportstreamaudioenginenode-setlfxstate.md) | Sets the state of the local effects (LFX) node that is in the path of the audio stream. |
| [IMiniportAudioEngineNode::GetDeviceChannelVolume method](..\portcls\nf-portcls-iminiportaudioenginenode-getdevicechannelvolume.md) | Gets the volume level for a given channel of the audio device. |
| [IPortWaveCyclic::Notify method](..\portcls\nf-portcls-iportwavecyclic-notify.md) | The Notify method notifies the port driver that an interrupt indicating the progress of the DMA pointer has occurred. It should be called from the miniport driver's interrupt service routine (ISR). |
| [IMiniportWaveRTStreamNotification::RegisterNotificationEvent method](..\portcls\nf-portcls-iminiportwavertstreamnotification-registernotificationevent.md) | The RegisterNotificationEvent method registers an event to be notified for DMA-driven event notification. |
| [IMiniportWaveCyclic::Init method](..\portcls\nf-portcls-iminiportwavecyclic-init.md) | The Init method initializes the WaveCyclic miniport object. Initialization includes verification of the hardware using the resources specified in the resource list. |
| [PcUnregisterAdapterPnpManagement function](..\portcls\nf-portcls-pcunregisteradapterpnpmanagement.md) | The PcUnregisterAdapterPnpManagement function unregisters the audio adapter's PnP management interface from the PortCls class driver. It is used to support PnP rebalance. |
| [IMiniportWavePci::NewStream method](..\portcls\nf-portcls-iminiportwavepci-newstream.md) | The NewStream method creates a new instance of a logical stream associated with a specified physical channel. |
| [IPortWavePci::Notify method](..\portcls\nf-portcls-iportwavepci-notify.md) | The Notify method notifies the port driver that an interrupt indicating the progress of the DMA pointer has occurred. |
| [PcNewPort function](..\portcls\nf-portcls-pcnewport.md) | The PcNewPort function creates a new system-supplied port-driver object, whose interface (derived from base class IPort) is specified by a class ID. |
| [IPortClsRuntimePower::UnregisterPowerControlCallback method](..\portcls\nf-portcls-iportclsruntimepower-unregisterpowercontrolcallback.md) | The port class driver (PortCls) uses the UnregisterPowerControlCallback method to unregister a power control callback. |
| [IServiceGroup::RemoveMember method](..\portcls\nf-portcls-iservicegroup-removemember.md) | The RemoveMember method removes the specified member from the service group. |
| [PcDestroyContent function](..\portcls\nf-portcls-pcdestroycontent.md) | The PcDestroyContent function deletes a DRM content ID that was created by PcCreateContentMixed. Note that this function call is identical in operation to the DrmDestroyContent function, and its parameter definitions and return value are also identical. |
| [PcRegisterAdapterPnpManagement function](..\portcls\nf-portcls-pcregisteradapterpnpmanagement.md) | The PcRegisterAdapterPnpManagement function registers the adapter's PnP-management interface with the PortCls system driver. It is used to support PnP rebalance. |
| [PcRequestNewPowerState function](..\portcls\nf-portcls-pcrequestnewpowerstate.md) | The PcRequestNewPowerState function is used to request a new power state for the device. This function is typically not needed by adapter drivers but can occasionally be useful in working around some kinds of hardware problems. |
| [PcUnregisterIoTimeout function](..\portcls\nf-portcls-pcunregisteriotimeout.md) | The PcUnregisterIoTimeout function unregisters a driver-supplied I/O-timer callback routine for a specified device object. |
| [PcNewResourceList function](..\portcls\nf-portcls-pcnewresourcelist.md) | The PcNewResourceList function creates and initializes a resource list. |
| [IResourceList::AddEntryFromParent method](..\portcls\nf-portcls-iresourcelist-addentryfromparent.md) | The AddEntryFromParent method adds to a resource list an entry found in the resource list's parent list. |
| [IResourceList::TranslatedList method](..\portcls\nf-portcls-iresourcelist-translatedlist.md) | The TranslatedList method returns the list of translated resources. |
| [PcCompletePendingPropertyRequest function](..\portcls\nf-portcls-pccompletependingpropertyrequest.md) | The PcCompletePendingPropertyRequest function is called to complete a pending property request. |
| [IPortWavePciStream::TerminatePacket method](..\portcls\nf-portcls-iportwavepcistream-terminatepacket.md) | The TerminatePacket method terminates the packet currently being mapped. |
| [IPortClsPnp::RegisterAdapterPnpManagement method](..\portcls\nf-portcls-iportclspnp-registeradapterpnpmanagement.md) | The RegisterAdapterPowerManagement method registers the PnP management interface of the adapter with PortCls. |
| [IPortClsRuntimePower::RegisterPowerControlCallback method](..\portcls\nf-portcls-iportclsruntimepower-registerpowercontrolcallback.md) | The port class driver (PortCls) uses the RegisterPowerControlCallback method to register a power control callback. |
| [PcGetTimeInterval function](..\portcls\nf-portcls-pcgettimeinterval.md) | The PcGetTimeInterval function returns the time elapsed since a specified time. Time is measured in 100-nanosecond units. |
| [IMiniportAudioEngineNode::GetDeviceAttributeSteppings method](..\portcls\nf-portcls-iminiportaudioenginenode-getdeviceattributesteppings.md) | Gets the allowed stepping value for the audio device attribute. |
| [IMiniportWavePci::Init method](..\portcls\nf-portcls-iminiportwavepci-init.md) | The Init method initializes the WavePci miniport object. Initialization includes verification of the hardware using the resources specified in the resource list. |
| [PcNewServiceGroup function](..\portcls\nf-portcls-pcnewservicegroup.md) | The PcNewServiceGroup function creates and initializes a service group. |
| [IMiniportWaveRT::Init method](..\portcls\nf-portcls-iminiportwavert-init.md) | The Init method initializes the WaveRT miniport driver object. |
| [IMiniportWaveRT::GetDeviceDescription method](..\portcls\nf-portcls-iminiportwavert-getdevicedescription.md) | The GetDeviceDescription method returns a pointer to a DEVICE_DESCRIPTION structure describing the device. |
| [IPortClsRuntimePower::SendPowerControl method](..\portcls\nf-portcls-iportclsruntimepower-sendpowercontrol.md) | The port class driver (PortCls) uses the SendPowerControl method to send power control codes to the audio adapter. |
| [IMiniportStreamAudioEngineNode::GetStreamLinearBufferPosition method](..\portcls\nf-portcls-iminiportstreamaudioenginenode-getstreamlinearbufferposition.md) | Gets the number of bytes that the DMA has fetched from the audio buffer since the beginning of the stream. |
| [IResourceList::FindTranslatedEntry method](..\portcls\nf-portcls-iresourcelist-findtranslatedentry.md) | The FindTranslatedEntry method returns a pointer to a translated entry of the specified type, or NULL if no such entry is found. |
| [IMiniportAudioSignalProcessing::GetModes method](..\portcls\nf-portcls-iminiportaudiosignalprocessing-getmodes.md) | The GetModes method, Gets the audio signal processing modes supported by an audio pin. |
| [IInterruptSync::RegisterServiceRoutine method](..\portcls\nf-portcls-iinterruptsync-registerserviceroutine.md) | The RegisterServiceRoutine method registers an interrupt service routine (ISR) that is to be called when an interrupt occurs. |
| [PcInitializeAdapterDriver function](..\portcls\nf-portcls-pcinitializeadapterdriver.md) | The PcInitializeAdapterDriver function binds an adapter driver to the PortCls system driver. |
| [PcRegisterPhysicalConnectionFromExternal function](..\portcls\nf-portcls-pcregisterphysicalconnectionfromexternal.md) | The PcRegisterPhysicalConnectionFromExternal function registers a physical connection to an audio adapter filter from an external audio adapter filter. |
| [IUnregisterSubdevice::UnregisterSubdevice method](..\portcls\nf-portcls-iunregistersubdevice-unregistersubdevice.md) | The UnregisterSubdevice method deletes the registration of a subdevice that was previously registered by a call to PcRegisterSubdevice. |
| [IMiniportAudioEngineNode::GetGfxState method](..\portcls\nf-portcls-iminiportaudioenginenode-getgfxstate.md) | Gets the state of the global effects (GFX) node in the audio engine. |
| [IMiniportAudioEngineNode::GetDeviceChannelCount method](..\portcls\nf-portcls-iminiportaudioenginenode-getdevicechannelcount.md) | Gets a count of the number of channels supported by the audio device. |
| [IAdapterPowerManagement::QueryPowerChangeState method](..\portcls\nf-portcls-iadapterpowermanagement-querypowerchangestate.md) | The QueryPowerChangeState method is called by PortCls in response to the receipt of an IRP_MN_QUERY_POWER power IRP. |
| [IMiniportAudioEngineNode::GetAudioEngineDescriptor method](..\portcls\nf-portcls-iminiportaudioenginenode-getaudioenginedescriptor.md) | Gets the descriptor for the audio engine node. |
| [IDrmPort2::AddContentHandlers method](..\portcls\nf-portcls-idrmport2-addcontenthandlers.md) | The AddContentHandlers method provides the system with a list of functions that handle protected content. |
| [IRegistryKey::EnumerateKey method](..\portcls\nf-portcls-iregistrykey-enumeratekey.md) | The EnumerateKey method returns information about the subkeys of the open key. |
| [PcNewRegistryKey function](..\portcls\nf-portcls-pcnewregistrykey.md) | The PcNewRegistryKey function opens or creates a new registry key and creates an IRegistryKey object to represent the key. The caller accesses the key through this object. |
| [PcAddAdapterDevice function](..\portcls\nf-portcls-pcaddadapterdevice.md) | The PcAddAdapterDevice function adds an adapter device to the WDM device stack. |
| [IPortWaveRTStream::FreePagesFromMdl method](..\portcls\nf-portcls-iportwavertstream-freepagesfrommdl.md) | The FreePagesFromMdl method frees a memory descriptor list (MDL). |
| [PcRegisterPhysicalConnectionToExternal function](..\portcls\nf-portcls-pcregisterphysicalconnectiontoexternal.md) | The PcRegisterPhysicalConnectionToExternal function registers a physical connection from an audio adapter filter to an external audio adapter filter. |
| [IMiniportStreamAudioEngineNode::SetStreamChannelMute method](..\portcls\nf-portcls-iminiportstreamaudioenginenode-setstreamchannelmute.md) | Sets the state of the Mute node in the path of the audio stream. |
| [IPortWMIRegistration::RegisterWMIProvider method](..\portcls\nf-portcls-iportwmiregistration-registerwmiprovider.md) | The RegisterWMIProvider method registers the Event Tracing for Windows (ETW) capability of the miniport driver with PortCls. |
| [PcCreateContentMixed function](..\portcls\nf-portcls-pccreatecontentmixed.md) | The PcCreateContentMixed function computes the DRM content rights for a composite stream containing mixed content from some number of KS audio streams. |
| [IMiniportAudioEngineNode::GetDeviceFormat method](..\portcls\nf-portcls-iminiportaudioenginenode-getdeviceformat.md) | Gets the audio data format for an audio device. |
| [IMiniportWavePci::Service method](..\portcls\nf-portcls-iminiportwavepci-service.md) | The Service method notifies the miniport driver of a request for service. |
| [IMiniportWavePciStream::SetFormat method](..\portcls\nf-portcls-iminiportwavepcistream-setformat.md) | The SetFormat method sets the KS data format of the wave stream. |
| [PcDispatchIrp function](..\portcls\nf-portcls-pcdispatchirp.md) | The PcDispatchIrp function dispatches an IRP to the PortCls system driver's default handler. |
| [PcForwardContentToInterface function](..\portcls\nf-portcls-pcforwardcontenttointerface.md) | The PcForwardContentToInterface function accepts a pointer to the COM interface of an object to which the caller intends to forward protected content. |
| [PcForwardContentToDeviceObject function](..\portcls\nf-portcls-pcforwardcontenttodeviceobject.md) | The PcForwardContentToDeviceObject function accepts a device object representing a device to which the caller intends to forward protected content. |
| [IPortClsPnp::UnregisterAdapterPnpManagement method](..\portcls\nf-portcls-iportclspnp-unregisteradapterpnpmanagement.md) | The UnRegisterAdapterPowerManagement method unregisters the PnP management interface of the adapter from PortCls. |
| [IPortClsPower::SetIdlePowerManagement method](..\portcls\nf-portcls-iportclspower-setidlepowermanagement.md) | The SetIdlePowerManagement method provides a way for the adapter driver to opt in or opt out of idle state detection. |
| [IMiniportStreamAudioEngineNode::GetStreamChannelMute method](..\portcls\nf-portcls-iminiportstreamaudioenginenode-getstreamchannelmute.md) | Gets the state of the Mute node in the path of the audio stream. |
| [PcNewResourceSublist function](..\portcls\nf-portcls-pcnewresourcesublist.md) | The PcNewResourceSublist function creates and initializes an empty resource list that is derived from another resource list. |
| [PcGetDeviceProperty function](..\portcls\nf-portcls-pcgetdeviceproperty.md) | The PcGetDeviceProperty function returns the requested device property from the registry. |
| [IMiniportWavePciStream::MappingAvailable method](..\portcls\nf-portcls-iminiportwavepcistream-mappingavailable.md) | The MappingAvailable method indicates that a new mapping is available. |
| [IMiniportWaveRTOutputStream::GetOutputStreamPresentationPosition method](..\portcls\nf-portcls-iminiportwavertoutputstream-getoutputstreampresentationposition.md) | Returns stream presentation information. |
| [IMiniportStreamAudioEngineNode::SetStreamChannelVolume method](..\portcls\nf-portcls-iminiportstreamaudioenginenode-setstreamchannelvolume.md) | Sets the volume level to be applied to the audio stream. |
| [IInterruptSync::Disconnect method](..\portcls\nf-portcls-iinterruptsync-disconnect.md) | The Disconnect method disconnects the synchronization object from the interrupt. |
| [IMiniportStreamAudioEngineNode2::SetStreamCurrentWritePositionForLastBuffer method](..\portcls\nf-portcls-iminiportstreamaudioenginenode2-setstreamcurrentwritepositionforlastbuffer.md) | Sets the current cursor position in the last audio data stream that was written to the audio buffer. |
| [IPinCount::PinCount method](..\portcls\nf-portcls-ipincount-pincount.md) | The PinCount method queries the miniport driver for its pin count. |
| [IPortClsPower::UnregisterAdapterPowerManagement method](..\portcls\nf-portcls-iportclspower-unregisteradapterpowermanagement.md) | The UnregisterAdapterPowerManagement method unregisters the adapter's power management interface with PortCls. |
| [IPortWaveCyclic::NewMasterDmaChannel method](..\portcls\nf-portcls-iportwavecyclic-newmasterdmachannel.md) | The NewMasterDmaChannel method creates a new instance of a bus-master DMA channel. |
| [IMiniportAudioEngineNode::GetSupportedDeviceFormats method](..\portcls\nf-portcls-iminiportaudioenginenode-getsupporteddeviceformats.md) | Gets the supported audio data formats for the audio device. |
| [IAdapterPowerManagement2::PowerChangeState2 method](..\portcls\nf-portcls-iadapterpowermanagement2-powerchangestate2.md) | Portcls calls the IAdapterPowerManagement2 |
| [IPortWavePciStream::ReleaseMapping method](..\portcls\nf-portcls-iportwavepcistream-releasemapping.md) | The ReleaseMapping method releases a mapping that was obtained by a previous call to IPortWavePciStream |
| [IMiniportMidiStream::SetFormat method](..\portcls\nf-portcls-iminiportmidistream-setformat.md) | The SetFormat method sets the KS data format of the MIDI stream. |
| [IPortMidi::Notify method](..\portcls\nf-portcls-iportmidi-notify.md) | The Notify method notifies the port driver that an interrupt indicating the progress of the DMA pointer has occurred. It should be called from the miniport driver's interrupt service routine (ISR). |
| [IDrmPort2::ForwardContentToDeviceObject method](..\portcls\nf-portcls-idrmport2-forwardcontenttodeviceobject.md) | The ForwardContentToDeviceObject method accepts a device object representing a device to which the caller intends to forward protected content. |
| [IMiniportWaveRTOutputStream::GetPacketCount method](..\portcls\nf-portcls-iminiportwavertoutputstream-getpacketcount.md) | GetPacketCount returns the (1-based) count of packets completely transferred from the WaveRT buffer into hardware. |
| [IMiniportStreamAudioEngineNode::GetStreamAttributeSteppings method](..\portcls\nf-portcls-iminiportstreamaudioenginenode-getstreamattributesteppings.md) | Gets the allowed stepping value for the audio stream attribute. |
| [IPortWMIRegistration::UnregisterWMIProvider method](..\portcls\nf-portcls-iportwmiregistration-unregisterwmiprovider.md) | The UnregisterWMIProvider method unregisters the Event Tracing for Windows (ETW) interface that was previously registered with a call to the RegisterWMIProvider method. The unregistration disables the ETW registration with PortCls. |
| [PcUnregisterAdapterPowerManagement function](..\portcls\nf-portcls-pcunregisteradapterpowermanagement.md) | The PcUnregisterAdapterPowerManagement function unregisters the audio adapter's power management interface from the PortCls class driver. The PcUnregisterAdapterPowerManagement function is available in Windows 7 and later versions of Windows. |
| [IPortEvents::GenerateEventList method](..\portcls\nf-portcls-iportevents-generateeventlist.md) | The GenerateEventList method notifies clients through the port driver's list of event entries that a particular event has occurred. |
| [IRegistryKey::DeleteKey method](..\portcls\nf-portcls-iregistrykey-deletekey.md) | The DeleteKey method deletes the registry key. |
| [IPortWavePci::NewMasterDmaChannel method](..\portcls\nf-portcls-iportwavepci-newmasterdmachannel.md) | The NewMasterDmaChannel method creates a new instance of a bus-master DMA channel. |
| [IPortWaveRTStream::AllocateContiguousPagesForMdl method](..\portcls\nf-portcls-iportwavertstream-allocatecontiguouspagesformdl.md) | The AllocateContiguousPagesForMdl method allocates a list of contiguous, nonpaged, physical memory pages and returns a pointer to a memory descriptor list (MDL) that describes them. |
| [IPowerNotify::PowerChangeNotify method](..\portcls\nf-portcls-ipowernotify-powerchangenotify.md) | The PowerChangeNotify method notifies the miniport driver of changes in the power state. |
| [IMiniportStreamAudioEngineNode::GetStreamChannelPeakMeter method](..\portcls\nf-portcls-iminiportstreamaudioenginenode-getstreamchannelpeakmeter.md) | Gets the value of the PeakMeter node in the path of the audio stream. |
| [IMiniportStreamAudioEngineNode::GetLfxState method](..\portcls\nf-portcls-iminiportstreamaudioenginenode-getlfxstate.md) | Gets the state of the local effects (LFX) node that is in the path of the audio stream. |
| [IResourceList::AddEntry method](..\portcls\nf-portcls-iresourcelist-addentry.md) | The AddEntry method adds an entry to a resource list. |
| [IMiniportWavePciStream::RevokeMappings method](..\portcls\nf-portcls-iminiportwavepcistream-revokemappings.md) | The RevokeMappings method revokes mappings that were previously obtained through IPortWavePciStream |
| [IAdapterPowerManagement3::D3ExitLatencyChanged method](..\portcls\nf-portcls-iadapterpowermanagement3-d3exitlatencychanged.md) | PortCls calls the D3ExitLatencyChanged method while the device is in sleep (D3) power state, to provide a new exit latency value. |
| [IMiniportMidi::Service method](..\portcls\nf-portcls-iminiportmidi-service.md) | The Service method notifies the miniport driver of a request for service. |
| [IAdapterPowerManagement::PowerChangeState method](..\portcls\nf-portcls-iadapterpowermanagement-powerchangestate.md) | The PowerChangeState method requests that the device change to a new power state. |
| [IRegistryKey::QueryRegistryValues method](..\portcls\nf-portcls-iregistrykey-queryregistryvalues.md) | The QueryRegistryValues method allows the caller to query several values from the registry with a single call. |
| [IPortClsVersion::GetVersion method](..\portcls\nf-portcls-iportclsversion-getversion.md) | The GetVersion method returns the version of the Windows operating system that the driver is running on. |
| [IPortWaveCyclic::NewSlaveDmaChannel method](..\portcls\nf-portcls-iportwavecyclic-newslavedmachannel.md) | The NewSlaveDmaChannel method creates a new instance of a subordinate DMA channel. |
| [IMiniportWavePciStream::NormalizePhysicalPosition method](..\portcls\nf-portcls-iminiportwavepcistream-normalizephysicalposition.md) | The NormalizePhysicalPosition method converts a physical buffer position to a time-based value. |
| [IInterruptSync::CallSynchronizedRoutine method](..\portcls\nf-portcls-iinterruptsync-callsynchronizedroutine.md) | The CallSynchronizedRoutine method calls a routine that is not an interrupt service routine (ISR) but whose execution needs to be synchronized with ISRs. |
| [IServiceGroup::RequestDelayedService method](..\portcls\nf-portcls-iservicegroup-requestdelayedservice.md) | The RequestDelayedService method requests service after the specified delay. |
| [IResourceList::FindUntranslatedEntry method](..\portcls\nf-portcls-iresourcelist-finduntranslatedentry.md) | The FindUntranslatedEntry method returns a pointer to an untranslated entry of the specified type, or NULL if no such pointer is found. |
| [IMiniportAudioEngineNode::GetEngineFormatSize method](..\portcls\nf-portcls-iminiportaudioenginenode-getengineformatsize.md) | Gets the format type and the buffer size for the audio engine's audio data format. |
| [IMiniportMidiStream::SetState method](..\portcls\nf-portcls-iminiportmidistream-setstate.md) | The SetState method sets the stream's transport state to a new state value. |
| [IPortClsNotifications::SendNotification method](..\portcls\nf-portcls-iportclsnotifications-sendnotification.md) | Sends a notification to the listening UWP apps, to allow for communications between audio modules and UWP apps. |
| [IUnregisterPhysicalConnection::UnregisterPhysicalConnection method](..\portcls\nf-portcls-iunregisterphysicalconnection-unregisterphysicalconnection.md) | The UnregisterPhysicalConnection method deletes the registration of a physical connection that was registered by a previous call to PcRegisterPhysicalConnection. |
| [IMiniportStreamAudioEngineNode::GetStreamPresentationPosition method](..\portcls\nf-portcls-iminiportstreamaudioenginenode-getstreampresentationposition.md) | Gets the current cursor position in the audio data stream that is being rendered to the endpoint. |
| [IPortClsNotifications::FreeNotificationBuffer method](..\portcls\nf-portcls-iportclsnotifications-freenotificationbuffer.md) | Frees a previously allocated IPortClsNotifications buffer. The buffer is used in sending notifications, to allow for communications between audio modules and UWP apps. |
| [PcForwardIrpSynchronous function](..\portcls\nf-portcls-pcforwardirpsynchronous.md) | The PcForwardIrpSynchronous function is used by IRP handlers to forward Plug and Play IRPs to the physical device object (PDO). |
| [IUnregisterPhysicalConnection::UnregisterPhysicalConnectionToExternal method](..\portcls\nf-portcls-iunregisterphysicalconnection-unregisterphysicalconnectiontoexternal.md) | The UnregisterPhysicalConnectionToExternal method deletes the registration of a physical connection that was registered by a previous call to PcRegisterPhysicalConnectionToExternal. |
| [IPortClsStreamResourceManager2::AddStreamResource2 method](..\portcls\nf-portcls-iportclsstreamresourcemanager2-addstreamresource2.md) | AddStreamResource2 adds a stream resource. Two type of stream resources are supported |
| [IPortWavePciStream::GetMapping method](..\portcls\nf-portcls-iportwavepcistream-getmapping.md) | The GetMapping method obtains a mapping from the port driver and associates a tag with the mapping. |
| [IMiniportMidiStream::Read method](..\portcls\nf-portcls-iminiportmidistream-read.md) | The Read method reads data from an incoming MIDI stream. |
| [IMiniportWaveRTStreamNotification::FreeBufferWithNotification method](..\portcls\nf-portcls-iminiportwavertstreamnotification-freebufferwithnotification.md) | The FreeBufferWithNotification method is used to free an audio buffer previously allocated with a call to IMiniportWaveRTStreamNotification |
| [PcNewDmaChannel function](..\portcls\nf-portcls-pcnewdmachannel.md) | The PcNewDmaChannel function creates a new DMA-channel object. This function is obsolete; for more information, see the following comments. |
| [IMiniportWaveRTStreamNotification::AllocateBufferWithNotification method](..\portcls\nf-portcls-iminiportwavertstreamnotification-allocatebufferwithnotification.md) | The AllocateAudioBufferWithNotification method allocates a cyclic buffer for audio data when you want to implement DMA-driven event notification. If you do not want event notification, you must use IMiniportWaveRTStream |
| [IPortClsEtwHelper::MiniportWriteEtwEvent method](..\portcls\nf-portcls-iportclsetwhelper-miniportwriteetwevent.md) | The MiniportWriteEtwEvent method is used by an audio miniport driver for providing the information about an Event Tracing for Windows (ETW) event. |
| [IAdapterPowerManagement::QueryDeviceCapabilities method](..\portcls\nf-portcls-iadapterpowermanagement-querydevicecapabilities.md) | The QueryDeviceCapabilities method is called by PortCls in response to a Plug and Play IRP_MN_QUERY_CAPABILITIES IRP. |
| [IMiniportWaveRTInputStream::GetReadPacket method](..\portcls\nf-portcls-iminiportwavertinputstream-getreadpacket.md) | Returns information about captured data. |
| [IMiniportMidiStream::Write method](..\portcls\nf-portcls-iminiportmidistream-write.md) | The Write method writes data to an outgoing MIDI stream. |
| [IMusicTechnology::SetTechnology method](..\portcls\nf-portcls-imusictechnology-settechnology.md) | The SetTechnology method changes the Technology member of each KSDATARANGE_MUSIC structure in the data ranges for the miniport driver's pins. |
| [IServiceGroup::SupportDelayedService method](..\portcls\nf-portcls-iservicegroup-supportdelayedservice.md) | The SupportDelayedService method indicates that the service group should prepare to support delayed service. |
| [IMiniportAudioEngineNode::GetBufferSizeRange method](..\portcls\nf-portcls-iminiportaudioenginenode-getbuffersizerange.md) | Gets the minimum and maximum buffer size that the hardware audio engine can support. |
| [IPortWaveRTStream::GetPhysicalPagesCount method](..\portcls\nf-portcls-iportwavertstream-getphysicalpagescount.md) | The GetPhysicalPagesCount method returns the count of the physical pages in a memory descriptor list (MDL). |
| [IMiniportStreamAudioEngineNode::SetStreamLoopbackProtection method](..\portcls\nf-portcls-iminiportstreamaudioenginenode-setstreamloopbackprotection.md) | Sets the loopback protection status of the audio engine node. |
| [IMiniportWaveCyclicStream::SetFormat method](..\portcls\nf-portcls-iminiportwavecyclicstream-setformat.md) | The SetFormat method sets the KS data format of the wave stream. |
| [IPortMidi::RegisterServiceGroup method](..\portcls\nf-portcls-iportmidi-registerservicegroup.md) | The RegisterServiceGroup method registers the service group to be used for the IPortMidi |
| [IPortWaveRTStream::MapAllocatedPages method](..\portcls\nf-portcls-iportwavertstream-mapallocatedpages.md) | The MapAllocatedPages method maps a list of previously allocated physical pages into a contiguous block of virtual memory that is accessible from kernel-mode. |
| [PcCompleteIrp function](..\portcls\nf-portcls-pccompleteirp.md) | The PcCompleteIrp function completes an IRP that was previously marked as pending. |
| [IMiniportAudioEngineNode::GetMixFormat method](..\portcls\nf-portcls-iminiportaudioenginenode-getmixformat.md) | Gets the audio data format for the audio engine mixer. |
| [PcRegisterPhysicalConnection function](..\portcls\nf-portcls-pcregisterphysicalconnection.md) | The PcRegisterPhysicalConnection function registers a physical connection between two audio adapter filters that are instantiated by the same adapter driver. |
| [IMiniportStreamAudioEngineNode::GetStreamChannelCount method](..\portcls\nf-portcls-iminiportstreamaudioenginenode-getstreamchannelcount.md) | Gets a count of the number of channels available for the stream. |
| [IMiniportAudioEngineNode::SetDeviceChannelVolume method](..\portcls\nf-portcls-iminiportaudioenginenode-setdevicechannelvolume.md) | Sets the volume level for a given channel of the audio device. |
| [IRegistryKey::SetValueKey method](..\portcls\nf-portcls-iregistrykey-setvaluekey.md) | The SetValueKey method replaces or creates a value entry under the open key. |
| [PcRegisterAdapterPowerManagement function](..\portcls\nf-portcls-pcregisteradapterpowermanagement.md) | The PcRegisterAdapterPowerManagement function registers the adapter's power-management interface with the PortCls system driver. |
| [PcGetContentRights function](..\portcls\nf-portcls-pcgetcontentrights.md) | The PcGetContentRights function retrieves the DRM content rights assigned to a DRM content ID. Note that this function call is identical in operation to the DrmGetContentRights function, and its parameter definitions and return value are also identical. |
| [PcRemoveStreamResource function](..\portcls\nf-portcls-pcremovestreamresource.md) | PcRemoveStreamResource removes an existing stream resource. |
| [IMiniportWaveCyclicStream::GetPosition method](..\portcls\nf-portcls-iminiportwavecyclicstream-getposition.md) | The GetPosition method gets the current position of the stream. |
| [IMiniportWavePciStream::GetPosition method](..\portcls\nf-portcls-iminiportwavepcistream-getposition.md) | The GetPosition method gets the current position of the stream. |
| [PcAddStreamResource function](..\portcls\nf-portcls-pcaddstreamresource.md) | PcAddStreamResource adds a stream resource. |
| [IMiniportWavePciStream::GetAllocatorFraming method](..\portcls\nf-portcls-iminiportwavepcistream-getallocatorframing.md) | The GetAllocatorFraming method gets the preferred allocator-framing parameters for the stream. |
| [IInterruptSync::GetKInterrupt method](..\portcls\nf-portcls-iinterruptsync-getkinterrupt.md) | The GetKInterrupt method gets a WDM interrupt object from a port-class synchronization object. |
| [IMiniportStreamAudioEngineNode::GetStreamChannelVolume method](..\portcls\nf-portcls-iminiportstreamaudioenginenode-getstreamchannelvolume.md) | Gets the current volume level that is applied to the audio stream. |
| [IUnregisterPhysicalConnection::UnregisterPhysicalConnectionFromExternal method](..\portcls\nf-portcls-iunregisterphysicalconnection-unregisterphysicalconnectionfromexternal.md) | The UnregisterPhysicalConnectionFromExternal method deletes the registration of a physical connection that was registered by a previous call to PcRegisterPhysicalConnectionFromExternal. |
| [IMiniportWavePciStream::SetState method](..\portcls\nf-portcls-iminiportwavepcistream-setstate.md) | The SetState method changes the state of the stream transport. |
| [PcRegisterIoTimeout function](..\portcls\nf-portcls-pcregisteriotimeout.md) | The PcRegisterIoTimeout function registers a driver-supplied I/O-timer callback routine for a specified device object. |
| [IMiniportMidi::Init method](..\portcls\nf-portcls-iminiportmidi-init.md) | The Init method initializes the MIDI miniport object. |
| [IPortWaveRTStream::GetPhysicalPageAddress method](..\portcls\nf-portcls-iportwavertstream-getphysicalpageaddress.md) | The GetPhysicalPageAddress method returns the physical address for a page within a memory descriptor list (MDL). |
| [IPinName::GetPinName method](..\portcls\nf-portcls-ipinname-getpinname.md) | The GetPinName method retrieves the friendly name of an audio endpoint. |
| [PcRegisterSubdevice function](..\portcls\nf-portcls-pcregistersubdevice.md) | The PcRegisterSubdevice function registers a subdevice to make it available for use by clients. |
| [IPortClsPower::RegisterAdapterPowerManagement method](..\portcls\nf-portcls-iportclspower-registeradapterpowermanagement.md) | The RegisterAdapterPowerManagement method registers the power management interface of the adapter with PortCls. |
| [IRegistryKey::EnumerateValueKey method](..\portcls\nf-portcls-iregistrykey-enumeratevaluekey.md) | The EnumerateValueKey method returns information about a registry entry that contains a value key. |
| [IMiniportWaveCyclicStream::NormalizePhysicalPosition method](..\portcls\nf-portcls-iminiportwavecyclicstream-normalizephysicalposition.md) | The NormalizePhysicalPosition method converts a physical buffer position to a time-based value. |
| [IMiniportAudioEngineNode::SetDeviceChannelMute method](..\portcls\nf-portcls-iminiportaudioenginenode-setdevicechannelmute.md) | Sets the state of the Mute node for the audio device channel. |
| [PcAddContentHandlers function](..\portcls\nf-portcls-pcaddcontenthandlers.md) | The PcAddContentHandlers function provides the system with a list of functions that handle protected content. |
| [IMiniportAudioEngineNode::GetDeviceChannelPeakMeter method](..\portcls\nf-portcls-iminiportaudioenginenode-getdevicechannelpeakmeter.md) | Gets the PeakMeter value for the audio device channel. |
| [PcGetPhysicalDeviceObject function](..\portcls\nf-portcls-pcgetphysicaldeviceobject.md) | The PcGetPhysicalDeviceObject function enables audio miniport drivers to retrieve the underlying physical device object of the audio device. |
| [IMiniportMidi::NewStream method](..\portcls\nf-portcls-iminiportmidi-newstream.md) | The NewStream method creates a new instance of a logical stream associated with a specified physical channel. |
| [IPortWaveRTStream::UnmapAllocatedPages method](..\portcls\nf-portcls-iportwavertstream-unmapallocatedpages.md) | The UnmapAllocatedPages method releases a mapping. |
| [IPreFetchOffset::SetPreFetchOffset method](..\portcls\nf-portcls-iprefetchoffset-setprefetchoffset.md) | The SetPreFetchOffset method sets the prefetch offset, which is the number of bytes of data separating the write cursor from the play cursor in a DirectSound output stream. |
| [IRegistryKey::NewSubKey method](..\portcls\nf-portcls-iregistrykey-newsubkey.md) | The NewSubKey method either creates a new registry subkey or opens an existing subkey under the key represented by the IRegistryKey object. |
| [IPortWaveRTStream::AllocatePagesForMdl method](..\portcls\nf-portcls-iportwavertstream-allocatepagesformdl.md) | The AllocatePagesForMdl method allocates a list of nonpaged physical memory pages and returns a pointer to a memory descriptor list (MDL) that describes them. |
| [IMiniportWaveRTOutputStream::SetWritePacket method](..\portcls\nf-portcls-iminiportwavertoutputstream-setwritepacket.md) | SetWritePacket informs the driver that the OS has written valid data to the WaveRT buffer. |
| [IMiniportWaveCyclicStream::SetNotificationFreq method](..\portcls\nf-portcls-iminiportwavecyclicstream-setnotificationfreq.md) | The SetNotificationFreq method controls the frequency at which notification interrupts are generated by setting the interval between successive interrupts. |
| [IServiceGroup::AddMember method](..\portcls\nf-portcls-iservicegroup-addmember.md) | The AddMember method adds a member to the service group. |
| [IMiniportTopology::Init method](..\portcls\nf-portcls-iminiporttopology-init.md) | The Init method initializes the topology miniport object. |
| [IMiniportWaveCyclicStream::Silence method](..\portcls\nf-portcls-iminiportwavecyclicstream-silence.md) | The Silence method is used to copy silence samples to a specified buffer. |
| [IRegistryKey::QueryValueKey method](..\portcls\nf-portcls-iregistrykey-queryvaluekey.md) | The QueryValueKey method retrieves information about a registry key's value entries, including their names, types, data sizes, and values. |
| [IMiniportWavePciStream::Service method](..\portcls\nf-portcls-iminiportwavepcistream-service.md) | The Service method notifies the miniport driver of a request for service. |
| [IServiceGroup::CancelDelayedService method](..\portcls\nf-portcls-iservicegroup-canceldelayedservice.md) | The CancelDelayedService method cancels the previously requested delayed service. |
| [IResourceList::NumberOfEntries method](..\portcls\nf-portcls-iresourcelist-numberofentries.md) | The NumberOfEntries method returns the number of resource items in the resource list. |
| [IPortClsNotifications::AllocNotificationBuffer method](..\portcls\nf-portcls-iportclsnotifications-allocnotificationbuffer.md) | Allocates a buffer of the specified size, in the specified memory pool, for use in sending notifications, to allow for communications between audio modules and UWP apps. |
| [PcForwardContentToFileObject function](..\portcls\nf-portcls-pcforwardcontenttofileobject.md) | The PcForwardContentToFileObject function is obsolete and is maintained only to support existing drivers. |
| [IMiniportStreamAudioEngineNode::SetStreamCurrentWritePosition method](..\portcls\nf-portcls-iminiportstreamaudioenginenode-setstreamcurrentwriteposition.md) | Sets the current cursor position in the audio data stream that is being captured from the endpoint. |
| [IRegistryKey::QueryKey method](..\portcls\nf-portcls-iregistrykey-querykey.md) | The QueryKey method retrieves information about a registry key, including the key name, key class, and the number of subkeys and their sizes. |
| [PcNewInterruptSync function](..\portcls\nf-portcls-pcnewinterruptsync.md) | The PcNewInterruptSync function creates and initializes an interrupt-synchronization object. |
| [IMiniportAudioEngineNode::SetDeviceFormat method](..\portcls\nf-portcls-iminiportaudioenginenode-setdeviceformat.md) | Sets the audio data format for an audio device. |
| [IResourceList::UntranslatedList method](..\portcls\nf-portcls-iresourcelist-untranslatedlist.md) | The UntranslatedList method returns the list of untranslated resources. |
| [IMiniportWaveRT::NewStream method](..\portcls\nf-portcls-iminiportwavert-newstream.md) | The NewStream method creates a new instance of a WaveRT stream object. |
| [IMiniportWaveCyclic::NewStream method](..\portcls\nf-portcls-iminiportwavecyclic-newstream.md) | The NewStream method creates a new instance of a logical stream that is associated with a specified physical channel. |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IPortClsEtwHelper interface](..\portcls\nn-portcls-iportclsetwhelper.md) | The IPortClsEtwHelper interface allows an audio miniport driver to access the Event Tracing for Windows (ETW) helper functions. |
| [IMiniportAudioEngineNode interface](..\portcls\nn-portcls-iminiportaudioenginenode.md) | This interface allows a miniport driver to use KS properties that access the audio engine via a KS filter handle. |
| [IAdapterPowerManagement3 interface](..\portcls\nn-portcls-iadapterpowermanagement3.md) | The IAdapterPowerManagement3 interface inherits from IUnknown, and it is used for receiving power management messages. |
| [IMiniportAudioSignalProcessing interface](..\portcls\nn-portcls-iminiportaudiosignalprocessing.md) | The IMiniportAudioSignalProcessing interface is implemented by the WaveRT miniport component of any audio driver, if any of its pins support audio signal processing modes. |
| [IMiniportStreamAudioEngineNode2 interface](..\portcls\nn-portcls-iminiportstreamaudioenginenode2.md) | The IMiniportStreamAudioEngineNode2 interface allows an audio miniport driver to extend the capabilities of the IMiniportStreamAudioEngineNode interface. |
| [IMiniportStreamAudioEngineNode interface](..\portcls\nn-portcls-iminiportstreamaudioenginenode.md) | This interface allows a miniport driver to use KS properties that access the audio engine via a pin instance handle. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [PC_REBALANCE_TYPE enumeration](..\portcls\ne-portcls-pc-rebalance-type.md) | The PC_REBALANCE_TYPE enum describes the type of support for rebalancing. |
| [EPcMiniportEngineEvent enumeration](..\portcls\ne-portcls-epcminiportengineevent.md) | This topic introduces the EPcMiniportEngineEvent enum, and describes the parameters that provide additional information when the miniport driver reports a glitching error. |
| [eEngineFormatType enumeration](..\portcls\ne-portcls-eengineformattype.md) | The eEngineFormatType enumeration defines constants that specify the audio data type supported by the audio engine. |
| [PcStreamResourceType enumeration](..\portcls\ne-portcls--pcstreamresourcetype.md) | This topic discusses the PcStreamResourceType enum, and describes its members. The PcStreamResourceType enum is used to define the type of resources used for specific audio streaming. |
| [PC_EXIT_LATENCY enumeration](..\portcls\ne-portcls--pc-exit-latency.md) | This topic discusses the PC_EXIT_LATENCY enum, and describes its members. The latency times map to specific maximum times in which the device must be able to exit its sleep state and enter the fully functional state (D0). |
| [eChannelTargetType enumeration](..\portcls\ne-portcls-echanneltargettype.md) | The eChannelTargetType enumeration defines constants that specify a type of node (target) in a given channel. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PCSTREAMRESOURCE_DESCRIPTOR structure](..\portcls\ns-portcls--pcstreamresource-descriptor.md) | PCSTREAMRESOURCE_DESCRIPTOR defines the stream resource. Use PCSTREAMRESOURCE_DESCRIPTOR_INIT to correctly initialize this structure. |
| [PCNOTIFICATION_BUFFER structure](..\portcls\ns-portcls--pcnotification-buffer.md) | The notification buffer used by IPortClsNotifications. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PCPFNEVENT_HANDLER callback](..\portcls\nc-portcls-pcpfnevent-handler.md) | An EventHandler routine processes event requests. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_USBSBAUD_GET_VOLUME_STATUS_UPDATE IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-get-volume-status-update.md) | TBD |
| [IOCTL_USBSBAUD_SET_MUTE IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-set-mute.md) | TBD |
| [IOCTL_USBSBAUD_GET_SIDETONE_VOLUMEPROPERTYVALUES IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-get-sidetone-volumepropertyvalues.md) | TBD |
| [IOCTL_USBSBAUD_SET_STREAM_CLOSE IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-set-stream-close.md) | TBD |
| [IOCTL_USBSBAUD_GET_ERROR_STATUS_UPDATE IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-get-error-status-update.md) | TBD |
| [IOCTL_USBSBAUD_GET_ENDPOINT_DESCRIPTOR IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-get-endpoint-descriptor.md) | TBD |
| [IOCTL_USBSBAUD_GET_SIDETONE_STATUS_UPDATE IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-get-sidetone-status-update.md) | TBD |
| [IOCTL_USBSBAUD_SET_SIDETONE_PROPERTY IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-set-sidetone-property.md) | TBD |
| [IOCTL_USBSBAUD_SET_STREAM_OPEN IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-set-stream-open.md) | TBD |
| [IOCTL_USBSBAUD_GET_MUTE_STATUS_UPDATE IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-get-mute-status-update.md) | TBD |
| [IOCTL_USBSBAUD_GET_VOLUMEPROPERTYVALUES IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-get-volumepropertyvalues.md) | TBD |
| [IOCTL_USBSBAUD_GET_SHADOW_RESOURCES IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-get-shadow-resources.md) | TBD |
| [IOCTL_USBSBAUD_GET_SUPPORTED_FORMATS IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-get-supported-formats.md) | TBD |
| [IOCTL_USBSBAUD_SET_VOLUME IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-set-volume.md) | TBD |
| [IOCTL_USBSBAUD_GET_DEVICE_DESCRIPTOR IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-get-device-descriptor.md) | TBD |
| [IOCTL_USBSBAUD_GET_STREAM_STATUS_UPDATE IOCTL](..\usbsidebandaudio\ni-usbsidebandaudio-ioctl-usbsbaud-get-stream-status-update.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [USBSIDEBANDAUDIO_DEVICE_DESCRIPTOR structure](..\usbsidebandaudio\ns-usbsidebandaudio--usbsidebandaudio-device-descriptor.md) | TBD. |


This technology is in the following headers:


| Header        | 

| [bthhfpddi](..\bthhfpddi\~PORTAL~bthhfpddi.md) | 

| [dmusicks](..\dmusicks\~PORTAL~dmusicks.md) | 

| [dmusprop](..\dmusprop\~PORTAL~dmusprop.md) | 

| [drmk](..\drmk\~PORTAL~drmk.md) | 

| [hdaudio](..\hdaudio\~PORTAL~hdaudio.md) | 

| [keyworddetectoroemadapter](..\keyworddetectoroemadapter\~PORTAL~keyworddetectoroemadapter.md) | 

| [ksmedia](..\ksmedia\~PORTAL~ksmedia.md) | 

| [portcls](..\portcls\~PORTAL~portcls.md) | 

| [punknown](..\punknown\~PORTAL~punknown.md) | 

| [unknown](..\unknown\~PORTAL~unknown.md) | 

| [usbsidebandaudio](..\usbsidebandaudio\~PORTAL~usbsidebandaudio.md) | 
