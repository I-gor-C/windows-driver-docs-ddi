---
UID: NC.ks.PFNKSPINVOID
title: PFNKSPINVOID
author: windows-driver-content
description: An AVStream minidriver's AVStrMiniPinDisconnect routine is called when the relevant KSPIN is serving as a sink pin and this sink pin is disconnected from an AVStream source pin.
old-location: stream\avstrminipindisconnect.htm
old-project: stream
ms.assetid: 64bcbc05-8dbd-4f97-afbb-dadd44b60078
ms.author: windowsdriverdev
ms.date: 12/14/2017
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
req.alt-api: AVStrMiniPinDisconnect
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
---

# PFNKSPINVOID callback



## -description
An AVStream minidriver's <i>AVStrMiniPinDisconnect</i> routine is called when the relevant <a href="stream.kspin">KSPIN</a> is serving as a sink pin and this sink pin is disconnected from an AVStream source pin.



## -prototype

````
PFNKSPINVOID AVStrMiniPinDisconnect;

void AVStrMiniPinDisconnect(
  _In_ PKSPIN Pin
)
{ ... }
````


## -parameters

### -param Pin [in]

Pointer to the relevant <a href="stream.kspin">KSPIN</a>, serving as a sink pin.


## -returns
None


## -remarks
The minidriver specifies this routine's address in the <b>Disconnect</b> member of its <a href="stream.kspin_dispatch">KSPIN_DISPATCH</a> structure.

This routine is optional.

Also see <a href="https://msdn.microsoft.com/04d0d17b-c326-417d-b2e8-58b33420455a">KS Pins</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="stream.kspin_dispatch">KSPIN_DISPATCH</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVStrMiniPinDisconnect routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

