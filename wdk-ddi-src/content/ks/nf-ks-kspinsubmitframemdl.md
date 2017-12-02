---
UID: NF.ks.KsPinSubmitFrameMdl
title: KsPinSubmitFrameMdl
author: windows-driver-content
description: If a pin has been placed into injection mode by a call to KsPinRegisterFrameReturnCallback, the KsPinSubmitFrameMdl function submits a frame directly into the transport circuit.
old-location: stream\kspinsubmitframemdl.htm
old-project: stream
ms.assetid: 8033c0a9-86dd-4d54-b93e-66c926cae952
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsPinSubmitFrameMdl
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
req.alt-api: KsPinSubmitFrameMdl
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

# KsPinSubmitFrameMdl function



## -description
<p>If a pin has been placed into injection mode by a call to <a href="..\ks\nf-ks-kspinregisterframereturncallback.md">KsPinRegisterFrameReturnCallback</a>, the <b>KsPinSubmitFrameMdl</b> function submits a frame directly into the transport circuit.</p>


## -syntax

````
NTSTATUS KsPinSubmitFrameMdl(
  _In_     PKSPIN           Pin,
  _In_opt_ PMDL             Mdl,
  _In_opt_ PKSSTREAM_HEADER StreamHeader,
  _In_opt_ PVOID            Context
);
````


## -parameters
<dl>

### -param Pin [in]

<dd>
<p>A pointer to a <a href="..\ks\ns-ks--kspin.md">KSPIN</a> structure representing the pin on which to submit a frame.</p>
</dd>

### -param Mdl [in, optional]

<dd>
<p>A pointer to a memory descriptor list describing the frame buffer. Optional.</p>
</dd>

### -param StreamHeader [in, optional]

<dd>
<p>A pointer to a <a href="stream.ksstream_header">KSSTREAM_HEADER</a> structure. The stream header is copied if this parameter is supplied. Optional.</p>
</dd>

### -param Context [in, optional]

<dd>
<p>A pointer to a caller-allocated buffer that is passed to the frame return callback registered through <a href="..\ks\nf-ks-kspinregisterframereturncallback.md">KsPinRegisterFrameReturnCallback</a>. This parameter is optional and is solely for the caller's use.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if frame submission is successful. Otherwise returns an appropriate error code.</p>

## -remarks
<p>The difference between this function and <a href="..\ks\nf-ks-kspinsubmitframe.md">KsPinSubmitFrame</a> is that this function will submit a frame using an <a href="wdkgloss.m#wdkgloss.mdl#wdkgloss.mdl"><i>MDL</i></a> structure rather than a data and size argument.</p>

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
<a href="..\ks\nf-ks-kspinsubmitframe.md">KsPinSubmitFrame</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspinregisterframereturncallback.md">KsPinRegisterFrameReturnCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinSubmitFrameMdl function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
