# Dispmprt.h header


This header is used by unknown technology.

Dispmprt.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [DxgkInitialize function](nf-dispmprt-dxgkinitialize.md) | The DxgkInitialize function loads and initializes the DirectX graphics kernel subsystem (Dxgkrnl.sys). |
| [DxgkInitializeDisplayOnlyDriver function](nf-dispmprt-dxgkinitializedisplayonlydriver.md) | Loads and initializes the DirectX graphics kernel subsystem (Dxgkrnl.sys) for use by a kernel mode display-only driver (KMDOD). |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [DXGKCB_ACQUIRE_POST_DISPLAY_OWNERSHIP callback](nc-dispmprt-dxgkcb-acquire-post-display-ownership.md) | Called by a Windows Display Driver Model (WDDM) 1.2 or later display miniport driver to obtain the display information from the current power-on self-test (POST) display device or the previously running WDDM driver. |
| [DXGKCB_ACQUIRE_POST_DISPLAY_OWNERSHIP2 callback](nc-dispmprt-dxgkcb-acquire-post-display-ownership2.md) | Called by a display miniport driver to obtain the display information from the current power-on self-test (POST) display device or the previously running Windows Display Driver Model (WDDM) driver. |
| [DXGKCB_AGP_ALLOCATE_POOL callback](nc-dispmprt-dxgkcb-agp-allocate-pool.md) | The AgpAllocatePool function reserves, commits, and maps AGP memory. |
| [DXGKCB_AGP_FREE_POOL callback](nc-dispmprt-dxgkcb-agp-free-pool.md) | The AgpFreePool function frees AGP memory that was previously allocated by AgpAllocatePool. |
| [DXGKCB_AGP_SET_COMMAND callback](nc-dispmprt-dxgkcb-agp-set-command.md) | The AgpSetCommand function sets the AGP rate and specifies whether side band addressing and fast write transactions are enabled. |
| [DXGKCB_EVAL_ACPI_METHOD callback](nc-dispmprt-dxgkcb-eval-acpi-method.md) | The DxgkCbEvalAcpiMethod function evaluates a specified ACPI method on a display adapter or on a child device of a display adapter. |
| [DXGKCB_EXCLUDE_ADAPTER_ACCESS callback](nc-dispmprt-dxgkcb-exclude-adapter-access.md) | The DxgkCbExcludeAdapterAccess function prevents all access to the display adapter and calls a provided DxgkProtectedCallback callback routine while in this protected state. |
| [DXGKCB_GET_DEVICE_INFORMATION callback](nc-dispmprt-dxgkcb-get-device-information.md) | The DxgkCbGetDeviceInformation function gets information, including the registry path and a list of translated resources, about a specified display adapter. |
| [DXGKCB_INDICATE_CHILD_STATUS callback](nc-dispmprt-dxgkcb-indicate-child-status.md) | The DxgkCbIndicateChildStatus function records the current status of a specified child device of a display adapter. |
| [DXGKCB_IS_DEVICE_PRESENT callback](nc-dispmprt-dxgkcb-is-device-present.md) | The DxgkCbIsDevicePresent function determines whether a specified PCI device is present. |
| [DXGKCB_LOG_ETW_EVENT callback](nc-dispmprt-dxgkcb-log-etw-event.md) | The DxgkCbLogEtwEvent function logs an Event Tracing for Windows (ETW) event. |
| [DXGKCB_MAP_MEMORY callback](nc-dispmprt-dxgkcb-map-memory.md) | The DxgkCbMapMemory function maps a range of translated physical addresses (associated with a memory resource assigned to a display adapter) into system space or the virtual address space of a user-mode process. |
| [DXGKCB_MIRACAST_REPORT_CHUNK_INFO callback](nc-dispmprt-dxgkcb-miracast-report-chunk-info.md) | Called by the display miniport driver to report info about an encode chunk. |
| [DXGKCB_MIRACAST_SEND_MESSAGE callback](nc-dispmprt-dxgkcb-miracast-send-message.md) | Sends an asynchronous message to the user-mode display driver. |
| [DXGKCB_MIRACAST_SEND_MESSAGE_CALLBACK callback](nc-dispmprt-dxgkcb-miracast-send-message-callback.md) | Called in kernel mode when the message that was sent to the user-mode driver with a call to the DxgkCbMiracastSendMessage function has completed or has been canceled. |
| [DXGKCB_QUERY_SERVICES callback](nc-dispmprt-dxgkcb-query-services.md) | The DxgkCbQueryServices function returns an interface implemented by the display port driver. |
| [DXGKCB_QUEUE_DPC callback](nc-dispmprt-dxgkcb-queue-dpc.md) | The DxgkCbQueueDpc function queues a deferred procedure call (DPC) for execution at IRQL DISPATCH_LEVEL. |
| [DXGKCB_READ_DEVICE_SPACE callback](nc-dispmprt-dxgkcb-read-device-space.md) | The DxgkCbReadDeviceSpace function reads from a device configuration space or the expansion ROM of a display adapter. |
| [DXGKCB_SYNCHRONIZE_EXECUTION callback](nc-dispmprt-dxgkcb-synchronize-execution.md) | The DxgkCbSynchronizeExecution function synchronizes a specified function, implemented by the display miniport driver, with the display miniport driver's DxgkDdiInterruptRoutine function. |
| [DXGKCB_UNMAP_MEMORY callback](nc-dispmprt-dxgkcb-unmap-memory.md) | The DxgkCbUnmapMemory function unmaps a range of addresses previously mapped by DxgkCbMapMemory. |
| [DXGKCB_WRITE_DEVICE_SPACE callback](nc-dispmprt-dxgkcb-write-device-space.md) | The DxgkCbWriteDeviceSpace function writes to a device configuration space or the expansion ROM of a display adapter. |
| [DXGKDDI_EXCHANGEPRESTARTINFO callback](nc-dispmprt-dxgkddi-exchangeprestartinfo.md) | Allows very simple data to be exchanged between the OS and driver which may be required prior to DxgkDdiStartDevice device being called and therefore cannot be queried through normal caps or adapter info DDIs. |
| [DXGKDDI_I2C_RECEIVE_DATA_FROM_DISPLAY callback](nc-dispmprt-dxgkddi-i2c-receive-data-from-display.md) | The DxgkDdiI2CReceiveDataFromDisplay returns data received from an I2C device in a monitor. |
| [DXGKDDI_I2C_TRANSMIT_DATA_TO_DISPLAY callback](nc-dispmprt-dxgkddi-i2c-transmit-data-to-display.md) | The DxgkDdiI2CTransmitDataToDisplay function transmits data to an I2C device in a monitor. |
| [DXGKDDI_MIRACAST_CREATE_CONTEXT callback](nc-dispmprt-dxgkddi-miracast-create-context.md) | Creates a kernel-mode context for a Miracast device. |
| [DXGKDDI_MIRACAST_DESTROY_CONTEXT callback](nc-dispmprt-dxgkddi-miracast-destroy-context.md) | Destroys an instance of a Miracast device. |
| [DXGKDDI_MIRACAST_HANDLE_IO_CONTROL callback](nc-dispmprt-dxgkddi-miracast-handle-io-control.md) | Called by the operating system to request that the display miniport driver process a synchronous I/O control request in response to a user-mode display driver call to the MiracastIoControl function. |
| [DXGKDDI_MIRACAST_QUERY_CAPS callback](nc-dispmprt-dxgkddi-miracast-query-caps.md) | Queries the Miracast capabilities of the current display adapter. |
| [DXGKDDI_OPM_CONFIGURE_PROTECTED_OUTPUT callback](nc-dispmprt-dxgkddi-opm-configure-protected-output.md) | The DxgkDdiOPMConfigureProtectedOutput function configures the given protected output object. |
| [DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT callback](nc-dispmprt-dxgkddi-opm-create-protected-output.md) | The DxgkDdiOPMCreateProtectedOutput function creates a new protected output object with Certified Output Protection Protocol (COPP) or OPM semantics. |
| [DXGKDDI_OPM_DESTROY_PROTECTED_OUTPUT callback](nc-dispmprt-dxgkddi-opm-destroy-protected-output.md) | The DxgkDdiOPMDestroyProtectedOutput function destroys the given protected output object. |
| [DXGKDDI_OPM_GET_CERTIFICATE callback](nc-dispmprt-dxgkddi-opm-get-certificate.md) | The DxgkDdiOPMGetCertificate function retrieves a certificate of the given type and size. |
| [DXGKDDI_OPM_GET_CERTIFICATE_SIZE callback](nc-dispmprt-dxgkddi-opm-get-certificate-size.md) | The DxgkDdiOPMGetCertificateSize function retrieves the size of a certificate of the given type. |
| [DXGKDDI_OPM_GET_COPP_COMPATIBLE_INFORMATION callback](nc-dispmprt-dxgkddi-opm-get-copp-compatible-information.md) | The DxgkDdiOPMGetCOPPCompatibleInformation function retrieves information that is compatible with the Certified Output Protection Protocol (COPP) from the given protected output object. |
| [DXGKDDI_OPM_GET_INFORMATION callback](nc-dispmprt-dxgkddi-opm-get-information.md) | The DxgkDdiOPMGetInformation function retrieves information from the given protected output object. |
| [DXGKDDI_OPM_GET_RANDOM_NUMBER callback](nc-dispmprt-dxgkddi-opm-get-random-number.md) | The DxgkDdiOPMGetRandomNumber function retrieves the given protected output object's 128-bit cryptographically secure random number. |
| [DXGKDDI_OPM_SET_SIGNING_KEY_AND_SEQUENCE_NUMBERS callback](nc-dispmprt-dxgkddi-opm-set-signing-key-and-sequence-numbers.md) | The DxgkDdiOPMSetSigningKeyAndSequenceNumbers function sets the given protected output object's signing key and two sequence numbers. |
| [DXGKDDI_PROTECTED_CALLBACK callback](nc-dispmprt-dxgkddi-protected-callback.md) | The DxgkProtectedCallback callback routine is implemented by the display miniport driver and is called by DxgkCbExcludeAdapterAccess during a protected state when all access to the display adapter is prevented. |
| [DXGKDDI_SETTARGETADJUSTEDCOLORIMETRY callback](nc-dispmprt-dxgkddi-settargetadjustedcolorimetry.md) | Reports the colorimetry values selected by the OS for a target. |
| [DXGKDDI_UNLOAD callback](nc-dispmprt-dxgkddi-unload.md) | The DxgkDdiUnload function frees any resources allocated during execution of the display miniport driver's DriverEntry function. |
| [DXGK_BRIGHTNESS_GET callback](nc-dispmprt-dxgk-brightness-get.md) | The DxgkDdiGetBrightness function retrieves the currently active brightness level of an integrated display panel. |
| [DXGK_BRIGHTNESS_GET_BACKLIGHT_REDUCTION callback](nc-dispmprt-dxgk-brightness-get-backlight-reduction.md) | Retrieves the current level of backlight reduction that is applied to the integrated display panel. |
| [DXGK_BRIGHTNESS_GET_CAPS callback](nc-dispmprt-dxgk-brightness-get-caps.md) | Retrieves brightness control capabilities of an integrated display panel. |
| [DXGK_BRIGHTNESS_GET_POSSIBLE callback](nc-dispmprt-dxgk-brightness-get-possible.md) | The DxgkDdiGetPossibleBrightness function retrieves the brightness levels that an integrated display panel supports. |
| [DXGK_BRIGHTNESS_SET callback](nc-dispmprt-dxgk-brightness-set.md) | The DxgkDdiSetBrightness function sets a new brightness level. |
| [DXGK_BRIGHTNESS_SET_BACKLIGHT_OPTIMIZATION callback](nc-dispmprt-dxgk-brightness-set-backlight-optimization.md) | Called by the Microsoft DirectX graphics kernel subsystem to set the level of optimization that the display miniport driver uses to control the brightness of an integrated display panel. |
| [DXGK_BRIGHTNESS_SET_STATE callback](nc-dispmprt-dxgk-brightness-set-state.md) | Enables smooth brightness control on an integrated display panel. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [DRIVER_INITIALIZATION_DATA structure](ns-dispmprt--driver-initialization-data.md) | The DRIVER_INITIALIZATION_DATA structure contains pointers to functions implemented by the display miniport driver. |
| [DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS structure](ns-dispmprt--dxgkarg-system-display-enable-flags.md) | Reserved for system use. Do not use it in your driver. |
| [DXGKRNL_INTERFACE structure](ns-dispmprt--dxgkrnl-interface.md) | The DXGKRNL_INTERFACE structure contains a handle to a display adapter and a set of function pointers. |
| [DXGK_AGP_INTERFACE structure](ns-dispmprt--dxgk-agp-interface.md) | The DXGK_AGP_INTERFACE structure contains pointers to functions in the AGP interface, which is implemented by the display port driver. |
| [DXGK_CHILD_CAPABILITIES structure](ns-dispmprt--dxgk-child-capabilities.md) | The DXGK_CHILD_CAPABILITIES structure contains information about the capabilities of an individual child device of a display adapter. |
| [DXGK_CHILD_CONTAINER_ID structure](ns-dispmprt--dxgk-child-container-id.md) | Contains the container ID for a child device that is connected to a display adapter. |
| [DXGK_CHILD_DESCRIPTOR structure](ns-dispmprt--dxgk-child-descriptor.md) | The DXGK_CHILD_DESCRIPTOR structure holds identification and capability information for an individual child device of the display adapter. |
| [DXGK_CHILD_STATUS structure](ns-dispmprt--dxgk-child-status.md) | The DXGK_CHILD_STATUS structure contains members that indicate the status of a child device of the display adapter. |
| [DXGK_DEBUG_REPORT_INTERFACE structure](ns-dispmprt--dxgk-debug-report-interface.md) | The DXGK_DEBUG_REPORT_INTERFACE structure contains pointers to functions in the Debug Report interface, which is implemented by the display port driver. |
| [DXGK_DEVICE_DESCRIPTOR structure](ns-dispmprt--dxgk-device-descriptor.md) | The DXGK_DEVICE_DESCRIPTOR structure is used by the display port driver to request that the display miniport driver return all or a portion of a monitor's Extended Display Identification Data (EDID). |
| [DXGK_DEVICE_INFO structure](ns-dispmprt--dxgk-device-info.md) | The DXGK_DEVICE_INFO structure holds information that describes a display adapter. |
| [DXGK_DISPLAY_OWNERSHIP_FLAGS structure](ns-dispmprt--dxgk-display-ownership-flags.md) | Structure filled in by OS upon successful completion of the DxgkCbAcquirePostDisplayOwnership2 callback to provide information about the display state a driver is inheriting. |
| [DXGK_FIRMWARE_TABLE_INTERFACE structure](ns-dispmprt--dxgk-firmware-table-interface.md) | Contains pointers to functions in the System Firmware Table interface that the display miniport driver can call to enumerate and read the system firmware table. |
| [DXGK_GENERIC_DESCRIPTOR structure](ns-dispmprt--dxgk-generic-descriptor.md) | The DXGK_GENERIC_DESCRIPTOR structure contains descriptive information about a child device of the display adapter. |
| [DXGK_I2C_INTERFACE structure](ns-dispmprt--dxgk-i2c-interface.md) | The DXGK_I2C_INTERFACE structure contains pointers to functions in the I2C interface, which is implemented by the display miniport driver. |
| [DXGK_INTEGRATED_DISPLAY_CHILD structure](ns-dispmprt--dxgk-integrated-display-child.md) | Gives information about the connected integrated display. |
| [DXGK_MIRACAST_CAPS structure](ns-dispmprt--dxgk-miracast-caps.md) | Used by a display miniport driver to identify capabilities of a Miracast device. |
| [DXGK_MIRACAST_DISPLAY_CALLBACKS structure](ns-dispmprt--dxgk-miracast-display-callbacks.md) | Contains pointers to functions in the Wireless display (Miracast) display callback interface that the display miniport driver can call to send messages and report encode chunk info. |
| [DXGK_MIRACAST_INTERFACE structure](ns-dispmprt--dxgk-miracast-interface.md) | Contains pointers to functions in the Wireless display (Miracast) interface that the display miniport driver implements to create, destroy, query, and control Miracast device resources. |
| [DXGK_OPM_INTERFACE structure](ns-dispmprt--dxgk-opm-interface.md) | The DXGK_OPM_INTERFACE structure contains pointers to functions in the Output Protection Manager (OPM) Interface, which is implemented by the display miniport driver. |
| [DXGK_OPM_INTERFACE_3 structure](ns-dispmprt--dxgk-opm-interface-3.md) | The DXGK_OPM_INTERFACE_3 structure contains pointers to functions in the Output Protection Manager (OPM) Interface, which is implemented by the display miniport driver. |
| [DXGK_PRE_START_INFO structure](ns-dispmprt--dxgk-pre-start-info.md) | Structure to allow very simple data to be exchanged between the OS and driver which may be required prior to start device being called and therefore cannot be queried through normal caps or adapter info DDIs. |
| [DXGK_SPB_INTERFACE structure](ns-dispmprt--dxgk-spb-interface.md) | Contains pointers to functions in the Simple Peripheral Bus (SPB) Interface that the display miniport driver can call to inspect and alter SPB resources. |
| [DXGK_START_INFO structure](ns-dispmprt--dxgk-start-info.md) | The DXGK_START_INFO structure holds information that is needed by the display miniport driver's DxgkDdiStartDevice function. |
| [DXGK_TIMED_OPERATION structure](ns-dispmprt--dxgk-timed-operation.md) | The DXGK_TIMED_OPERATION structure describes a timed operation, which is used in the Timed Operation Interface. |
| [DXGK_TIMED_OPERATION_INTERFACE structure](ns-dispmprt--dxgk-timed-operation-interface.md) | The DXGK_TIMED_OPERATION_INTERFACE structure contains pointers to functions in the Timed Operation Interface, which is implemented by the display port driver. |
| [DXGK_VIDEO_OUTPUT_CAPABILITIES structure](ns-dispmprt--dxgk-video-output-capabilities.md) | The DXGK_VIDEO_OUTPUT_CAPABILITIES structure contains information about the capabilities of a video output on a display adapter. |
| [KMDDOD_INITIALIZATION_DATA structure](ns-dispmprt--kmddod-initialization-data.md) | Contains pointers to functions implemented by a kernel mode display-only driver (KMDOD). The KMDOD's DriverEntry function provides the Microsoft DirectX graphics kernel subsystem with entry points by filling in the members of this structure. |
| [LINKED_DEVICE structure](ns-dispmprt--linked-device.md) | The LINKED_DEVICE structure holds information that describes a linked display adapter configuration. |
| [PDXGK_BRIGHTNESS_INTERFACE structure](ns-dispmprt-pdxgk-brightness-interface.md) | The DXGK_BRIGHTNESS_INTERFACE structure contains pointers to functions in the Panel Brightness Control Interface, which is implemented by the display miniport driver. |
| [PDXGK_BRIGHTNESS_INTERFACE_2 structure](ns-dispmprt-pdxgk-brightness-interface-2.md) | Contains pointers to functions in the Panel Brightness Control Interface Version 2. Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers that support adaptive and smooth brightness control. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [DOCKING_STATE enumeration](ne-dispmprt-docking-state.md) | The DOCKING_STATE enumeration is used to describe the state of a portable computer that can be attached to a docking station. |
| [DXGK_CHILD_DEVICE_TYPE enumeration](ne-dispmprt--dxgk-child-device-type.md) | The DXGK_CHILD_DEVICE_TYPE enumeration is used to indicate the type of a child device of the display adapter. |
| [DXGK_CHILD_STATUS_TYPE enumeration](ne-dispmprt--dxgk-child-status-type.md) | The DXGK_CHILD_STATUS_TYPE enumeration indicates the type of status being requested or reported for a child device of the display adapter. |
| [DXGK_EVENT_TYPE enumeration](ne-dispmprt--dxgk-event-type.md) | The DXGK_EVENT_TYPE enumeration indicates the event type in a call to the display miniport driver's DxgkDdiNotifyAcpiEvent function. |
| [DXGK_FRAMEBUFFER_STATE enumeration](ne-dispmprt--dxgk-framebuffer-state.md) | The frame buffer state is provided to the driver in order that the driver can infer details of the display configuration based on knowledge of how firmware and the driver will set a particular resolution even though only basic information is made directly available by the OS to the driver. |
| [DXGK_SERVICES enumeration](ne-dispmprt-dxgk-services.md) | The DXGK_SERVICES enumeration indicates the type of interface being requested by a call to the DxgkCbQueryServices function. |
| [DXGK_SURPRISE_REMOVAL_TYPE enumeration](ne-dispmprt--dxgk-surprise-removal-type.md) | Indicates the type of surprise removal event when an external display device is disconnected from the system. |
