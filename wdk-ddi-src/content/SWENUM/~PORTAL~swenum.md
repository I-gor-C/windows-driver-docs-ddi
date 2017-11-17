# Declarations in the swenum header
This header Swenum contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [KsGetBusEnumIdentifier function](nf-swenum-ksgetbusenumidentifier.md) | The KsGetBusEnumIdentifier function retrieves the software bus enumerator identifier for the bus device associated with the given IRP. |
| [KsServiceBusEnumPnpRequest function](nf-swenum-ksservicebusenumpnprequest.md) | The KsServiceBusEnumPnpRequest function services IRP_MJ_PNP requests on behalf of the demand-load bus enumerator object that was created with KsCreateBusEnumObject. |
| [KsIsBusEnumChildDevice function](nf-swenum-ksisbusenumchilddevice.md) | The KsIsBusEnumChildDevice function determines if the given device object is a child device of the demand-load bus enumerator object. |
| [KsCreateBusEnumObject function](nf-swenum-kscreatebusenumobject.md) | The KsCreateBusEnumObject function creates a demand-load bus enumerator object and initializes it for use with the demand-load bus enumerator services. |
| [KsDereferenceSoftwareBusObject function](nf-swenum-ksdereferencesoftwarebusobject.md) | The KsDereferenceSoftwareBusObject function decrements the reference count of the demand-load bus enumerator object's PDO. |
| [KsReferenceSoftwareBusObject function](nf-swenum-ksreferencesoftwarebusobject.md) | The KsReferenceSoftwareBusObject function increments the reference count of the demand-load bus enumerator object's PDO. |
| [KsRemoveBusEnumInterface function](nf-swenum-ksremovebusenuminterface.md) | The KsRemoveBusEnumInterface function removes an interface to the demand-load bus enumerator object. |
| [DEFINE_GUIDEX function](nf-swenum-define-guidex.md) | TBD |
| [KsGetBusEnumParentFDOFromChildPDO function](nf-swenum-ksgetbusenumparentfdofromchildpdo.md) | The KsGetBusEnumParentFDOFromChildPDO function retrieves the FDO of the parent of the given child PDO. |
| [KsInstallBusEnumInterface function](nf-swenum-ksinstallbusenuminterface.md) | The KsInstallBusEnumInterface function installs an interface to the demand-load bus enumerator object. |
| [KsQuerySoftwareBusInterface function](nf-swenum-ksquerysoftwarebusinterface.md) | The KsQuerySoftwareBusInterface function creates a buffer from the paged pool and copies the reference string associated with the demand-load bus enumerator object's PDO into the buffer. |
| [KsGetBusEnumPnpDeviceObject function](nf-swenum-ksgetbusenumpnpdeviceobject.md) | The KsGetBusEnumPnpDeviceObject function retrieves the Plug and Play device object attached to the given device object. |
| [KsServiceBusEnumCreateRequest function](nf-swenum-ksservicebusenumcreaterequest.md) | The KsServiceBusEnumCreateRequest function services IRP_MJ_CREATE requests for the software bus device interface. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SWENUM_INSTALL_INTERFACE structure](ns-swenum--swenum-install-interface.md) | The SWENUM_INSTALL_INTERFACE structure describes a specific demand-load bus enumerator object interface to install. |
| [BUS_INTERFACE_SWENUM structure](ns-swenum--bus-interface-swenum.md) | The BUS_INTERFACE_SWENUM structure describes the demand-load bus enumerator object's interface. |
| [BUSID_SoftwareDeviceEnumerator structure](ns-swenum-busid-softwaredeviceenumerator.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFNQUERYREFERENCESTRING callback function](nc-swenum-pfnqueryreferencestring.md) | TBD |
| [PFNREFERENCEDEVICEOBJECT callback function](nc-swenum-pfnreferencedeviceobject.md) | TBD |
| [PFNDEREFERENCEDEVICEOBJECT callback function](nc-swenum-pfndereferencedeviceobject.md) | TBD |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_SWENUM_REMOVE_INTERFACE IOCTL](ni-swenum-ioctl-swenum-remove-interface.md) | The IOCTL_SWENUM_REMOVE_INTERFACE control code... |
| [IOCTL_SWENUM_INSTALL_INTERFACE IOCTL](ni-swenum-ioctl-swenum-install-interface.md) | The IOCTL_SWENUM_INSTALL_INTERFACE control code... |
| [IOCTL_SWENUM_GET_BUS_ID IOCTL](ni-swenum-ioctl-swenum-get-bus-id.md) | The IOCTL_SWENUM_GET_BUS_ID control code... |

This header is used in these topics:

- [stream](..content/_stream)
