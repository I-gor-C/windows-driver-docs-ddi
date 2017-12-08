---
UID: NS.DRMK.PKSP_DRMAUDIOSTREAM_CONTENTID
title: PKSP_DRMAUDIOSTREAM_CONTENTID
author: windows-driver-content
description: The KSP_DRMAUDIOSTREAM_CONTENTID structure specifies the property, request type, and context for a KSPROPERTY_DRMAUDIOSTREAM_CONTENTIDset-property request. It also specifies a list of function pointers to the DRM functions.
old-location: audio\ksp_drmaudiostream_contentid.htm
old-project: audio
ms.assetid: 16a83c46-c183-4dc2-9d98-877976cf5750
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: PKSP_DRMAUDIOSTREAM_CONTENTID, KSP_DRMAUDIOSTREAM_CONTENTID, *PKSP_DRMAUDIOSTREAM_CONTENTID
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: drmk.h
req.include-header: Drmk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSP_DRMAUDIOSTREAM_CONTENTID
req.alt-loc: drmk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
---

# PKSP_DRMAUDIOSTREAM_CONTENTID structure



## -description
The KSP_DRMAUDIOSTREAM_CONTENTID structure specifies the property, request type, and context for a <a href="https://msdn.microsoft.com/library/windows/hardware/ff537351">KSPROPERTY_DRMAUDIOSTREAM_CONTENTID</a>set-property request. It also specifies a list of function pointers to the <a href="audio.drm_functions">DRM functions</a>.


## -syntax

````
typedef struct {
  KSPROPERTY                         Property;
  PVOID                              Context;
  PFNDRMADDCONTENTHANDLERS           DrmAddContentHandlers;
  PFNDRMCREATECONTENTMIXED           DrmCreateContentMixed;
  PFNDRMDESTROYCONTENT               DrmDestroyContent;
  PFNDRMFORWARDCONTENTTODEVICEOBJECT DrmForwardContentToDeviceObject;
  PFNDRMFORWARDCONTENTTOFILEOBJECT   DrmForwardContentToFileObject;
  PFNDRMFORWARDCONTENTTOINTERFACE    DrmForwardContentToInterface;
  PFNDRMGETCONTENTRIGHTS             DrmGetContentRights;
} KSP_DRMAUDIOSTREAM_CONTENTID, *PKSP_DRMAUDIOSTREAM_CONTENTID;
````


## -struct-fields

### -field Property

Specifies the property to get or set. This member is a structure of type <a href="stream.ksproperty">KSPROPERTY</a>.

### -field Context

Pointer to context data. This is the context specified in the <a href="audio.drmforwardcontenttodeviceobject">DrmForwardContentToDeviceObject</a> function's <i>DrmForward</i> parameter.

### -field DrmAddContentHandlers

Pointer to <a href="audio.drmaddcontenthandlers">DrmAddContentHandlers</a> function.

### -field DrmCreateContentMixed

Pointer to <a href="audio.drmcreatecontentmixed">DrmCreateContentMixed</a> function.

### -field DrmDestroyContent

Pointer to <a href="audio.drmdestroycontent">DrmDestroyContent</a> function.

### -field DrmForwardContentToDeviceObject

Pointer to <a href="audio.drmforwardcontenttodeviceobject">DrmForwardContentToDeviceObject</a> function.

### -field DrmForwardContentToFileObject

Pointer to <a href="audio.drmforwardcontenttofileobject">DrmForwardContentToFileObject</a> function.

### -field DrmForwardContentToInterface

Pointer to <a href="audio.drmforwardcontenttointerface">DrmForwardContentToInterface</a> function.

### -field DrmGetContentRights

Pointer to <a href="audio.drmgetcontentrights">DrmGetContentRights</a> function.

## -remarks
The structure contains function pointers to the DRM library functions in order to provide the driver with convenient access to these functions.

## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Drmk.h (include Drmk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.ksproperty">KSPROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537351">KSPROPERTY_DRMAUDIOSTREAM_CONTENTID</a>
</dt>
<dt>
<a href="audio.drmaddcontenthandlers">DrmAddContentHandlers</a>
</dt>
<dt>
<a href="audio.drmcreatecontentmixed">DrmCreateContentMixed</a>
</dt>
<dt>
<a href="audio.drmdestroycontent">DrmDestroyContent</a>
</dt>
<dt>
<a href="audio.drmforwardcontenttodeviceobject">DrmForwardContentToDeviceObject</a>
</dt>
<dt>
<a href="audio.drmforwardcontenttofileobject">DrmForwardContentToFileObject</a>
</dt>
<dt>
<a href="audio.drmforwardcontenttointerface">DrmForwardContentToInterface</a>
</dt>
<dt>
<a href="audio.drmgetcontentrights">DrmGetContentRights</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSP_DRMAUDIOSTREAM_CONTENTID structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
