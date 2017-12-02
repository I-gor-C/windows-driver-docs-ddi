---
UID: NC.ks.PFNKSFILTERVOID
title: PFNKSFILTERVOID
author: windows-driver-content
description: An AVStream minidriver's AVStrMiniFilterReset routine is called when AVStream receives an IOCTL_KS_RESET_STATE to return the filter to the state it was in at Acquire-time.
old-location: stream\avstrminifilterreset.htm
old-project: stream
ms.assetid: 8259117b-87ef-410a-955b-6f99966574a6
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
req.alt-api: AVStrMiniFilterReset
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
req.irql: 
req.iface: 
---

# PFNKSFILTERVOID callback



## -description
<p>An AVStream minidriver's <i>AVStrMiniFilterReset</i> routine is called when AVStream receives an IOCTL_KS_RESET_STATE to return the filter to the state it was in at <i>Acquire</i>-time. This routine is also called when a queue associated with a pin on the filter is flushed. <i>This routine will only be called for a filter-centric filter</i>.</p>


## -prototype

````
PFNKSFILTERVOID AVStrMiniFilterReset;

NTSTATUS AVStrMiniFilterReset(
  _In_ PKSFILTER Filter
)
{ ... }
````


## -parameters
<dl>

### -param Filter [in]

<dd>
<p>Pointer to the <a href="..\ks\ns-ks--ksfilter.md">KSFILTER</a> to return to its previous state.</p>
</dd>
</dl>

## -returns
<p>AVStream does not currently use the return value.</p>

## -remarks
<p>For more information, see <a href="https://msdn.microsoft.com/e56c5102-7ea6-4687-ae5e-1550db9500f0">Filter-Centric Processing</a>.</p>

<p>Note that it is not the filter in question, but rather a pin on this filter that actually receives the reset IOCTL.</p>

<p>The minidriver specifies this routine's address in the <b>Reset</b> member of its <a href="..\ks\ns-ks--ksfilter-dispatch.md">KSFILTER_DISPATCH</a> structure.</p>

<p>The filter control mutex may be held during this function. See <a href="https://msdn.microsoft.com/402795a0-e567-4e7e-a7d8-b2ce29ffb8fd">Filter Control Mutex in AVStream</a>.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\ns-ks--ksfilter-dispatch.md">KSFILTER_DISPATCH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVStrMiniFilterReset routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
