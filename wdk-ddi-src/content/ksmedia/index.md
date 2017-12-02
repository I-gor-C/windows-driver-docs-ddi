# Ksmedia.h header


This header is used by Streaming media devices, Audio, Display. For more information, see
- [Streaming media devices](../_stream/index.md)
- [Audio](../_audio/index.md)
- [Display](../_display/index.md)

Ksmedia.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [DDPIXELFORMAT structure](ns-ksmedia--ddpixelformat.md) | The DDPIXELFORMAT structure describes the pixel format of a DirectDrawSurface object. |
| [DDVIDEOPORTCONNECT structure](ns-ksmedia--ddvideoportconnect.md) | The DDVIDEOPORTCONNECT structure describes a hardware video port connection. |
| [DS3DVECTOR structure](ns-ksmedia--ds3dvector.md) | The DS3DVECTOR structure contains three-dimensional position coordinates, position vector components, or velocity vector components. |
| [KSAUDIOMODULE_DESCRIPTOR structure](ns-ksmedia--ksaudiomodule-descriptor.md) | The KSAUDIOMODULE_DESCRIPTOR structure describes the static, external properties of audio modules. |
| [KSAUDIOMODULE_NOTIFICATION structure](ns-ksmedia--ksaudiomodule-notification.md) | The KSAUDIOMODULE_NOTIFICATION structure describes the properties associated with audio modules change notification. |
| [KSAUDIOMODULE_PROPERTY structure](ns-ksmedia--ksaudiomodule-property.md) | The KSAUDIOMODULE_DESCRIPTOR structure describes the static, external properties of the audio modules. |
| [KSAUDIO_PACKETSIZE_CONSTRAINTS structure](ns-ksmedia--ksaudio-packetsize-constraints.md) | The KSAUDIO_PACKETSIZE_CONSTRAINTS structure describes the physical hardware constraints. |
| [KSAUDIO_PACKETSIZE_CONSTRAINTS2 structure](ns-ksmedia--ksaudio-packetsize-constraints2.md) | The KSAUDIO_PACKETSIZE_CONSTRAINTS2 structure describes the physical hardware constraints. |
| [KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT structure](ns-ksmedia--ksaudio-packetsize-signalprocessingmode-constraint.md) | The KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT structure describes the constraints specific to any signal processing mode. |
| [KSCAMERA_EXTENDEDPROP_PROFILE structure](ns-ksmedia--kscamera-extendedprop-profile.md) | The payload of the KSPROPERTY_CAMERACONTROL_EXTENDED_PROFILE control contains KSCAMERA_EXTENDEDPROP_HEADER + KSCAMERA_EXTENDEDPROP_PROFILE. |
| [KSCAMERA_PROFILE_CONCURRENCYINFO structure](ns-ksmedia--kscamera-profile-concurrencyinfo.md) | An array of KSCAMERA_PROFILE_CONCURRENCYINFO structures form the Camera.Concurrency parameter of the KSDEVICE_PROFILE_INFO structure (whose array size is specified by Camera.CountOfConcurrency parameter) indicating which profiles the profile identified in the KSCAMERA_PROFILE_INFO structure may run simultaneously on different cameras. |
| [KSCAMERA_PROFILE_INFO structure](ns-ksmedia--kscamera-profile-info.md) | The KSCAMERA_PROFILE_INFO structure is used to uniquely identify a given profile. |
| [KSCAMERA_PROFILE_MEDIAINFO structure](ns-ksmedia--kscamera-profile-mediainfo.md) | This structure contains the relevant media type information presented for each camera profile. |
| [KSCAMERA_PROFILE_PININFO structure](ns-ksmedia--kscamera-profile-pininfo.md) | This structure specifies the available list of media types for each of the camera driver pins. |
| [KSDEVICE_PROFILE_INFO structure](ns-ksmedia--ksdevice-profile-info.md) | The KSDEVICE_PROFILE_INFO is a generic structure designed to handle profile information for various device types. |
| [KSMPEGVID_RECT structure](ns-ksmedia--ksmpegvid-rect.md) | KSMPEGVID_RECT structure |
| [KSPROPERTY_SPHLI structure](ns-ksmedia--ksproperty-sphli.md) | The KSPROPERTY_SPHLI structure is used to describe a rectangle of subpicture or screen whose color or contrast is to be changed. |
| [KSPROPERTY_SPPAL structure](ns-ksmedia--ksproperty-sppal.md) | The KSPROPERTY_SPPAL structure is used to describe the palette of a subpicture display. |
| [KS_COLCON structure](ns-ksmedia--ks-colcon.md) | The KS_COLCON structure is used to describe color and contrast settings. |
| [KS_COPY_MACROVISION structure](ns-ksmedia--ks-copy-macrovision.md) | The KS_COPY_MACROVISION structure specifies the Macrovision level of the data stream. |
| [KS_DVDCOPY_BUSKEY structure](ns-ksmedia--ks-dvdcopy-buskey.md) | The KS_DVDCOPY_BUSKEY structure is used to describe the bus key information for the DVD copyright protection authentication process. |
| [KS_DVDCOPY_CHLGKEY structure](ns-ksmedia--ks-dvdcopy-chlgkey.md) | The KS_DVDCOPY_CHLGKEY structure is used to describe the challenge key information for the DVD copyright protection authentication process. |
| [KS_DVDCOPY_DISCKEY structure](ns-ksmedia--ks-dvdcopy-disckey.md) | The KS_DVDCOPY_DISCKEY structure is used to describe the disc key information for the DVD copyright protection authentication process. |
| [KS_DVDCOPY_REGION structure](ns-ksmedia--ks-dvdcopy-region.md) | The KS_DVDCOPY_REGION structure is used to describe the copy control region according to language restrictions. |
| [KS_DVDCOPY_SET_COPY_STATE structure](ns-ksmedia--ks-dvdcopy-set-copy-state.md) | The KS_DVDCOPY_SET_COPY_STATE structure is used to specify the copyright protection state of the DVD decoder stream. |
| [KS_DVDCOPY_TITLEKEY structure](ns-ksmedia--ks-dvdcopy-titlekey.md) | The KS_DVDCOPY_TITLEKEY structure is used to describe the title key information for the DVD copyright protection authentication process. |
| [KS_DVD_YCrCb structure](ns-ksmedia--ks-dvd-ycrcb.md) | The KS_DVD_YCrCb structure is used to describe a color in the YCrCb colorspace. |
| [KS_DVD_YUV structure](ns-ksmedia--ks-dvd-yuv.md) | The KS_DVD_YUV structure is used to describe a color in the YUV colorspace. |
| [KS_VIDEO_STREAM_CONFIG_CAPS structure](ns-ksmedia--ks-video-stream-config-caps.md) | The KS_VIDEO_STREAM_CONFIG_CAPS structure describes the configuration and capabilities of a video stream, including analog video standard (for example, NTSC, PAL or SECAM), scaling, and cropping capabilities; minimum and maximum frame rates; and minimum and maximum data rates. |
| [PKSAC3_ALTERNATE_AUDIO structure](ns-ksmedia-pksac3-alternate-audio.md) | The KSAC3_ALTERNATE_AUDIO structure specifies whether the two mono channels in an AC-3-encoded stream should be interpreted as a stereo pair or as two independent program channels. |
| [PKSAC3_BIT_STREAM_MODE structure](ns-ksmedia-pksac3-bit-stream-mode.md) | The KSAC3_BIT_STREAM_MODE structure specifies the bit-stream mode, which is the type of audio service that is encoded into an AC-3 stream. |
| [PKSAC3_DIALOGUE_LEVEL structure](ns-ksmedia-pksac3-dialogue-level.md) | The KSAC3_DIALOGUE_LEVEL structure specifies the average volume level of spoken dialog within the audio program encoded in an AC-3 stream. |
| [PKSAC3_DOWNMIX structure](ns-ksmedia-pksac3-downmix.md) | The KSAC3_DOWNMIX structure specifies whether the program channels in an AC-3-encoded stream need to be downmixed to accommodate the speaker configuration. |
| [PKSAC3_ERROR_CONCEALMENT structure](ns-ksmedia-pksac3-error-concealment.md) | The KSAC3_ERROR_CONCEALMENT structure specifies how errors in an AC-3-encoded stream should be concealed during playback. |
| [PKSAC3_ROOM_TYPE structure](ns-ksmedia-pksac3-room-type.md) | The KSAC3_ROOM_TYPE structure specifies the type of audio mixing room in which an AC-3-encoded stream was produced. |
| [PKSAUDIO_CHANNEL_CONFIG structure](ns-ksmedia-pksaudio-channel-config.md) | The KSAUDIO_CHANNEL_CONFIG structure specifies the configuration of channels within the data format of an audio stream. |
| [PKSAUDIO_COPY_PROTECTION structure](ns-ksmedia-pksaudio-copy-protection.md) | The KSAUDIO_COPY_PROTECTION structure specifies the copy-protection status of an audio stream. |
| [PKSAUDIO_DYNAMIC_RANGE structure](ns-ksmedia-pksaudio-dynamic-range.md) | The KSAUDIO_DYNAMIC_RANGE structure specifies the dynamic range of an audio stream. This structure is used to get or set the data value for the KSPROPERTY_AUDIO_DYNAMIC_RANGE property. |
| [PKSAUDIO_MICROPHONE_COORDINATES structure](ns-ksmedia-pksaudio-microphone-coordinates.md) | The KSAUDIO_MICROPHONE_COORDINATES structure specifies the type and the coordinates of a single microphone in the microphone array. |
| [PKSAUDIO_MIC_ARRAY_GEOMETRY structure](ns-ksmedia-pksaudio-mic-array-geometry.md) | The KSAUDIO_MIC_ARRAY_GEOMETRY structure specifies the type and the geometry of the microphone array. |
| [PKSAUDIO_MIXCAP_TABLE structure](ns-ksmedia-pksaudio-mixcap-table.md) | The KSAUDIO_MIXCAP_TABLE structure specifies the mixing capabilities of a supermixer node (KSNODETYPE_SUPERMIX). This structure is used to get or set the data value for the KSPROPERTY_AUDIO_MIX_LEVEL_CAPS property. |
| [PKSAUDIO_MIXLEVEL structure](ns-ksmedia-pksaudio-mixlevel.md) | The KSAUDIO_MIXLEVEL structure specifies the mixing level of an input-output path in a supermixer node (KSNODETYPE_SUPERMIX). |
| [PKSAUDIO_MIX_CAPS structure](ns-ksmedia-pksaudio-mix-caps.md) | The KSAUDIO_MIX_CAPS structure specifies the mixing capabilities of a particular data path from one input channel of a supermixer node (KSNODETYPE_SUPERMIX) to an output channel of the same node. |
| [PKSAUDIO_POSITION structure](ns-ksmedia-pksaudio-position.md) | The KSAUDIO_POSITION structure specifies the current positions of the play and write cursors in the sound buffer for an audio stream. |
| [PKSAUDIO_POSITIONEX structure](ns-ksmedia-pksaudio-positionex.md) | The KSAUDIO_POSITIONEX structure specifies the stream position and the associated timestamp information for a kernel streaming (KS)-based audio driver. |
| [PKSAUDIO_PREFERRED_STATUS structure](ns-ksmedia-pksaudio-preferred-status.md) | The KSAUDIO_PREFERRED_STATUS structure specifies the status of a preferred device. |
| [PKSAUDIO_PRESENTATION_POSITION structure](ns-ksmedia-pksaudio-presentation-position.md) | The KSAUDIO_PRESENTATION_POSITION structure specifies the current cursor position in audio data stream that is being rendered to the endpoint. |
| [PKSCAMERA_PERFRAMESETTING_CAP_HEADER structure](ns-ksmedia-pkscamera-perframesetting-cap-header.md) | This structure contains the header information for the per frame settings capabilities. |
| [PKSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER structure](ns-ksmedia-pkscamera-perframesetting-cap-item-header.md) | This structure contains the header information for a per-frame settings item. |
| [PKSCAMERA_PERFRAMESETTING_CUSTOM_ITEM structure](ns-ksmedia-pkscamera-perframesetting-custom-item.md) | This structure contains a custom item. |
| [PKSCAMERA_PERFRAMESETTING_FRAME_HEADER structure](ns-ksmedia-pkscamera-perframesetting-frame-header.md) | This structure contains the header information for a frame in a per-frame settings payload. |
| [PKSCAMERA_PERFRAMESETTING_HEADER structure](ns-ksmedia-pkscamera-perframesetting-header.md) | This structure contains header information for the per-frame settings payload. |
| [PKSCAMERA_PERFRAMESETTING_ITEM_HEADER structure](ns-ksmedia-pkscamera-perframesetting-item-header.md) | This structure contains the header information for a per-frame settings item. |
| [PKSDATAFORMAT_DSOUND structure](ns-ksmedia-pksdataformat-dsound.md) | The KSDATAFORMAT_DSOUND structure provides detailed information about a DirectSound audio stream. |
| [PKSDATAFORMAT_WAVEFORMATEX structure](ns-ksmedia-pksdataformat-waveformatex.md) | The KSDATAFORMAT_WAVEFORMATEX structure provides detailed information about the data format of an audio stream consisting of wave data. |
| [PKSDATARANGE_AUDIO structure](ns-ksmedia-pksdatarange-audio.md) | The KSDATARANGE_AUDIO structure specifies a range of audio formats. |
| [PKSDATARANGE_MUSIC structure](ns-ksmedia-pksdatarange-music.md) | The KSDATARANGE_MUSIC structure specifies a range of DirectMusic MIDI formats. |
| [PKSDS3D_BUFFER_ALL structure](ns-ksmedia-pksds3d-buffer-all.md) | The KSDS3D_BUFFER_ALL structure specifies all the 3D characteristics of a DirectSound 3D buffer. |
| [PKSDS3D_BUFFER_CONE_ANGLES structure](ns-ksmedia-pksds3d-buffer-cone-angles.md) | A KSDS3D_BUFFER_CONE_ANGLES structure specifies the inside and outside cone angles. |
| [PKSDS3D_HRTF_FILTER_FORMAT_MSG structure](ns-ksmedia-pksds3d-hrtf-filter-format-msg.md) | The KSDS3D_HRTF_FILTER_FORMAT_MSG structure specifies the filter format to use for a head-relative transfer function (HRTF). |
| [PKSDS3D_HRTF_INIT_MSG structure](ns-ksmedia-pksds3d-hrtf-init-msg.md) | The KSDS3D_HRTF_INIT_MSG structure specifies the parameter settings to use to initialize the head-relative transfer function (HRTF). |
| [PKSDS3D_HRTF_PARAMS_MSG structure](ns-ksmedia-pksds3d-hrtf-params-msg.md) | The KSDS3D_HRTF_PARAMS_MSG structure specifies the parameter settings to apply to a head-relative transfer function (HRTF). |
| [PKSDS3D_ITD_PARAMS structure](ns-ksmedia-pksds3d-itd-params.md) | The KSDS3D_ITD_PARAMS structure specifies the parameters applied by the interaural time delay (ITD) algorithm to the left or right channel in a 3D node (KSNODETYPE_3D_EFFECTS). |
| [PKSDS3D_ITD_PARAMS_MSG structure](ns-ksmedia-pksds3d-itd-params-msg.md) | The KSDS3D_ITD_PARAMS_MSG structure specifies the parameters used by the interaural time delay (ITD) algorithm in a 3D node (KSNODETYPE_3D_EFFECTS). |
| [PKSDS3D_LISTENER_ALL structure](ns-ksmedia-pksds3d-listener-all.md) | The KSDS3D_LISTENER_ALL structure specifies all the properties of the DirectSound 3D listener. This structure is used to get or set the data value for the KSPROPERTY_DIRECTSOUND3DLISTENER_ALL property. |
| [PKSDS3D_LISTENER_ORIENTATION structure](ns-ksmedia-pksds3d-listener-orientation.md) | A KSD3D_LISTENER_ORIENTATION structure specifies the position vector of the 3D listener. This structure is used to get or set the data value for the KSPROPERTY_DIRECTSOUND3DLISTENER_ORIENTATION property. |
| [PKSDSOUND_BUFFERDESC structure](ns-ksmedia-pksdsound-bufferdesc.md) | The KSDSOUND_BUFFERDESC structure describes a DirectSound buffer. |
| [PKSEVENT_TUNER_INITIATE_SCAN_S structure](ns-ksmedia-pksevent-tuner-initiate-scan-s.md) | The KSEVENT_TUNER_INITIATE_SCAN_S structure is used in the KSEVENT_TUNER_INITIATE_SCAN event within the EVENTSETID_TUNER event set. |
| [PKSMUSICFORMAT structure](ns-ksmedia-pksmusicformat.md) | The KSMUSICFORMAT structure is used to send and receive information about MIDI data that is input from and output to WDM audio devices. |
| [PKSNODEPROPERTY structure](ns-ksmedia-pksnodeproperty.md) | The KSNODEPROPERTY structure specifies a node and a property of that node. |
| [PKSNODEPROPERTY_AUDIO_CHANNEL structure](ns-ksmedia-pksnodeproperty-audio-channel.md) | The KSNODEPROPERTY_AUDIO_CHANNEL structure specifies a property of a channel in a node. |
| [PKSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS_S structure](ns-ksmedia-pksproperty-allocator-control-capture-caps-s.md) | The KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS_S structure specifies if interleaved capture is supported. |
| [PKSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE_S structure](ns-ksmedia-pksproperty-allocator-control-capture-interleave-s.md) | The KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE_S structure specifies if interleaved capture is possible. |
| [PKSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE_S structure](ns-ksmedia-pksproperty-allocator-control-surface-size-s.md) | The KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE_S structure specifies the width and height of an overlay surface. |
| [PKSPROPERTY_CAMERACONTROL_FLASH_S structure](ns-ksmedia-pksproperty-cameracontrol-flash-s.md) | Describes flash control properties in the PROPSETID_VIDCAP_CAMERACONTROL_FLASH camera control property set. This structure specifies property values that are used by applications to configure the camera's flash. |
| [PKSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S structure](ns-ksmedia-pksproperty-cameracontrol-focal-length-s.md) | The KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S structure returns filter-specific data requested using the KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH property. |
| [PKSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_S structure](ns-ksmedia-pksproperty-cameracontrol-image-pin-capability-s.md) | Describes image pin control properties in the PROPSETID_VIDCAP_CAMERACONTROL_IMAGE_PIN_CAPABILITY camera control property set. |
| [PKSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S structure](ns-ksmedia-pksproperty-cameracontrol-node-focal-length-s.md) | The KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S structure returns node-specific data requested using the KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH property. |
| [PKSPROPERTY_CAMERACONTROL_NODE_S structure](ns-ksmedia-pksproperty-cameracontrol-node-s.md) | The KSPROPERTY_CAMERACONTROL_NODE_S structure describes node-based properties in the PROPSETID_VIDCAP_CAMERACONTROL property set. This structure specifies property values in requests to the USB Video Class driver. |
| [PKSPROPERTY_CAMERACONTROL_NODE_S2 structure](ns-ksmedia-pksproperty-cameracontrol-node-s2.md) | The KSPROPERTY_CAMERACONTROL_NODE_S2 structure describes node-based properties in the PROPSETID_VIDCAP_CAMERACONTROL property set that use two values at the same time. This structure specifies property values in requests to the USB video class driver. |
| [PKSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S structure](ns-ksmedia-pksproperty-cameracontrol-region-of-interest-s.md) | Describes region of interest (ROI) control properties in the PROPSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST camera control property set. |
| [PKSPROPERTY_CAMERACONTROL_S structure](ns-ksmedia-pksproperty-cameracontrol-s.md) | The KSPROPERTY_CAMERACONTROL_S structure describes filter-based properties in the PROPSETID_VIDCAP_CAMERACONTROL property set. |
| [PKSPROPERTY_CAMERACONTROL_S2 structure](ns-ksmedia-pksproperty-cameracontrol-s2.md) | The KSPROPERTY_CAMERACONTROL_S2 structure describes filter-based properties in the PROPSETID_VIDCAP_CAMERACONTROL property set that use two values at the same time. |
| [PKSPROPERTY_CAMERACONTROL_S_EX structure](ns-ksmedia-pksproperty-cameracontrol-s-ex.md) | Specifies a camera control operation, including setting the flash, the image pin control properties, the region of interest in the image, or video stabilization. |
| [PKSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S structure](ns-ksmedia-pksproperty-cameracontrol-videostabilization-mode-s.md) | Describes video stabilization control properties in the PROPSETID_VIDCAP_CAMERACONTROL_VIDEO_STABILIZATION camera control property set. This structure specifies property values that are used in requests to the camera driver. |
| [PKSPROPERTY_CROSSBAR_CAPS_S structure](ns-ksmedia-pksproperty-crossbar-caps-s.md) | The KSPROPERTY_CROSSBAR_CAPS_S structure describes the crossbar capabilities for a device. |
| [PKSPROPERTY_CROSSBAR_PININFO_S structure](ns-ksmedia-pksproperty-crossbar-pininfo-s.md) | The KSPROPERTY_CROSSBAR_PININFO_S structure describes the crossbar pin information for a device. |
| [PKSPROPERTY_CROSSBAR_ROUTE_S structure](ns-ksmedia-pksproperty-crossbar-route-s.md) | The KSPROPERTY_CROSSBAR_ROUTE_S structure describes whether a particular routing is possible and specifies the current routing for a pin. |
| [PKSPROPERTY_DROPPEDFRAMES_CURRENT_S structure](ns-ksmedia-pksproperty-droppedframes-current-s.md) | The KSPROPERTY_DROPPEDFRAMES_CURRENT_S structure describes the dropped frame information from the minidriver. |
| [PKSPROPERTY_EXTDEVICE_S structure](ns-ksmedia-pksproperty-extdevice-s.md) | The KSPROPERTY_EXTDEVICE_S structure describes an external device and its capabilities. |
| [PKSPROPERTY_EXTXPORT_NODE_S structure](ns-ksmedia-pksproperty-extxport-node-s.md) | The KSPROPERTY_EXTXPORT_NODE_S structure describes an external transport and its capabilities. |
| [PKSPROPERTY_EXTXPORT_S structure](ns-ksmedia-pksproperty-extxport-s.md) | The KSPROPERTY_EXTXPORT_S structure describes an external transport and its capabilities. |
| [PKSPROPERTY_SELECTOR_NODE_S structure](ns-ksmedia-pksproperty-selector-node-s.md) | The KSPROPERTY_SELECTOR_NODE_S structure describes node-based property settings in the PROPSETID_VIDCAP_SELECTOR property set. |
| [PKSPROPERTY_SELECTOR_S structure](ns-ksmedia-pksproperty-selector-s.md) | The KSPROPERTY_SELECTOR_S structure describes filter-based property settings in the PROPSETID_VIDCAP_SELECTOR property set. |
| [PKSPROPERTY_TIMECODE_NODE_S structure](ns-ksmedia-pksproperty-timecode-node-s.md) | The KSPROPERTY_TIMECODE_NODE_S structure describes a timecode. |
| [PKSPROPERTY_TIMECODE_S structure](ns-ksmedia-pksproperty-timecode-s.md) | The KSPROPERTY_TIMECODE_S structure describes a timecode. |
| [PKSPROPERTY_TUNER_CAPS_S structure](ns-ksmedia-pksproperty-tuner-caps-s.md) | The KSPROPERTY_TUNER_CAPS_S structure describes the hardware capabilities of TV and radio tuning devices. |
| [PKSPROPERTY_TUNER_FREQUENCY_S structure](ns-ksmedia-pksproperty-tuner-frequency-s.md) | The KSPROPERTY_TUNER_FREQUENCY_S structure describes the frequency of a TV or radio tuner device. |
| [PKSPROPERTY_TUNER_IF_MEDIUM_S structure](ns-ksmedia-pksproperty-tuner-if-medium-s.md) | The KSPROPERTY_TUNER_IF_MEDIUM_S structure returns the Medium GUID for the pin that is capable of supporting tuning to an intermediate frequency. |
| [PKSPROPERTY_TUNER_INPUT_S structure](ns-ksmedia-pksproperty-tuner-input-s.md) | The KSPROPERTY_TUNER_INPUT_S structure describes the input connection index of a tuner device for devices that support multiple inputs. |
| [PKSPROPERTY_TUNER_MODE_CAPS_S structure](ns-ksmedia-pksproperty-tuner-mode-caps-s.md) | The KS_PROPERTY_TUNER_MODE_CAPS_S structure describes the capabilities of TV and radio tuner devices. |
| [PKSPROPERTY_TUNER_MODE_S structure](ns-ksmedia-pksproperty-tuner-mode-s.md) | The KSPROPERTY_TUNER_MODE_S structure describes the mode of a TV or radio tuner device. |
| [PKSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S structure](ns-ksmedia-pksproperty-tuner-networktype-scan-caps-s.md) | The KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S structure describes the scanning capabilities of a broadcast network type that a tuning device supports. |
| [PKSPROPERTY_TUNER_SCAN_CAPS_S structure](ns-ksmedia-pksproperty-tuner-scan-caps-s.md) | The KSPROPERTY_TUNER_SCAN_CAPS_S structure describes the hardware scanning capabilities of a tuning device. |
| [PKSPROPERTY_TUNER_SCAN_STATUS_S structure](ns-ksmedia-pksproperty-tuner-scan-status-s.md) | The KSPROPERTY_TUNER_SCAN_STATUS_S structure describes status for a scanning operation. |
| [PKSPROPERTY_TUNER_STANDARD_MODE_S structure](ns-ksmedia-pksproperty-tuner-standard-mode-s.md) | The KSPROPERTY_TUNER_STANDARD_MODE_S structure describes whether the tuning device can identify the tuner standard from the signal itself. |
| [PKSPROPERTY_TUNER_STANDARD_S structure](ns-ksmedia-pksproperty-tuner-standard-s.md) | The KSPROPERTY_TUNER_STANDARD_S structure describe the standard of a TV tuner device, such as PAL, NTSC or SECAM. |
| [PKSPROPERTY_TUNER_STATUS_S structure](ns-ksmedia-pksproperty-tuner-status-s.md) | The KSPROPERTY_TUNER_STATUS_S structure describes the progress of a tuning operation for TV and radio tuner devices, including present tuning frequency. |
| [PKSPROPERTY_TVAUDIO_CAPS_S structure](ns-ksmedia-pksproperty-tvaudio-caps-s.md) | The KSPROPERTY_TVAUDIO_CAPS_S structure describes the capability of a TV audio device, such as stereo versus mono audio support and language capabilities. |
| [PKSPROPERTY_TVAUDIO_S structure](ns-ksmedia-pksproperty-tvaudio-s.md) | The KSPROPERTY_TVAUDIO_S structure describes the current TV audio mode, such as stereo or mono audio and language settings. |
| [PKSPROPERTY_VIDEOCOMPRESSION_GETINFO_S structure](ns-ksmedia-pksproperty-videocompression-getinfo-s.md) | The KSPROPERTY_VIDEOCOMPRESSION_GETINFO_S structure describes information about the video compression capabilities supported by a device. |
| [PKSPROPERTY_VIDEOCOMPRESSION_S structure](ns-ksmedia-pksproperty-videocompression-s.md) | The KSPROPERTY_VIDEOCOMPRESSION_S structure describes a single KSPROPERTY_VIDEOCOMPRESSION_Xxx property of a specified stream. |
| [PKSPROPERTY_VIDEOCONTROL_ACTUAL_FRAME_RATE_S structure](ns-ksmedia-pksproperty-videocontrol-actual-frame-rate-s.md) | The KSPROPERTY_VIDEOCONTROL_ACTUAL_FRAME_RATE_S structure describes actual frame rate information in response to KSPROPERTY_VIDEOCONTROL_ACTUAL_FRAME_RATE property requests. |
| [PKSPROPERTY_VIDEOCONTROL_CAPS_S structure](ns-ksmedia-pksproperty-videocontrol-caps-s.md) | The KSPROPERTY_VIDEOCONTROL_CAPS_S structure describes the video-control capabilities of a minidriver, such as image flipping or event triggering abilities. |
| [PKSPROPERTY_VIDEOCONTROL_FRAME_RATES_S structure](ns-ksmedia-pksproperty-videocontrol-frame-rates-s.md) | The KSPROPERTY_VIDEOCONTROL_FRAME_RATES structure describes available frame rates in 100-nanosecond units. |
| [PKSPROPERTY_VIDEOCONTROL_MODE_S structure](ns-ksmedia-pksproperty-videocontrol-mode-s.md) | The KSPROPERTY_VIDEOCONTROL_MODE_S structure describes video-control modes for a stream, such as image flipping or event triggering abilities. |
| [PKSPROPERTY_VIDEODECODER_CAPS_S structure](ns-ksmedia-pksproperty-videodecoder-caps-s.md) | The KSPROPERTY_VIDEODECODER_CAPS_S structure describes the hardware capabilities of the video decoder device. |
| [PKSPROPERTY_VIDEODECODER_S structure](ns-ksmedia-pksproperty-videodecoder-s.md) | The KSPROPERTY_VIDEODECODER_S structure describes property settings in the PROPSETID_VIDCAP_VIDEODECODER property set. |
| [PKSPROPERTY_VIDEODECODER_STATUS_S structure](ns-ksmedia-pksproperty-videodecoder-status-s.md) | The KSPROPERTY_VIDEODECODER_STATUS_S structure describes the present status of a video decoding device, such as number of lines in the incoming analog signal and whether the signal is locked in. |
| [PKSPROPERTY_VIDEOPROCAMP_NODE_S structure](ns-ksmedia-pksproperty-videoprocamp-node-s.md) | The KSPROPERTY_VIDEOPROCAMP_NODE_S structure describes node-based property settings in the PROPSETID_VIDCAP_VIDEOPROCAMP property set. |
| [PKSPROPERTY_VIDEOPROCAMP_NODE_S2 structure](ns-ksmedia-pksproperty-videoprocamp-node-s2.md) | The KSPROPERTY_VIDEOPROCAMP_NODE_S2 structure describes node-based property settings in the PROPSETID_VIDCAP_VIDEOPROCAMP property set that use two values at the same time. |
| [PKSPROPERTY_VIDEOPROCAMP_S structure](ns-ksmedia-pksproperty-videoprocamp-s.md) | The KSPROPERTY_VIDEOPROCAMP_S structure describes filter-based property settings in the PROPSETID_VIDCAP_VIDEOPROCAMP property set. |
| [PKSRTAUDIO_BUFFER structure](ns-ksmedia-pksrtaudio-buffer.md) | The KSRTAUDIO_BUFFER structure specifies the buffer address, size, and a call memory barrier flag for a cyclic audio data buffer. |
| [PKSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION structure](ns-ksmedia-pksrtaudio-buffer-property-with-notification.md) | The KSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION structure appends a buffer base address, a requested buffer size, and a notification count to a KSPROPERTY structure. |
| [PKSRTAUDIO_GETREADPACKET_INFO structure](ns-ksmedia-pksrtaudio-getreadpacket-info.md) | The KSRTAUDIO_GETREADPACKET_INFO structure describes information for an audio packet. |
| [PKSRTAUDIO_HWLATENCY structure](ns-ksmedia-pksrtaudio-hwlatency.md) | The KSRTAUDIO_HWLATENCY structure describes the latency that the audio hardware adds to a wave stream during playback or recording. |
| [PKSRTAUDIO_HWREGISTER structure](ns-ksmedia-pksrtaudio-hwregister.md) | The KSRTAUDIO_HWREGISTER structure specifies the address and additional information about a hardware register requested by the client. |
| [PKSRTAUDIO_HWREGISTER_PROPERTY structure](ns-ksmedia-pksrtaudio-hwregister-property.md) | The KSRTAUDIO_HWREGISTRY_PROPERTY structure appends a register base address to a KSPROPERTY structure. |
| [PKSRTAUDIO_NOTIFICATION_EVENT_PROPERTY structure](ns-ksmedia-pksrtaudio-notification-event-property.md) | The KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY structure appends an event handle to a KSPROPERTY structure |
| [PKSRTAUDIO_SETWRITEPACKET_INFO structure](ns-ksmedia-pksrtaudio-setwritepacket-info.md) | The KSRTAUDIO_SETWRITEPACKET_INFO structure describes information associated with an audio packet. |
| [PKSVPMAXPIXELRATE structure](ns-ksmedia-pksvpmaxpixelrate.md) | The KSVPMAXPIXELRATE structure is used to describe the maximum pixel rate of a video port. |
| [PKSVPMAXPIXELRATE structure](ns-ksmedia-pksvpmaxpixelrate~r1.md) | The KSVPMAXPIXELRATE structure is used to describe the maximum pixel rate of a video port. |
| [PKSVPSURFACEPARAMS structure](ns-ksmedia-pksvpsurfaceparams.md) | The KSVPSURFACEPARAMS structure is used to describe the surface parameters of a video port surface. |
| [PKSVPSURFACEPARAMS structure](ns-ksmedia-pksvpsurfaceparams~r1.md) | The KSVPSURFACEPARAMS structure is used to describe the surface parameters of a video port surface. |
| [PKSWAVE_BUFFER structure](ns-ksmedia-pkswave-buffer.md) | The KSWAVE_BUFFER structure is used to describe a sample buffer. |
| [PKSWAVE_COMPATCAPS structure](ns-ksmedia-pkswave-compatcaps.md) | The KSWAVE_COMPATCAPS structure is used to describe the compatible capabilities of a device. |
| [PKSWAVE_INPUT_CAPABILITIES structure](ns-ksmedia-pkswave-input-capabilities.md) | The KSWAVE_INPUT_CAPABILITIES structure is used to describe the input capabilities of a device. |
| [PKSWAVE_OUTPUT_CAPABILITIES structure](ns-ksmedia-pkswave-output-capabilities.md) | The KSWAVE_OUTPUT_CAPABILITIES structure is used to describe the output capabilities of a device. |
| [PKSWAVE_VOLUME structure](ns-ksmedia-pkswave-volume.md) | The KSWAVE_VOLUME structure is used to describe sample volume. |
| [PKS_AM_ExactRateChange structure](ns-ksmedia-pks-am-exactratechange.md) | The KS_AM_ExactRateChange structure is not yet implemented. |
| [PKS_AM_SimpleRateChange structure](ns-ksmedia-pks-am-simpleratechange.md) | The KS_AM_SimpleRateChange structure is used to describe a simple rate change (fast-forward or rewind) for an MPEG2 stream. |
| [PLOOPEDSTREAMING_POSITION_EVENT_DATA structure](ns-ksmedia-ploopedstreaming-position-event-data.md) | The LOOPEDSTREAMING_POSITION_EVENT_DATA structure describes a position event in a looped buffer. |
| [PMEDIUM_INFO structure](ns-ksmedia-pmedium-info.md) | The MEDIUM_INFO structure describes the media loaded into an external device. |
| [PSYSAUDIO_ATTACH_VIRTUAL_SOURCE structure](ns-ksmedia-psysaudio-attach-virtual-source.md) | The SYSAUDIO_ATTACH_VIRTUAL_SOURCE structure is used to attach a mixer-line virtual source (for example, a volume or mute control) to a mixer pin on the virtual audio device. |
| [PSYSAUDIO_CREATE_VIRTUAL_SOURCE structure](ns-ksmedia-psysaudio-create-virtual-source.md) | The SYSAUDIO_CREATE_VIRTUAL_SOURCE structure is used to create a mixer-line virtual source such as a volume control or mute. |
| [PSYSAUDIO_INSTANCE_INFO structure](ns-ksmedia-psysaudio-instance-info.md) | The SYSAUDIO_INSTANCE_INFO structure specifies which virtual audio device to open and includes flags for configuring that device. |
| [PSYSAUDIO_SELECT_GRAPH structure](ns-ksmedia-psysaudio-select-graph.md) | The SYSAUDIO_SELECT_GRAPH structure is used to specify a graph that includes an optional node such as an AEC control. |
| [PTRANSPORT_STATE structure](ns-ksmedia-ptransport-state.md) | The TRANSPORT_STATE structure |
| [PTUNER_ANALOG_CAPS_S structure](ns-ksmedia-ptuner-analog-caps-s.md) | The TUNER_ANALOG_CAPS_S structure describes the hardware scanning capabilities of a tuning device that supports an analog broadcast network. |
| [PVRAM_SURFACE_INFO structure](ns-ksmedia-pvram-surface-info.md) | The VRAM_SURFACE_INFO structure describes a region of system or display memory into which an AVStream minidriver captures audio or video data. |
| [PVRAM_SURFACE_INFO_PROPERTY_S structure](ns-ksmedia-pvram-surface-info-property-s.md) | The VRAM_SURFACE_INFO_PROPERTY_S structure describes property items in the KSPROPSETID_VramCapture property set. |
| [PWAVEFORMATEXTENSIBLE structure](ns-ksmedia-pwaveformatextensible.md) | The WAVEFORMATEXTENSIBLE structure specifies the format of an audio wave stream. |
| [SOUNDDETECTOR_PATTERNHEADER structure](ns-ksmedia-sounddetector-patternheader.md) | The SOUNDDETECTOR_PATTERNHEADER structure specifies the pattern header for the sound detector in the KSPROPERTY_SOUNDDETECTOR_PATTERNS property. |
| [tagDEVCAPS structure](ns-ksmedia-tagdevcaps.md) | The DEVCAPS structure describes the capabilities of an external device. |
| [tagKSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE structure](ns-ksmedia-tagksattribute-audiosignalprocessing-mode.md) | The KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE structure specifies an audio signal processing mode. |
| [tagKSAUDIOENGINE_BUFFER_SIZE_RANGE structure](ns-ksmedia--tagksaudioengine-buffer-size-range.md) | The KSAUDIOENGINE_BUFFER_SIZE_RANGE structure specifies the minimum and maximum buffer size that the hardware audio engine can support at the instance when it is called. |
| [tagKSAUDIOENGINE_DESCRIPTOR structure](ns-ksmedia--tagksaudioengine-descriptor.md) | The KSAUDIOENGINE_DESCRIPTOR structure describes the static, external properties of the audio engine. |
| [tagKSAUDIOENGINE_VOLUMELEVEL structure](ns-ksmedia--tagksaudioengine-volumelevel.md) | The KSAUDIOENGINE_VOLUMELEVEL structure specifies the target volume level, ramp type, and duration within which the volume level should change, for a given volume level request via the KSPROPERTY_AUDIOENGINE_VOLUMELEVEL property. |
| [tagKSCAMERA_EXTENDEDPROP_CAMERAOFFSET structure](ns-ksmedia-tagkscamera-extendedprop-cameraoffset.md) | The KSCAMERA_EXTENDEDPROP_CAMERAOFFSET structure contains the parameters for the Camera Angle Offset Control property. |
| [tagKSCAMERA_EXTENDEDPROP_EVCOMPENSATION structure](ns-ksmedia-tagkscamera-extendedprop-evcompensation.md) | The EV Compensation Control provides for exposure control that is adjusted by increments of EV compensation steps. |
| [tagKSCAMERA_EXTENDEDPROP_FIELDOFVIEW structure](ns-ksmedia-tagkscamera-extendedprop-fieldofview.md) | The Field of View Control property describes the current Field of View (FOV) of the camera along with the pitch angle of the camera position. |
| [tagKSCAMERA_EXTENDEDPROP_HEADER structure](ns-ksmedia-tagkscamera-extendedprop-header.md) | The KSCAMERA_EXTENDEDPROP_HEADER structure is the payload header for an extend control property. |
| [tagKSCAMERA_EXTENDEDPROP_METADATAINFO structure](ns-ksmedia-tagkscamera-extendedprop-metadatainfo.md) | This structure represents the metadata information for the extended property control. |
| [tagKSCAMERA_EXTENDEDPROP_PHOTOMODE structure](ns-ksmedia-tagkscamera-extendedprop-photomode.md) | The KSCAMERA_EXTENDEDPROP_PHOTOMODE structure contains the property data for the history frame counts in photo mode. |
| [tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS structure](ns-ksmedia-tagkscamera-extendedprop-roi-configcaps.md) | This structure contains the capabilities for an ROI control. |
| [tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER structure](ns-ksmedia-tagkscamera-extendedprop-roi-configcapsheader.md) | This structure contains the header information for ROI capabilities. |
| [tagKSCAMERA_EXTENDEDPROP_ROI_EXPOSURE structure](ns-ksmedia-tagkscamera-extendedprop-roi-exposure.md) | This structure contains the ROI info structure for exposure. |
| [tagKSCAMERA_EXTENDEDPROP_ROI_FOCUS structure](ns-ksmedia-tagkscamera-extendedprop-roi-focus.md) | This structure contains the ROI info structure for focus. |
| [tagKSCAMERA_EXTENDEDPROP_ROI_INFO structure](ns-ksmedia-tagkscamera-extendedprop-roi-info.md) | This structure contains information about an ROI. |
| [tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL structure](ns-ksmedia-tagkscamera-extendedprop-roi-ispcontrol.md) | This structure contains information for an ROI ISP control. |
| [tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER structure](ns-ksmedia-tagkscamera-extendedprop-roi-ispcontrolheader.md) | This structure contains the header information for ROI ISP controls. |
| [tagKSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE structure](ns-ksmedia-tagkscamera-extendedprop-roi-whitebalance.md) | This structure contains the ROI info structure for white balance. |
| [tagKSCAMERA_EXTENDEDPROP_VALUE structure](ns-ksmedia-tagkscamera-extendedprop-value.md) | The KSCAMERA_EXTENDEDPROP_VALUE structure is a data type union used to express an extended property value. |
| [tagKSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING structure](ns-ksmedia-tagkscamera-extendedprop-videoprocsetting.md) | The KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING is a property payload structure for video processing settings related to white balance, exposure mode, and focus mode. |
| [tagKSCAMERA_MAXVIDEOFPS_FORPHOTORES structure](ns-ksmedia-tagkscamera-maxvideofps-forphotores.md) | The KSCAMERA_MAXVIDEOFPS_FORPHOTORES structure contains the property data for maximum frame rate at a particular resolution for a camera supporting preview and capture. |
| [tagKSCAMERA_METADATA_ITEMHEADER structure](ns-ksmedia-tagkscamera-metadata-itemheader.md) | This structure contains the metadata header information that is filled by the camera driver. |
| [tagKSCAMERA_METADATA_PHOTOCONFIRMATION structure](ns-ksmedia-tagkscamera-metadata-photoconfirmation.md) | This structure contains the photo confirmation metadata information that is filled by the camera driver. |
| [tagKSJACK_SINK_INFORMATION structure](ns-ksmedia--tagksjack-sink-information.md) | The KSJACK_SINK_INFORMATION structure specifies information about a display-related digital audio device, such as an HDMI device or a display port. |
| [tagKSTELEPHONY_CALLCONTROL structure](ns-ksmedia--tagkstelephony-callcontrol.md) | The KSTELEPHONY_CALLCONTROL structure specifies the phone call type and control operation to use for the KSPROPERTY_TELEPHONY_CALLCONTROL property. |
| [tagKSTELEPHONY_CALLINFO structure](ns-ksmedia--tagkstelephony-callinfo.md) | The KSTELEPHONY_CALLINFO structure specifies the type and state of a phone call for the KSPROPERTY_TELEPHONY_CALLINFO property. |
| [tagKSTELEPHONY_PROVIDERCHANGE structure](ns-ksmedia--tagkstelephony-providerchange.md) | The KSTELEPHONY_PROVIDERCHANGE structure specifies the phone call type and provider change operation to use for the KSPROPERTY_TELEPHONY_PROVIDERCHANGE property. |
| [tagKSTOPOLOGY_ENDPOINTID structure](ns-ksmedia--tagkstopology-endpointid.md) | The KSTOPOLOGY_ENDPOINTID structure specifies the name and the pin ID of a topology endpoint. |
| [tagKSTOPOLOGY_ENDPOINTIDPAIR structure](ns-ksmedia--tagkstopology-endpointidpair.md) | The KSTOPOLOGY_ENDPOINTIDPAIR structure specifies the render and capture endpoint IDs to use for the KSPROPERTY_TELEPHONY_ENDPOINTIDPAIR property. |
| [tagKS_AMVPDATAINFO structure](ns-ksmedia-tagks-amvpdatainfo.md) | The KS_AMVPDATAINFO structure is used to describe the properties of a video port. |
| [tagKS_AMVPDIMINFO structure](ns-ksmedia-tagks-amvpdiminfo.md) | The KS_AMVPDIMINFO structure is used to describe the dimensions of a video port. |
| [tagKS_AMVPSIZE structure](ns-ksmedia-tagks-amvpsize.md) | The KS_AMVPSIZE structure is used to describe the dimension of a video port (width by height). |
| [tagKS_AnalogVideoInfo structure](ns-ksmedia-tagks-analogvideoinfo.md) | The KS_ANALOGVIDEOINFO structure describes an analog video stream. |
| [tagKS_BITMAPINFOHEADER structure](ns-ksmedia-tagks-bitmapinfoheader.md) | The KS_BITMAPINFOHEADER structure describes details about the video stream, such as image dimensions and pixel depth. |
| [tagKS_DATAFORMAT_H264VIDEOINFO structure](ns-ksmedia-tagks-dataformat-h264videoinfo.md) | The KS_DATAFORMAT_H264VIDEOINFO structure describes the data formats range available for a stream. |
| [tagKS_DATAFORMAT_IMAGEINFO structure](ns-ksmedia-tagks-dataformat-imageinfo.md) | Specifies an image data format that is used for an independent image pin (or stream). |
| [tagKS_DATAFORMAT_VBIINFOHEADER structure](ns-ksmedia-tagks-dataformat-vbiinfoheader.md) | The KS_DATAFORMAT_VBIINFOHEADER structure describes a vertical blanking interval (VBI) stream. |
| [tagKS_DATAFORMAT_VIDEOINFOHEADER structure](ns-ksmedia-tagks-dataformat-videoinfoheader.md) | The KS_DATAFORMAT_VIDEOINFOHEADER structure describes a video stream that does not include bob or weave settings. |
| [tagKS_DATAFORMAT_VIDEOINFOHEADER2 structure](ns-ksmedia-tagks-dataformat-videoinfoheader2.md) | The KS_DATAFORMAT_VIDEOINFOHEADER2 structure describes a video stream that includes settings for bob or weave. |
| [tagKS_DATAFORMAT_VIDEOINFO_PALETTE structure](ns-ksmedia-tagks-dataformat-videoinfo-palette.md) | The KS_DATAFORMAT_VIDEOINFO_PALETTE structure describes color palette information. |
| [tagKS_DATARANGE_ANALOGVIDEO structure](ns-ksmedia-tagks-datarange-analogvideo.md) | The KS_DATARANGE_ANALOGVIDEO structure describes an analog video stream. |
| [tagKS_DATARANGE_H264_VIDEO structure](ns-ksmedia-tagks-datarange-h264-video.md) | The KS_DATARANGE_H264_VIDEO structure describes the range of MPEG-2 video formats available for a stream. |
| [tagKS_DATARANGE_IMAGE structure](ns-ksmedia-tagks-datarange-image.md) | Specifies an image data range that is used in the KSPIN_DESCRIPTOR structure that describes a pin (or stream). |
| [tagKS_DATARANGE_MPEG1_VIDEO structure](ns-ksmedia-tagks-datarange-mpeg1-video.md) | The KS_DATARANGE_MPEG1_VIDEO structure describes the range of MPEG-1 video formats available for a stream. |
| [tagKS_DATARANGE_MPEG2_VIDEO structure](ns-ksmedia-tagks-datarange-mpeg2-video.md) | The KS_DATARANGE_MPEG2_VIDEO structure describes the range of MPEG-2 video formats available for a stream. |
| [tagKS_DATARANGE_VIDEO structure](ns-ksmedia-tagks-datarange-video.md) | The KS_DATARANGE_VIDEO structure describes a range of video streams without bob or weave settings. |
| [tagKS_DATARANGE_VIDEO2 structure](ns-ksmedia-tagks-datarange-video2.md) | The KS_DATARANGE_VIDEO2 structure describes a video stream including bob or weave settings. |
| [tagKS_DATARANGE_VIDEO_PALETTE structure](ns-ksmedia-tagks-datarange-video-palette.md) | The KS_DATARANGE_VIDEO_PALETTE structure describes a stream and its color capabilities. |
| [tagKS_DATARANGE_VIDEO_VBI structure](ns-ksmedia-tagks-datarange-video-vbi.md) | The KS_DATARANGE_VIDEO_VBI structure describes a range of data formats containing vertical blanking interval (VBI) data. |
| [tagKS_FRAME_INFO structure](ns-ksmedia-tagks-frame-info.md) | The KS_FRAME_INFO structure extends the KSSTREAM_HEADER structure for video streams. |
| [tagKS_H264VIDEOINFO structure](ns-ksmedia-tagks-h264videoinfo.md) | The KS_H264VIDEOINFO describes the device capabilities that apply to the current media type. |
| [tagKS_MPEAUDIOINFO structure](ns-ksmedia-tagks-mpeaudioinfo.md) | The KS_MPEGAUDIOINFO structure describes an MPEG audio stream. |
| [tagKS_MPEG1VIDEOINFO structure](ns-ksmedia-tagks-mpeg1videoinfo.md) | The KS_MPEG1VIDEOINFO structure describes an MPEG-1 video stream. |
| [tagKS_MPEGVIDEOINFO2 structure](ns-ksmedia-tagks-mpegvideoinfo2.md) | The KS_MPEGVIDEOINFO2 structure describes an MPEG-2 video stream, including bob or weave settings. |
| [tagKS_RGBQUAD structure](ns-ksmedia-tagks-rgbquad.md) | The KS_RGBQUAD structure describes a color consisting of relative intensities of red, green, and blue, ranging from 0 to 255 (0x0 to 0xff). |
| [tagKS_TVTUNER_CHANGE_INFO structure](ns-ksmedia-tagks-tvtuner-change-info.md) | The KS_TVTUNER_CHANGE_INFO structure provides vertical blanking interval (VBI) codecs with information about the currently tuned channel. |
| [tagKS_VBIINFOHEADER structure](ns-ksmedia-tagks-vbiinfoheader.md) | The KS_VBIINFOHEADER structure describes raw vertical blanking interval (VBI) streams. |
| [tagKS_VBI_FRAME_INFO structure](ns-ksmedia-tagks-vbi-frame-info.md) | The KS_VBI_FRAME_INFO structure extends the KSSTREAM_HEADER structure for vertical blanking interval (VBI) streams. |
| [tagKS_VIDEOINFO structure](ns-ksmedia-tagks-videoinfo.md) | The KS_VIDEOINFO structure describes the bitmap and color information for a video stream. |
| [tagKS_VIDEOINFOHEADER structure](ns-ksmedia-tagks-videoinfoheader.md) | The KS_VIDEOINFOHEADER structure describes the bitmap and color information for a video stream. |
| [tagKS_VIDEOINFOHEADER2 structure](ns-ksmedia-tagks-videoinfoheader2.md) | The KS_VIDEOINFOHEADER2 structure describes the details of a video stream, including bob or weave settings, copy protection, and pixel aspect ratio. |
| [tagTIMECODE_SAMPLE structure](ns-ksmedia-tagtimecode-sample.md) | The TIMECODE_SAMPLE structure describes a complete timecode. |
| [tagTRANSPORTAUDIOPARMS structure](ns-ksmedia-tagtransportaudioparms.md) | The TRANSPORTAUDIOPARMS structure is defined but not used. |
| [tagTRANSPORTBASICPARMS structure](ns-ksmedia-tagtransportbasicparms.md) | The TRANSPORTBASICPARMS structure is defined but not used. |
| [tagTRANSPORTSTATUS structure](ns-ksmedia-tagtransportstatus.md) | The TRANSPORTSTATUS structure describes the current transport status. |
| [tagTRANSPORTVIDEOPARMS structure](ns-ksmedia-tagtransportvideoparms.md) | The TRANSPORTVIDEOPARMS structure is defined but not presently used. It may be used in the future. |
| [tag_KS_TRUECOLORINFO structure](ns-ksmedia-tag-ks-truecolorinfo.md) | The KS_TRUECOLORINFO structure describes color palette and bitmask information for video images that also contain a palette. |
| [timecode structure](ns-ksmedia--timecode.md) | The TIMECODE union describes a timecode from an external device. This structure is no longer used. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [AUDIO_CURVE_TYPE enumeration](ne-ksmedia-audio-curve-type.md) | The AUDIO_CURVE_TYPE enumeration defines constants that specify a curve algorithm to be applied to set a volume level. |
| [KSCAMERA_EXTENDEDPROP_FOCUSSTATE enumeration](ne-ksmedia-kscamera-extendedprop-focusstate.md) | This enumeration contains the focus states. |
| [KSCAMERA_EXTENDEDPROP_MetadataAlignment enumeration](ne-ksmedia-kscamera-extendedprop-metadataalignment.md) | This enumeration contains identifiers for the metadata alignment. |
| [KSCAMERA_EXTENDEDPROP_ROITYPE enumeration](ne-ksmedia-kscamera-extendedprop-roitype.md) | This enumeration contains the ROI types. |
| [KSCAMERA_MetadataId enumeration](ne-ksmedia-kscamera-metadataid.md) | This enumeration contains identifiers for a metadata item. |
| [KSCAMERA_PERFRAMESETTING_ITEM_TYPE enumeration](ne-ksmedia-kscamera-perframesetting-item-type.md) | This enumeration contains the different item types for the per-frame settings DDI. |
| [KSEVENT_CAMERACONTROL enumeration](ne-ksmedia-ksevent-cameracontrol.md) | Specifies camera control event notifications that the driver generates to indicate that an operation has been completed or canceled. |
| [KSEVENT_CAMERAEVENT enumeration](ne-ksmedia-ksevent-cameraevent.md) | KSEVENT_CAMERAEVENT enumerates a kernel streaming event set that can be used by the pipeline to enable or disable camera event notifications from the driver. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_PROPERTY enumeration](ne-ksmedia-ksproperty-cameracontrol-extended-property.md) | This enumeration contains extended camera controls. |
| [KSPROPERTY_CAMERACONTROL_FLASH enumeration](ne-ksmedia-ksproperty-cameracontrol-flash.md) | Used to specify camera flash control. |
| [KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY enumeration](ne-ksmedia-ksproperty-cameracontrol-image-pin-capability.md) | Used to identify whether the camera's image pin and record pin are mutually exclusive. If they are mutually exclusive, then when the record pin is active, the image pin cannot be active, and vice-versa. |
| [KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_PROPERTY enumeration](ne-ksmedia-ksproperty-cameracontrol-perframesetting-property.md) | This enumeration contains the property IDs defined for the per-frame property set. |
| [KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST enumeration](ne-ksmedia-ksproperty-cameracontrol-region-of-interest.md) | Used to specify a camera region of interest. |
| [KSPROPERTY_CAMERACONTROL_VIDEO_STABILIZATION_MODE enumeration](ne-ksmedia-ksproperty-cameracontrol-video-stabilization-mode.md) | Used to specify camera video stabilization. |
| [KS_AMPixAspectRatio enumeration](ne-ksmedia-ks-ampixaspectratio.md) | The KS_AMPixAspectRatio enumeration defines the pixel aspect ratio that corresponds to a 720 480 NTSC video signal or a 720 × 576 PAL video signal. |
| [KS_AMVP_MODE enumeration](ne-ksmedia-ks-amvp-mode.md) | The KS_AMVP_MODE enumeration defines video port display modes. |
| [KS_AMVP_SELECTFORMATBY enumeration](ne-ksmedia-ks-amvp-selectformatby.md) | The KS_AMVP_SELECTFORMATBY enumeration specifies the criteria that the Overlay Mixer Filter should use to select the video format. |
| [KS_AnalogVideoStandard enumeration](ne-ksmedia-ks-analogvideostandard.md) | The KS_AnalogVideoStandard enumeration defines various analog video standards that are used worldwide. |
| [KS_CameraControlAsyncOperation enumeration](ne-ksmedia-ks-cameracontrolasyncoperation.md) | Defines notifications that the driver uses to start and stop an asynchronous camera operation, including setting the flash, the image pin control properties, the region of interest in the image, or video stabilization. |
| [KS_CompressionCaps enumeration](ne-ksmedia-ks-compressioncaps.md) | The KS_CompressionCaps enumeration defines compression capabilities of a device. |
| [KS_DVDCOPYSTATE enumeration](ne-ksmedia-ks-dvdcopystate.md) | The KS_DVDCOPYSTATE enumeration describes the progress of the DVD copyright protection initialization, authentication and key negotiation sequence. |
| [KS_MPEG2Level enumeration](ne-ksmedia-ks-mpeg2level.md) | The KS_MPEG2Level enumeration describes MPEG-2 levels. |
| [KS_MPEG2Profile enumeration](ne-ksmedia-ks-mpeg2profile.md) | The KS_MPEG2Profile enumeration describes MPEG-2 profiles. |
| [KS_TUNER_STRATEGY enumeration](ne-ksmedia-ks-tuner-strategy.md) | The KS_TUNER_STRATEGY enumeration defines tuning method strategies. |
| [KS_TUNER_TUNING_FLAGS enumeration](ne-ksmedia-ks-tuner-tuning-flags.md) | The KS_TUNER_TUNING_FLAGS enumeration defines tuning flags that describe the granularity of a tuning operation. |
| [KS_VIDEODECODER_FLAGS enumeration](ne-ksmedia-ks-videodecoder-flags.md) | The KS_VIDEODECODER_FLAGS enumeration defines video decoder capabilities. |
| [KS_VideoControlFlags enumeration](ne-ksmedia-ks-videocontrolflags.md) | The KS_VideoControlFlags enumeration defines video control capabilities for a specific stream. |
| [KS_VideoStreamingHints enumeration](ne-ksmedia-ks-videostreaminghints.md) | The KS_VideoStreamingHints enumeration defines video compression hints. |
| [PCAPTURE_MEMORY_ALLOCATION_FLAGS enumeration](ne-ksmedia-pcapture-memory-allocation-flags.md) | The CAPTURE_MEMORY_ALLOCATION_FLAGS enumeration defines types of memory surfaces to which AVStream minidrivers can capture audio and video data. |
| [TELEPHONY_CALLCONTROLOP enumeration](ne-ksmedia-telephony-callcontrolop.md) | The TELEPHONY_CALLCONTROLOP enumeration defines constants that specify an operation to perform on a phone call. |
| [TELEPHONY_CALLSTATE enumeration](ne-ksmedia-telephony-callstate.md) | The TELEPHONY_CALLSTATE enumeration defines constants that specify the state of a phone call. |
| [TELEPHONY_CALLTYPE enumeration](ne-ksmedia-telephony-calltype.md) | The TELEPHONY_CALLTYPE enumeration defines constants that specify the type of phone call. |
| [TELEPHONY_PROVIDERCHANGEOP enumeration](ne-ksmedia-telephony-providerchangeop.md) | The TELEPHONY_PROVIDERCHANGEOP enumeration defines constants that specify the requested provider change operation. |
| [VIDEOENCODER_BITRATE_MODE enumeration](ne-ksmedia-videoencoder-bitrate-mode.md) | The VIDEOENCODER_BITRATE_MODE enumeration describes the bit rate encoding modes supported by the device. |
