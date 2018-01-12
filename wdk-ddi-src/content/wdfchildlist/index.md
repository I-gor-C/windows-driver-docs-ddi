---
UID: NA:wdfchildlist
---

# Wdfchildlist.h header

## -description

This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdfchildlist.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [PFN_WDFCHILDLISTADDORUPDATECHILDDESCRIPTIONASPRESENT function](nc-wdfchildlist-pfn_wdfchildlistaddorupdatechilddescriptionaspresent.md) | The WdfChildListAddOrUpdateChildDescriptionAsPresent method adds a new child description to a list of children or updates an existing child description. |
| [PFN_WDFCHILDLISTBEGINITERATION function](nc-wdfchildlist-pfn_wdfchildlistbeginiteration.md) | The WdfChildListBeginIteration method prepares the framework for retrieving items from a specified child list. |
| [PFN_WDFCHILDLISTBEGINSCAN function](nc-wdfchildlist-pfn_wdfchildlistbeginscan.md) | The WdfChildListBeginScan method prepares a specified list of child devices so the driver can update the information in the list. |
| [PFN_WDFCHILDLISTCREATE function](nc-wdfchildlist-pfn_wdfchildlistcreate.md) | The WdfChildListCreate method creates a child list for a specified parent device. |
| [PFN_WDFCHILDLISTENDITERATION function](nc-wdfchildlist-pfn_wdfchildlistenditeration.md) | The WdfChildListEndIteration method processes modifications to a specified child list. |
| [PFN_WDFCHILDLISTENDSCAN function](nc-wdfchildlist-pfn_wdfchildlistendscan.md) | The WdfChildListEndScan method processes modifications to a specified child list. |
| [PFN_WDFCHILDLISTGETDEVICE function](nc-wdfchildlist-pfn_wdfchildlistgetdevice.md) | The WdfChildListGetDevice method returns a handle to the framework device object that represents the parent device of a specified child list. |
| [PFN_WDFCHILDLISTREQUESTCHILDEJECT function](nc-wdfchildlist-pfn_wdfchildlistrequestchildeject.md) | The WdfChildListRequestChildEject method informs the framework that a specified device is about to be ejected from its docking station. |
| [PFN_WDFCHILDLISTRETRIEVEADDRESSDESCRIPTION function](nc-wdfchildlist-pfn_wdfchildlistretrieveaddressdescription.md) | The WdfChildListRetrieveAddressDescription method locates a child device that has a specified identification description and retrieves the device's address description. |
| [PFN_WDFCHILDLISTRETRIEVENEXTDEVICE function](nc-wdfchildlist-pfn_wdfchildlistretrievenextdevice.md) | The WdfChildListRetrieveNextDevice method traverses a specified child list and retrieves the next child device that matches specified criteria. |
| [PFN_WDFCHILDLISTRETRIEVEPDO function](nc-wdfchildlist-pfn_wdfchildlistretrievepdo.md) | The WdfChildListRetrievePdo method returns a handle to the framework device object that is associated with a specified child description in a child list. |
| [PFN_WDFCHILDLISTUPDATEALLCHILDDESCRIPTIONSASPRESENT function](nc-wdfchildlist-pfn_wdfchildlistupdateallchilddescriptionsaspresent.md) | The WdfChildListUpdateAllChildDescriptionsAsPresent method informs the framework that all of the child devices in a specified child list are plugged in and available. |
| [PFN_WDFCHILDLISTUPDATECHILDDESCRIPTIONASMISSING function](nc-wdfchildlist-pfn_wdfchildlistupdatechilddescriptionasmissing.md) | The WdfChildListUpdateChildDescriptionAsMissing method informs the framework that a specified child device is currently unplugged or otherwise unavailable. |
| [WDF_CHILD_ADDRESS_DESCRIPTION_HEADER_INIT function](nf-wdfchildlist-wdf_child_address_description_header_init.md) | The WDF_CHILD_ADDRESS_DESCRIPTION_HEADER_INIT function initializes a WDF_CHILD_ADDRESS_DESCRIPTION_HEADER structure. |
| [WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT function](nf-wdfchildlist-wdf_child_identification_description_header_init.md) | The WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT function initializes a WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER structure. |
| [WDF_CHILD_LIST_CONFIG_INIT function](nf-wdfchildlist-wdf_child_list_config_init.md) | The WDF_CHILD_LIST_CONFIG_INIT function initializes a WDF_CHILD_LIST_CONFIG structure. |
| [WDF_CHILD_LIST_ITERATOR_INIT function](nf-wdfchildlist-wdf_child_list_iterator_init.md) | The WDF_CHILD_LIST_ITERATOR_INIT function initializes a WDF_CHILD_LIST_ITERATOR structure. |
| [WDF_CHILD_RETRIEVE_INFO_INIT function](nf-wdfchildlist-wdf_child_retrieve_info_init.md) | The WDF_CHILD_RETRIEVE_INFO_INIT function initializes a WDF_CHILD_RETRIEVE_INFO structure. |
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

## Structures

| Title   | Description   |
| ---- |:---- |
| [_WDF_CHILD_ADDRESS_DESCRIPTION_HEADER structure](ns-wdfchildlist-_wdf_child_address_description_header.md) | The WDF_CHILD_ADDRESS_DESCRIPTION_HEADER structure is a header structure that must be the first member of every address description structure. |
| [_WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER structure](ns-wdfchildlist-_wdf_child_identification_description_header.md) | The WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER structure is a header structure that must be the first member of every identification description structure. |
| [_WDF_CHILD_LIST_CONFIG structure](ns-wdfchildlist-_wdf_child_list_config.md) | The WDF_CHILD_LIST_CONFIG structure contains configuration information for a list of child devices. |
| [_WDF_CHILD_LIST_ITERATOR structure](ns-wdfchildlist-_wdf_child_list_iterator.md) | The WDF_CHILD_LIST_ITERATOR structure identifies the type of child devices that the framework will retrieve when a driver calls WdfChildListRetrieveNextDevice. |
| [_WDF_CHILD_RETRIEVE_INFO structure](ns-wdfchildlist-_wdf_child_retrieve_info.md) | The WDF_CHILD_RETRIEVE_INFO structure contains information about a child device that is obtained by calling WdfChildListRetrieveNextDevice or WdfChildListRetrievePdo. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS enumeration](ne-wdfchildlist-_wdf_child_list_retrieve_device_status.md) | The WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS enumeration defines device status values that the framework stores in a driver's WDF_CHILD_RETRIEVE_INFO structure. |
| [_WDF_RETRIEVE_CHILD_FLAGS enumeration](ne-wdfchildlist-_wdf_retrieve_child_flags.md) | The WDF_RETRIEVE_CHILD_FLAGS enumeration defines flags that a driver can set before calling WdfChildListBeginIteration. |
