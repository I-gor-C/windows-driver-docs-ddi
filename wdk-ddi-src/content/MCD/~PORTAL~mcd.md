# Declarations in the mcd header
This header Mcd contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [DriverEntry function](nf-mcd-driverentry.md) | TBD |
| [ChangerSetAccess function](nf-mcd-changersetaccess.md) | ChangerSetAccess handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_SET_ACCESS. |
| [ChangerGetElementStatus function](nf-mcd-changergetelementstatus.md) | ChangerGetElementStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_ELEMENT_STATUS. |
| [ChangerMoveMedium function](nf-mcd-changermovemedium.md) | ChangerMoveMedium handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_MOVE_MEDIUM. |
| [MCDebugPrint function](nf-mcd-mcdebugprint.md) | TBD |
| [ChangerClassAllocatePool function](nf-mcd-changerclassallocatepool.md) | The ChangerClassAllocatePool function allocates pool memory. |
| [ChangerClassCreate function](nf-mcd-changerclasscreate.md) | TBD |
| [ChangerVerifyInquiry function](nf-mcd-changerverifyinquiry.md) | TBD |
| [ChangerInitializeElementStatus function](nf-mcd-changerinitializeelementstatus.md) | ChangerInitializeElementStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_INITIALIZE_ELEMENT_STATUS. |
| [ChangerAdditionalExtensionSize function](nf-mcd-changeradditionalextensionsize.md) | ChangerAdditionalExtensionSize indicates the number of bytes the changer miniclass driver requires to store device-specific information in the device extension. |
| [ChangerInitialize function](nf-mcd-changerinitialize.md) | ChangerInitialize readies the changer to receive other requests. |
| [ChangerSetPosition function](nf-mcd-changersetposition.md) | ChangerSetPosition handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_SET_POSITION. |
| [ChangerPerformDiagnostics function](nf-mcd-changerperformdiagnostics.md) | ChangerPerformDiagnostics performs diagnostic tests on the changer device. |
| [DebugPrint function](nf-mcd-debugprint.md) | TBD |
| [ChangerExchangeMedium function](nf-mcd-changerexchangemedium.md) | ChangerExchangeMedium handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_EXCHANGE_MEDIUM. |
| [ChangerGetParameters function](nf-mcd-changergetparameters.md) | ChangerGetParameters handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_PARAMETERS. |
| [ChangerClassFreePool function](nf-mcd-changerclassfreepool.md) | The ChangerClassFreePool routine frees pool memory previously allocated using ChangerClassAllocatePool. |
| [ChangerGetProductData function](nf-mcd-changergetproductdata.md) | ChangerGetProductData handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_PRODUCT_DATA. |
| [ChangerQueryVolumeTags function](nf-mcd-changerqueryvolumetags.md) | ChangerQueryVolumeTags handles the device-specific aspects of a device-control IRP with the IOCTL code of IOCTL_CHANGER_QUERY_VOLUME_TAGS. |
| [ChangerError function](nf-mcd-changererror.md) | ChangerError performs device-specific error handling. |
| [ChangerClassInitialize function](nf-mcd-changerclassinitialize.md) | The ChangerClassInitialize routine initializes the driver. |
| [ChangerClassDebugPrint function](nf-mcd-changerclassdebugprint.md) | The ChangerClassDebugPrint function prints debugging information. |
| [ChangerGetStatus function](nf-mcd-changergetstatus.md) | ChangerGetStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_STATUS. |
| [ChangerReinitializeUnit function](nf-mcd-changerreinitializeunit.md) | ChangerReinitializeUnit handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_REINITIALIZE_TRANSPORT. |
| [ChangerClassSendSrbSynchronous function](nf-mcd-changerclasssendsrbsynchronous.md) | The ChangerClassSendSrbSynchronous routine synchronously sends an SRB to a specified device. |
| [ChangerClassDeviceControl function](nf-mcd-changerclassdevicecontrol.md) | The ChangerClassDeviceControl routine is called by a changer minidriver to allow the class driver perform device-independent aspects of a device control operation. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [ELEMENT_STATUS_PAGE structure](ns-mcd--element-status-page.md) | TBD |
| [ELEMENT_STATUS_HEADER structure](ns-mcd--element-status-header.md) | TBD |
| [MODE_DEVICE_CAPABILITIES_PAGE structure](ns-mcd--mode-device-capabilities-page.md) | TBD |
| [MODE_ELEMENT_ADDRESS_PAGE structure](ns-mcd--mode-element-address-page.md) | TBD |
| [MCD_INIT_DATA structure](ns-mcd--mcd-init-data.md) | The changer miniclass driver fills the MCD_INIT_DATA structure with pointers to its internal command processing routines and passes them to the changer class driver. |
| [MODE_TRANSPORT_GEOMETRY_PAGE structure](ns-mcd--mode-transport-geometry-page.md) | TBD |
| [ELEMENT_DESCRIPTOR structure](ns-mcd--element-descriptor.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [CHANGER_PERFORM_DIAGNOSTICS callback function](nc-mcd-changer-perform-diagnostics.md) | TBD |
| [CHANGER_EXTENSION_SIZE callback function](nc-mcd-changer-extension-size.md) | TBD |
| [CHANGER_ERROR_ROUTINE callback function](nc-mcd-changer-error-routine.md) | TBD |
| [CHANGER_INITIALIZE callback function](nc-mcd-changer-initialize.md) | TBD |
| [CHANGER_COMMAND_ROUTINE callback function](nc-mcd-changer-command-routine.md) | TBD |

This header is used in these topics:

- [Storage](..content/_Storage)
