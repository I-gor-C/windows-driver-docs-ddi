---
UID : NA:drmk
ms.assetid : d0869a59-50dc-35f9-a3cc-2e955c1a9812
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# drmk.h header



drmk.h contains the following programming interfaces:



## Interfaces
| Title | Description |
| ---- |:---- |
| [IDrmAudioStream](nn-drmk-idrmaudiostream.md) | The IDrmAudioStream interface assigns DRM protection to the digital content in an audio stream. |



## Functions
| Title | Description |
| ---- |:---- |
| [PFNDRMADDCONTENTHANDLERS](nc-drmk-pfndrmaddcontenthandlers.md) | This callback function is reserved for system use. |
| [PFNDRMCREATECONTENTMIXED](nc-drmk-pfndrmcreatecontentmixed.md) | This callback function is reserved for system use. |
| [PFNDRMDESTROYCONTENT](nc-drmk-pfndrmdestroycontent.md) | This callback function is reserved for system use. |
| [PFNDRMFORWARDCONTENTTODEVICEOBJECT](nc-drmk-pfndrmforwardcontenttodeviceobject.md) | This callback function is reserved for system use. |
| [PFNDRMFORWARDCONTENTTOFILEOBJECT](nc-drmk-pfndrmforwardcontenttofileobject.md) | This callback function is reserved for system use. |
| [PFNDRMFORWARDCONTENTTOINTERFACE](nc-drmk-pfndrmforwardcontenttointerface.md) | This callback function is reserved for system use. |
| [PFNDRMGETCONTENTRIGHTS](nc-drmk-pfndrmgetcontentrights.md) | This callback function is reserved for system use. |
| [DrmAddContentHandlers](nf-drmk-drmaddcontenthandlers.md) | The DrmAddContentHandlers function provides the system with a list of functions that handle protected content. |
| [DrmCreateContentMixed](nf-drmk-drmcreatecontentmixed.md) | The DrmCreateContentMixed function creates a DRM content ID to identify a KS audio stream containing mixed content from a number of streams. |
| [DrmDestroyContent](nf-drmk-drmdestroycontent.md) | The DrmDestroyContent function deletes a DRM content ID that was created by DrmCreateContentMixed. |
| [DrmForwardContentToDeviceObject](nf-drmk-drmforwardcontenttodeviceobject.md) | The DrmForwardContentToDeviceObject function accepts a device object representing a device to which the caller intends to forward protected content. |
| [DrmForwardContentToFileObject](nf-drmk-drmforwardcontenttofileobject.md) | The DrmForwardContentToFileObject function is obsolete and is maintained only to support existing drivers. |
| [DrmForwardContentToInterface](nf-drmk-drmforwardcontenttointerface.md) | The DrmForwardContentToInterface function accepts a pointer to the COM interface of an object to which the caller intends to forward protected content. |
| [DrmGetContentRights](nf-drmk-drmgetcontentrights.md) | The DrmGetContentRights function retrieves the DRM content rights assigned to a DRM content ID. |



## Structures
| Title | Description |
| ---- |:---- |
| [KSDRMAUDIOSTREAM_CONTENTID](ns-drmk-ksdrmaudiostream_contentid.md) | The KSDRMAUDIOSTREAM_CONTENTID structure specifies the DRM content ID and DRM content rights for a KSPROPERTY_DRMAUDIOSTREAM_CONTENTIDset-property request. |
| [KSP_DRMAUDIOSTREAM_CONTENTID](ns-drmk-ksp_drmaudiostream_contentid.md) | The KSP_DRMAUDIOSTREAM_CONTENTID structure specifies the property, request type, and context for a KSPROPERTY_DRMAUDIOSTREAM_CONTENTIDset-property request. It also specifies a list of function pointers to the DRM functions. |
| [tagDRMFORWARD](ns-drmk-tagdrmforward.md) | The DRMFORWARD structure contains the information that the DRMK system driver needs in order to forward a DRM content ID to a device that handles protected content. |
| [tagDRMRIGHTS](ns-drmk-tagdrmrights.md) | The DRMRIGHTS structure specifies the DRM content rights assigned to a KS audio pin or to a port-class driver's stream object. |