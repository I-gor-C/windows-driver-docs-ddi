---
UID: NC.ks.PFNKSPIN
title: PFNKSPIN
author: windows-driver-content
description: An AVStream minidriver's AVStrMiniPinConnect routine is called when the relevant KSPIN is serving as a sink pin and is connected to an AVStream source pin.
old-location: stream\avstrminipinconnect.htm
old-project: stream
ms.assetid: 5933a200-3790-447f-b923-1095c79cadd4
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: AVStrMiniPinConnect
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

# PFNKSPIN callback



## -description
<p>An AVStream minidriver's <i>AVStrMiniPinConnect</i> routine is called when the relevant <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> is serving as a sink pin and is connected to an AVStream source pin.</p>


## -prototype

````
PFNKSPIN AVStrMiniPinConnect;

NTSTATUS AVStrMiniPinConnect(
  _In_ PKSPIN Pin
)
{ ... }
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>Pointer to the relevant <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> serving as sink pin.</p>
</dd>
</dl>

## -returns
<p>Return STATUS_SUCCESS or the error returned from the attempt to establish an intra-connection. Do not return STATUS_PENDING. <i>AVStream treats a pending return value as invalid and causes the connection to fail</i>.</p>

## -remarks
<p>The minidriver specifies this routine's address in the <b>Connect</b> member of its <a href="https://msdn.microsoft.com/library/windows/hardware/ff563535">KSPIN_DISPATCH</a> structure.</p>

<p>This routine is optional.</p>

<p>Also see <a href="NULL">KS Pins</a>.</p>

<p>The minidriver specifies this routine's address in the <b>Connect</b> member of its <a href="https://msdn.microsoft.com/library/windows/hardware/ff563535">KSPIN_DISPATCH</a> structure.</p>

<p>This routine is optional.</p>

<p>Also see <a href="NULL">KS Pins</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563535">KSPIN_DISPATCH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVStrMiniPinConnect routine%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
