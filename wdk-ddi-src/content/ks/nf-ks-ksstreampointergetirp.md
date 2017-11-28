---
UID: NF.ks.KsStreamPointerGetIrp
title: KsStreamPointerGetIrp
author: windows-driver-content
description: The KsStreamPointerGetIrp function returns the IRP associated with the frame that is referenced by the given stream pointer.
old-location: stream\ksstreampointergetirp.htm
old-project: stream
ms.assetid: 3ed4ed2f-66be-4429-b2d6-2d9d3f9bcf3e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsStreamPointerGetIrp
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
req.alt-api: KsStreamPointerGetIrp
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

# KsStreamPointerGetIrp function



## -description
<p>The<b> KsStreamPointerGetIrp </b>function returns the IRP associated with the frame that is referenced by the given stream pointer.</p>


## -syntax

````
PIRP KsStreamPointerGetIrp(
  _In_      PKSSTREAM_POINTER StreamPointer,
  _Out_opt_ PBOOLEAN          FirstFrameInIrp,
  _Out_opt_ PBOOLEAN          LastFrameInIrp
);
````


## -parameters
<dl>

### -param <i>StreamPointer</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567139">KSSTREAM_POINTER</a> structure that references the frame for which the associated IRP is returned.</p>
</dd>

### -param <i>FirstFrameInIrp</i> [out, optional]

<dd>
<p>A pointer to a caller-supplied BOOLEAN value set to <b>TRUE</b> on return if the frame referenced by <i>StreamPointer</i> is the first frame in the returned IRP and <b>FALSE</b> if not. If <b>NULL</b>, AVStream does not test this condition.</p>
</dd>

### -param <i>LastFrameInIrp</i> [out, optional]

<dd>
<p>A pointer to a caller-supplied BOOLEAN value set to <b>TRUE</b> if the frame referenced by the stream pointer is the last frame in the returned IRP and <b>FALSE</b> if not. If <b>NULL</b>, AVStream does not test this condition.</p>
</dd>
</dl>

## -returns
<p><b>KsStreamPointerGetIrp </b>returns either a pointer to the IRP associated with the frame that is referenced by the given stream pointer, or returns <b>NULL</b>. A return value of <b>NULL</b> indicates that the stream pointer is not locked.</p>

## -remarks
<p><b>KsStreamPointerGetIrp </b>can also be used to determine if <i>StreamPointer</i> references the first and/or last frame contained in the returned IRP.</p>

<p><i>StreamPointer</i> must be locked in order for <b>KsStreamPointerGetIrp </b>to execute successfully. Any attempt to call this function with an unlocked stream pointer results in a <b>NULL</b> return value.</p>

<p><i>FirstFrameInIrp </i>and<i>/</i>or <i>LastFrameInIrp</i> must be non-<b>NULL</b> at call-time in order for AVStream to fill in these values.</p>

<p>Also see <a href="NULL">Stream Pointers</a>.</p>

<p><b>KsStreamPointerGetIrp </b>can also be used to determine if <i>StreamPointer</i> references the first and/or last frame contained in the returned IRP.</p>

<p><i>StreamPointer</i> must be locked in order for <b>KsStreamPointerGetIrp </b>to execute successfully. Any attempt to call this function with an unlocked stream pointer results in a <b>NULL</b> return value.</p>

<p><i>FirstFrameInIrp </i>and<i>/</i>or <i>LastFrameInIrp</i> must be non-<b>NULL</b> at call-time in order for AVStream to fill in these values.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567132">KsStreamPointerGetMdl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsStreamPointerGetIrp function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
