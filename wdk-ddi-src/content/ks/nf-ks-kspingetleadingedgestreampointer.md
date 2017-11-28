---
UID: NF.ks.KsPinGetLeadingEdgeStreamPointer
title: KsPinGetLeadingEdgeStreamPointer
author: windows-driver-content
description: The KsPinGetLeadingEdgeStreamPointer function acquires the leading edge stream pointer for the queue associated with the given pin.
old-location: stream\kspingetleadingedgestreampointer.htm
old-project: stream
ms.assetid: 05615730-dbeb-496a-b4a8-a16830b31586
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsPinGetLeadingEdgeStreamPointer
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
req.alt-api: KsPinGetLeadingEdgeStreamPointer
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

# KsPinGetLeadingEdgeStreamPointer function



## -description
<p>The<b> KsPinGetLeadingEdgeStreamPointer</b> function acquires the leading edge stream pointer for the queue associated with the given pin.</p>


## -syntax

````
PKSSTREAM_POINTER KsPinGetLeadingEdgeStreamPointer(
  _In_ PKSPIN                 Pin,
  _In_ KSSTREAM_POINTER_STATE State
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> structure owning the queue for which the leading edge stream pointer should be acquired.</p>
</dd>

### -param <i>State</i> [in]

<dd>
<p>This parameter specifies how to acquire the leading edge stream pointer. Can be one of the following:</p>
<p></p>
<dl>

### -param <a id="KSSTREAM_POINTER_STATE_UNLOCKED"></a><a id="ksstream_pointer_state_unlocked"></a>KSSTREAM_POINTER_STATE_UNLOCKED

<dd>
<p>Acquire the leading edge stream pointer regardless of whether it references a data frame or not. </p>
<p>No attempts can be made to access any data associated with the pointer until the pointer is locked. Also note that frames associated with an unlocked stream pointer can be canceled.</p>
</dd>

### -param <a id="KSSTREAM_POINTER_STATE_LOCKED"></a><a id="ksstream_pointer_state_locked"></a>KSSTREAM_POINTER_STATE_LOCKED

<dd>
<p>Acquire and lock the leading edge stream pointer. If no data frame is associated with the stream pointer, return <b>NULL</b>. If a non<b>null</b> pointer is returned, it is a locked stream pointer and has a data frame associated with it. Frames associated with a locked stream pointer <b>cannot</b> be canceled. </p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p><b>KsPinGetLeadingEdgeStreamPointer</b> returns a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567139">KSSTREAM_POINTER</a> structure or <b>NULL</b>. A return value of <b>NULL</b> may occur because there is no queue associated with the pin, indicating that the pin does not use the standard transport mechanism. Alternatively, a return value of <b>NULL</b> may occur because an attempt to lock the leading edge failed, indicating that there is no data frame associated with the leading edge.</p>

## -remarks
<p>Filters that implement <a href="NULL">Pin-Centric Processing</a> often call <b>KsPinGetLeadingEdgeStreamPointer</b>.</p>

<p>Filters that implement <a href="NULL">Pin-Centric Processing</a> often call <b>KsPinGetLeadingEdgeStreamPointer</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn892390">KsStreamPointerLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567137">KsStreamPointerUnlock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567125">KsStreamPointerAdvance</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567127">KsStreamPointerAdvanceOffsetsAndUnlock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn892389">KsStreamPointerClone</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567130">KsStreamPointerDelete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563518">KsPinGetTrailingEdgeStreamPointer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinGetLeadingEdgeStreamPointer function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
