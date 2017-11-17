# Declarations in the wudfddi_types header
This header Wudfddi_Types contains these programming interfaces:

Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_EVENT_TYPE enumeration](ne-wudfddi-types--wdf-event-type.md) | The WDF_EVENT_TYPE enumeration specifies. |
| [WDF_DEVICE_HWACCESS_TARGET_SIZE enumeration](ne-wudfddi-types--wdf-device-hwaccess-target-size.md) | The WDF_DEVICE_HWACCESS_TARGET_SIZE enumeration is used internally by the framework. Do not use. |
| [WDF_PROPERTY_STORE_ROOT_CLASS enumeration](ne-wudfddi-types--wdf-property-store-root-class.md) | The WDF_PROPERTY_STORE_ROOT_CLASS enumeration identifies the registry keys that UMDF property stores represent. |
| [WDF_PNP_CAPABILITY enumeration](ne-wudfddi-types--wdf-pnp-capability.md) | The WDF_PNP_CAPABILITY enumeration contains values that identify Plug and Play (PnP) capabilities for a device. |
| [WDF_DEVICE_IO_BUFFER_RETRIEVAL enumeration](ne-wudfddi-types--wdf-device-io-buffer-retrieval.md) | The WDF_DEVICE_IO_BUFFER_RETRIEVAL enumeration is used to specify when UMDF makes an I/O request's buffers available to the driver. |
| [WDF_REQUEST_SEND_OPTIONS_FLAGS enumeration](ne-wudfddi-types--wdf-request-send-options-flags.md) | The WDF_REQUEST_SEND_OPTIONS_FLAGS enumeration type defines flags that a driver can specify when it calls IWDFIoRequest |
| [WDF_IO_TARGET_STATE enumeration](ne-wudfddi-types--wdf-io-target-state.md) | The WDF_IO_TARGET_STATE enumeration specifies the states that an I/O target can be in. |
| [WDF_IO_TARGET_SENT_IO_ACTION enumeration](ne-wudfddi-types--wdf-io-target-sent-io-action.md) | The WDF_IO_TARGET_SENT_IO_ACTION enumeration identifies the actions that the framework can take when a driver calls IWDFIoTargetStateManagement |
| [WDF_POWER_DEVICE_STATE enumeration](ne-wudfddi-types--wdf-power-device-state.md) | The WDF_POWER_DEVICE_STATE enumeration contains values that identify the power state that a device might support. |
| [WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS enumeration](ne-wudfddi-types--wdf-power-policy-idle-timeout-constants.md) | The WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS enumeration is reserved for internal use. |
| [WDF_CALLBACK_CONSTRAINT enumeration](ne-wudfddi-types--wdf-callback-constraint.md) | WDF_CALLBACK_CONSTRAINT enumeration |
| [WDF_TRI_STATE enumeration](ne-wudfddi-types--wdf-tri-state.md) | The WDF_TRI_STATE enumeration type defines three values that the framework uses for some structure members and function parameters. |
| [WDF_DEVICE_HWACCESS_TARGET_TYPE enumeration](ne-wudfddi-types--wdf-device-hwaccess-target-type.md) | The WDF_DEVICE_HWACCESS_TARGET_TYPE enumeration is used internally by the framework. Do not use. |
| [WDF_POWER_POLICY_S0_IDLE_CAPABILITIES enumeration](ne-wudfddi-types--wdf-power-policy-s0-idle-capabilities.md) | The WDF_POWER_POLICY_S0_IDLE_CAPABILITIES enumeration identifies the capabilities that a device can support when it enters a low-power state while it is idling. |
| [WDF_REQUEST_TYPE enumeration](ne-wudfddi-types--wdf-request-type.md) | The WDF_REQUEST_TYPE enumeration identifies the types of I/O requests that a UMDF request object can represent. |
| [WDF_KPROCESSOR_MODE enumeration](ne-wudfddi-types--wdf-kprocessor-mode.md) | The WDF_KPROCESSOR_MODE enumeration type identifies the processor modes in which a thread can execute. |
| [WDF_IO_QUEUE_DISPATCH_TYPE enumeration](ne-wudfddi-types--wdf-io-queue-dispatch-type.md) | The WDF_IO_QUEUE_DISPATCH_TYPE enumeration contains values that identify how a driver must receive requests from an I/O queue. |
| [WDF_PNP_STATE enumeration](ne-wudfddi-types--wdf-pnp-state.md) | The WDF_PNP_STATE enumeration contains values that identify the status of Plug and Play (PnP) for a device. |
| [WDF_POWER_POLICY_S0_IDLE_USER_CONTROL enumeration](ne-wudfddi-types--wdf-power-policy-s0-idle-user-control.md) | The WDF_POWER_POLICY_S0_IDLE_USER_CONTROL enumeration identifies whether a user can control a device's behavior when the device is idle and the system is in its working (S0) state. |
| [WDF_POWER_POLICY_SX_WAKE_USER_CONTROL enumeration](ne-wudfddi-types--wdf-power-policy-sx-wake-user-control.md) | The WDF_POWER_POLICY_SX_WAKE_USER_CONTROL enumeration identifies whether a user can control a device's ability to wake the system from a low system power state. |
| [WDF_IO_QUEUE_STATE enumeration](ne-wudfddi-types--wdf-io-queue-state.md) | The WDF_IO_QUEUE_STATE enumeration contains values that identify the state of an I/O queue. |
| [WDF_FILE_INFORMATION_CLASS enumeration](ne-wudfddi-types--wdf-file-information-class.md) | The WDF_FILE_INFORMATION_CLASS enumeration identifies the types of file information that a driver can obtain or set. |
| [WDF_DEVICE_IO_TYPE enumeration](ne-wudfddi-types--wdf-device-io-type.md) | The WDF_DEVICE_IO_TYPE enumeration is used to specify a method for accessing data buffers. |
| [WDF_PROPERTY_STORE_DISPOSITION enumeration](ne-wudfddi-types--wdf-property-store-disposition.md) | The WDF_PROPERTY_STORE_DISPOSITION enumeration contains values that indicate whether a registry value was created or already existed when a driver obtained a property store interface. |
| [WDF_REQUEST_STOP_ACTION_FLAGS enumeration](ne-wudfddi-types--wdf-request-stop-action-flags.md) | The WDF_REQUEST_STOP_ACTION_FLAGS enumeration contains values that identify the state of a stop action request in a call to the driver's IQueueCallbackIoStop |
| [WDF_PROPERTY_STORE_RETRIEVE_FLAGS enumeration](ne-wudfddi-types--wdf-property-store-retrieve-flags.md) | The WDF_PROPERTY_STORE_RETRIEVE_FLAGS enumeration contains values that indicate whether UMDF should create a registry key if the key does not already exist. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WUDF_DEVICE_POWER_POLICY_IDLE_SETTINGS structure](ns-wudfddi-types--wudf-device-power-policy-idle-settings.md) | TBD |
| [WDFMEMORY_OFFSET structure](ns-wudfddi-types--wdfmemory-offset.md) | The WDFMEMORY_OFFSET structure describes the location and size of information that is accessed within a memory block. |
| [UMDF_VERSION_DATA structure](ns-wudfddi-types-umdf-version-data.md) | The UMDF_VERSION_DATA structure describes a version of the framework. |
| [WDF_PROPERTY_STORE_ROOT structure](ns-wudfddi-types--wdf-property-store-root.md) | The WDF_PROPERTY_STORE_ROOT structure contains information that identifies a UMDF property store. |

This header is used in these topics:

- [wdf](..content/_wdf)
