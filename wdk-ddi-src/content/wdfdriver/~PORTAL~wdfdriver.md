# Declarations in the wdfdriver header
This header Wdfdriver contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfGetDriver function](nf-wdfdriver-wdfgetdriver.md) | The WdfGetDriver method returns a handle to the framework driver object that represents the calling driver. |
| [WDF_DRIVER_CONFIG_COMPANION_INIT function](nf-wdfdriver-wdf-driver-config-companion-init.md) | TBD |
| [WdfDriverGetRegistryPath function](nf-wdfdriver-wdfdrivergetregistrypath.md) | The WdfDriverGetRegistryPath method retrieves the path to the driver's registry key in the registry's Services tree. |
| [WdfDriverIsVersionAvailable function](nf-wdfdriver-wdfdriverisversionavailable.md) | The WdfDriverIsVersionAvailable method returns a Boolean value that indicates whether the driver is running with a specified version of the Kernel-Mode Driver Framework library. |
| [WDF_DRIVER_CONFIG_INIT function](nf-wdfdriver-wdf-driver-config-init.md) | The WDF_DRIVER_CONFIG_INIT function initializes a driver's WDF_DRIVER_CONFIG structure. |
| [WdfDriverRetrieveVersionString function](nf-wdfdriver-wdfdriverretrieveversionstring.md) | The WdfDriverRetrieveVersionString method retrieves a Unicode string that identifies the version of the Kernel-Mode Driver Framework that the driver is running with. |
| [WdfDriverOpenParametersRegistryKey function](nf-wdfdriver-wdfdriveropenparametersregistrykey.md) | The WdfDriverOpenParametersRegistryKey method opens the driver's Parameters registry key and retrieves a handle to a framework registry-key object that represents the key. |
| [WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT function](nf-wdfdriver-wdf-driver-version-available-params-init.md) | The WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT function initializes a WDF_DRIVER_VERSION_AVAILABLE_PARAMS structure. |
| [WdfWdmDriverGetWdfDriverHandle function](nf-wdfdriver-wdfwdmdrivergetwdfdriverhandle.md) | The WdfWdmDriverGetWdfDriverHandle method returns a handle to the framework driver object that is associated with a specified Windows Driver Model (WDM) driver object. |
| [WdfDriverRegisterTraceInfo function](nf-wdfdriver-wdfdriverregistertraceinfo.md) | The WdfDriverRegisterTraceInfo method is reserved for internal use only. |
| [WdfDriverWdmGetDriverObject function](nf-wdfdriver-wdfdriverwdmgetdriverobject.md) | The WdfDriverWdmGetDriverObject method retrieves a pointer to the Windows Driver Model (WDM) driver object that is associated with a specified framework driver object. |
| [WdfDriverCreate function](nf-wdfdriver-wdfdrivercreate.md) | The WdfDriverCreate method creates a framework driver object for the calling driver. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFDRIVERCREATE callback function](nc-wdfdriver-pfn-wdfdrivercreate.md) | TBD |
| [PFN_WDFDRIVERWDMGETDRIVEROBJECT callback function](nc-wdfdriver-pfn-wdfdriverwdmgetdriverobject.md) | TBD |
| [PFN_WDFDRIVERRETRIEVEVERSIONSTRING callback function](nc-wdfdriver-pfn-wdfdriverretrieveversionstring.md) | TBD |
| [EVT_WDF_DRIVER_UNLOAD callback](nc-wdfdriver-evt-wdf-driver-unload.md) | A driver's EvtDriverUnload event callback function performs operations that must take place before the driver is unloaded. |
| [EVT_WDF_DRIVER_DEVICE_ADD callback](nc-wdfdriver-evt-wdf-driver-device-add.md) | A driver's EvtDriverDeviceAdd event callback function performs device initialization operations when the Plug and Play (PnP) manager reports the existence of a device. |
| [PFN_WDFDRIVEROPENPARAMETERSREGISTRYKEY callback function](nc-wdfdriver-pfn-wdfdriveropenparametersregistrykey.md) | TBD |
| [PFN_WDFDRIVERGETREGISTRYPATH callback function](nc-wdfdriver-pfn-wdfdrivergetregistrypath.md) | TBD |
| [EVT_WDF_TRACE_CALLBACK callback function](nc-wdfdriver-evt-wdf-trace-callback.md) | TBD |
| [PFN_WDFDRIVERREGISTERTRACEINFO callback function](nc-wdfdriver-pfn-wdfdriverregistertraceinfo.md) | TBD |
| [PFN_WDFWDMDRIVERGETWDFDRIVERHANDLE callback function](nc-wdfdriver-pfn-wdfwdmdrivergetwdfdriverhandle.md) | TBD |
| [PFN_WDFDRIVERISVERSIONAVAILABLE callback function](nc-wdfdriver-pfn-wdfdriverisversionavailable.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DRIVER_VERSION_AVAILABLE_PARAMS structure](ns-wdfdriver--wdf-driver-version-available-params.md) | The WDF_DRIVER_VERSION_AVAILABLE_PARAMS structure specifies major and minor version numbers for the Kernel-Mode Driver Framework's library. |
| [WDF_DRIVER_CONFIG structure](ns-wdfdriver--wdf-driver-config.md) | The WDF_DRIVER_CONFIG structure is an input parameter to WdfDriverCreate. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DRIVER_INIT_FLAGS enumeration](ne-wdfdriver--wdf-driver-init-flags.md) | The WDF_DRIVER_INIT_FLAGS enumeration specifies driver initialization flags. |

This header is used in these topics:

- [wdf](..content/_wdf)
