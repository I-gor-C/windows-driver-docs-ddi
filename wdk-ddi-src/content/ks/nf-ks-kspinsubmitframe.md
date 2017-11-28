---
UID: NF.ks.KsPinSubmitFrame
title: KsPinSubmitFrame
author: windows-driver-content
description: If a pin has been placed into injection mode by a call to KsPinRegisterFrameReturnCallback, the KsPinSubmitFrame function submits a frame directly into the transport circuit.
old-location: stream\kspinsubmitframe.htm
old-project: stream
ms.assetid: 3fdb83b2-85b7-4f86-9a59-a42138000214
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsPinSubmitFrame
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
req.alt-api: KsPinSubmitFrame
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

# KsPinSubmitFrame function



## -description
<p>If a pin has been placed into injection mode by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff563522">KsPinRegisterFrameReturnCallback</a>, the <b>KsPinSubmitFrame</b> function submits a frame directly into the transport circuit.</p>


## -syntax

````
NTSTATUS KsPinSubmitFrame(
  _In_     PKSPIN           Pin,
  _In_opt_ PVOID            Data,
  _In_opt_ ULONG            Size,
  _In_opt_ PKSSTREAM_HEADER StreamHeader,
  _In_opt_ PVOID            Context
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> structure on which to submit a frame.</p>
</dd>

### -param <i>Data</i> [in, optional]

<dd>
<p>A pointer to a frame buffer. This should be <b>NULL</b> if and only if <i>Size</i> is equal to 0. Optional.</p>
</dd>

### -param <i>Size</i> [in, optional]

<dd>
<p>The size in bytes of the frame buffer to which the <i>Data</i> field points. If the <i>Data</i> field is <b>NULL</b>, set this parameter to zero. Optional.</p>
</dd>

### -param <i>StreamHeader</i> [in, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567138">KSSTREAM_HEADER</a> structure. The stream header is copied if this parameter is supplied. Optional.</p>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated buffer. AVStream provides this pointer to the frame return callback registered through a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff563522">KsPinRegisterFrameReturnCallback</a>. Optional.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if frame submission is successful. Otherwise returns an appropriate error code.</p>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563530">KsPinSubmitFrameMdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563522">KsPinRegisterFrameReturnCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinSubmitFrame function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
