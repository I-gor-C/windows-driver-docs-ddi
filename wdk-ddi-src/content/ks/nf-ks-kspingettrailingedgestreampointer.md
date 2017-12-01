---
UID: NF.ks.KsPinGetTrailingEdgeStreamPointer
title: KsPinGetTrailingEdgeStreamPointer
author: windows-driver-content
description: The KsPinGetTrailingEdgeStreamPointer function acquires the trailing edge stream pointer for the queue associated with the specified pin.
old-location: stream\kspingettrailingedgestreampointer.htm
old-project: stream
ms.assetid: 763f1f66-4d83-44aa-9db5-206cf6b6f9b1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsPinGetTrailingEdgeStreamPointer
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
req.alt-api: KsPinGetTrailingEdgeStreamPointer
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

# KsPinGetTrailingEdgeStreamPointer function



## -description
<p>The<b> KsPinGetTrailingEdgeStreamPointer</b> function acquires the trailing edge stream pointer for the queue associated with the specified pin.</p>


## -syntax

````
PKSSTREAM_POINTER KsPinGetTrailingEdgeStreamPointer(
  _In_ PKSPIN                 Pin,
  _In_ KSSTREAM_POINTER_STATE State
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to the <a href="..\ks\ns-ks--kspin.md">KSPIN</a> structure for whose queue to return the trailing edge stream pointer.</p>
</dd>

### -param <i>State</i> [in]

<dd>
<p>This parameter specifies the state in which to acquire the trailing edge stream pointer. Can be one of the following:</p>
<p></p>
<dl>

### -param <a id="KSSTREAM_POINTER_STATE_UNLOCKED"></a><a id="ksstream_pointer_state_unlocked"></a>KSSTREAM_POINTER_STATE_UNLOCKED

<dd>
<p>Acquire the leading edge stream pointer regardless of whether it references a data frame or not. </p>
<p>No attempts can be made to access any data associated with the pointer until the pointer is locked. Also note that frames associated with an unlocked stream pointer can be canceled.</p>
</dd>

### -param <a id="KSSTREAM_POINTER_STATE_LOCKED"></a><a id="ksstream_pointer_state_locked"></a>KSSTREAM_POINTER_STATE_LOCKED

<dd>
<p>Acquire and lock the leading edge stream pointer. If no data frame is associated with the stream pointer, return <b>NULL</b>. If a non<b>null</b> pointer is returned, it is a locked stream pointer and has a data frame associated with it. Frames associated with a locked stream pointer <i>cannot</i> be canceled. </p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p><b>KsPinGetTrailingEdgeStreamPointer</b> returns either a pointer to a <a href="..\ks\ns-ks--ksstream-pointer.md">KSSTREAM_POINTER</a> structure representing the trailing edge stream pointer or <b>NULL</b>. A return value of <b>NULL</b> can indicate that there is no trailing edge for the queue associated with the pin. In this case, the pin descriptor probably does not specify that the pin should have a distinct trailing edge. Alternatively, <b>NULL</b> can indicate that there is no queue associated with the pin. In this case, the pin in question does not use the standard transport mechanism. A return value of <b>NULL</b> can also indicate that an attempt to lock the trailing edge failed. In other words, there is no data frame currently associated with the leading edge.</p>

## -remarks
<p>The trailing edge stream pointer is a special pointer into the data stream that exists if and only if the pin descriptor for the pin specifies a distinct trailing edge. If this pointer exists, it points to the oldest data in the queue unless specifically advanced by a <b>KsStreamPointerAdvance</b><i>Xxx</i> or a <a href="..\ks\nf-ks-ksstreampointerunlock.md">KsStreamPointerUnlock</a> call. Older data can exist in the queue also if cloned stream pointers exist for frames older than the one pointed to by the trailing edge.</p>

<p>Data frames that reside in the window between the leading edge stream pointer and the trailing edge stream pointer have at least one reference count and thus will not leave the queue and be completed until they exit the window as a result of the advancement of the trailing edge. Note that frames between the leading edge and trailing edge are <b>not</b> locked by default and therefore can be canceled.</p>

<p><b>KsPinGetTrailingEdgeStreamPointer</b> is mostly of use in pin-centric filters. For more information, see <a href="NULL">Pin-Centric Processing</a> and <a href="NULL">Filter-Centric Processing</a>.</p>

<p><b>KsPinGetTrailingEdgeStreamPointer</b> will not work unless the pin descriptor for the pin specifies that the queue is to have a distinct trailing edge by setting the KSPIN_FLAG_DISTINCT_TRAILING_EDGE flag.</p>

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
<a href="..\ks\nf-ks-kspingetleadingedgestreampointer.md">KsPinGetLeadingEdgeStreamPointer</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointerlock.md">KsStreamPointerLock</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointerunlock.md">KsStreamPointerUnlock</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointeradvance.md">KsStreamPointerAdvance</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointeradvanceoffsetsandunlock.md">KsStreamPointerAdvanceOffsetsAndUnlock</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointerclone.md">KsStreamPointerClone</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointerdelete.md">KsStreamPointerDelete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinGetTrailingEdgeStreamPointer function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
