---
UID: NC.ks.PFNKSFILTERPROCESS
title: PFNKSFILTERPROCESS
author: windows-driver-content
description: An AVStream minidriver's AVStrMiniFilterProcess routine is called when the filter is meant to process frames. It is used to perform Filter-Centric Processing.
old-location: stream\avstrminifilterprocess.htm
old-project: stream
ms.assetid: f1998d68-1c9e-4527-a174-b22a8c301e63
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AVStrMiniFilterProcess
req.alt-loc: ks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: (See Remarks section)
req.iface: 
---

# PFNKSFILTERPROCESS callback



## -description
<p>An AVStream minidriver's <i>AVStrMiniFilterProcess</i> routine is called when the filter is meant to process frames. It is used to perform <a href="NULL">Filter-Centric Processing</a>.</p>


## -prototype

````
PFNKSFILTERPROCESS AVStrMiniFilterProcess;

NTSTATUS AVStrMiniFilterProcess(
  _In_ PKSFILTER                Filter,
  _In_ PKSPROCESSPIN_INDEXENTRY ProcessPinsIndex
)
{ ... }
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>Pointer to the <a href="..\ks\ns-ks--ksfilter.md">KSFILTER</a> structure that must process frames.</p>
</dd>

### -param <i>ProcessPinsIndex</i> [in]

<dd>
<p>Pointer to an array of <a href="..\ks\ns-ks--ksprocesspin-indexentry.md">KSPROCESSPIN_INDEXENTRY</a> structures that AVStream orders by pin ID.</p>
</dd>
</dl>

## -returns
<p>Return STATUS_SUCCESS to continue processing. Return STATUS_PENDING to stop processing until the next triggering event. The minidriver may return an error code, but this will be treated as described for STATUS_PENDING.</p>

## -remarks
<p>The minidriver specifies this routine's address in the <b>Process</b> member of its <a href="..\ks\ns-ks--ksfilter-dispatch.md">KSFILTER_DISPATCH</a> structure.</p>

<p>The routine is called at either IRQL = DISPATCH_LEVEL or PASSIVE_LEVEL depending on the preference expressed in the filter descriptor. Filter descriptors that specify KSFILTER_FLAG_DISPATCH_LEVEL_PROCESSING may have their process callback at DISPATCH_LEVEL; filter descriptors that do not specify this flag will have their process callback at PASSIVE_LEVEL.</p>

<p>For more information, see <a href="NULL">Filter-Centric Processing</a> and <a href="NULL">Restarting Processing in AVStream</a>.</p>

<p>This routine is optional.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>(See Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\ns-ks--ksfilter-dispatch.md">KSFILTER_DISPATCH</a>
</dt>
<dt>
<a href="..\ks\ns-ks--ksprocesspin-indexentry.md">KSPROCESSPIN_INDEXENTRY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVStrMiniFilterProcess routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
