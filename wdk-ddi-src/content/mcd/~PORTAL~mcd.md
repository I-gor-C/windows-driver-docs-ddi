# Mcd.h header


This header is used by unknown technology.

Mcd.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [ChangerAdditionalExtensionSize function](nf-mcd-changeradditionalextensionsize.md) | ChangerAdditionalExtensionSize indicates the number of bytes the changer miniclass driver requires to store device-specific information in the device extension. |
| [ChangerClassAllocatePool function](nf-mcd-changerclassallocatepool.md) | The ChangerClassAllocatePool function allocates pool memory. |
| [ChangerClassDebugPrint function](nf-mcd-changerclassdebugprint.md) | The ChangerClassDebugPrint function prints debugging information. |
| [ChangerClassDeviceControl function](nf-mcd-changerclassdevicecontrol.md) | The ChangerClassDeviceControl routine is called by a changer minidriver to allow the class driver perform device-independent aspects of a device control operation. |
| [ChangerClassFreePool function](nf-mcd-changerclassfreepool.md) | The ChangerClassFreePool routine frees pool memory previously allocated using ChangerClassAllocatePool. |
| [ChangerClassInitialize function](nf-mcd-changerclassinitialize.md) | The ChangerClassInitialize routine initializes the driver. |
| [ChangerClassSendSrbSynchronous function](nf-mcd-changerclasssendsrbsynchronous.md) | The ChangerClassSendSrbSynchronous routine synchronously sends an SRB to a specified device. |
| [ChangerError function](nf-mcd-changererror.md) | ChangerError performs device-specific error handling. |
| [ChangerExchangeMedium function](nf-mcd-changerexchangemedium.md) | ChangerExchangeMedium handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_EXCHANGE_MEDIUM. |
| [ChangerGetElementStatus function](nf-mcd-changergetelementstatus.md) | ChangerGetElementStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_ELEMENT_STATUS. |
| [ChangerGetParameters function](nf-mcd-changergetparameters.md) | ChangerGetParameters handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_PARAMETERS. |
| [ChangerGetProductData function](nf-mcd-changergetproductdata.md) | ChangerGetProductData handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_PRODUCT_DATA. |
| [ChangerGetStatus function](nf-mcd-changergetstatus.md) | ChangerGetStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_STATUS. |
| [ChangerInitialize function](nf-mcd-changerinitialize.md) | ChangerInitialize readies the changer to receive other requests. |
| [ChangerInitializeElementStatus function](nf-mcd-changerinitializeelementstatus.md) | ChangerInitializeElementStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_INITIALIZE_ELEMENT_STATUS. |
| [ChangerMoveMedium function](nf-mcd-changermovemedium.md) | ChangerMoveMedium handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_MOVE_MEDIUM. |
| [ChangerPerformDiagnostics function](nf-mcd-changerperformdiagnostics.md) | ChangerPerformDiagnostics performs diagnostic tests on the changer device. |
| [ChangerQueryVolumeTags function](nf-mcd-changerqueryvolumetags.md) | ChangerQueryVolumeTags handles the device-specific aspects of a device-control IRP with the IOCTL code of IOCTL_CHANGER_QUERY_VOLUME_TAGS. |
| [ChangerReinitializeUnit function](nf-mcd-changerreinitializeunit.md) | ChangerReinitializeUnit handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_REINITIALIZE_TRANSPORT. |
| [ChangerSetAccess function](nf-mcd-changersetaccess.md) | ChangerSetAccess handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_SET_ACCESS. |
| [ChangerSetPosition function](nf-mcd-changersetposition.md) | ChangerSetPosition handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_SET_POSITION. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [MCD_INIT_DATA structure](ns-mcd--mcd-init-data.md) | The changer miniclass driver fills the MCD_INIT_DATA structure with pointers to its internal command processing routines and passes them to the changer class driver. |
