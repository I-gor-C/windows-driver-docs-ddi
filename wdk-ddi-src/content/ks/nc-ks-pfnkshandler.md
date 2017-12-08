---
UID: NC.ks.PFNKSHANDLER
title: PFNKSHANDLER
author: windows-driver-content
description: The minidriver-provided KStrGetPropertyHandler routine is called when Kernel Streaming receives a get property request.
old-location: stream\kstrgetpropertyhandler.htm
old-project: stream
ms.assetid: f1e02bce-2904-4325-b5fd-e9d311a17288
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KStrGetPropertyHandler
req.alt-loc: ks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
---

# PFNKSHANDLER callback



## -description
The minidriver-provided <i>KStrGetPropertyHandler</i> routine is called when Kernel Streaming receives a get property request.


## -prototype

````
PFNKSHANDLER KStrGetPropertyHandler;

NTSTATUS KStrGetPropertyHandler(
  _In_    PIRP          Irp,
  _In_    PKSIDENTIFIER Request,
  _Inout_ PVOID         Data
)
{ ... }
````


## -parameters

### -param Irp [in]

Pointer to an IRP that contains the get property request.

### -param Request [in]

Pointer to a <a href="stream.ksidentifier">KSIDENTIFIER</a> that identifies the specific request. This is typically a pointer to a <a href="stream.ksproperty">KSPROPERTY</a> structure.

### -param Data [in, out]

Pointer to a caller-supplied buffer that specifies information relevant to the request.

## -returns
Return STATUS_SUCCESS if the request is handled. Appropriate error values depend on the property being handled. Return STATUS_NOT_SUPPORTED to indicate that the property is not supported or STATUS_BUFFER_TOO_SMALL if the caller-allocated <i>Data</i> buffer is not large enough.

## -remarks
The minidriver specifies this routine's address in the <b>GetPropertyHandler</b> member of the <a href="stream.ksproperty_item">KSPROPERTY_ITEM</a> structure.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
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
<a href="stream.ksproperty_item">KSPROPERTY_ITEM</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KStrGetPropertyHandler routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
