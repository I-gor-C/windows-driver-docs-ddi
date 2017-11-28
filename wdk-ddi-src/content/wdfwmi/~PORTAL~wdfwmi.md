# Wdfwmi.h header


This header is used by unknown technology.

Wdfwmi.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [WDF_WMI_BUFFER_APPEND_STRING function](nf-wdfwmi-wdf-wmi-buffer-append-string.md) | The WDF_WMI_BUFFER_APPEND_STRING function copies a specified Unicode string into a specified buffer in the format that WMI requires. |
| [WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER function](nf-wdfwmi-wdf-wmi-instance-config-init-provider.md) | The WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER function initializes a WDF_WMI_INSTANCE_CONFIG structure and stores a specified handle to a WMI provider object. |
| [WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER_CONFIG function](nf-wdfwmi-wdf-wmi-instance-config-init-provider-config.md) | The WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER_CONFIG function initializes a WDF_WMI_INSTANCE_CONFIG structure and stores a pointer to a specified WDF_WMI_PROVIDER_CONFIG structure. |
| [WDF_WMI_PROVIDER_CONFIG_INIT function](nf-wdfwmi-wdf-wmi-provider-config-init.md) | The WDF_WMI_PROVIDER_CONFIG_INIT function initializes a WDF_WMI_PROVIDER_CONFIG structure. |
| [WdfWmiInstanceCreate function](nf-wdfwmi-wdfwmiinstancecreate.md) | The WdfWmiInstanceCreate method creates a WMI instance object that represents an instance of a WMI data provider. |
| [WdfWmiInstanceDeregister function](nf-wdfwmi-wdfwmiinstancederegister.md) | The WdfWmiInstanceDeregister method deregisters a specified instance of a WMI data provider from the system's WMI service. |
| [WdfWmiInstanceFireEvent function](nf-wdfwmi-wdfwmiinstancefireevent.md) | The WdfWmiInstanceFireEvent method sends a WMI event to WMI clients that have registered to receive event notification. |
| [WdfWmiInstanceGetDevice function](nf-wdfwmi-wdfwmiinstancegetdevice.md) | The WdfWmiInstanceGetDevice method returns a handle to the framework device object that is associated with a specified WMI instance object. |
| [WdfWmiInstanceGetProvider function](nf-wdfwmi-wdfwmiinstancegetprovider.md) | The WdfWmiInstanceGetProvider method returns a handle to the WMI provider object that is the parent object of a specified WMI instance object. |
| [WdfWmiInstanceRegister function](nf-wdfwmi-wdfwmiinstanceregister.md) | The WdfWmiInstanceRegister method registers a specified instance of a WMI data provider with the system's WMI service. |
| [WdfWmiProviderCreate function](nf-wdfwmi-wdfwmiprovidercreate.md) | The WdfWmiProviderCreate method creates a WMI provider object that represents a WMI data block. |
| [WdfWmiProviderGetDevice function](nf-wdfwmi-wdfwmiprovidergetdevice.md) | The WdfWmiProviderGetDevice method returns a handle to the framework device object that is the parent of a specified WMI provider object. |
| [WdfWmiProviderGetTracingHandle function](nf-wdfwmi-wdfwmiprovidergettracinghandle.md) | The WdfWmiProviderGetTracingHandle method returns a handle to the event logger of a WPP software tracing session. |
| [WdfWmiProviderIsEnabled function](nf-wdfwmi-wdfwmiproviderisenabled.md) | The WdfWmiProviderIsEnabled method determines if either data collection or event notification is enabled for a specified WMI data provider. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_WDF_WMI_INSTANCE_EXECUTE_METHOD callback](nc-wdfwmi-evt-wdf-wmi-instance-execute-method.md) | A driver's EvtWmiInstanceExecuteMethod callback function executes a specified method that the driver provides for a WMI data provider's instance. |
| [EVT_WDF_WMI_INSTANCE_QUERY_INSTANCE callback](nc-wdfwmi-evt-wdf-wmi-instance-query-instance.md) | A driver's EvtWmiInstanceQueryInstance callback function copies a WMI provider's instance data into a buffer for delivery to a WMI client. |
| [EVT_WDF_WMI_INSTANCE_SET_INSTANCE callback](nc-wdfwmi-evt-wdf-wmi-instance-set-instance.md) | A driver's EvtWmiInstanceSetInstance callback function sets all of a WMI data provider's instance data to values that a WMI client supplies. |
| [EVT_WDF_WMI_INSTANCE_SET_ITEM callback](nc-wdfwmi-evt-wdf-wmi-instance-set-item.md) | A driver's EvtWmiInstanceSetItem callback function sets a single item of a WMI data provider's instance data to a value that a WMI client supplies. |
| [EVT_WDF_WMI_PROVIDER_FUNCTION_CONTROL callback](nc-wdfwmi-evt-wdf-wmi-provider-function-control.md) | A driver's EvtWmiProviderFunctionControl callback function enables and disables the driver's support for collecting data and sending events for a specified WMI data provider. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [WDF_WMI_INSTANCE_CONFIG structure](ns-wdfwmi--wdf-wmi-instance-config.md) | The WDF_WMI_INSTANCE_CONFIG structure contains configuration information for an instance of a WMI data provider. |
| [WDF_WMI_PROVIDER_CONFIG structure](ns-wdfwmi--wdf-wmi-provider-config.md) | The WDF_WMI_PROVIDER_CONFIG structure contains configuration information for a driver's WMI data block. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [WDF_WMI_PROVIDER_CONTROL enumeration](ne-wdfwmi--wdf-wmi-provider-control.md) | The WDF_WMI_PROVIDER_CONTROL enumeration defines the type of control functions that a WMI data provider can support. |
| [WDF_WMI_PROVIDER_FLAGS enumeration](ne-wdfwmi--wdf-wmi-provider-flags.md) | The WDF_WMI_PROVIDER_FLAGS enumeration defines configuration flags for a driver's WMI data provider. |
