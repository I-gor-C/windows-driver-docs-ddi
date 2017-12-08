---
UID: NF.ks.KsGetObjectTypeFromIrp
title: KsGetObjectTypeFromIrp function
author: windows-driver-content
description: The KsGetObjectTypeFromIrp function returns the AVStream object type that is associated with a given IRP.
old-location: stream\ksgetobjecttypefromirp.htm
old-project: stream
ms.assetid: 4fe45811-a823-4cc6-bdc4-a1f2ac892d37
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KsGetObjectTypeFromIrp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsGetObjectTypeFromIrp
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: Any level
---

# KsGetObjectTypeFromIrp function



## -description
The<b> KsGetObjectTypeFromIrp</b> function returns the AVStream object type that is associated with a given IRP.


## -syntax

````
KSOBJECTTYPE KsGetObjectTypeFromIrp(
  _In_ PIRP Irp
);
````


## -parameters

### -param Irp [in]

A pointer to the <a href="kernel.irp">IRP</a> structure for which to find the associated AVStream object type.

## -returns
<b>KsGetObjectTypeFromIrp</b> returns the type of AVStream object associated with the given IRP as a <a href="..\ks\ne-ks-ksobjecttype.md">KSOBJECTTYPE</a> enumeration. This is one of the following: <b>KsObjectTypeDevice</b>, <b>KsObjectTypeFilterFactory</b>, <b>KsObjectTypeFilter</b>, <b>KsObjectTypePin</b>.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
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
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
Any level
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.irp">IRP</a>
</dt>
<dt>
<a href="stream.ksaddirptocancelablequeue">KsAddIrpToCancelableQueue</a>
</dt>
<dt>
<a href="stream.ksforwardirp">KsForwardIrp</a>
</dt>
<dt>
<a href="stream.ksdispatchirp">KsDispatchIrp</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGetObjectTypeFromIrp function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
