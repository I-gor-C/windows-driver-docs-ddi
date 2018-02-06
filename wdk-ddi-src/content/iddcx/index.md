---
UID: NA:iddcx
ms.assetid: 520b5c9a-8579-38f3-8a64-3694aada76a9
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# iddcx.h header



iddcx.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [EVT_IDD_CX_ADAPTER_COMMIT_MODES](nc-iddcx-evt_idd_cx_adapter_commit_modes.md) | EVT_IDD_CX_ADAPTER_COMMIT_MODES is called by the OS to inform the driver of a mode change for monitors on the adapter. |
| [EVT_IDD_CX_ADAPTER_INIT_FINISHED](nc-iddcx-evt_idd_cx_adapter_init_finished.md) | EVT_IDD_CX_ADAPTER_INIT_FINISHED is called by the OS to inform the driver that the adapter initialization has completed. |
| [EVT_IDD_CX_MONITOR_ASSIGN_SWAPCHAIN](nc-iddcx-evt_idd_cx_monitor_assign_swapchain.md) | EVT_IDD_CX_MONITOR_ASSIGN_SWAPCHAIN is called by the OS to inform the driver of a mode change for monitors on the adapter. |
| [EVT_IDD_CX_MONITOR_GET_DEFAULT_DESCRIPTION_MODES](nc-iddcx-evt_idd_cx_monitor_get_default_description_modes.md) | EVT_IDD_CX_MONITOR_GET_DEFAULT_DESCRIPTION_MODES is called by the OS to request the default monitor mode list from the driver for the specified monitor when a monitor without a description is connected. |
| [EVT_IDD_CX_MONITOR_I2C_RECEIVE](nc-iddcx-evt_idd_cx_monitor_i2c_receive.md) | EVT_IDD_CX_MONITOR_I2C_RECEIVE is called by the OS to return data received from an I2C device in a monitor. |
| [EVT_IDD_CX_MONITOR_I2C_TRANSMIT](nc-iddcx-evt_idd_cx_monitor_i2c_transmit.md) | EVT_IDD_CX_MONITOR_I2C_TRANSMIT is called by the OS to return data received to an I2C device in a monitor. |
| [EVT_IDD_CX_MONITOR_OPM_CONFIGURE_PROTECTED_OUTPUT](nc-iddcx-evt_idd_cx_monitor_opm_configure_protected_output.md) | EVT_IDD_CX_MONITOR_OPM_CONFIGURE_PROTECTED_OUTPUT is called by the OS to configure the protected output. |
| [EVT_IDD_CX_MONITOR_OPM_CREATE_PROTECTED_OUTPUT](nc-iddcx-evt_idd_cx_monitor_opm_create_protected_output.md) | EVT_IDD_CX_MONITOR_OPM_CREATE_PROTECTED_OUTPUT is called by the OS to create an OPM protected output context. |
| [EVT_IDD_CX_MONITOR_OPM_DESTROY_PROTECTED_OUTPUT](nc-iddcx-evt_idd_cx_monitor_opm_destroy_protected_output.md) | EVT_IDD_CX_MONITOR_OPM_DESTROY_PROTECTED_OUTPUT is called by the OS to destroy an OPM protected output context. |
| [EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE](nc-iddcx-evt_idd_cx_monitor_opm_get_certificate.md) | EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE is called by the OS to get an OPM certificate. |
| [EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE](nc-iddcx-evt_idd_cx_monitor_opm_get_certificate_size.md) | EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE is called by the OS to get the size of an OPM certificate. |
| [EVT_IDD_CX_MONITOR_OPM_GET_INFOMATION](nc-iddcx-evt_idd_cx_monitor_opm_get_infomation.md) | EVT_IDD_CX_MONITOR_OPM_GET_INFOMATION is called by the OS to get OPM information. |
| [EVT_IDD_CX_MONITOR_OPM_GET_RANDOM_NUMBER](nc-iddcx-evt_idd_cx_monitor_opm_get_random_number.md) | EVT_IDD_CX_MONITOR_OPM_GET_RANDOM_NUMBER is called by the OS to get an OPM random number. |
| [EVT_IDD_CX_MONITOR_OPM_SET_SIGNING_KEY_AND_SEQUENCE_NUMBERS](nc-iddcx-evt_idd_cx_monitor_opm_set_signing_key_and_sequence_numbers.md) | EVT_IDD_CX_MONITOR_OPM_SET_SIGNING_KEY_AND_SEQUENCE_NUMBERS is called by the OS to set the signing key and sequence number. |
| [EVT_IDD_CX_MONITOR_QUERY_TARGET_MODES](nc-iddcx-evt_idd_cx_monitor_query_target_modes.md) | EVT_IDD_CX_MONITOR_QUERY_TARGET_MODES is called by the OS to get a list of target modes supported by the driver for a monitor connected to the endpoint. |
| [EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP](nc-iddcx-evt_idd_cx_monitor_set_gamma_ramp.md) | EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP is called by the OS to set a gamma ramp on the specified monitor. |
| [EVT_IDD_CX_MONITOR_UNASSIGN_SWAPCHAIN](nc-iddcx-evt_idd_cx_monitor_unassign_swapchain.md) | EVT_IDD_CX_MONITOR_UNASSIGN_SWAPCHAIN is called by the OS to inform the driver that a swapchain associated with a monitor is not valid anymore. |
| [EVT_IDD_CX_PARSE_MONITOR_DESCRIPTION](nc-iddcx-evt_idd_cx_parse_monitor_description.md) | EVT_IDD_CX_PARSE_MONITOR_DESCRIPTION is called by the OS to request the driver to parse a monitor description into a list of modes the monitor supports. |
| [IDD_CX_CLIENT_CONFIG_INIT](nf-iddcx-idd_cx_client_config_init.md) | Initializes the IDD_CX_CLIENT_CONFIG structure. |
| [IddCxAdapterInitAsync](nf-iddcx-iddcxadapterinitasync.md) | An asynchronous initiation function called by the driver to create a WDDM graphics adapter. |
| [IddCxAdapterUpdateMaxDisplayPipelineRate](nf-iddcx-iddcxadapterupdatemaxdisplaypipelinerate.md) | An OS callback function the driver calls to report that the max display pipeline rate has changed. |
| [IddCxDeviceInitConfig](nf-iddcx-iddcxdeviceinitconfig.md) | Creates a WDFDEVICE initialization structure to allow indirect displays to be used. |
| [IddCxDeviceInitialize](nf-iddcx-iddcxdeviceinitialize.md) | Initializes a WDF device. |
| [IddCxMonitorArrival](nf-iddcx-iddcxmonitorarrival.md) | An OS callback function the driver calls to report a monitor arrival on the WDDM graphics adapter. |
| [IddCxMonitorCreate](nf-iddcx-iddcxmonitorcreate.md) | An OS callback function the driver calls to create a monitor object that can later be used for arrival. |
| [IddCxMonitorDeparture](nf-iddcx-iddcxmonitordeparture.md) | An OS callback function the driver calls to report a monitor departure from the WDDM graphics adapter. |
| [IddCxMonitorQueryHardwareCursor](nf-iddcx-iddcxmonitorqueryhardwarecursor.md) | An OS callback function the driver calls when it wants obtain the updated cursor information. The driver normally only calls this when the event that signals cursor update has triggered. |
| [IddCxMonitorSetupHardwareCursor](nf-iddcx-iddcxmonitorsetuphardwarecursor.md) | An OS callback function the driver calls when it wants to setup hardware cursor support for the path. |
| [IddCxMonitorUpdateModes](nf-iddcx-iddcxmonitorupdatemodes.md) | An OS callback function the driver calls to update the mode list. |
| [IddCxSwapChainFinishedProcessingFrame](nf-iddcx-iddcxswapchainfinishedprocessingframe.md) | An OS callback function the driver calls report all GPU command for processing this frame have been queue. |
| [IddCxSwapChainGetDirtyRects](nf-iddcx-iddcxswapchaingetdirtyrects.md) | An OS callback function the driver calls when it wants retrieve the dirty rects for the current frame. |
| [IddCxSwapChainGetMoveRegions](nf-iddcx-iddcxswapchaingetmoveregions.md) | n OS callback function the driver calls when it wants retrieve the move regions for the current frame. |
| [IddCxSwapChainReleaseAndAcquireBuffer](nf-iddcx-iddcxswapchainreleaseandacquirebuffer.md) | An OS callback function the driver calls when it wants to release the current buffer in the swap chain and acquire a new one. |
| [IddCxSwapChainReportFrameStatistics](nf-iddcx-iddcxswapchainreportframestatistics.md) | An OS callback function the driver calls to report the frame statistics after it has processed a frame completely. |
| [IddCxSwapChainSetDevice](nf-iddcx-iddcxswapchainsetdevice.md) | An OS callback function the driver calls within its SetSwapChain routine to setup the swap-chain with a particular DXGI device. |



## Structures
| Title | Description |
| ---- |:---- |
| [IDARG_IN_ADAPTER_INIT](ns-iddcx-idarg_in_adapter_init.md) | Initializes an adapter that will be hosted on a WDF device. |
| [IDARG_IN_ADAPTER_INIT_FINISHED](ns-iddcx-idarg_in_adapter_init_finished.md) | Gives the status of the adapter initialization. |
| [IDARG_IN_COMMITMODES](ns-iddcx-idarg_in_commitmodes.md) | Gives information about the paths that need to be committed. |
| [IDARG_IN_GETDEFAULTDESCRIPTIONMODES](ns-iddcx-idarg_in_getdefaultdescriptionmodes.md) | Gives information about the default monitor modes passed into the driver. |
| [IDARG_IN_GETDIRTYRECTS](ns-iddcx-idarg_in_getdirtyrects.md) | Gives information about the parts of the surface that have changed since the last present. |
| [IDARG_IN_GETMOVEREGIONS](ns-iddcx-idarg_in_getmoveregions.md) | Gives information to the OS about move regions. |
| [IDARG_IN_I2C_RECEIVE](ns-iddcx-idarg_in_i2c_receive.md) | Gives information about I2C data being received by the OS. |
| [IDARG_IN_I2C_TRANSMIT](ns-iddcx-idarg_in_i2c_transmit.md) | Gives information about the I2C data being transmitted by the OS. |
| [IDARG_IN_MAXDISPLAYPIPELINERATE](ns-iddcx-idarg_in_maxdisplaypipelinerate.md) | Gives information about the maximum display pipeline rate. |
| [IDARG_IN_MONITORCREATE](ns-iddcx-idarg_in_monitorcreate.md) | Gives information about the monitor object that will be created. |
| [IDARG_IN_OPM_CONFIGURE_PROTECTED_OUTPUT](ns-iddcx-idarg_in_opm_configure_protected_output.md) | Gives information about the buffer that the driver will copy configuration parameters to. |
| [IDARG_IN_OPM_CREATE_PROTECTED_OUTPUT](ns-iddcx-idarg_in_opm_create_protected_output.md) | Gives information about the video output semantics for the OPM context that will be created. |
| [IDARG_IN_OPM_GET_CERTIFICATE](ns-iddcx-idarg_in_opm_get_certificate.md) | Gives information about the OPM certificate. |
| [IDARG_IN_OPM_GET_CERTIFICATE_SIZE](ns-iddcx-idarg_in_opm_get_certificate_size.md) | Gives information about the OPM certificate size. |
| [IDARG_IN_OPM_GET_INFOMATION](ns-iddcx-idarg_in_opm_get_infomation.md) | Gives information about the OPM. |
| [IDARG_IN_OPM_SET_SIGNING_KEY_AND_SEQUENCE_NUMBERS](ns-iddcx-idarg_in_opm_set_signing_key_and_sequence_numbers.md) | Gives information about parameters necessary to set the signing key and sequence numbers. |
| [IDARG_IN_PARSEMONITORDESCRIPTION](ns-iddcx-idarg_in_parsemonitordescription.md) | Gives information about the monitor description. |
| [IDARG_IN_QUERY_HWCURSOR](ns-iddcx-idarg_in_query_hwcursor.md) | Gives information about the cursor associated with the monitor. |
| [IDARG_IN_QUERYTARGETMODES](ns-iddcx-idarg_in_querytargetmodes.md) | Gives information about the target modes associated with a monitor. |
| [IDARG_IN_REPORTFRAMESTATISTICS](ns-iddcx-idarg_in_reportframestatistics.md) | Gives information about frame statistics. |
| [IDARG_IN_SET_GAMMARAMP](ns-iddcx-idarg_in_set_gammaramp.md) | Gives information about the gamma ramp being set. |
| [IDARG_IN_SETSWAPCHAIN](ns-iddcx-idarg_in_setswapchain.md) | Gives information used to set the indirect swapchain. |
| [IDARG_IN_SETUP_HWCURSOR](ns-iddcx-idarg_in_setup_hwcursor.md) | Gives information about new cursors associated with a monitor. |
| [IDARG_IN_SWAPCHAINSETDEVICE](ns-iddcx-idarg_in_swapchainsetdevice.md) | Gives information about the device that will process the swap chain. |
| [IDARG_IN_UPDATEMODES](ns-iddcx-idarg_in_updatemodes.md) | Gives information about the target modes that will be updated by the driver. |
| [IDARG_OUT_ADAPTER_INIT](ns-iddcx-idarg_out_adapter_init.md) | Gives information about the initialized adapter that can be used by the OS to call functions. |
| [IDARG_OUT_GETDEFAULTDESCRIPTIONMODES](ns-iddcx-idarg_out_getdefaultdescriptionmodes.md) | Gives information about the default description modes for the monitor, as well as the preferred mode of the monitor. |
| [IDARG_OUT_GETDIRTYRECTS](ns-iddcx-idarg_out_getdirtyrects.md) | Gives information about the recs that have changed on the surface since the last load. |
| [IDARG_OUT_GETMOVEREGIONS](ns-iddcx-idarg_out_getmoveregions.md) | Gives information about move regions that were handled by the OS. |
| [IDARG_OUT_MONITORARRIVAL](ns-iddcx-idarg_out_monitorarrival.md) | Gives information about the monitor that is exposed to the OS. |
| [IDARG_OUT_MONITORCREATE](ns-iddcx-idarg_out_monitorcreate.md) | Gives information about the newly created monitor object. |
| [IDARG_OUT_OPM_GET_CERTIFICATE_SIZE](ns-iddcx-idarg_out_opm_get_certificate_size.md) | Gives information about the OPM certificate size. |
| [IDARG_OUT_OPM_GET_INFOMATION](ns-iddcx-idarg_out_opm_get_infomation.md) | Gives the OPM information that was requested. |
| [IDARG_OUT_OPM_GET_RANDOM_NUMBER](ns-iddcx-idarg_out_opm_get_random_number.md) | Gives the OPM random number generated by the driver. |
| [IDARG_OUT_PARSEMONITORDESCRIPTION](ns-iddcx-idarg_out_parsemonitordescription.md) | Gives information about the number of monitor modes and preferred monitor mode of a monitor. |
| [IDARG_OUT_QUERY_HWCURSOR](ns-iddcx-idarg_out_query_hwcursor.md) | Gives information about the coordinates and shape of the current cursor. |
| [IDARG_OUT_QUERYTARGETMODES](ns-iddcx-idarg_out_querytargetmodes.md) | Gives information about the number of target modes provided by the OS. |
| [IDARG_OUT_RELEASEANDACQUIREBUFFER](ns-iddcx-idarg_out_releaseandacquirebuffer.md) | Gives information about the acquired swap chain buffer. |
| [IDD_CX_CLIENT_CONFIG](ns-iddcx-idd_cx_client_config.md) | The IDD_CX_CLIENT_CONFIG structure contains IDDCX callback functions that the display driver can use. |
| [IDD_DRIVER_GLOBALS](ns-iddcx-idd_driver_globals.md) | Holds per-driver Indirect Display information. Reserved for use by the system. |
| [IDDCX_ADAPTER_CAPS](ns-iddcx-iddcx_adapter_caps.md) | Gives information about the capabilities of the adapter. |
| [IDDCX_CURSOR_CAPS](ns-iddcx-iddcx_cursor_caps.md) | Gives information about the capabilities of the cursor. |
| [IDDCX_CURSOR_SHAPE_INFO](ns-iddcx-iddcx_cursor_shape_info.md) | Gives information about the shape of the cursor. |
| [IDDCX_ENDPOINT_DIAGNOSTIC_INFO](ns-iddcx-iddcx_endpoint_diagnostic_info.md) | Gives information about the video data endpoint. |
| [IDDCX_ENDPOINT_VERSION](ns-iddcx-iddcx_endpoint_version.md) | Gives version information about the video data endpoint. |
| [IDDCX_FRAME_STATISTICS](ns-iddcx-iddcx_frame_statistics.md) | Gives information about the current frame being processed. |
| [IDDCX_FRAME_STATISTICS_STEP](ns-iddcx-iddcx_frame_statistics_step.md) | Gives information about the frame processing step being used by the driver. |
| [IDDCX_METADATA](ns-iddcx-iddcx_metadata.md) | Gives information about the current provided surface and what is displayed on it. |
| [IDDCX_MONITOR_DESCRIPTION](ns-iddcx-iddcx_monitor_description.md) | Gives information about the current monitor description. |
| [IDDCX_MONITOR_INFO](ns-iddcx-iddcx_monitor_info.md) | Gives information about the current monitor and its connection type. |
| [IDDCX_MONITOR_MODE](ns-iddcx-iddcx_monitor_mode.md) | Gives information about the current monitor mode. |
| [IDDCX_MOVEREGION](ns-iddcx-iddcx_moveregion.md) | Gives information about the current move region. |
| [IDDCX_OPM_CONFIGURE_PARAMETERS](ns-iddcx-iddcx_opm_configure_parameters.md) | Gives information about the OPM configure parameters. |
| [IDDCX_OPM_ENCRYPTED_INITIALIZATION_PARAMETERS](ns-iddcx-iddcx_opm_encrypted_initialization_parameters.md) | Gives information about the OPM encrypted initialization parameters. |
| [IDDCX_OPM_GET_INFO_PARAMETERS](ns-iddcx-iddcx_opm_get_info_parameters.md) | Gives the parameters for the information request. |
| [IDDCX_OPM_GET_RANDOM_NUMBER](ns-iddcx-iddcx_opm_get_random_number.md) | Gives the OPM random number generated by the driver. |
| [IDDCX_OPM_REQUESTED_INFORMATION](ns-iddcx-iddcx_opm_requested_information.md) | Gives the information requested from the OPM. |
| [IDDCX_PATH](ns-iddcx-iddcx_path.md) | Call IDDCX_PATH_INIT to initialize this structure. |
| [IDDCX_TARGET_MODE](ns-iddcx-iddcx_target_mode.md) | Gives information about the target mode signal, including the bandwidth needed for the mode. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [IDDCX_ADAPTER_FLAGS](ne-iddcx-iddcx_adapter_flags.md) | Specifies boolean flags for an indirect display adapter. |
| [IDDCX_CURSOR_SHAPE_TYPE](ne-iddcx-iddcx_cursor_shape_type.md) | Describes the type of cursor. |
| [IDDCX_FEATURE_IMPLEMENTATION](ne-iddcx-iddcx_feature_implementation.md) | Enum used to indicate how a given supported feature is implemented. |
| [IDDCX_FRAME_STATISTICS_FLAGS](ne-iddcx-iddcx_frame_statistics_flags.md) | Indicates whether a frame was altered by the driver. |
| [IDDCX_FRAME_STATISTICS_STEP_TYPE](ne-iddcx-iddcx_frame_statistics_step_type.md) | Defines the type of frame processing step. |
| [IDDCX_FRAME_STATUS](ne-iddcx-iddcx_frame_status.md) | Defines the processing status of the frame. |
| [IDDCX_GAMMARAMP_TYPE](ne-iddcx-iddcx_gammaramp_type.md) | An enumeration indicating the type of gamma ramp being set. |
| [IDDCX_MONITOR_DESCRIPTION_TYPE](ne-iddcx-iddcx_monitor_description_type.md) | Used to describe the monitor description. |
| [IDDCX_MONITOR_MODE_ORIGIN](ne-iddcx-iddcx_monitor_mode_origin.md) | Used to describe a mode the monitor supports based on the monitor description. |
| [IDDCX_PATH_FLAGS](ne-iddcx-iddcx_path_flags.md) | Indicates the state of the path. |
| [IDDCX_TRANSMISSION_TYPE](ne-iddcx-iddcx_transmission_type.md) | Enum used to indicate the link type for transmission of the video data. |
| [IDDCX_UPDATE_REASON](ne-iddcx-iddcx_update_reason.md) | Describes why the driver is calling to update the mode list. |