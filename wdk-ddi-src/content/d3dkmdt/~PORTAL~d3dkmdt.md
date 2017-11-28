# D3Dkmdt.h header


This header is used by unknown technology.

D3Dkmdt.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [D3DKMDT_VPPR_GET_CONTENT_ROTATION function](nf-d3dkmdt-d3dkmdt-vppr-get-content-rotation.md) | A helper function that extracts the combined rotation that the user sees from the default display orientation from a given value of the D3DKMDT_VIDPN_PRESENT_PATH_ROTATION enumeration. |
| [D3DKMDT_VPPR_GET_CONTENT_ROTATION_PART function](nf-d3dkmdt-d3dkmdt-vppr-get-content-rotation-part.md) | A helper function that extracts the rotation angle from a given value of the D3DKMDT_VIDPN_PRESENT_PATH_ROTATION enumeration. |
| [D3DKMDT_VPPR_GET_OFFSET_ROTATION function](nf-d3dkmdt-d3dkmdt-vppr-get-offset-rotation.md) | A helper function that extracts the offset angle from a given value of the D3DKMDT_VIDPN_PRESENT_PATH_ROTATION enumeration. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [D3DKMDT_2DREGION structure](ns-d3dkmdt--d3dkmdt-2dregion.md) | The D3DKMDT_2DREGION structure is used to represent a point or an offset in a two-dimensional space. |
| [D3DKMDT_COLOR_COEFF_DYNAMIC_RANGES structure](ns-d3dkmdt--d3dkmdt-color-coeff-dynamic-ranges.md) | The D3DKMDT_COLOR_COEFF_DYNAMIC_RANGES contains values that indicate the dynamic range of each color channel of a video present target or a monitor. |
| [D3DKMDT_FREQUENCY_RANGE structure](ns-d3dkmdt--d3dkmdt-frequency-range.md) | The D3DKMDT_FREQUENCY_RANGE structure contains the minimum and maximum refresh rates supported by a monitor. |
| [D3DKMDT_GAMMA_RAMP structure](ns-d3dkmdt--d3dkmdt-gamma-ramp.md) | The D3DKMDT_GAMMA_RAMP structure contains descriptive information about a gamma lookup table and a pointer to the lookup table. |
| [D3DKMDT_GDISURFACEDATA structure](ns-d3dkmdt--d3dkmdt-gdisurfacedata.md) | The D3DKMDT_GDISURFACEDATA structure describes surfaces that are used by GDI hardware acceleration and the Desktop Window Manager (DWM). |
| [D3DKMDT_GDISURFACEFLAGS structure](ns-d3dkmdt--d3dkmdt-gdisurfaceflags.md) | The D3DKMDT_GDISURFACEFLAGS structure is reserved for system use. Do not use it in your driver. |
| [D3DKMDT_GRAPHICS_RENDERING_FORMAT structure](ns-d3dkmdt--d3dkmdt-graphics-rendering-format.md) | The D3DKMDT_GRAPHICS_RENDERING_FORMAT structure contains information about a primary rendering surface. |
| [D3DKMDT_MONITOR_DESCRIPTOR structure](ns-d3dkmdt--d3dkmdt-monitor-descriptor.md) | The D3DKMDT_MONITOR_DESCRIPTOR structure contains a pointer to a monitor descriptor along with information about the monitor descriptor. |
| [D3DKMDT_MONITOR_FREQUENCY_RANGE structure](ns-d3dkmdt--d3dkmdt-monitor-frequency-range.md) | The D3DKMDT_MONITOR_FREQUENCY_RANGE structure contains information about a range of frequencies supported by a monitor. |
| [D3DKMDT_MONITOR_SOURCE_MODE structure](ns-d3dkmdt--d3dkmdt-monitor-source-mode.md) | The D3DKMDT_MONITOR_SOURCE_MODE structure contains information about a monitor source mode. |
| [D3DKMDT_PALETTEDATA structure](ns-d3dkmdt--d3dkmdt-palettedata.md) | The D3DKMDT_PALETTEDATA structure describes a palette entry for the display. |
| [D3DKMDT_PREEMPTION_CAPS structure](ns-d3dkmdt--d3dkmdt-preemption-caps.md) | Specifies the capabilities for the preemption of graphic processing unit (GPU) graphics requests that the display miniport driver supports. |
| [D3DKMDT_SHADOWSURFACEDATA structure](ns-d3dkmdt--d3dkmdt-shadowsurfacedata.md) | The D3DKMDT_SHADOWSURFACEDATA structure describes a lockable shadow surface, which matches the primary surface in format and resolution for a given display mode. |
| [D3DKMDT_SHAREDPRIMARYSURFACEDATA structure](ns-d3dkmdt--d3dkmdt-sharedprimarysurfacedata.md) | The D3DKMDT_SHAREDPRIMARYSURFACEDATA structure describes a shared primary surface. |
| [D3DKMDT_STAGINGSURFACEDATA structure](ns-d3dkmdt--d3dkmdt-stagingsurfacedata.md) | The D3DKMDT_STAGINGSURFACEDATA structure describes the lockable staging surface that data is transferred into from an application's back buffer. |
| [D3DKMDT_VIDEO_PRESENT_SOURCE structure](ns-d3dkmdt--d3dkmdt-video-present-source.md) | The D3DKMDT_VIDEO_PRESENT_SOURCE structure contains the unique identifier of a video present source. |
| [D3DKMDT_VIDEO_PRESENT_TARGET structure](ns-d3dkmdt--d3dkmdt-video-present-target.md) | The D3DKMDT_VIDEO_PRESENT_TARGET structure contains information about a video present target. |
| [D3DKMDT_VIDEO_SIGNAL_INFO structure](ns-d3dkmdt--d3dkmdt-video-signal-info.md) | The D3DKMDT_VIDEO_SIGNAL_INFO structure contains information about a video signal driven by a video output on a display adapter. |
| [D3DKMDT_VIDPN_HW_CAPABILITY structure](ns-d3dkmdt--d3dkmdt-vidpn-hw-capability.md) | The D3DKMDT_VIDPN_HW_CAPABILITY structure describes the capabilities of the display miniport driver to perform display operations on a specified functional VidPN without dedicated GPU hardware support. |
| [D3DKMDT_VIDPN_PRESENT_PATH structure](ns-d3dkmdt--d3dkmdt-vidpn-present-path.md) | The D3DKMDT_VIDPN_PRESENT_PATH structure contains information about a video present path. |
| [D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION structure](ns-d3dkmdt--d3dkmdt-vidpn-present-path-copyprotection.md) | The D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION structure contains information about the copy protection that is supported (as well as the copy protection that is currently active) on a particular VidPN present path. |
| [D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_SUPPORT structure](ns-d3dkmdt--d3dkmdt-vidpn-present-path-copyprotection-support.md) | The D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_SUPPORT structure is used to indicate the types of copy protection that are supported by a particular VidPN present path. |
| [D3DKMDT_VIDPN_PRESENT_PATH_ROTATION_SUPPORT structure](ns-d3dkmdt--d3dkmdt-vidpn-present-path-rotation-support.md) | The D3DKMDT_VIDPN_PRESENT_PATH_ROTATION_SUPPORT structure is used to indicate the angles of rotation that are supported by a particular VidPN present path. |
| [D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT structure](ns-d3dkmdt--d3dkmdt-vidpn-present-path-scaling-support.md) | The D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT structure is used to indicate the types of scaling (and centering) that are supported by a particular VidPN present path. |
| [D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION structure](ns-d3dkmdt--d3dkmdt-vidpn-present-path-transformation.md) | The D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION structure contains information about the transformations (for example, rotation, scaling, centering) that are pinned and the transformations that are supported for a path in a video present network (VIDPN). |
| [D3DKMDT_VIDPN_SOURCE_MODE structure](ns-d3dkmdt--d3dkmdt-vidpn-source-mode.md) | The D3DKMDT_VIDPN_SOURCE_MODE structure contains information about a video present network (VidPN) source mode. |
| [D3DKMDT_VIDPN_TARGET_MODE structure](ns-d3dkmdt--d3dkmdt-vidpn-target-mode.md) | The D3DKMDT_VIDPN_TARGET_MODE structure contains information about a video present network (VidPN) target mode. |
| [D3DKMDT_WIRE_FORMAT_AND_PREFERENCE structure](ns-d3dkmdt--d3dkmdt-wire-format-and-preference.md) | Holds information about the preferred pixel encoding format. |
| [D3DKMT_MOVE_RECT structure](ns-d3dkmdt--d3dkmt-move-rect.md) | Provides information on a screen-to-screen move and a dirty rectangle copy operation. |
| [D3DKMT_WDDM_1_2_CAPS structure](ns-d3dkmdt--d3dkmt-wddm-1-2-caps.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_WDDM_1_3_CAPS structure](ns-d3dkmdt--d3dkmt-wddm-1-3-caps.md) | Reserved for system use. Do not use in your driver. |
| [D3DKMT_WDDM_2_0_CAPS structure](ns-d3dkmdt--d3dkmt-wddm-2-0-caps.md) | Reserved for system use. Do not use in your driver. |
| [DISPLAYID_DETAILED_TIMING_TYPE_I structure](ns-d3dkmdt--displayid-detailed-timing-type-i.md) | The DISPLAYID_DETAILED_TIMING_TYPE_I structure specifies an additional target mode set for a video present target. |
| [DXGKARG_SETPALETTE structure](ns-d3dkmdt--dxgkarg-setpalette.md) | The DXGKARG_SETPALETTE structure describes the palette to set for a display. |
| [DXGKMDT_OPM_ACP_AND_CGMSA_SIGNALING structure](ns-d3dkmdt--dxgkmdt-opm-acp-and-cgmsa-signaling.md) | The DXGKMDT_OPM_ACP_AND_CGMSA_SIGNALING structure describes how the signal that goes through the physical connector that is associated with the protected output object is protected. |
| [DXGKMDT_OPM_ACTUAL_OUTPUT_FORMAT structure](ns-d3dkmdt--dxgkmdt-opm-actual-output-format.md) | The DXGKMDT_OPM_ACTUAL_OUTPUT_FORMAT structure describes the format of the signal that is transmitted from a physical connector that is associated with a protected output to a monitor. |
| [DXGKMDT_OPM_CONFIGURE_PARAMETERS structure](ns-d3dkmdt--dxgkmdt-opm-configure-parameters.md) | The DXGKMDT_OPM_CONFIGURE_PARAMETERS structure contains parameters that are used to configure a protected output object in a call to the DxgkDdiOPMConfigureProtectedOutput function. |
| [DXGKMDT_OPM_CONNECTED_HDCP_DEVICE_INFORMATION structure](ns-d3dkmdt--dxgkmdt-opm-connected-hdcp-device-information.md) | The DXGKMDT_OPM_CONNECTED_HDCP_DEVICE_INFORMATION structure contains High-bandwidth Digital Content Protection (HDCP) information that is retrieved in a call to the DxgkDdiOPMGetInformation function. |
| [DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS structure](ns-d3dkmdt--dxgkmdt-opm-copp-compatible-get-info-parameters.md) | The DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS structure contains parameters that are used to retrieve information from a protected output object in a call to the DxgkDdiOPMGetCOPPCompatibleInformation function. |
| [DXGKMDT_OPM_ENCRYPTED_PARAMETERS structure](ns-d3dkmdt--dxgkmdt-opm-encrypted-parameters.md) | The DXGKMDT_OPM_ENCRYPTED_PARAMETERS structure contains data that is encrypted with the public key from an appropriate certificate. |
| [DXGKMDT_OPM_GET_INFO_PARAMETERS structure](ns-d3dkmdt--dxgkmdt-opm-get-info-parameters.md) | The DXGKMDT_OPM_GET_INFO_PARAMETERS structure contains parameters that are used to retrieve information from a protected output object in a call to the DxgkDdiOPMGetInformation function. |
| [DXGKMDT_OPM_HDCP_KEY_SELECTION_VECTOR structure](ns-d3dkmdt--dxgkmdt-opm-hdcp-key-selection-vector.md) | The DXGKMDT_OPM_HDCP_KEY_SELECTION_VECTOR structure contains a key-selection vector (KSV) for a High-bandwidth Digital Content Protection (HDCP) protected output. |
| [DXGKMDT_OPM_OMAC structure](ns-d3dkmdt--dxgkmdt-opm-omac.md) | The DXGKMDT_OPM_OMAC structure contains a One-key Cipher Block Chaining (CBC)-mode message authentication code (OMAC) for message authenticity. |
| [DXGKMDT_OPM_OUTPUT_ID structure](ns-d3dkmdt--dxgkmdt-opm-output-id.md) | The DXGKMDT_OPM_OUTPUT_ID structure identifies the output connector. |
| [DXGKMDT_OPM_RANDOM_NUMBER structure](ns-d3dkmdt--dxgkmdt-opm-random-number.md) | The DXGKMDT_OPM_RANDOM_NUMBER structure contains a 128-bit cryptographically secure random number. |
| [DXGKMDT_OPM_REQUESTED_INFORMATION structure](ns-d3dkmdt--dxgkmdt-opm-requested-information.md) | The DXGKMDT_OPM_REQUESTED_INFORMATION structure contains information that was requested in a call to the DxgkDdiOPMGetInformation or DxgkDdiOPMGetCOPPCompatibleInformation function. |
| [DXGKMDT_OPM_SET_ACP_AND_CGMSA_SIGNALING_PARAMETERS structure](ns-d3dkmdt--dxgkmdt-opm-set-acp-and-cgmsa-signaling-parameters.md) | The DXGKMDT_OPM_SET_ACP_AND_CGMSA_SIGNALING_PARAMETERS structure contains parameters to set Analog Content Protection (ACP) and Content Generation Management System Analog (CGMS-A) signaling for a protected output. |
| [DXGKMDT_OPM_SET_HDCP_SRM_PARAMETERS structure](ns-d3dkmdt--dxgkmdt-opm-set-hdcp-srm-parameters.md) | The DXGKMDT_OPM_SET_HDCP_SRM_PARAMETERS structure contains parameters to set the version of a High-bandwidth Digital Content Protection (HDCP) System Renewability Message (SRM) for a protected output. |
| [DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS structure](ns-d3dkmdt--dxgkmdt-opm-set-protection-level-parameters.md) | The DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS structure contains parameters to set the protection level of a protected output in a call to the DxgkDdiOPMConfigureProtectedOutput function. |
| [DXGKMDT_OPM_STANDARD_INFORMATION structure](ns-d3dkmdt--dxgkmdt-opm-standard-information.md) | The DXGKMDT_OPM_STANDARD_INFORMATION structure contains information that is retrieved in a call to the DxgkDdiOPMGetInformation or DxgkDdiOPMGetCOPPCompatibleInformation function. The type of information is described in the ulInformation member. |
| [DXGK_BACKLIGHT_INFO structure](ns-d3dkmdt--dxgk-backlight-info.md) | Contains the current level of backlight reduction that is applied to the integrated display panel. Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers that support adaptive brightness control. |
| [DXGK_BRIGHTNESS_CAPS structure](ns-d3dkmdt--dxgk-brightness-caps.md) | Identifies brightness control capabilities of an integrated display panel that the display miniport driver provides through a call to its DxgkDdiGetBrightnessCaps function. |
| [DXGK_BRIGHTNESS_STATE structure](ns-d3dkmdt--dxgk-brightness-state.md) | Used to enable smooth brightness control for an integrated display panel. |
| [DXGK_DISPLAY_INFORMATION structure](ns-d3dkmdt--dxgk-display-information.md) | Contains the display information that is passed between the operating system and the display miniport driver when the driver is started or stopped in response to a Plug and Play (PnP) event. |
| [DXGK_FAULT_ERROR_CODE structure](ns-d3dkmdt--dxgk-fault-error-code.md) | The DXGK_FAULT_ERROR_CODE structure provides a status code for the graphics processing unit (GPU) error reported via a page fault interrupt. |
| [DXGK_MONITORLINKINFO_CAPABILITIES structure](ns-d3dkmdt--dxgk-monitorlinkinfo-capabilities.md) | Flags which describe the capabilities for driving the monitor. |
| [DXGK_MONITORLINKINFO_USAGEHINTS structure](ns-d3dkmdt--dxgk-monitorlinkinfo-usagehints.md) | Hints to the driver on the intended usage of the display device. |
| [DXGK_TARGETMODE_DETAIL_TIMING structure](ns-d3dkmdt--dxgk-targetmode-detail-timing.md) | The DXGK_TARGETMODE_DETAIL_TIMING structure describes a video present target's additional timing modes that are compatible with the display device. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [D3DKMDT_COLOR_BASIS enumeration](ne-d3dkmdt--d3dkmdt-color-basis.md) | The D3DKMDT_COLOR_BASIS enumeration contains constants that indicate the color basis used to encode the content of a video present source or the signal on a video present target. |
| [D3DKMDT_COMPUTE_PREEMPTION_GRANULARITY enumeration](ne-d3dkmdt--d3dkmdt-compute-preemption-granularity.md) | Specifies the capabilities for the preemption of graphic processing unit (GPU) compute shader operations that the display miniport driver supports. |
| [D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE enumeration](ne-d3dkmdt--d3dkmdt-enumcofuncmodality-pivot-type.md) | The D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE enumeration indicates the pivot type in a call to DxgkDdiEnumVidPnCofuncModality. |
| [D3DKMDT_GDISURFACETYPE enumeration](ne-d3dkmdt--d3dkmdt-gdisurfacetype.md) | The D3DKMDT_GDISURFACETYPE enumeration indicates the type of lockable surface that is used by the Desktop Window Manager (DWM) for redirection. |
| [D3DKMDT_GRAPHICS_PREEMPTION_GRANULARITY enumeration](ne-d3dkmdt--d3dkmdt-graphics-preemption-granularity.md) | Specifies the capabilities for the preemption of graphic processing unit (GPU) graphics operations that the display miniport driver supports. |
| [D3DKMDT_GTFCOMPLIANCE enumeration](ne-d3dkmdt--d3dkmdt-gtfcompliance.md) | The D3DKMDT_GTFCOMPLIANCE enumeration is reserved for system use. Do not use it in your driver. |
| [D3DKMDT_MODE_PREFERENCE enumeration](ne-d3dkmdt--d3dkmdt-mode-preference.md) | The D3DKMDT_MODE_PREFERENCE enumeration is used to indicate whether a particular mode is one of the modes preferred by the monitor connected to a given video present target. |
| [D3DKMDT_MONITOR_CAPABILITIES_ORIGIN enumeration](ne-d3dkmdt--d3dkmdt-monitor-capabilities-origin.md) | The D3DKMDT_MONITOR_CAPABILITIES_ORIGIN enumeration is used to indicate where a monitor's capability information was obtained. |
| [D3DKMDT_MONITOR_CONNECTIVITY_CHECKS enumeration](ne-d3dkmdt--d3dkmdt-monitor-connectivity-checks.md) | The D3DKMDT_MONITOR_CONNECTIVITY_CHECKS enumerated type indicates whether the DxgkDdiCommitVidPn function should verify that certain video outputs have connected monitors. |
| [D3DKMDT_MONITOR_DESCRIPTOR_TYPE enumeration](ne-d3dkmdt--d3dkmdt-monitor-descriptor-type.md) | The D3DKMDT_MONITOR_DESCRIPTOR_TYPE enumeration is used to indicate a particular type of monitor descriptor. |
| [D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT enumeration](ne-d3dkmdt--d3dkmdt-monitor-frequency-range-constraint.md) | The D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT enumeration is used to indicate the type of constraint under which a monitor frequency range is supported. |
| [D3DKMDT_MONITOR_ORIENTATION enumeration](ne-d3dkmdt--d3dkmdt-monitor-orientation.md) | The D3DKMDT_MONITOR_ORIENTATION enumeration is used to describe the orientation (rotation angle) of a connected external display device. |
| [D3DKMDT_MONITOR_ORIENTATION_AWARENESS enumeration](ne-d3dkmdt--d3dkmdt-monitor-orientation-awareness.md) | The D3DKMDT_MONITOR_ORIENTATION_AWARENESS enumeration is used to describe the ability of a video output device (on the display adapter) to detect changes in the orientation (rotation angle) of a connected external display device. |
| [D3DKMDT_MONITOR_TIMING_TYPE enumeration](ne-d3dkmdt--d3dkmdt-monitor-timing-type.md) | The D3DKMDT_MONITOR_TIMING_TYPE enumeration is reserved for system use. Do not use it in your driver. |
| [D3DKMDT_PIXEL_VALUE_ACCESS_MODE enumeration](ne-d3dkmdt--d3dkmdt-pixel-value-access-mode.md) | The D3DKMDT_PIXEL_VALUE_ACCESS_MODE enumeration is used to indicate the way color values or palette indices are stored in the primary surface of a video present source. |
| [D3DKMDT_STANDARDALLOCATION_TYPE enumeration](ne-d3dkmdt--d3dkmdt-standardallocation-type.md) | The D3DKMDT_STANDARDALLOCATION_TYPE enumeration type contains values that identify particular types of surfaces. |
| [D3DKMDT_TEXT_RENDERING_FORMAT enumeration](ne-d3dkmdt--d3dkmdt-text-rendering-format.md) | The D3DKMDT_TEXT_RENDERING_FORMAT enumeration is currently not used. |
| [D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY enumeration](ne-d3dkmdt--d3dkmdt-video-output-technology.md) | The D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY enumerated type indicates the type of connector a video output device (on the display adapter) uses to connect to an external display device. |
| [D3DKMDT_VIDEO_SIGNAL_STANDARD enumeration](ne-d3dkmdt--d3dkmdt-video-signal-standard.md) | The D3DKMDT_VIDEO_SIGNAL_STANDARD enumeration contains constants that represent video signal standards. |
| [D3DKMDT_VIDPN_PRESENT_PATH_CONTENT enumeration](ne-d3dkmdt--d3dkmdt-vidpn-present-path-content.md) | The D3DKMDT_VIDPN_PRESENT_PATH_CONTENT enumeration is used to indicate the type of content that is displayed on a VidPN present path. |
| [D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE enumeration](ne-d3dkmdt--d3dkmdt-vidpn-present-path-copyprotection-type.md) | The D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE enumeration is used to indicate the type of copy protection that is supported by a VidPN present path. |
| [D3DKMDT_VIDPN_PRESENT_PATH_IMPORTANCE enumeration](ne-d3dkmdt--d3dkmdt-vidpn-present-path-importance.md) | The D3DKMDT_VIDPN_PRESENT_PATH_IMPORTANCE enumeration indicates the importance of a video present path. |
| [D3DKMDT_VIDPN_PRESENT_PATH_ROTATION enumeration](ne-d3dkmdt--d3dkmdt-vidpn-present-path-rotation.md) | The D3DKMDT_VIDPN_PRESENT_PATH_ROTATION enumeration is used to indicate the rotation angle applied to content displayed on a VidPN present path. |
| [D3DKMDT_VIDPN_PRESENT_PATH_SCALING enumeration](ne-d3dkmdt--d3dkmdt-vidpn-present-path-scaling.md) | The D3DKMDT_VIDPN_PRESENT_PATH_SCALING enumeration is used to indicate the scaling transformation applied to content displayed on a VidPN present path. |
| [D3DKMDT_VIDPN_SOURCE_MODE_TYPE enumeration](ne-d3dkmdt--d3dkmdt-vidpn-source-mode-type.md) | The D3DKMDT_VIDPN_SOURCE_MODE_TYPE enumeration is used to indicate whether a video present network (VidPN) source mode is a graphics mode, a text mode, or a stereo mode. |
| [DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO enumeration](ne-d3dkmdt--displayid-detailed-timing-type-i-aspect-ratio.md) | The DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO enumeration indicates the display device's aspect ratio, defined as width by height (width x height). |
| [DISPLAYID_DETAILED_TIMING_TYPE_I_SCANNING_MODE enumeration](ne-d3dkmdt--displayid-detailed-timing-type-i-scanning-mode.md) | The DISPLAYID_DETAILED_TIMING_TYPE_I_SCANNING_MODE enumeration indicates the display device's frame scanning mode. |
| [DISPLAYID_DETAILED_TIMING_TYPE_I_STEREO_MODE enumeration](ne-d3dkmdt--displayid-detailed-timing-type-i-stereo-mode.md) | The DISPLAYID_DETAILED_TIMING_TYPE_I_STEREO_MODE enumeration indicates the display device's stereo vision mode. |
| [DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY enumeration](ne-d3dkmdt--displayid-detailed-timing-type-i-sync-polarity.md) | The DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY enumeration indicates the display device's sync polarity (whether the sync signal is positive or negative). |
| [DXGKDT_OPM_DVI_CHARACTERISTICS enumeration](ne-d3dkmdt--dxgkdt-opm-dvi-characteristics.md) | The DXGKDT_OPM_DVI_CHARACTERISTICS enumeration indicates the Digital Video Interface (DVI) electrical characteristics of a connector. |
| [DXGKMDT_CERTIFICATE_TYPE enumeration](ne-d3dkmdt--dxgkmdt-certificate-type.md) | The DXGKMDT_CERTIFICATE_TYPE enumeration identifies the type of certificate that callers of the DxgkDdiOPMGetCertificateSize and DxgkDdiOPMGetCertificate functions require. |
| [DXGKMDT_OPM_ACP_PROTECTION_LEVEL enumeration](ne-d3dkmdt--dxgkmdt-opm-acp-protection-level.md) | The DXGKMDT_OPM_ACP_PROTECTION_LEVEL enumeration indicates the protection levels for a protected output that supports Analog Copy Protection (ACP). |
| [DXGKMDT_OPM_BUS_TYPE_AND_IMPLEMENTATION enumeration](ne-d3dkmdt--dxgkmdt-opm-bus-type-and-implementation.md) | The DXGKMDT_OPM_BUS_TYPE_AND_IMPLEMENTATION enumeration contains values that indicate the type and implementation of the bus that connects a graphics adapter to a motherboard chipset's north bridge. |
| [DXGKMDT_OPM_CGMSA enumeration](ne-d3dkmdt--dxgkmdt-opm-cgmsa.md) | The DXGKMDT_OPM_CGMSA enumeration indicates the protection levels for a protected output that supports Content Generation Management System Analog (CGMS-A). |
| [DXGKMDT_OPM_CONNECTOR_TYPE enumeration](ne-d3dkmdt--dxgkmdt-opm-connector-type.md) | Reserved for system use. Do not use in your driver. |
| [DXGKMDT_OPM_HDCP_FLAG enumeration](ne-d3dkmdt--dxgkmdt-opm-hdcp-flag.md) | The DXGKMDT_OPM_HDCP_FLAG enumeration identifies whether a protected output's physical connector is connected to a High-bandwidth Digital Content Protection (HDCP) repeater. |
| [DXGKMDT_OPM_HDCP_PROTECTION_LEVEL enumeration](ne-d3dkmdt--dxgkmdt-opm-hdcp-protection-level.md) | The DXGKMDT_OPM_HDCP_PROTECTION_LEVEL enumeration indicates the protection levels for a protected output that supports High-bandwidth Digital Content Protection (HDCP). |
| [DXGKMDT_OPM_INTERLEAVE_FORMAT enumeration](ne-d3dkmdt--dxgkmdt-opm-interleave-format.md) | The DXGKMDT_OPM_INTERLEAVE_FORMAT enumeration indicates the scan line ordering of a video frame from a protected output's signal. |
| [DXGKMDT_OPM_PROTECTION_STANDARD enumeration](ne-d3dkmdt--dxgkmdt-opm-protection-standard.md) | The DXGKMDT_OPM_PROTECTION_STANDARD enumeration indicates the type of television signal for which a video output supports protection. |
| [DXGKMDT_OPM_PROTECTION_TYPE enumeration](ne-d3dkmdt--dxgkmdt-opm-protection-type.md) | The DXGKMDT_OPM_PROTECTION_TYPE enumeration indicates the type of protections that a video output supports. |
| [DXGKMDT_OPM_STATUS enumeration](ne-d3dkmdt--dxgkmdt-opm-status.md) | The DXGKMDT_OPM_STATUS enumeration identifies the status of a protected output. |
| [DXGKMDT_OPM_VIDEO_OUTPUT_SEMANTICS enumeration](ne-d3dkmdt--dxgkmdt-opm-video-output-semantics.md) | The DXGKMDT_OPM_VIDEO_OUTPUT_SEMANTICS enumeration identifies the semantics of a protected output that is created in a call to the DxgkDdiOPMCreateProtectedOutput function. |
| [DXGK_BACKLIGHT_OPTIMIZATION_LEVEL enumeration](ne-d3dkmdt-dxgk-backlight-optimization-level.md) | Indicates the optimization level of brightness control. Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers that support adaptive brightness control. |
| [DXGK_CHILD_DEVICE_HPD_AWARENESS enumeration](ne-d3dkmdt--dxgk-child-device-hpd-awareness.md) | The DXGK_CHILD_DEVICE_HPD_AWARENESS enumeration is used to describe the hot plug capabilities of a child device of a display adapter. |
| [DXGK_DISPLAY_DESCRIPTOR_TYPE enumeration](ne-d3dkmdt--dxgk-display-descriptor-type.md) | Enum used to express the display descriptor type. |
| [DXGK_DISPLAY_TECHNOLOGY enumeration](ne-d3dkmdt--dxgk-display-technology.md) | Enum used to specify the display technology being used. |
| [DXGK_DISPLAY_USAGE enumeration](ne-d3dkmdt--dxgk-display-usage.md) | Enum used to specify the display type being used. |
| [DXGK_ENGINE_TYPE enumeration](ne-d3dkmdt-dxgk-engine-type.md) | Indicates the type of engine on a GPU node. Note the selection rules discussed in Remarks. |
| [DXGK_GENERAL_ERROR_CODE enumeration](ne-d3dkmdt--dxgk-general-error-code.md) | The DXGK_GENERAL_ERROR_CODE enumeration specifies a set of predefined graphics processing unit (GPU) errors reported via a page fault interrupt. |
| [DXGK_PAGE_FAULT_FLAGS enumeration](ne-d3dkmdt--dxgk-page-fault-flags.md) | DXGK_PAGE_FAULT_FLAGS enumeration describes the nature of the page fault that has occurred and the prescribed OS recovery action. |
| [DXGK_RENDER_PIPELINE_STAGE enumeration](ne-d3dkmdt--dxgk-render-pipeline-stage.md) | The DXGK_RENDER_PIPELINE_STAGE enumeration describes the render pipeline stage during which the GPU error has occurred. |
