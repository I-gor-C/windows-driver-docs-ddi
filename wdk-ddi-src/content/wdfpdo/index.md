---
UID: NA:wdfpdo
---

# Wdfpdo.h header

## -description

This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdfpdo.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [PFN_WDFPDOADDEJECTIONRELATIONSPHYSICALDEVICE function](nc-wdfpdo-pfn_wdfpdoaddejectionrelationsphysicaldevice.md) | The WdfPdoAddEjectionRelationsPhysicalDevice method indicates that a specified device is ejected when another specified device is ejected. |
| [PFN_WDFPDOCLEAREJECTIONRELATIONSDEVICES function](nc-wdfpdo-pfn_wdfpdoclearejectionrelationsdevices.md) | The WdfPdoClearEjectionRelationsDevices method removes all devices from the list of devices that must be ejected when a specified device is ejected. |
| [PFN_WDFPDOGETPARENT function](nc-wdfpdo-pfn_wdfpdogetparent.md) | The WdfPdoGetParent method returns a handle to the framework device object that represents the parent device of a specified device. |
| [PFN_WDFPDOINITADDCOMPATIBLEID function](nc-wdfpdo-pfn_wdfpdoinitaddcompatibleid.md) | The WdfPdoInitAddCompatibleID method adds a compatible ID to the list of compatible IDs for a child device. |
| [PFN_WDFPDOINITADDDEVICETEXT function](nc-wdfpdo-pfn_wdfpdoinitadddevicetext.md) | The WdfPdoInitAddDeviceText method adds a device description and device location to a device, for a specified locale. |
| [PFN_WDFPDOINITADDHARDWAREID function](nc-wdfpdo-pfn_wdfpdoinitaddhardwareid.md) | The WdfPdoInitAddHardwareID method adds a hardware ID to the list of hardware IDs for a child device. |
| [PFN_WDFPDOINITALLOCATE function](nc-wdfpdo-pfn_wdfpdoinitallocate.md) | The WdfPdoInitAllocate method allocates a WDFDEVICE_INIT structure for a framework-based bus driver, which the bus driver uses when reporting a new device. |
| [PFN_WDFPDOINITALLOWFORWARDINGREQUESTTOPARENT function](nc-wdfpdo-pfn_wdfpdoinitallowforwardingrequesttoparent.md) | The WdfPdoInitAllowForwardingRequestToParent method enables a driver's ability to call WdfRequestForwardToParentDeviceIoQueue. |
| [PFN_WDFPDOINITASSIGNCONTAINERID function](nc-wdfpdo-pfn_wdfpdoinitassigncontainerid.md) | The WdfPdoInitAssignContainerID method updates the container ID for a child device. |
| [PFN_WDFPDOINITASSIGNDEVICEID function](nc-wdfpdo-pfn_wdfpdoinitassigndeviceid.md) | The WdfPdoInitAssignDeviceID method updates the device ID for a child device. |
| [PFN_WDFPDOINITASSIGNINSTANCEID function](nc-wdfpdo-pfn_wdfpdoinitassigninstanceid.md) | The WdfPdoInitAssignInstanceID method updates the instance ID for a child device. |
| [PFN_WDFPDOINITSETDEFAULTLOCALE function](nc-wdfpdo-pfn_wdfpdoinitsetdefaultlocale.md) | The WdfPdoInitSetDefaultLocale method sets a device's default locale. |
| [PFN_WDFPDOINITSETEVENTCALLBACKS function](nc-wdfpdo-pfn_wdfpdoinitseteventcallbacks.md) | The WdfPdoInitSetEventCallbacks method registers a bus driver's event callback functions. |
| [PFN_WDFPDOMARKMISSING function](nc-wdfpdo-pfn_wdfpdomarkmissing.md) | The WdfPdoMarkMissing method informs the framework that a device is no longer accessible. |
| [PFN_WDFPDOREMOVEEJECTIONRELATIONSPHYSICALDEVICE function](nc-wdfpdo-pfn_wdfpdoremoveejectionrelationsphysicaldevice.md) | The WdfPdoRemoveEjectionRelationsPhysicalDevice method removes a specified device from the list of devices that must be ejected when another specified device is ejected. |
| [PFN_WDFPDOREQUESTEJECT function](nc-wdfpdo-pfn_wdfpdorequesteject.md) | The WdfPdoRequestEject method informs the framework that a specified device is about to be ejected from its docking station. |
| [PFN_WDFPDORETRIEVEADDRESSDESCRIPTION function](nc-wdfpdo-pfn_wdfpdoretrieveaddressdescription.md) | The WdfPdoRetrieveAddressDescription method retrieves the address description that is associated with a specified framework device object. |
| [PFN_WDFPDORETRIEVEIDENTIFICATIONDESCRIPTION function](nc-wdfpdo-pfn_wdfpdoretrieveidentificationdescription.md) | The WdfPdoRetrieveIdentificationDescription method retrieves the identification description that is associated with a specified framework device object. |
| [PFN_WDFPDOUPDATEADDRESSDESCRIPTION function](nc-wdfpdo-pfn_wdfpdoupdateaddressdescription.md) | The WdfPdoUpdateAddressDescription method updates the address description that is associated with a specified framework device object. |
| [WDF_PDO_EVENT_CALLBACKS_INIT function](nf-wdfpdo-wdf_pdo_event_callbacks_init.md) | The WDF_PDO_EVENT_CALLBACKS_INIT function initializes a WDF_PDO_EVENT_CALLBACKS structure. |
| [WdfPdoAddEjectionRelationsPhysicalDevice function](nf-wdfpdo-wdfpdoaddejectionrelationsphysicaldevice.md) | The WdfPdoAddEjectionRelationsPhysicalDevice method indicates that a specified device is ejected when another specified device is ejected. |
| [WdfPdoClearEjectionRelationsDevices function](nf-wdfpdo-wdfpdoclearejectionrelationsdevices.md) | The WdfPdoClearEjectionRelationsDevices method removes all devices from the list of devices that must be ejected when a specified device is ejected. |
| [WdfPdoGetParent function](nf-wdfpdo-wdfpdogetparent.md) | The WdfPdoGetParent method returns a handle to the framework device object that represents the parent device of a specified device. |
| [WdfPdoInitAddCompatibleID function](nf-wdfpdo-wdfpdoinitaddcompatibleid.md) | The WdfPdoInitAddCompatibleID method adds a compatible ID to the list of compatible IDs for a child device. |
| [WdfPdoInitAddDeviceText function](nf-wdfpdo-wdfpdoinitadddevicetext.md) | The WdfPdoInitAddDeviceText method adds a device description and device location to a device, for a specified locale. |
| [WdfPdoInitAddHardwareID function](nf-wdfpdo-wdfpdoinitaddhardwareid.md) | The WdfPdoInitAddHardwareID method adds a hardware ID to the list of hardware IDs for a child device. |
| [WdfPdoInitAllocate function](nf-wdfpdo-wdfpdoinitallocate.md) | The WdfPdoInitAllocate method allocates a WDFDEVICE_INIT structure for a framework-based bus driver, which the bus driver uses when reporting a new device. |
| [WdfPdoInitAllowForwardingRequestToParent function](nf-wdfpdo-wdfpdoinitallowforwardingrequesttoparent.md) | The WdfPdoInitAllowForwardingRequestToParent method enables a driver's ability to call WdfRequestForwardToParentDeviceIoQueue. |
| [WdfPdoInitAssignContainerID function](nf-wdfpdo-wdfpdoinitassigncontainerid.md) | The WdfPdoInitAssignContainerID method updates the container ID for a child device. |
| [WdfPdoInitAssignDeviceID function](nf-wdfpdo-wdfpdoinitassigndeviceid.md) | The WdfPdoInitAssignDeviceID method updates the device ID for a child device. |
| [WdfPdoInitAssignInstanceID function](nf-wdfpdo-wdfpdoinitassigninstanceid.md) | The WdfPdoInitAssignInstanceID method updates the instance ID for a child device. |
| [WdfPdoInitAssignRawDevice function](nf-wdfpdo-wdfpdoinitassignrawdevice.md) | The WdfPdoInitAssignRawDevice method indicates that the calling driver can support a specified device in raw mode. |
| [WdfPdoInitSetDefaultLocale function](nf-wdfpdo-wdfpdoinitsetdefaultlocale.md) | The WdfPdoInitSetDefaultLocale method sets a device's default locale. |
| [WdfPdoInitSetEventCallbacks function](nf-wdfpdo-wdfpdoinitseteventcallbacks.md) | The WdfPdoInitSetEventCallbacks method registers a bus driver's event callback functions. |
| [WdfPdoMarkMissing function](nf-wdfpdo-wdfpdomarkmissing.md) | The WdfPdoMarkMissing method informs the framework that a device is no longer accessible. |
| [WdfPdoRemoveEjectionRelationsPhysicalDevice function](nf-wdfpdo-wdfpdoremoveejectionrelationsphysicaldevice.md) | The WdfPdoRemoveEjectionRelationsPhysicalDevice method removes a specified device from the list of devices that must be ejected when another specified device is ejected. |
| [WdfPdoRequestEject function](nf-wdfpdo-wdfpdorequesteject.md) | The WdfPdoRequestEject method informs the framework that a specified device is about to be ejected from its docking station. |
| [WdfPdoRetrieveAddressDescription function](nf-wdfpdo-wdfpdoretrieveaddressdescription.md) | The WdfPdoRetrieveAddressDescription method retrieves the address description that is associated with a specified framework device object. |
| [WdfPdoRetrieveIdentificationDescription function](nf-wdfpdo-wdfpdoretrieveidentificationdescription.md) | The WdfPdoRetrieveIdentificationDescription method retrieves the identification description that is associated with a specified framework device object. |
| [WdfPdoUpdateAddressDescription function](nf-wdfpdo-wdfpdoupdateaddressdescription.md) | The WdfPdoUpdateAddressDescription method updates the address description that is associated with a specified framework device object. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_WDF_PDO_EVENT_CALLBACKS structure](ns-wdfpdo-_wdf_pdo_event_callbacks.md) | The WDF_PDO_EVENT_CALLBACKS structure is the dispatch table for a bus driver's event callback functions. |
