# Wdfchildlist.h header


This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdfchildlist.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [WDF_CHILD_ADDRESS_DESCRIPTION_HEADER_INIT function](nf-wdfchildlist-wdf-child-address-description-header-init.md) | The WDF_CHILD_ADDRESS_DESCRIPTION_HEADER_INIT function initializes a WDF_CHILD_ADDRESS_DESCRIPTION_HEADER structure. |
| [WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT function](nf-wdfchildlist-wdf-child-identification-description-header-init.md) | The WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT function initializes a WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER structure. |
| [WDF_CHILD_LIST_CONFIG_INIT function](nf-wdfchildlist-wdf-child-list-config-init.md) | The WDF_CHILD_LIST_CONFIG_INIT function initializes a WDF_CHILD_LIST_CONFIG structure. |
| [WDF_CHILD_LIST_ITERATOR_INIT function](nf-wdfchildlist-wdf-child-list-iterator-init.md) | The WDF_CHILD_LIST_ITERATOR_INIT function initializes a WDF_CHILD_LIST_ITERATOR structure. |
| [WDF_CHILD_RETRIEVE_INFO_INIT function](nf-wdfchildlist-wdf-child-retrieve-info-init.md) | The WDF_CHILD_RETRIEVE_INFO_INIT function initializes a WDF_CHILD_RETRIEVE_INFO structure. |
| [WdfChildListAddOrUpdateChildDescriptionAsPresent function](nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent.md) | The WdfChildListAddOrUpdateChildDescriptionAsPresent method adds a new child description to a list of children or updates an existing child description. |
| [WdfChildListBeginIteration function](nf-wdfchildlist-wdfchildlistbeginiteration.md) | The WdfChildListBeginIteration method prepares the framework for retrieving items from a specified child list. |
| [WdfChildListBeginScan function](nf-wdfchildlist-wdfchildlistbeginscan.md) | The WdfChildListBeginScan method prepares a specified list of child devices so the driver can update the information in the list. |
| [WdfChildListCreate function](nf-wdfchildlist-wdfchildlistcreate.md) | The WdfChildListCreate method creates a child list for a specified parent device. |
| [WdfChildListEndIteration function](nf-wdfchildlist-wdfchildlistenditeration.md) | The WdfChildListEndIteration method processes modifications to a specified child list. |
| [WdfChildListEndScan function](nf-wdfchildlist-wdfchildlistendscan.md) | The WdfChildListEndScan method processes modifications to a specified child list. |
| [WdfChildListGetDevice function](nf-wdfchildlist-wdfchildlistgetdevice.md) | The WdfChildListGetDevice method returns a handle to the framework device object that represents the parent device of a specified child list. |
| [WdfChildListRequestChildEject function](nf-wdfchildlist-wdfchildlistrequestchildeject.md) | The WdfChildListRequestChildEject method informs the framework that a specified device is about to be ejected from its docking station. |
| [WdfChildListRetrieveAddressDescription function](nf-wdfchildlist-wdfchildlistretrieveaddressdescription.md) | The WdfChildListRetrieveAddressDescription method locates a child device that has a specified identification description and retrieves the device's address description. |
| [WdfChildListRetrieveNextDevice function](nf-wdfchildlist-wdfchildlistretrievenextdevice.md) | The WdfChildListRetrieveNextDevice method traverses a specified child list and retrieves the next child device that matches specified criteria. |
| [WdfChildListRetrievePdo function](nf-wdfchildlist-wdfchildlistretrievepdo.md) | The WdfChildListRetrievePdo method returns a handle to the framework device object that is associated with a specified child description in a child list. |
| [WdfChildListUpdateAllChildDescriptionsAsPresent function](nf-wdfchildlist-wdfchildlistupdateallchilddescriptionsaspresent.md) | The WdfChildListUpdateAllChildDescriptionsAsPresent method informs the framework that all of the child devices in a specified child list are plugged in and available. |
| [WdfChildListUpdateChildDescriptionAsMissing function](nf-wdfchildlist-wdfchildlistupdatechilddescriptionasmissing.md) | The WdfChildListUpdateChildDescriptionAsMissing method informs the framework that a specified child device is currently unplugged or otherwise unavailable. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_CLEANUP callback](nc-wdfchildlist-evt-wdf-child-list-address-description-cleanup.md) | A driver's EvtChildListAddressDescriptionCleanup event callback function frees any memory allocations for an address description that the driver's EvtChildListAddressDescriptionDuplicate callback function allocated. |
| [EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_COPY callback](nc-wdfchildlist-evt-wdf-child-list-address-description-copy.md) | A driver's EvtChildListAddressDescriptionCopy event callback function copies a child address description from one specified location to another. |
| [EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_DUPLICATE callback](nc-wdfchildlist-evt-wdf-child-list-address-description-duplicate.md) | A driver's EvtChildListAddressDescriptionDuplicate event callback function duplicates a child address description. |
| [EVT_WDF_CHILD_LIST_CREATE_DEVICE callback](nc-wdfchildlist-evt-wdf-child-list-create-device.md) | A bus driver'sEvtChildListCreateDevice event callback function creates a framework device object for a new device that has been dynamically enumerated. |
| [EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED callback](nc-wdfchildlist-evt-wdf-child-list-device-reenumerated.md) | A driver's EvtChildListDeviceReenumerated event callback function enables the driver to approve or cancel a reenumeration of a specified device. |
| [EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_CLEANUP callback](nc-wdfchildlist-evt-wdf-child-list-identification-description-cleanup.md) | A driver's EvtChildListIdentificationDescriptionCleanup event callback function frees any memory allocations for an identification description that the driver's EvtChildListIdentificationDescriptionDuplicate callback function allocated. |
| [EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_COMPARE callback](nc-wdfchildlist-evt-wdf-child-list-identification-description-compare.md) | A driver's EvtChildListIdentificationDescriptionCompare event callback function compares one child identification description with another. |
| [EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_COPY callback](nc-wdfchildlist-evt-wdf-child-list-identification-description-copy.md) | A driver's EvtChildListIdentificationDescriptionCopy event callback function copies a child identification description from one specified location to another. |
| [EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE callback](nc-wdfchildlist-evt-wdf-child-list-identification-description-duplicate.md) | A driver's EvtChildListIdentificationDescriptionDuplicate event callback function duplicates a child identification description. |
| [EVT_WDF_CHILD_LIST_SCAN_FOR_CHILDREN callback](nc-wdfchildlist-evt-wdf-child-list-scan-for-children.md) | A driver's EvtChildListScanForChildren event callback function must report all of the child devices that are present. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [WDF_CHILD_ADDRESS_DESCRIPTION_HEADER structure](ns-wdfchildlist--wdf-child-address-description-header.md) | The WDF_CHILD_ADDRESS_DESCRIPTION_HEADER structure is a header structure that must be the first member of every address description structure. |
| [WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER structure](ns-wdfchildlist--wdf-child-identification-description-header.md) | The WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER structure is a header structure that must be the first member of every identification description structure. |
| [WDF_CHILD_LIST_CONFIG structure](ns-wdfchildlist--wdf-child-list-config.md) | The WDF_CHILD_LIST_CONFIG structure contains configuration information for a list of child devices. |
| [WDF_CHILD_LIST_ITERATOR structure](ns-wdfchildlist--wdf-child-list-iterator.md) | The WDF_CHILD_LIST_ITERATOR structure identifies the type of child devices that the framework will retrieve when a driver calls WdfChildListRetrieveNextDevice. |
| [WDF_CHILD_RETRIEVE_INFO structure](ns-wdfchildlist--wdf-child-retrieve-info.md) | The WDF_CHILD_RETRIEVE_INFO structure contains information about a child device that is obtained by calling WdfChildListRetrieveNextDevice or WdfChildListRetrievePdo. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS enumeration](ne-wdfchildlist--wdf-child-list-retrieve-device-status.md) | The WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS enumeration defines device status values that the framework stores in a driver's WDF_CHILD_RETRIEVE_INFO structure. |
| [WDF_RETRIEVE_CHILD_FLAGS enumeration](ne-wdfchildlist--wdf-retrieve-child-flags.md) | The WDF_RETRIEVE_CHILD_FLAGS enumeration defines flags that a driver can set before calling WdfChildListBeginIteration. |
