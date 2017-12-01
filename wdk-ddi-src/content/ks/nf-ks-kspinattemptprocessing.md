---
UID: NF.ks.KsPinAttemptProcessing
title: KsPinAttemptProcessing
author: windows-driver-content
description: The KsPinAttemptProcessing function is used to resume processing on a specific pin on a pin-centric filter. It attempts to initiate processing on Pin by sending a processing dispatch call to Pin's processing object.
old-location: stream\kspinattemptprocessing.htm
old-project: stream
ms.assetid: 9b916114-85aa-4ab7-acaa-6b19d0a4d776
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsPinAttemptProcessing
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
req.alt-api: KsPinAttemptProcessing
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
req.irql: <=DISPATCH_LEVEL (See Remarks)
req.iface: 
---

# KsPinAttemptProcessing function



## -description
<p>The<b> KsPinAttemptProcessing</b> function is used to resume processing on a specific pin on a pin-centric filter. It attempts to initiate processing on <i>Pin</i> by sending a processing dispatch call to <i>Pin</i>'s processing object.</p>


## -syntax

````
void KsPinAttemptProcessing(
  _In_ PKSPIN  Pin,
  _In_ BOOLEAN Asynchronous
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to a <a href="..\ks\ns-ks--kspin.md">KSPIN</a> structure that represents the AVStream pin object on which to attempt processing.</p>
<p>
<div class="alert"><b>Warning</b>  This parameter is mandatory. If you call <b>KsPinAttemptProcessing</b> with a <i>Pin</i> value of <b>NULL</b>, system instability may result.</div>
<div> </div>
</p>
</dd>

### -param <i>Asynchronous</i> [in]

<dd>
<p>This parameter indicates the minidriver's preference whether the processing should occur synchronously or asynchronously. If <b>TRUE</b>, processing is always asynchronous. However, synchronous processing only happens under certain circumstances. For more information, see the Remarks section below.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A minidriver may need to call <b>KsPinAttemptProcessing</b> to resume processing in various situations. For example, if the client has shut off the processing control gate with <a href="..\ks\nf-ks-ksgateturninputoff.md">KsGateTurnInputOff</a>, call this function when ready to attempt processing. Note that this only causes a processing dispatch if the process control gate is in the open state. Another situation involves the minidriver having previously returning STATUS_PENDING to a processing dispatch. For more details, see <a href="NULL">Restarting Processing in AVStream</a> and <a href="NULL">Flow Control Gates in AVStream</a>.</p>

<p>The processing dispatch occurs either synchronously or asynchronously, and <i>only</i> if the processing control gate is open. The <i>Asynchronous</i> flag specifies the minidriver's preference. If the minidriver requests an asynchronous process dispatch, the dispatch is always asynchronous. However, even if the caller sets <i>Asynchronous</i> to <b>FALSE</b>, a synchronous dispatch only occurs if the system is currently running at an IRQL less than the maximum processing IRQL. In other words, if the minidriver does not specify dispatch level processing and the call is made at IRQL = DISPATCH_LEVEL, then the call occurs in an asynchronous work item at PASSIVE_LEVEL regardless of the value of <i>Asynchronous</i>. For more information, see <a href="NULL">Filter-Centric Processing</a> and <a href="NULL">Pin-Centric Processing</a>.</p>

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
<p>&lt;=DISPATCH_LEVEL (See Remarks)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\ns-ks--ksgate.md">KSGATE</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksfilterattemptprocessing.md">KsFilterAttemptProcessing</a>
</dt>
<dt><b>KSGATE</b></dt>
<dt>
<a href="..\ks\ns-ks--ksfilter-dispatch.md">KSFILTER_DISPATCH</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgatecapturethreshold.md">KsGateCaptureThreshold</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinAttemptProcessing function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
