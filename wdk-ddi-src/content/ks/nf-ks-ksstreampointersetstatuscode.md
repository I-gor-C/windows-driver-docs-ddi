---
UID: NF.ks.KsStreamPointerSetStatusCode
title: KsStreamPointerSetStatusCode
author: windows-driver-content
description: The KsStreamPointerSetStatusCode function allows specification of a successful or unsuccessful error code with which to complete the given IRP.
old-location: stream\ksstreampointersetstatuscode.htm
old-project: stream
ms.assetid: 88d554d9-55b7-42d4-b799-f8cb2029b1ae
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsStreamPointerSetStatusCode
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
req.alt-api: KsStreamPointerSetStatusCode
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# KsStreamPointerSetStatusCode function



## -description
<p>The<b> KsStreamPointerSetStatusCode</b> function allows specification of a successful or unsuccessful error code with which to complete the given IRP.</p>


## -syntax

````
NTSTATUS KsStreamPointerSetStatusCode(
  _In_ PKSSTREAM_POINTER StreamPointer,
  _In_ NTSTATUS          Status
);
````


## -parameters
<dl>

### -param StreamPointer [in]

<dd>
<p>A pointer to a <a href="..\ks\ns-ks--ksstream-pointer.md">KSSTREAM_POINTER</a> structure. This pointer points to the frame contained in the IRP.</p>
</dd>

### -param Status [in]

<dd>
<p>The error code with which to complete the IRP.</p>
</dd>
</dl>

## -returns
<p><b>KsStreamPointerSetStatusCode</b> returns STATUS_SUCCESS if the IRP is completed with the requested status code. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>Note that the IRP contains the frame to which <i>StreamPointer</i> points.</p>

<p>Also see <a href="https://msdn.microsoft.com/4bac68a0-34d2-431a-9ed9-8a42751a736f">Stream Pointers</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\ns-ks--kspin-dispatch.md">KSPIN_DISPATCH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsStreamPointerSetStatusCode function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
