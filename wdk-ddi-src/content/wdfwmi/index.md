---
UID: NA:wdfwmi
---

# Wdfwmi.h header

## -description

This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdfwmi.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [PFN_WDFWMIINSTANCECREATE function](nc-wdfwmi-pfn_wdfwmiinstancecreate.md) | The WdfWmiInstanceCreate method creates a WMI instance object that represents an instance of a WMI data provider. |
| [PFN_WDFWMIINSTANCEDEREGISTER function](nc-wdfwmi-pfn_wdfwmiinstancederegister.md) | The WdfWmiInstanceDeregister method deregisters a specified instance of a WMI data provider from the system's WMI service. |
| [PFN_WDFWMIINSTANCEFIREEVENT function](nc-wdfwmi-pfn_wdfwmiinstancefireevent.md) | The WdfWmiInstanceFireEvent method sends a WMI event to WMI clients that have registered to receive event notification. |
| [PFN_WDFWMIINSTANCEGETDEVICE function](nc-wdfwmi-pfn_wdfwmiinstancegetdevice.md) | The WdfWmiInstanceGetDevice method returns a handle to the framework device object that is associated with a specified WMI instance object. |
| [PFN_WDFWMIINSTANCEGETPROVIDER function](nc-wdfwmi-pfn_wdfwmiinstancegetprovider.md) | The WdfWmiInstanceGetProvider method returns a handle to the WMI provider object that is the parent object of a specified WMI instance object. |
| [PFN_WDFWMIINSTANCEREGISTER function](nc-wdfwmi-pfn_wdfwmiinstanceregister.md) | The WdfWmiInstanceRegister method registers a specified instance of a WMI data provider with the system's WMI service. |
| [PFN_WDFWMIPROVIDERCREATE function](nc-wdfwmi-pfn_wdfwmiprovidercreate.md) | The WdfWmiProviderCreate method creates a WMI provider object that represents a WMI data block. |
| [PFN_WDFWMIPROVIDERGETDEVICE function](nc-wdfwmi-pfn_wdfwmiprovidergetdevice.md) | The WdfWmiProviderGetDevice method returns a handle to the framework device object that is the parent of a specified WMI provider object. |
| [PFN_WDFWMIPROVIDERGETTRACINGHANDLE function](nc-wdfwmi-pfn_wdfwmiprovidergettracinghandle.md) | The WdfWmiProviderGetTracingHandle method returns a handle to the event logger of a WPP software tracing session. |
| [PFN_WDFWMIPROVIDERISENABLED function](nc-wdfwmi-pfn_wdfwmiproviderisenabled.md) | The WdfWmiProviderIsEnabled method determines if either data collection or event notification is enabled for a specified WMI data provider. |
| [WDF_WMI_BUFFER_APPEND_STRING function](nf-wdfwmi-wdf_wmi_buffer_append_string.md) | The WDF_WMI_BUFFER_APPEND_STRING function copies a specified Unicode string into a specified buffer in the format that WMI requires. |
| [WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER function](nf-wdfwmi-wdf_wmi_instance_config_init_provider.md) | The WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER function initializes a WDF_WMI_INSTANCE_CONFIG structure and stores a specified handle to a WMI provider object. |
| [WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER_CONFIG function](nf-wdfwmi-wdf_wmi_instance_config_init_provider_config.md) | The WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER_CONFIG function initializes a WDF_WMI_INSTANCE_CONFIG structure and stores a pointer to a specified WDF_WMI_PROVIDER_CONFIG structure. |
| [WDF_WMI_PROVIDER_CONFIG_INIT function](nf-wdfwmi-wdf_wmi_provider_config_init.md) | The WDF_WMI_PROVIDER_CONFIG_INIT function initializes a WDF_WMI_PROVIDER_CONFIG structure. |
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

## Structures

| Title   | Description   |
| ---- |:---- |
| [_WDF_WMI_INSTANCE_CONFIG structure](ns-wdfwmi-_wdf_wmi_instance_config.md) | The WDF_WMI_INSTANCE_CONFIG structure contains configuration information for an instance of a WMI data provider. |
| [_WDF_WMI_PROVIDER_CONFIG structure](ns-wdfwmi-_wdf_wmi_provider_config.md) | The WDF_WMI_PROVIDER_CONFIG structure contains configuration information for a driver's WMI data block. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_WDF_WMI_PROVIDER_CONTROL enumeration](ne-wdfwmi-_wdf_wmi_provider_control.md) | The WDF_WMI_PROVIDER_CONTROL enumeration defines the type of control functions that a WMI data provider can support. |
| [_WDF_WMI_PROVIDER_FLAGS enumeration](ne-wdfwmi-_wdf_wmi_provider_flags.md) | The WDF_WMI_PROVIDER_FLAGS enumeration defines configuration flags for a driver's WMI data provider. |
