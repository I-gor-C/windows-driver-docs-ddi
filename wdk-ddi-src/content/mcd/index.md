---
UID : NA:mcd
ms.assetid : d0f47be9-5c97-3970-aeb3-d7c1f17ca997
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# mcd.h header



mcd.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [ChangerAdditionalExtensionSize](nf-mcd-changeradditionalextensionsize.md) | ChangerAdditionalExtensionSize indicates the number of bytes the changer miniclass driver requires to store device-specific information in the device extension. |
| [ChangerClassAllocatePool](nf-mcd-changerclassallocatepool.md) | The ChangerClassAllocatePool function allocates pool memory. |
| [ChangerClassDebugPrint](nf-mcd-changerclassdebugprint.md) | The ChangerClassDebugPrint function prints debugging information. |
| [ChangerClassDeviceControl](nf-mcd-changerclassdevicecontrol.md) | The ChangerClassDeviceControl routine is called by a changer minidriver to allow the class driver perform device-independent aspects of a device control operation. |
| [ChangerClassFreePool](nf-mcd-changerclassfreepool.md) | The ChangerClassFreePool routine frees pool memory previously allocated using ChangerClassAllocatePool. |
| [ChangerClassInitialize](nf-mcd-changerclassinitialize.md) | The ChangerClassInitialize routine initializes the driver. |
| [ChangerClassSendSrbSynchronous](nf-mcd-changerclasssendsrbsynchronous.md) | The ChangerClassSendSrbSynchronous routine synchronously sends an SRB to a specified device. |
| [ChangerError](nf-mcd-changererror.md) | ChangerError performs device-specific error handling. |
| [ChangerExchangeMedium](nf-mcd-changerexchangemedium.md) | ChangerExchangeMedium handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_EXCHANGE_MEDIUM. |
| [ChangerGetElementStatus](nf-mcd-changergetelementstatus.md) | ChangerGetElementStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_ELEMENT_STATUS. |
| [ChangerGetParameters](nf-mcd-changergetparameters.md) | ChangerGetParameters handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_PARAMETERS. |
| [ChangerGetProductData](nf-mcd-changergetproductdata.md) | ChangerGetProductData handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_PRODUCT_DATA. |
| [ChangerGetStatus](nf-mcd-changergetstatus.md) | ChangerGetStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_STATUS. |
| [ChangerInitialize](nf-mcd-changerinitialize.md) | ChangerInitialize readies the changer to receive other requests. |
| [ChangerInitializeElementStatus](nf-mcd-changerinitializeelementstatus.md) | ChangerInitializeElementStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_INITIALIZE_ELEMENT_STATUS. |
| [ChangerMoveMedium](nf-mcd-changermovemedium.md) | ChangerMoveMedium handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_MOVE_MEDIUM. |
| [ChangerPerformDiagnostics](nf-mcd-changerperformdiagnostics.md) | ChangerPerformDiagnostics performs diagnostic tests on the changer device. |
| [ChangerQueryVolumeTags](nf-mcd-changerqueryvolumetags.md) | ChangerQueryVolumeTags handles the device-specific aspects of a device-control IRP with the IOCTL code of IOCTL_CHANGER_QUERY_VOLUME_TAGS. |
| [ChangerReinitializeUnit](nf-mcd-changerreinitializeunit.md) | ChangerReinitializeUnit handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_REINITIALIZE_TRANSPORT. |
| [ChangerSetAccess](nf-mcd-changersetaccess.md) | ChangerSetAccess handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_SET_ACCESS. |
| [ChangerSetPosition](nf-mcd-changersetposition.md) | ChangerSetPosition handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_SET_POSITION. |



## Structures
| Title | Description |
| ---- |:---- |
| [_MCD_INIT_DATA](ns-mcd-_mcd_init_data.md) | The changer miniclass driver fills the MCD_INIT_DATA structure with pointers to its internal command processing routines and passes them to the changer class driver. |