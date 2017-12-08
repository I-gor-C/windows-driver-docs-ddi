# Iddcx.h header


This header is used by Display. For more information, see
- [Display](../_display/index.md)

Iddcx.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [IDD_CX_CLIENT_CONFIG_INIT function](nf-iddcx-idd-cx-client-config-init.md) | Initializes the IDD_CX_CLIENT_CONFIG structure. |
| [IddCxAdapterInitAsync function](nf-iddcx-iddcxadapterinitasync.md) | An asynchronous initiation function called by the driver to create a WDDM graphics adapter. |
| [IddCxAdapterUpdateMaxDisplayPipelineRate function](nf-iddcx-iddcxadapterupdatemaxdisplaypipelinerate.md) | An OS callback function the driver calls to report that the max display pipeline rate has changed. |
| [IddCxDeviceInitConfig function](nf-iddcx-iddcxdeviceinitconfig.md) | Creates a WDFDEVICE initialization structure to allow indirect displays to be used. |
| [IddCxDeviceInitialize function](nf-iddcx-iddcxdeviceinitialize.md) | Initializes a WDF device. |
| [IddCxMonitorArrival function](nf-iddcx-iddcxmonitorarrival.md) | An OS callback function the driver calls to report a monitor arrival on the WDDM graphics adapter. |
| [IddCxMonitorCreate function](nf-iddcx-iddcxmonitorcreate.md) | An OS callback function the driver calls to create a monitor object that can later be used for arrival. |
| [IddCxMonitorDeparture function](nf-iddcx-iddcxmonitordeparture.md) | An OS callback function the driver calls to report a monitor departure from the WDDM graphics adapter. |
| [IddCxMonitorQueryHardwareCursor function](nf-iddcx-iddcxmonitorqueryhardwarecursor.md) | An OS callback function the driver calls when it wants obtain the updated cursor information. The driver normally only calls this when the event that signals cursor update has triggered. |
| [IddCxMonitorSetupHardwareCursor function](nf-iddcx-iddcxmonitorsetuphardwarecursor.md) | An OS callback function the driver calls when it wants to setup hardware cursor support for the path. |
| [IddCxMonitorUpdateModes function](nf-iddcx-iddcxmonitorupdatemodes.md) | An OS callback function the driver calls to update the mode list. |
| [IddCxSwapChainFinishedProcessingFrame function](nf-iddcx-iddcxswapchainfinishedprocessingframe.md) | An OS callback function the driver calls report all GPU command for processing this frame have been queue. |
| [IddCxSwapChainGetDirtyRects function](nf-iddcx-iddcxswapchaingetdirtyrects.md) | An OS callback function the driver calls when it wants retrieve the dirty rects for the current frame. |
| [IddCxSwapChainGetMoveRegions function](nf-iddcx-iddcxswapchaingetmoveregions.md) | n OS callback function the driver calls when it wants retrieve the move regions for the current frame. |
| [IddCxSwapChainReleaseAndAcquireBuffer function](nf-iddcx-iddcxswapchainreleaseandacquirebuffer.md) | An OS callback function the driver calls when it wants to release the current buffer in the swap chain and acquire a new one. |
| [IddCxSwapChainReportFrameStatistics function](nf-iddcx-iddcxswapchainreportframestatistics.md) | An OS callback function the driver calls to report the frame statistics after it has processed a frame completely. |
| [IddCxSwapChainSetDevice function](nf-iddcx-iddcxswapchainsetdevice.md) | An OS callback function the driver calls within its SetSwapChain routine to setup the swap-chain with a particular DXGI device. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_IDD_CX_ADAPTER_COMMIT_MODES callback](nc-iddcx-evt-idd-cx-adapter-commit-modes.md) | EVT_IDD_CX_ADAPTER_COMMIT_MODES is called by the OS to inform the driver of a mode change for monitors on the adapter. |
| [EVT_IDD_CX_ADAPTER_INIT_FINISHED callback](nc-iddcx-evt-idd-cx-adapter-init-finished.md) | EVT_IDD_CX_ADAPTER_INIT_FINISHED is called by the OS to inform the driver that the adapter initialization has completed. |
| [EVT_IDD_CX_MONITOR_ASSIGN_SWAPCHAIN callback](nc-iddcx-evt-idd-cx-monitor-assign-swapchain.md) | EVT_IDD_CX_MONITOR_ASSIGN_SWAPCHAIN is called by the OS to inform the driver of a mode change for monitors on the adapter. |
| [EVT_IDD_CX_MONITOR_GET_DEFAULT_DESCRIPTION_MODES callback](nc-iddcx-evt-idd-cx-monitor-get-default-description-modes.md) | EVT_IDD_CX_MONITOR_GET_DEFAULT_DESCRIPTION_MODES is called by the OS to request the default monitor mode list from the driver for the specified monitor when a monitor without a description is connected. |
| [EVT_IDD_CX_MONITOR_I2C_RECEIVE callback](nc-iddcx-evt-idd-cx-monitor-i2c-receive.md) | EVT_IDD_CX_MONITOR_I2C_RECEIVE is called by the OS to return data received from an I2C device in a monitor. |
| [EVT_IDD_CX_MONITOR_I2C_TRANSMIT callback](nc-iddcx-evt-idd-cx-monitor-i2c-transmit.md) | EVT_IDD_CX_MONITOR_I2C_TRANSMIT is called by the OS to return data received to an I2C device in a monitor. |
| [EVT_IDD_CX_MONITOR_OPM_CONFIGURE_PROTECTED_OUTPUT callback](nc-iddcx-evt-idd-cx-monitor-opm-configure-protected-output.md) | EVT_IDD_CX_MONITOR_OPM_CONFIGURE_PROTECTED_OUTPUT is called by the OS to configure the protected output. |
| [EVT_IDD_CX_MONITOR_OPM_CREATE_PROTECTED_OUTPUT callback](nc-iddcx-evt-idd-cx-monitor-opm-create-protected-output.md) | EVT_IDD_CX_MONITOR_OPM_CREATE_PROTECTED_OUTPUT is called by the OS to create an OPM protected output context. |
| [EVT_IDD_CX_MONITOR_OPM_DESTROY_PROTECTED_OUTPUT callback](nc-iddcx-evt-idd-cx-monitor-opm-destroy-protected-output.md) | EVT_IDD_CX_MONITOR_OPM_DESTROY_PROTECTED_OUTPUT is called by the OS to destroy an OPM protected output context. |
| [EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE callback](nc-iddcx-evt-idd-cx-monitor-opm-get-certificate.md) | EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE is called by the OS to get an OPM certificate. |
| [EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE callback](nc-iddcx-evt-idd-cx-monitor-opm-get-certificate-size.md) | EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE is called by the OS to get the size of an OPM certificate. |
| [EVT_IDD_CX_MONITOR_OPM_GET_INFOMATION callback](nc-iddcx-evt-idd-cx-monitor-opm-get-infomation.md) | EVT_IDD_CX_MONITOR_OPM_GET_INFOMATION is called by the OS to get OPM information. |
| [EVT_IDD_CX_MONITOR_OPM_GET_RANDOM_NUMBER callback](nc-iddcx-evt-idd-cx-monitor-opm-get-random-number.md) | EVT_IDD_CX_MONITOR_OPM_GET_RANDOM_NUMBER is called by the OS to get an OPM random number. |
| [EVT_IDD_CX_MONITOR_OPM_SET_SIGNING_KEY_AND_SEQUENCE_NUMBERS callback](nc-iddcx-evt-idd-cx-monitor-opm-set-signing-key-and-sequence-numbers.md) | EVT_IDD_CX_MONITOR_OPM_SET_SIGNING_KEY_AND_SEQUENCE_NUMBERS is called by the OS to set the signing key and sequence number. |
| [EVT_IDD_CX_MONITOR_QUERY_TARGET_MODES callback](nc-iddcx-evt-idd-cx-monitor-query-target-modes.md) | EVT_IDD_CX_MONITOR_QUERY_TARGET_MODES is called by the OS to get a list of target modes supported by the driver for a monitor connected to the endpoint. |
| [EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP callback](nc-iddcx-evt-idd-cx-monitor-set-gamma-ramp.md) | EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP is called by the OS to set a gamma ramp on the specified monitor. |
| [EVT_IDD_CX_MONITOR_UNASSIGN_SWAPCHAIN callback](nc-iddcx-evt-idd-cx-monitor-unassign-swapchain.md) | EVT_IDD_CX_MONITOR_UNASSIGN_SWAPCHAIN is called by the OS to inform the driver that a swapchain associated with a monitor is not valid anymore. |
| [EVT_IDD_CX_PARSE_MONITOR_DESCRIPTION callback](nc-iddcx-evt-idd-cx-parse-monitor-description.md) | EVT_IDD_CX_PARSE_MONITOR_DESCRIPTION is called by the OS to request the driver to parse a monitor description into a list of modes the monitor supports. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [IDARG_IN_ADAPTER_INIT structure](ns-iddcx-idarg-in-adapter-init.md) | Initializes an adapter that will be hosted on a WDF device. |
| [IDARG_IN_ADAPTER_INIT structure](ns-iddcx-idarg-in-adapter-init~r1.md) | Initializes an adapter that will be hosted on a WDF device. |
| [IDARG_IN_ADAPTER_INIT_FINISHED structure](ns-iddcx-idarg-in-adapter-init-finished.md) | Gives the status of the adapter initialization. |
| [IDARG_IN_ADAPTER_INIT_FINISHED structure](ns-iddcx-idarg-in-adapter-init-finished~r1.md) | Gives the status of the adapter initialization. |
| [IDARG_IN_COMMITMODES structure](ns-iddcx-idarg-in-commitmodes.md) | Gives information about the paths that need to be committed. |
| [IDARG_IN_COMMITMODES structure](ns-iddcx-idarg-in-commitmodes~r1.md) | Gives information about the paths that need to be committed. |
| [IDARG_IN_GETDEFAULTDESCRIPTIONMODES structure](ns-iddcx-idarg-in-getdefaultdescriptionmodes.md) | Gives information about the default monitor modes passed into the driver. |
| [IDARG_IN_GETDEFAULTDESCRIPTIONMODES structure](ns-iddcx-idarg-in-getdefaultdescriptionmodes~r1.md) | Gives information about the default monitor modes passed into the driver. |
| [IDARG_IN_GETDIRTYRECTS structure](ns-iddcx-idarg-in-getdirtyrects.md) | Gives information about the parts of the surface that have changed since the last present. |
| [IDARG_IN_GETDIRTYRECTS structure](ns-iddcx-idarg-in-getdirtyrects~r1.md) | Gives information about the parts of the surface that have changed since the last present. |
| [IDARG_IN_GETMOVEREGIONS structure](ns-iddcx-idarg-in-getmoveregions.md) | Gives information to the OS about move regions. |
| [IDARG_IN_GETMOVEREGIONS structure](ns-iddcx-idarg-in-getmoveregions~r1.md) | Gives information to the OS about move regions. |
| [IDARG_IN_I2C_RECEIVE structure](ns-iddcx-idarg-in-i2c-receive.md) | Gives information about I2C data being received by the OS. |
| [IDARG_IN_I2C_RECEIVE structure](ns-iddcx-idarg-in-i2c-receive~r1.md) | Gives information about I2C data being received by the OS. |
| [IDARG_IN_I2C_TRANSMIT structure](ns-iddcx-idarg-in-i2c-transmit.md) | Gives information about the I2C data being transmitted by the OS. |
| [IDARG_IN_I2C_TRANSMIT structure](ns-iddcx-idarg-in-i2c-transmit~r1.md) | Gives information about the I2C data being transmitted by the OS. |
| [IDARG_IN_MAXDISPLAYPIPELINERATE structure](ns-iddcx-idarg-in-maxdisplaypipelinerate.md) | Gives information about the maximum display pipeline rate. |
| [IDARG_IN_MAXDISPLAYPIPELINERATE structure](ns-iddcx-idarg-in-maxdisplaypipelinerate~r1.md) | Gives information about the maximum display pipeline rate. |
| [IDARG_IN_MONITORCREATE structure](ns-iddcx-idarg-in-monitorcreate.md) | Gives information about the monitor object that will be created. |
| [IDARG_IN_MONITORCREATE structure](ns-iddcx-idarg-in-monitorcreate~r1.md) | Gives information about the monitor object that will be created. |
| [IDARG_IN_OPM_CONFIGURE_PROTECTED_OUTPUT structure](ns-iddcx-idarg-in-opm-configure-protected-output.md) | Gives information about the buffer that the driver will copy configuration parameters to. |
| [IDARG_IN_OPM_CONFIGURE_PROTECTED_OUTPUT structure](ns-iddcx-idarg-in-opm-configure-protected-output~r1.md) | Gives information about the buffer that the driver will copy configuration parameters to. |
| [IDARG_IN_OPM_CREATE_PROTECTED_OUTPUT structure](ns-iddcx-idarg-in-opm-create-protected-output.md) | Gives information about the video output semantics for the OPM context that will be created. |
| [IDARG_IN_OPM_CREATE_PROTECTED_OUTPUT structure](ns-iddcx-idarg-in-opm-create-protected-output~r1.md) | Gives information about the video output semantics for the OPM context that will be created. |
| [IDARG_IN_OPM_GET_CERTIFICATE structure](ns-iddcx-idarg-in-opm-get-certificate.md) | Gives information about the OPM certificate. |
| [IDARG_IN_OPM_GET_CERTIFICATE structure](ns-iddcx-idarg-in-opm-get-certificate~r1.md) | Gives information about the OPM certificate. |
| [IDARG_IN_OPM_GET_CERTIFICATE_SIZE structure](ns-iddcx-idarg-in-opm-get-certificate-size.md) | Gives information about the OPM certificate size. |
| [IDARG_IN_OPM_GET_CERTIFICATE_SIZE structure](ns-iddcx-idarg-in-opm-get-certificate-size~r1.md) | Gives information about the OPM certificate size. |
| [IDARG_IN_OPM_GET_INFOMATION structure](ns-iddcx-idarg-in-opm-get-infomation.md) | Gives information about the OPM. |
| [IDARG_IN_OPM_GET_INFOMATION structure](ns-iddcx-idarg-in-opm-get-infomation~r1.md) | Gives information about the OPM. |
| [IDARG_IN_OPM_SET_SIGNING_KEY_AND_SEQUENCE_NUMBERS structure](ns-iddcx-idarg-in-opm-set-signing-key-and-sequence-numbers.md) | Gives information about parameters necessary to set the signing key and sequence numbers. |
| [IDARG_IN_OPM_SET_SIGNING_KEY_AND_SEQUENCE_NUMBERS structure](ns-iddcx-idarg-in-opm-set-signing-key-and-sequence-numbers~r1.md) | Gives information about parameters necessary to set the signing key and sequence numbers. |
| [IDARG_IN_PARSEMONITORDESCRIPTION structure](ns-iddcx-idarg-in-parsemonitordescription.md) | Gives information about the monitor description. |
| [IDARG_IN_PARSEMONITORDESCRIPTION structure](ns-iddcx-idarg-in-parsemonitordescription~r1.md) | Gives information about the monitor description. |
| [IDARG_IN_QUERYTARGETMODES structure](ns-iddcx-idarg-in-querytargetmodes.md) | Gives information about the target modes associated with a monitor. |
| [IDARG_IN_QUERYTARGETMODES structure](ns-iddcx-idarg-in-querytargetmodes~r1.md) | Gives information about the target modes associated with a monitor. |
| [IDARG_IN_QUERY_HWCURSOR structure](ns-iddcx-idarg-in-query-hwcursor.md) | Gives information about the cursor associated with the monitor. |
| [IDARG_IN_QUERY_HWCURSOR structure](ns-iddcx-idarg-in-query-hwcursor~r1.md) | Gives information about the cursor associated with the monitor. |
| [IDARG_IN_REPORTFRAMESTATISTICS structure](ns-iddcx-idarg-in-reportframestatistics.md) | Gives information about frame statistics. |
| [IDARG_IN_REPORTFRAMESTATISTICS structure](ns-iddcx-idarg-in-reportframestatistics~r1.md) | Gives information about frame statistics. |
| [IDARG_IN_SETSWAPCHAIN structure](ns-iddcx-idarg-in-setswapchain.md) | Gives information used to set the indirect swapchain. |
| [IDARG_IN_SETSWAPCHAIN structure](ns-iddcx-idarg-in-setswapchain~r1.md) | Gives information used to set the indirect swapchain. |
| [IDARG_IN_SETUP_HWCURSOR structure](ns-iddcx-idarg-in-setup-hwcursor.md) | Gives information about new cursors associated with a monitor. |
| [IDARG_IN_SETUP_HWCURSOR structure](ns-iddcx-idarg-in-setup-hwcursor~r1.md) | Gives information about new cursors associated with a monitor. |
| [IDARG_IN_SET_GAMMARAMP structure](ns-iddcx-idarg-in-set-gammaramp.md) | Gives information about the gamma ramp being set. |
| [IDARG_IN_SET_GAMMARAMP structure](ns-iddcx-idarg-in-set-gammaramp~r1.md) | Gives information about the gamma ramp being set. |
| [IDARG_IN_SWAPCHAINSETDEVICE structure](ns-iddcx-idarg-in-swapchainsetdevice.md) | Gives information about the device that will process the swap chain. |
| [IDARG_IN_SWAPCHAINSETDEVICE structure](ns-iddcx-idarg-in-swapchainsetdevice~r1.md) | Gives information about the device that will process the swap chain. |
| [IDARG_IN_UPDATEMODES structure](ns-iddcx-idarg-in-updatemodes.md) | Gives information about the target modes that will be updated by the driver. |
| [IDARG_IN_UPDATEMODES structure](ns-iddcx-idarg-in-updatemodes~r1.md) | Gives information about the target modes that will be updated by the driver. |
| [IDARG_OUT_ADAPTER_INIT structure](ns-iddcx-idarg-out-adapter-init.md) | Gives information about the initialized adapter that can be used by the OS to call functions. |
| [IDARG_OUT_ADAPTER_INIT structure](ns-iddcx-idarg-out-adapter-init~r1.md) | Gives information about the initialized adapter that can be used by the OS to call functions. |
| [IDARG_OUT_GETDEFAULTDESCRIPTIONMODES structure](ns-iddcx-idarg-out-getdefaultdescriptionmodes.md) | Gives information about the default description modes for the monitor, as well as the preferred mode of the monitor. |
| [IDARG_OUT_GETDEFAULTDESCRIPTIONMODES structure](ns-iddcx-idarg-out-getdefaultdescriptionmodes~r1.md) | Gives information about the default description modes for the monitor, as well as the preferred mode of the monitor. |
| [IDARG_OUT_GETDIRTYRECTS structure](ns-iddcx-idarg-out-getdirtyrects.md) | Gives information about the recs that have changed on the surface since the last load. |
| [IDARG_OUT_GETDIRTYRECTS structure](ns-iddcx-idarg-out-getdirtyrects~r1.md) | Gives information about the recs that have changed on the surface since the last load. |
| [IDARG_OUT_GETMOVEREGIONS structure](ns-iddcx-idarg-out-getmoveregions.md) | Gives information about move regions that were handled by the OS. |
| [IDARG_OUT_GETMOVEREGIONS structure](ns-iddcx-idarg-out-getmoveregions~r1.md) | Gives information about move regions that were handled by the OS. |
| [IDARG_OUT_MONITORARRIVAL structure](ns-iddcx-idarg-out-monitorarrival.md) | Gives information about the monitor that is exposed to the OS. |
| [IDARG_OUT_MONITORARRIVAL structure](ns-iddcx-idarg-out-monitorarrival~r1.md) | Gives information about the monitor that is exposed to the OS. |
| [IDARG_OUT_MONITORCREATE structure](ns-iddcx-idarg-out-monitorcreate.md) | Gives information about the newly created monitor object. |
| [IDARG_OUT_MONITORCREATE structure](ns-iddcx-idarg-out-monitorcreate~r1.md) | Gives information about the newly created monitor object. |
| [IDARG_OUT_OPM_GET_CERTIFICATE_SIZE structure](ns-iddcx-idarg-out-opm-get-certificate-size.md) | Gives information about the OPM certificate size. |
| [IDARG_OUT_OPM_GET_CERTIFICATE_SIZE structure](ns-iddcx-idarg-out-opm-get-certificate-size~r1.md) | Gives information about the OPM certificate size. |
| [IDARG_OUT_OPM_GET_INFOMATION structure](ns-iddcx-idarg-out-opm-get-infomation.md) | Gives the OPM information that was requested. |
| [IDARG_OUT_OPM_GET_INFOMATION structure](ns-iddcx-idarg-out-opm-get-infomation~r1.md) | Gives the OPM information that was requested. |
| [IDARG_OUT_OPM_GET_RANDOM_NUMBER structure](ns-iddcx-idarg-out-opm-get-random-number.md) | Gives the OPM random number generated by the driver. |
| [IDARG_OUT_OPM_GET_RANDOM_NUMBER structure](ns-iddcx-idarg-out-opm-get-random-number~r1.md) | Gives the OPM random number generated by the driver. |
| [IDARG_OUT_PARSEMONITORDESCRIPTION structure](ns-iddcx-idarg-out-parsemonitordescription.md) | Gives information about the number of monitor modes and preferred monitor mode of a monitor. |
| [IDARG_OUT_PARSEMONITORDESCRIPTION structure](ns-iddcx-idarg-out-parsemonitordescription~r1.md) | Gives information about the number of monitor modes and preferred monitor mode of a monitor. |
| [IDARG_OUT_QUERYTARGETMODES structure](ns-iddcx-idarg-out-querytargetmodes.md) | Gives information about the number of target modes provided by the OS. |
| [IDARG_OUT_QUERYTARGETMODES structure](ns-iddcx-idarg-out-querytargetmodes~r1.md) | Gives information about the number of target modes provided by the OS. |
| [IDARG_OUT_QUERY_HWCURSOR structure](ns-iddcx-idarg-out-query-hwcursor.md) | Gives information about the coordinates and shape of the current cursor. |
| [IDARG_OUT_QUERY_HWCURSOR structure](ns-iddcx-idarg-out-query-hwcursor~r1.md) | Gives information about the coordinates and shape of the current cursor. |
| [IDARG_OUT_RELEASEANDACQUIREBUFFER structure](ns-iddcx-idarg-out-releaseandacquirebuffer.md) | Gives information about the acquired swap chain buffer. |
| [IDARG_OUT_RELEASEANDACQUIREBUFFER structure](ns-iddcx-idarg-out-releaseandacquirebuffer~r1.md) | Gives information about the acquired swap chain buffer. |
| [IDDCX_ADAPTER_CAPS structure](ns-iddcx-iddcx-adapter-caps.md) | Gives information about the capabilities of the adapter. |
| [IDDCX_ADAPTER_CAPS structure](ns-iddcx-iddcx-adapter-caps~r1.md) | Gives information about the capabilities of the adapter. |
| [IDDCX_CURSOR_CAPS structure](ns-iddcx-iddcx-cursor-caps.md) | Gives information about the capabilities of the cursor. |
| [IDDCX_CURSOR_CAPS structure](ns-iddcx-iddcx-cursor-caps~r1.md) | Gives information about the capabilities of the cursor. |
| [IDDCX_CURSOR_SHAPE_INFO structure](ns-iddcx-iddcx-cursor-shape-info.md) | Gives information about the shape of the cursor. |
| [IDDCX_CURSOR_SHAPE_INFO structure](ns-iddcx-iddcx-cursor-shape-info~r1.md) | Gives information about the shape of the cursor. |
| [IDDCX_ENDPOINT_DIAGNOSTIC_INFO structure](ns-iddcx-iddcx-endpoint-diagnostic-info.md) | Gives information about the video data endpoint. |
| [IDDCX_ENDPOINT_DIAGNOSTIC_INFO structure](ns-iddcx-iddcx-endpoint-diagnostic-info~r1.md) | Gives information about the video data endpoint. |
| [IDDCX_ENDPOINT_VERSION structure](ns-iddcx-iddcx-endpoint-version.md) | Gives version information about the video data endpoint. |
| [IDDCX_ENDPOINT_VERSION structure](ns-iddcx-iddcx-endpoint-version~r1.md) | Gives version information about the video data endpoint. |
| [IDDCX_FRAME_STATISTICS structure](ns-iddcx-iddcx-frame-statistics.md) | Gives information about the current frame being processed. |
| [IDDCX_FRAME_STATISTICS structure](ns-iddcx-iddcx-frame-statistics~r1.md) | Gives information about the current frame being processed. |
| [IDDCX_FRAME_STATISTICS_STEP structure](ns-iddcx-iddcx-frame-statistics-step.md) | Gives information about the frame processing step being used by the driver. |
| [IDDCX_FRAME_STATISTICS_STEP structure](ns-iddcx-iddcx-frame-statistics-step~r1.md) | Gives information about the frame processing step being used by the driver. |
| [IDDCX_METADATA structure](ns-iddcx-iddcx-metadata.md) | Gives information about the current provided surface and what is displayed on it. |
| [IDDCX_METADATA structure](ns-iddcx-iddcx-metadata~r1.md) | Gives information about the current provided surface and what is displayed on it. |
| [IDDCX_MONITOR_DESCRIPTION structure](ns-iddcx-iddcx-monitor-description.md) | Gives information about the current monitor description. |
| [IDDCX_MONITOR_DESCRIPTION structure](ns-iddcx-iddcx-monitor-description~r1.md) | Gives information about the current monitor description. |
| [IDDCX_MONITOR_INFO structure](ns-iddcx-iddcx-monitor-info.md) | Gives information about the current monitor and its connection type. |
| [IDDCX_MONITOR_INFO structure](ns-iddcx-iddcx-monitor-info~r1.md) | Gives information about the current monitor and its connection type. |
| [IDDCX_MONITOR_MODE structure](ns-iddcx-iddcx-monitor-mode.md) | Gives information about the current monitor mode. |
| [IDDCX_MONITOR_MODE structure](ns-iddcx-iddcx-monitor-mode~r1.md) | Gives information about the current monitor mode. |
| [IDDCX_MOVEREGION structure](ns-iddcx-iddcx-moveregion.md) | Gives information about the current move region. |
| [IDDCX_MOVEREGION structure](ns-iddcx-iddcx-moveregion~r1.md) | Gives information about the current move region. |
| [IDDCX_OPM_CONFIGURE_PARAMETERS structure](ns-iddcx-iddcx-opm-configure-parameters.md) | Gives information about the OPM configure parameters. |
| [IDDCX_OPM_CONFIGURE_PARAMETERS structure](ns-iddcx-iddcx-opm-configure-parameters~r1.md) | Gives information about the OPM configure parameters. |
| [IDDCX_OPM_ENCRYPTED_INITIALIZATION_PARAMETERS structure](ns-iddcx-iddcx-opm-encrypted-initialization-parameters.md) | Gives information about the OPM encrypted initialization parameters. |
| [IDDCX_OPM_ENCRYPTED_INITIALIZATION_PARAMETERS structure](ns-iddcx-iddcx-opm-encrypted-initialization-parameters~r1.md) | Gives information about the OPM encrypted initialization parameters. |
| [IDDCX_OPM_GET_INFO_PARAMETERS structure](ns-iddcx-iddcx-opm-get-info-parameters.md) | Gives the parameters for the information request. |
| [IDDCX_OPM_GET_INFO_PARAMETERS structure](ns-iddcx-iddcx-opm-get-info-parameters~r1.md) | Gives the parameters for the information request. |
| [IDDCX_OPM_GET_RANDOM_NUMBER structure](ns-iddcx-iddcx-opm-get-random-number.md) | Gives the OPM random number generated by the driver. |
| [IDDCX_OPM_GET_RANDOM_NUMBER structure](ns-iddcx-iddcx-opm-get-random-number~r1.md) | Gives the OPM random number generated by the driver. |
| [IDDCX_OPM_REQUESTED_INFORMATION structure](ns-iddcx-iddcx-opm-requested-information.md) | Gives the information requested from the OPM. |
| [IDDCX_OPM_REQUESTED_INFORMATION structure](ns-iddcx-iddcx-opm-requested-information~r1.md) | Gives the information requested from the OPM. |
| [IDDCX_PATH structure](ns-iddcx-iddcx-path.md) | Call IDDCX_PATH_INIT to initialize this structure. |
| [IDDCX_PATH structure](ns-iddcx-iddcx-path~r1.md) | Call IDDCX_PATH_INIT to initialize this structure. |
| [IDDCX_TARGET_MODE structure](ns-iddcx-iddcx-target-mode.md) | Gives information about the target mode signal, including the bandwidth needed for the mode. |
| [IDDCX_TARGET_MODE structure](ns-iddcx-iddcx-target-mode~r1.md) | Gives information about the target mode signal, including the bandwidth needed for the mode. |
| [IDD_CX_CLIENT_CONFIG structure](ns-iddcx-idd-cx-client-config.md) | The IDD_CX_CLIENT_CONFIG structure contains IDDCX callback functions that the display driver can use. |
| [IDD_CX_CLIENT_CONFIG structure](ns-iddcx-idd-cx-client-config~r1.md) | The IDD_CX_CLIENT_CONFIG structure contains IDDCX callback functions that the display driver can use. |
| [IDD_DRIVER_GLOBALS structure](ns-iddcx-idd-driver-globals.md) | Holds per-driver Indirect Display information. Reserved for use by the system. |
| [IDD_DRIVER_GLOBALS structure](ns-iddcx-idd-driver-globals~r1.md) | Holds per-driver Indirect Display information. Reserved for use by the system. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [IDDCX_ADAPTER_FLAGS enumeration](ne-iddcx-iddcx-adapter-flags.md) | Specifies boolean flags for an indirect display adapter. |
| [IDDCX_CURSOR_SHAPE_TYPE enumeration](ne-iddcx-iddcx-cursor-shape-type.md) | Describes the type of cursor. |
| [IDDCX_FEATURE_IMPLEMENTATION enumeration](ne-iddcx-iddcx-feature-implementation.md) | Enum used to indicate how a given supported feature is implemented. |
| [IDDCX_FRAME_STATISTICS_FLAGS enumeration](ne-iddcx-iddcx-frame-statistics-flags.md) | Indicates whether a frame was altered by the driver. |
| [IDDCX_FRAME_STATISTICS_STEP_TYPE enumeration](ne-iddcx-iddcx-frame-statistics-step-type.md) | Defines the type of frame processing step. |
| [IDDCX_FRAME_STATUS enumeration](ne-iddcx-iddcx-frame-status.md) | Defines the processing status of the frame. |
| [IDDCX_GAMMARAMP_TYPE enumeration](ne-iddcx-iddcx-gammaramp-type.md) | An enumeration indicating the type of gamma ramp being set. |
| [IDDCX_MONITOR_DESCRIPTION_TYPE enumeration](ne-iddcx-iddcx-monitor-description-type.md) | Used to describe the monitor description. |
| [IDDCX_MONITOR_MODE_ORIGIN enumeration](ne-iddcx-iddcx-monitor-mode-origin.md) | Used to describe a mode the monitor supports based on the monitor description. |
| [IDDCX_PATH_FLAGS enumeration](ne-iddcx-iddcx-path-flags.md) | Indicates the state of the path. |
| [IDDCX_TRANSMISSION_TYPE enumeration](ne-iddcx-iddcx-transmission-type.md) | Enum used to indicate the link type for transmission of the video data. |
| [IDDCX_UPDATE_REASON enumeration](ne-iddcx-iddcx-update-reason.md) | Describes why the driver is calling to update the mode list. |
