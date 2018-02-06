---
UID: NA:swenum
ms.assetid: 631903f3-c726-3652-b341-ccbe7cdd2a44
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# swenum.h header



swenum.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_SWENUM_GET_BUS_ID](ni-swenum-ioctl_swenum_get_bus_id.md) |  |
| [IOCTL_SWENUM_INSTALL_INTERFACE](ni-swenum-ioctl_swenum_install_interface.md) |  |
| [IOCTL_SWENUM_REMOVE_INTERFACE](ni-swenum-ioctl_swenum_remove_interface.md) |  |


## Functions
| Title | Description |
| ---- |:---- |
| [KsCreateBusEnumObject](nf-swenum-kscreatebusenumobject.md) | The KsCreateBusEnumObject function creates a demand-load bus enumerator object and initializes it for use with the demand-load bus enumerator services. |
| [KsDereferenceSoftwareBusObject](nf-swenum-ksdereferencesoftwarebusobject.md) | The KsDereferenceSoftwareBusObject function decrements the reference count of the demand-load bus enumerator object's PDO. |
| [KsGetBusEnumIdentifier](nf-swenum-ksgetbusenumidentifier.md) | The KsGetBusEnumIdentifier function retrieves the software bus enumerator identifier for the bus device associated with the given IRP. |
| [KsGetBusEnumParentFDOFromChildPDO](nf-swenum-ksgetbusenumparentfdofromchildpdo.md) | The KsGetBusEnumParentFDOFromChildPDO function retrieves the FDO of the parent of the given child PDO. |
| [KsGetBusEnumPnpDeviceObject](nf-swenum-ksgetbusenumpnpdeviceobject.md) | The KsGetBusEnumPnpDeviceObject function retrieves the Plug and Play device object attached to the given device object. |
| [KsInstallBusEnumInterface](nf-swenum-ksinstallbusenuminterface.md) | The KsInstallBusEnumInterface function installs an interface to the demand-load bus enumerator object. |
| [KsIsBusEnumChildDevice](nf-swenum-ksisbusenumchilddevice.md) | The KsIsBusEnumChildDevice function determines if the given device object is a child device of the demand-load bus enumerator object. |
| [KsQuerySoftwareBusInterface](nf-swenum-ksquerysoftwarebusinterface.md) | The KsQuerySoftwareBusInterface function creates a buffer from the paged pool and copies the reference string associated with the demand-load bus enumerator object's PDO into the buffer. |
| [KsReferenceSoftwareBusObject](nf-swenum-ksreferencesoftwarebusobject.md) | The KsReferenceSoftwareBusObject function increments the reference count of the demand-load bus enumerator object's PDO. |
| [KsRemoveBusEnumInterface](nf-swenum-ksremovebusenuminterface.md) | The KsRemoveBusEnumInterface function removes an interface to the demand-load bus enumerator object. |
| [KsServiceBusEnumCreateRequest](nf-swenum-ksservicebusenumcreaterequest.md) | The KsServiceBusEnumCreateRequest function services IRP_MJ_CREATE requests for the software bus device interface. |
| [KsServiceBusEnumPnpRequest](nf-swenum-ksservicebusenumpnprequest.md) | The KsServiceBusEnumPnpRequest function services IRP_MJ_PNP requests on behalf of the demand-load bus enumerator object that was created with KsCreateBusEnumObject. |



## Structures
| Title | Description |
| ---- |:---- |
| [_BUS_INTERFACE_SWENUM](ns-swenum-_bus_interface_swenum.md) | The BUS_INTERFACE_SWENUM structure describes the demand-load bus enumerator object's interface. |
| [_SWENUM_INSTALL_INTERFACE](ns-swenum-_swenum_install_interface.md) | The SWENUM_INSTALL_INTERFACE structure describes a specific demand-load bus enumerator object interface to install. |