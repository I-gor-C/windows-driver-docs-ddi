---
UID: NF.ks.KsStreamPointerUnlock
title: KsStreamPointerUnlock
author: windows-driver-content
description: The KsStreamPointerUnlock function unlocks a stream pointer that has previously been locked by an acquisition function (KsGetXxxEdgeStreamPointer) or by KsStreamPointerLock.
old-location: stream\ksstreampointerunlock.htm
old-project: stream
ms.assetid: 1d03b97f-5c01-48b2-a0e4-2dc6bf732813
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsStreamPointerUnlock
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
req.alt-api: KsStreamPointerUnlock
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

# KsStreamPointerUnlock function



## -description
<p>The<b> KsStreamPointerUnlock </b>function unlocks a stream pointer that has previously been locked by an acquisition function <b>(KsGet</b><i>Xxx</i><b>EdgeStreamPointer</b>) or by <b>KsStreamPointerLock</b>.</p>


## -syntax

````
void KsStreamPointerUnlock(
  _In_ PKSSTREAM_POINTER StreamPointer,
  _In_ BOOLEAN           Eject
);
````


## -parameters
<dl>

### -param <i>StreamPointer</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567139">KSSTREAM_POINTER</a> structure representing the stream pointer to unlock.</p>
</dd>

### -param <i>Eject</i> [in]

<dd>
<p>This parameter specifies whether to advance <i>StreamPointer</i> to the next data frame. A value of <b>TRUE</b> advances the stream pointer.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>KsStreamPointerUnlock</b> can also advance the stream pointer to the next data frame. See the description of <i>Eject</i> above.</p>

<p>Also see <a href="NULL">Stream Pointers</a>.</p>

<p><b>KsStreamPointerUnlock</b> can also advance the stream pointer to the next data frame. See the description of <i>Eject</i> above.</p>

<p>Also see <a href="NULL">Stream Pointers</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567125">KsStreamPointerAdvance</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567126">KsStreamPointerAdvanceOffsets</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567127">KsStreamPointerAdvanceOffsetsAndUnlock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563513">KsPinGetLeadingEdgeStreamPointer</a>
</dt>
<dt><b>KsPinGetLeadingEdgeStreamPointer</b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567139">KSSTREAM_POINTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563535">KSPIN_DISPATCH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsStreamPointerUnlock function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
