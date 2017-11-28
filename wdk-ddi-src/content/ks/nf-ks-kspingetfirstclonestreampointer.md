---
UID: NF.ks.KsPinGetFirstCloneStreamPointer
title: KsPinGetFirstCloneStreamPointer
author: windows-driver-content
description: The KsPinGetFirstCloneStreamPointer function returns the first cloned stream pointer on Pin.
old-location: stream\kspingetfirstclonestreampointer.htm
old-project: stream
ms.assetid: 9b4880af-d748-4a4e-92ec-8081138d4e27
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsPinGetFirstCloneStreamPointer
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
req.alt-api: KsPinGetFirstCloneStreamPointer
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

# KsPinGetFirstCloneStreamPointer function



## -description
<p>The<b> KsPinGetFirstCloneStreamPointer</b> function returns the first cloned stream pointer on <i>Pin</i>.</p>


## -syntax

````
PKSSTREAM_POINTER KsPinGetFirstCloneStreamPointer(
  _In_ PKSPIN Pin
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> structure on which to return the first clone stream pointer.</p>
</dd>
</dl>

## -returns
<p><b>KsPinGetFirstCloneStreamPointer</b> returns a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567139">KSSTREAM_POINTER</a> structure. This pointer points to the first cloned stream pointer on <i>Pin</i>. If no clone stream pointers exist for <i>Pin</i>, <b>KsPinGetFirstCloneStreamPointer</b> returns <b>NULL</b>.</p>

## -remarks
<p><b>KsPinGetFirstCloneStreamPointer</b>, along with <a href="https://msdn.microsoft.com/library/windows/hardware/ff567133">KsStreamPointerGetNextClone</a> can be used to enumerate all clone stream pointers on a given pin in the order in which they were cloned. Also see <a href="NULL">Stream Pointers</a>.</p>

<p><b>KsPinGetFirstCloneStreamPointer</b>, along with <a href="https://msdn.microsoft.com/library/windows/hardware/ff567133">KsStreamPointerGetNextClone</a> can be used to enumerate all clone stream pointers on a given pin in the order in which they were cloned. Also see <a href="NULL">Stream Pointers</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567133">KsStreamPointerGetNextClone</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn892389">KsStreamPointerClone</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567139">KSSTREAM_POINTER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinGetFirstCloneStreamPointer function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
