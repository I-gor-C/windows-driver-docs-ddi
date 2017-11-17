# Declarations in the wdffdo header
This header Wdffdo contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfFdoInitSetFilter function](nf-wdffdo-wdffdoinitsetfilter.md) | The WdfFdoInitSetFilter method identifies the calling driver as an upper-level or lower-level filter driver, for a specified device. |
| [WdfFdoAddStaticChild function](nf-wdffdo-wdffdoaddstaticchild.md) | The WdfFdoAddStaticChild method adds a specified device to a function driver's list of child devices that have been identified by static enumeration. |
| [WdfFdoUnlockStaticChildListFromIteration function](nf-wdffdo-wdffdounlockstaticchildlistfromiteration.md) | The WdfFdoUnlockStaticChildListFromIteration method unlocks the list of child devices for a specified device and processes any changes to the list that the driver made while the list was locked. |
| [WDF_FDO_EVENT_CALLBACKS_INIT function](nf-wdffdo-wdf-fdo-event-callbacks-init.md) | The WDF_FDO_EVENT_CALLBACKS_INIT function initializes a WDF_FDO_EVENT_CALLBACKS structure. |
| [WdfFdoInitSetDefaultChildListConfig function](nf-wdffdo-wdffdoinitsetdefaultchildlistconfig.md) | The WdfFdoInitSetDefaultChildListConfig method configures a bus driver's default child list. |
| [WdfFdoRetrieveNextStaticChild function](nf-wdffdo-wdffdoretrievenextstaticchild.md) | The WdfFdoRetrieveNextStaticChild method retrieves a handle to the next framework device object in a list of child devices. |
| [WdfFdoInitQueryProperty function](nf-wdffdo-wdffdoinitqueryproperty.md) | The WdfFdoInitQueryProperty method retrieves a specified device property. |
| [WdfFdoGetDefaultChildList function](nf-wdffdo-wdffdogetdefaultchildlist.md) | The WdfFdoGetDefaultChildList method returns a handle to a specified device's default child list. |
| [WdfFdoInitSetEventCallbacks function](nf-wdffdo-wdffdoinitseteventcallbacks.md) | The WdfFdoInitSetEventCallbacks method registers a framework-based function driver's event callback functions, for a specified device. |
| [WdfFdoInitOpenRegistryKey function](nf-wdffdo-wdffdoinitopenregistrykey.md) | The WdfFdoInitOpenRegistryKey method opens a device's hardware key or a driver's software key in the registry and creates a framework registry-key object that represents the registry key. |
| [WdfFdoInitWdmGetPhysicalDevice function](nf-wdffdo-wdffdoinitwdmgetphysicaldevice.md) | The WdfFdoInitWdmGetPhysicalDevice method retrieves a device's WDM physical device object (PDO). |
| [WdfFdoQueryForInterface function](nf-wdffdo-wdffdoqueryforinterface.md) | The WdfFdoQueryForInterface method obtains access to another driver's GUID-identified interface. |
| [WdfFdoInitAllocAndQueryProperty function](nf-wdffdo-wdffdoinitallocandqueryproperty.md) | The WdfFdoInitAllocAndQueryProperty method allocates a buffer and retrieves a specified device property. |
| [WdfFdoInitQueryPropertyEx function](nf-wdffdo-wdffdoinitquerypropertyex.md) | The WdfFdoInitQueryPropertyEx method retrieves a specified device property. |
| [WdfFdoInitAllocAndQueryPropertyEx function](nf-wdffdo-wdffdoinitallocandquerypropertyex.md) | The WdfFdoInitAllocAndQueryPropertyEx method allocates a buffer and retrieves a specified device property. |
| [WdfFdoLockStaticChildListForIteration function](nf-wdffdo-wdffdolockstaticchildlistforiteration.md) | The WdfFdoLockStaticChildListForIteration method prepares the framework for retrieving items from the static child list that belongs to a specified parent device. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFFDOINITALLOCANDQUERYPROPERTYEX callback function](nc-wdffdo-pfn-wdffdoinitallocandquerypropertyex.md) | TBD |
| [PFN_WDFFDOINITQUERYPROPERTYEX callback function](nc-wdffdo-pfn-wdffdoinitquerypropertyex.md) | TBD |
| [PFN_WDFFDOUNLOCKSTATICCHILDLISTFROMITERATION callback function](nc-wdffdo-pfn-wdffdounlockstaticchildlistfromiteration.md) | TBD |
| [PFN_WDFFDOINITWDMGETPHYSICALDEVICE callback function](nc-wdffdo-pfn-wdffdoinitwdmgetphysicaldevice.md) | TBD |
| [PFN_WDFFDOGETDEFAULTCHILDLIST callback function](nc-wdffdo-pfn-wdffdogetdefaultchildlist.md) | TBD |
| [PFN_WDFFDOLOCKSTATICCHILDLISTFORITERATION callback function](nc-wdffdo-pfn-wdffdolockstaticchildlistforiteration.md) | TBD |
| [PFN_WDFFDOQUERYFORINTERFACE callback function](nc-wdffdo-pfn-wdffdoqueryforinterface.md) | TBD |
| [EVT_WDF_DEVICE_REMOVE_ADDED_RESOURCES callback](nc-wdffdo-evt-wdf-device-remove-added-resources.md) | A driver's EvtDeviceRemoveAddedResources event callback function removes hardware resources that the driver's EvtDeviceFilterAddResourceRequirements callback function added. |
| [PFN_WDFFDOINITSETDEFAULTCHILDLISTCONFIG callback function](nc-wdffdo-pfn-wdffdoinitsetdefaultchildlistconfig.md) | TBD |
| [PFN_WDFFDOINITSETEVENTCALLBACKS callback function](nc-wdffdo-pfn-wdffdoinitseteventcallbacks.md) | TBD |
| [PFN_WDFFDORETRIEVENEXTSTATICCHILD callback function](nc-wdffdo-pfn-wdffdoretrievenextstaticchild.md) | TBD |
| [PFN_WDFFDOINITALLOCANDQUERYPROPERTY callback function](nc-wdffdo-pfn-wdffdoinitallocandqueryproperty.md) | TBD |
| [PFN_WDFFDOINITSETFILTER callback function](nc-wdffdo-pfn-wdffdoinitsetfilter.md) | TBD |
| [PFN_WDFFDOINITQUERYPROPERTY callback function](nc-wdffdo-pfn-wdffdoinitqueryproperty.md) | TBD |
| [PFN_WDFFDOADDSTATICCHILD callback function](nc-wdffdo-pfn-wdffdoaddstaticchild.md) | TBD |
| [PFN_WDFFDOINITOPENREGISTRYKEY callback function](nc-wdffdo-pfn-wdffdoinitopenregistrykey.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_FDO_EVENT_CALLBACKS structure](ns-wdffdo--wdf-fdo-event-callbacks.md) | The WDF_FDO_EVENT_CALLBACKS structure contains pointers to a function driver's PnP event callback functions. |

This header is used in these topics:

- [wdf](..content/_wdf)
