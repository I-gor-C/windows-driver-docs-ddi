# Declarations in the wdfpdo header
This header Wdfpdo contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFPDOINITALLOWFORWARDINGREQUESTTOPARENT callback function](nc-wdfpdo-pfn-wdfpdoinitallowforwardingrequesttoparent.md) | TBD |
| [EVT_WDF_DEVICE_DISABLE_WAKE_AT_BUS callback](nc-wdfpdo-evt-wdf-device-disable-wake-at-bus.md) | A bus driver's EvtDeviceDisableWakeAtBus event callback function performs bus-level operations that disable the ability of one of the bus's devices to trigger a wake-up signal on the bus. |
| [EVT_WDF_DEVICE_SET_LOCK callback](nc-wdfpdo-evt-wdf-device-set-lock.md) | A driver's EvtDeviceSetLock event callback function locks the specified device so that it cannot be ejected, or unlocks the device so that it can be ejected. |
| [EVT_WDF_DEVICE_RESOURCE_REQUIREMENTS_QUERY callback](nc-wdfpdo-evt-wdf-device-resource-requirements-query.md) | A bus driver's EvtDeviceResourceRequirementsQuery event callback function creates a resource requirements list that represents the device's required hardware resources. |
| [PFN_WDFPDOINITADDHARDWAREID callback function](nc-wdfpdo-pfn-wdfpdoinitaddhardwareid.md) | TBD |
| [PFN_WDFPDOREMOVEEJECTIONRELATIONSPHYSICALDEVICE callback function](nc-wdfpdo-pfn-wdfpdoremoveejectionrelationsphysicaldevice.md) | TBD |
| [PFN_WDFPDORETRIEVEIDENTIFICATIONDESCRIPTION callback function](nc-wdfpdo-pfn-wdfpdoretrieveidentificationdescription.md) | TBD |
| [PFN_WDFPDOADDEJECTIONRELATIONSPHYSICALDEVICE callback function](nc-wdfpdo-pfn-wdfpdoaddejectionrelationsphysicaldevice.md) | TBD |
| [PFN_WDFPDOINITSETDEFAULTLOCALE callback function](nc-wdfpdo-pfn-wdfpdoinitsetdefaultlocale.md) | TBD |
| [EVT_WDF_DEVICE_EJECT callback](nc-wdfpdo-evt-wdf-device-eject.md) | A driver's EvtDeviceEject event callback function handles operations that are necessary to eject a device from its docking station. |
| [PFN_WDFPDOGETPARENT callback function](nc-wdfpdo-pfn-wdfpdogetparent.md) | TBD |
| [PFN_WDFPDOUPDATEADDRESSDESCRIPTION callback function](nc-wdfpdo-pfn-wdfpdoupdateaddressdescription.md) | TBD |
| [PFN_WDFPDOINITADDCOMPATIBLEID callback function](nc-wdfpdo-pfn-wdfpdoinitaddcompatibleid.md) | TBD |
| [PFN_WDFPDOREQUESTEJECT callback function](nc-wdfpdo-pfn-wdfpdorequesteject.md) | TBD |
| [PFN_WDFPDOINITALLOCATE callback function](nc-wdfpdo-pfn-wdfpdoinitallocate.md) | TBD |
| [PFN_WDFPDOINITADDDEVICETEXT callback function](nc-wdfpdo-pfn-wdfpdoinitadddevicetext.md) | TBD |
| [PFN_WDFPDOINITASSIGNCONTAINERID callback function](nc-wdfpdo-pfn-wdfpdoinitassigncontainerid.md) | TBD |
| [EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS callback](nc-wdfpdo-evt-wdf-device-enable-wake-at-bus.md) | A bus driver's EvtDeviceEnableWakeAtBus event callback function performs bus-level operations that enable one of the bus's devices to trigger a wake-up signal on the bus. |
| [PFN_WDFPDOCLEAREJECTIONRELATIONSDEVICES callback function](nc-wdfpdo-pfn-wdfpdoclearejectionrelationsdevices.md) | TBD |
| [PFN_WDFPDOINITSETEVENTCALLBACKS callback function](nc-wdfpdo-pfn-wdfpdoinitseteventcallbacks.md) | TBD |
| [PFN_WDFPDOINITASSIGNDEVICEID callback function](nc-wdfpdo-pfn-wdfpdoinitassigndeviceid.md) | TBD |
| [EVT_WDF_DEVICE_REPORTED_MISSING callback](nc-wdfpdo-evt-wdf-device-reported-missing.md) | A bus driver's EvtDeviceReportedMissing event callback function informs the driver that the framework has reported the physical device object (PDO) missing to the Plug and Play manager. |
| [PFN_WDFPDOINITASSIGNRAWDEVICE callback function](nc-wdfpdo-pfn-wdfpdoinitassignrawdevice.md) | TBD |
| [PFN_WDFPDORETRIEVEADDRESSDESCRIPTION callback function](nc-wdfpdo-pfn-wdfpdoretrieveaddressdescription.md) | TBD |
| [PFN_WDFPDOMARKMISSING callback function](nc-wdfpdo-pfn-wdfpdomarkmissing.md) | TBD |
| [PFN_WDFPDOINITASSIGNINSTANCEID callback function](nc-wdfpdo-pfn-wdfpdoinitassigninstanceid.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_PDO_EVENT_CALLBACKS structure](ns-wdfpdo--wdf-pdo-event-callbacks.md) | The WDF_PDO_EVENT_CALLBACKS structure is the dispatch table for a bus driver's event callback functions. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfPdoRetrieveAddressDescription function](nf-wdfpdo-wdfpdoretrieveaddressdescription.md) | The WdfPdoRetrieveAddressDescription method retrieves the address description that is associated with a specified framework device object. |
| [WdfPdoInitAssignContainerID function](nf-wdfpdo-wdfpdoinitassigncontainerid.md) | The WdfPdoInitAssignContainerID method updates the container ID for a child device. |
| [WdfPdoInitAddHardwareID function](nf-wdfpdo-wdfpdoinitaddhardwareid.md) | The WdfPdoInitAddHardwareID method adds a hardware ID to the list of hardware IDs for a child device. |
| [WdfPdoInitAllocate function](nf-wdfpdo-wdfpdoinitallocate.md) | The WdfPdoInitAllocate method allocates a WDFDEVICE_INIT structure for a framework-based bus driver, which the bus driver uses when reporting a new device. |
| [WdfPdoAddEjectionRelationsPhysicalDevice function](nf-wdfpdo-wdfpdoaddejectionrelationsphysicaldevice.md) | The WdfPdoAddEjectionRelationsPhysicalDevice method indicates that a specified device is ejected when another specified device is ejected. |
| [WdfPdoInitSetDefaultLocale function](nf-wdfpdo-wdfpdoinitsetdefaultlocale.md) | The WdfPdoInitSetDefaultLocale method sets a device's default locale. |
| [WdfPdoInitAssignInstanceID function](nf-wdfpdo-wdfpdoinitassigninstanceid.md) | The WdfPdoInitAssignInstanceID method updates the instance ID for a child device. |
| [WdfPdoInitAddDeviceText function](nf-wdfpdo-wdfpdoinitadddevicetext.md) | The WdfPdoInitAddDeviceText method adds a device description and device location to a device, for a specified locale. |
| [WdfPdoUpdateAddressDescription function](nf-wdfpdo-wdfpdoupdateaddressdescription.md) | The WdfPdoUpdateAddressDescription method updates the address description that is associated with a specified framework device object. |
| [WdfPdoInitAssignDeviceID function](nf-wdfpdo-wdfpdoinitassigndeviceid.md) | The WdfPdoInitAssignDeviceID method updates the device ID for a child device. |
| [WdfPdoInitAddCompatibleID function](nf-wdfpdo-wdfpdoinitaddcompatibleid.md) | The WdfPdoInitAddCompatibleID method adds a compatible ID to the list of compatible IDs for a child device. |
| [WdfPdoInitAllowForwardingRequestToParent function](nf-wdfpdo-wdfpdoinitallowforwardingrequesttoparent.md) | The WdfPdoInitAllowForwardingRequestToParent method enables a driver's ability to call WdfRequestForwardToParentDeviceIoQueue. |
| [WdfPdoRemoveEjectionRelationsPhysicalDevice function](nf-wdfpdo-wdfpdoremoveejectionrelationsphysicaldevice.md) | The WdfPdoRemoveEjectionRelationsPhysicalDevice method removes a specified device from the list of devices that must be ejected when another specified device is ejected. |
| [WdfPdoClearEjectionRelationsDevices function](nf-wdfpdo-wdfpdoclearejectionrelationsdevices.md) | The WdfPdoClearEjectionRelationsDevices method removes all devices from the list of devices that must be ejected when a specified device is ejected. |
| [WdfPdoInitSetEventCallbacks function](nf-wdfpdo-wdfpdoinitseteventcallbacks.md) | The WdfPdoInitSetEventCallbacks method registers a bus driver's event callback functions. |
| [WdfPdoInitAssignRawDevice function](nf-wdfpdo-wdfpdoinitassignrawdevice.md) | The WdfPdoInitAssignRawDevice method indicates that the calling driver can support a specified device in raw mode. |
| [WdfPdoRequestEject function](nf-wdfpdo-wdfpdorequesteject.md) | The WdfPdoRequestEject method informs the framework that a specified device is about to be ejected from its docking station. |
| [WdfPdoGetParent function](nf-wdfpdo-wdfpdogetparent.md) | The WdfPdoGetParent method returns a handle to the framework device object that represents the parent device of a specified device. |
| [WdfPdoMarkMissing function](nf-wdfpdo-wdfpdomarkmissing.md) | The WdfPdoMarkMissing method informs the framework that a device is no longer accessible. |
| [WDF_PDO_EVENT_CALLBACKS_INIT function](nf-wdfpdo-wdf-pdo-event-callbacks-init.md) | The WDF_PDO_EVENT_CALLBACKS_INIT function initializes a WDF_PDO_EVENT_CALLBACKS structure. |
| [WdfPdoRetrieveIdentificationDescription function](nf-wdfpdo-wdfpdoretrieveidentificationdescription.md) | The WdfPdoRetrieveIdentificationDescription method retrieves the identification description that is associated with a specified framework device object. |

This header is used in these topics:

- [wdf](..content/_wdf)
