# Declarations in the drmk header
This header Drmk contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [tagDRMRIGHTS structure](ns-drmk-tagdrmrights.md) | The DRMRIGHTS structure specifies the DRM content rights assigned to a KS audio pin or to a port-class driver's stream object. |
| [PKSP_DRMAUDIOSTREAM_CONTENTID structure](ns-drmk-pksp-drmaudiostream-contentid.md) | The KSP_DRMAUDIOSTREAM_CONTENTID structure specifies the property, request type, and context for a KSPROPERTY_DRMAUDIOSTREAM_CONTENTIDset-property request. It also specifies a list of function pointers to the DRM functions. |
| [PKSDRMAUDIOSTREAM_CONTENTID structure](ns-drmk-pksdrmaudiostream-contentid.md) | The KSDRMAUDIOSTREAM_CONTENTID structure specifies the DRM content ID and DRM content rights for a KSPROPERTY_DRMAUDIOSTREAM_CONTENTIDset-property request. |
| [tagDRMFORWARD structure](ns-drmk-tagdrmforward.md) | The DRMFORWARD structure contains the information that the DRMK system driver needs in order to forward a DRM content ID to a device that handles protected content. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFNDRMADDCONTENTHANDLERS callback](nc-drmk-pfndrmaddcontenthandlers.md) | This callback function is reserved for system use. |
| [PFNDRMCREATECONTENTMIXED callback](nc-drmk-pfndrmcreatecontentmixed.md) | This callback function is reserved for system use. |
| [PFNDRMGETCONTENTRIGHTS callback](nc-drmk-pfndrmgetcontentrights.md) | This callback function is reserved for system use. |
| [PFNDRMFORWARDCONTENTTOINTERFACE callback](nc-drmk-pfndrmforwardcontenttointerface.md) | This callback function is reserved for system use. |
| [PFNDRMDESTROYCONTENT callback](nc-drmk-pfndrmdestroycontent.md) | This callback function is reserved for system use. |
| [PFNDRMFORWARDCONTENTTOFILEOBJECT callback](nc-drmk-pfndrmforwardcontenttofileobject.md) | This callback function is reserved for system use. |
| [PFNDRMFORWARDCONTENTTODEVICEOBJECT callback](nc-drmk-pfndrmforwardcontenttodeviceobject.md) | This callback function is reserved for system use. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [DrmDestroyContent function](nf-drmk-drmdestroycontent.md) | The DrmDestroyContent function deletes a DRM content ID that was created by DrmCreateContentMixed. |
| [DrmForwardContentToFileObject function](nf-drmk-drmforwardcontenttofileobject.md) | The DrmForwardContentToFileObject function is obsolete and is maintained only to support existing drivers. |
| [IDrmAudioStream::QueryInterface method](nf-drmk-idrmaudiostream-queryinterface.md) | TBD |
| [DrmForwardContentToDeviceObject function](nf-drmk-drmforwardcontenttodeviceobject.md) | The DrmForwardContentToDeviceObject function accepts a device object representing a device to which the caller intends to forward protected content. |
| [DrmAddContentHandlers function](nf-drmk-drmaddcontenthandlers.md) | The DrmAddContentHandlers function provides the system with a list of functions that handle protected content. |
| [DrmGetContentRights function](nf-drmk-drmgetcontentrights.md) | The DrmGetContentRights function retrieves the DRM content rights assigned to a DRM content ID. |
| [IDrmAudioStream::AddRef method](nf-drmk-idrmaudiostream-addref.md) | TBD |
| [IDrmAudioStream::SetContentId method](nf-drmk-idrmaudiostream-setcontentid.md) | The SetContentId method sets the DRM content ID and its assigned DRM content rights on a KS audio stream. |
| [IDrmAudioStream::Release method](nf-drmk-idrmaudiostream-release.md) | TBD |
| [DrmForwardContentToInterface function](nf-drmk-drmforwardcontenttointerface.md) | The DrmForwardContentToInterface function accepts a pointer to the COM interface of an object to which the caller intends to forward protected content. |
| [DEFINE_DRMRIGHTS_DEFAULT function](nf-drmk-define-drmrights-default.md) | TBD |
| [DrmCreateContentMixed function](nf-drmk-drmcreatecontentmixed.md) | The DrmCreateContentMixed function creates a DRM content ID to identify a KS audio stream containing mixed content from a number of streams. |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IDrmAudioStream interface](nn-drmk-idrmaudiostream.md) | TBD |

This header is used in these topics:

- [audio](..content/_audio)
