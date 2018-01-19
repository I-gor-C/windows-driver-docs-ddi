---
UID : NA:wdffdo
ms.assetid : 3b4b9cb8-8139-3f49-a13d-762e25571789
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# wdffdo.h header



wdffdo.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [EVT_WDF_DEVICE_REMOVE_ADDED_RESOURCES](nc-wdffdo-evt_wdf_device_remove_added_resources.md) | A driver's EvtDeviceRemoveAddedResources event callback function removes hardware resources that the driver's EvtDeviceFilterAddResourceRequirements callback function added. |
| [WDF_FDO_EVENT_CALLBACKS_INIT](nf-wdffdo-wdf_fdo_event_callbacks_init.md) | The WDF_FDO_EVENT_CALLBACKS_INIT function initializes a WDF_FDO_EVENT_CALLBACKS structure. |
| [WdfFdoAddStaticChild](nf-wdffdo-wdffdoaddstaticchild.md) | The WdfFdoAddStaticChild method adds a specified device to a function driver's list of child devices that have been identified by static enumeration. |
| [WdfFdoGetDefaultChildList](nf-wdffdo-wdffdogetdefaultchildlist.md) | The WdfFdoGetDefaultChildList method returns a handle to a specified device's default child list. |
| [WdfFdoInitAllocAndQueryProperty](nf-wdffdo-wdffdoinitallocandqueryproperty.md) | The WdfFdoInitAllocAndQueryProperty method allocates a buffer and retrieves a specified device property. |
| [WdfFdoInitAllocAndQueryPropertyEx](nf-wdffdo-wdffdoinitallocandquerypropertyex.md) | The WdfFdoInitAllocAndQueryPropertyEx method allocates a buffer and retrieves a specified device property. |
| [WdfFdoInitOpenRegistryKey](nf-wdffdo-wdffdoinitopenregistrykey.md) | The WdfFdoInitOpenRegistryKey method opens a device's hardware key or a driver's software key in the registry and creates a framework registry-key object that represents the registry key. |
| [WdfFdoInitQueryProperty](nf-wdffdo-wdffdoinitqueryproperty.md) | The WdfFdoInitQueryProperty method retrieves a specified device property. |
| [WdfFdoInitQueryPropertyEx](nf-wdffdo-wdffdoinitquerypropertyex.md) | The WdfFdoInitQueryPropertyEx method retrieves a specified device property. |
| [WdfFdoInitSetDefaultChildListConfig](nf-wdffdo-wdffdoinitsetdefaultchildlistconfig.md) | The WdfFdoInitSetDefaultChildListConfig method configures a bus driver's default child list. |
| [WdfFdoInitSetEventCallbacks](nf-wdffdo-wdffdoinitseteventcallbacks.md) | The WdfFdoInitSetEventCallbacks method registers a framework-based function driver's event callback functions, for a specified device. |
| [WdfFdoInitSetFilter](nf-wdffdo-wdffdoinitsetfilter.md) | The WdfFdoInitSetFilter method identifies the calling driver as an upper-level or lower-level filter driver, for a specified device. |
| [WdfFdoInitWdmGetPhysicalDevice](nf-wdffdo-wdffdoinitwdmgetphysicaldevice.md) | The WdfFdoInitWdmGetPhysicalDevice method retrieves a device's WDM physical device object (PDO). |
| [WdfFdoLockStaticChildListForIteration](nf-wdffdo-wdffdolockstaticchildlistforiteration.md) | The WdfFdoLockStaticChildListForIteration method prepares the framework for retrieving items from the static child list that belongs to a specified parent device. |
| [WdfFdoQueryForInterface](nf-wdffdo-wdffdoqueryforinterface.md) | The WdfFdoQueryForInterface method obtains access to another driver's GUID-identified interface. |
| [WdfFdoRetrieveNextStaticChild](nf-wdffdo-wdffdoretrievenextstaticchild.md) | The WdfFdoRetrieveNextStaticChild method retrieves a handle to the next framework device object in a list of child devices. |
| [WdfFdoUnlockStaticChildListFromIteration](nf-wdffdo-wdffdounlockstaticchildlistfromiteration.md) | The WdfFdoUnlockStaticChildListFromIteration method unlocks the list of child devices for a specified device and processes any changes to the list that the driver made while the list was locked. |



## Structures
| Title | Description |
| ---- |:---- |
| [_WDF_FDO_EVENT_CALLBACKS](ns-wdffdo-_wdf_fdo_event_callbacks.md) | The WDF_FDO_EVENT_CALLBACKS structure contains pointers to a function driver's PnP event callback functions. |