---
UID: NE.ksmedia.TELEPHONY_CALLTYPE
title: TELEPHONY_CALLTYPE
author: windows-driver-content
description: The TELEPHONY_CALLTYPE enumeration defines constants that specify the type of phone call.
old-location: audio\telephony_calltype.htm
old-project: audio
ms.assetid: 8CF2CAF2-29F2-4B8B-B23F-B423392B2DAF
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10,Windows 10 Mobile
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TELEPHONY_CALLTYPE
req.alt-loc: ksmedia.h
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

# TELEPHONY_CALLTYPE enumeration



## -description
<p>The <b>TELEPHONY_CALLTYPE</b> enumeration defines constants that specify the type of phone call.</p>


## -syntax

````
typedef enum  { 
  TELEPHONY_CALLTYPE_CIRCUITSWITCHED      = 0,
  TELEPHONY_CALLTYPE_PACKETSWITCHED_LTE   = 1,
  TELEPHONY_CALLTYPE_PACKETSWITCHED_WLAN  = 2
} TELEPHONY_CALLTYPE;
````


## -enum-fields
<dl>

### -field <a id="TELEPHONY_CALLTYPE_CIRCUITSWITCHED"></a><a id="telephony_calltype_circuitswitched"></a><b>TELEPHONY_CALLTYPE_CIRCUITSWITCHED</b>

<dd>
<p>Specifies a circuit-switched phone call.</p>
</dd>

### -field <a id="TELEPHONY_CALLTYPE_PACKETSWITCHED_LTE"></a><a id="telephony_calltype_packetswitched_lte"></a><b>TELEPHONY_CALLTYPE_PACKETSWITCHED_LTE</b>

<dd>
<p>Specifies a packet-switched Long-Term Evolution (LTE) phone call.</p>
</dd>

### -field <a id="TELEPHONY_CALLTYPE_PACKETSWITCHED_WLAN"></a><a id="telephony_calltype_packetswitched_wlan"></a><b>TELEPHONY_CALLTYPE_PACKETSWITCHED_WLAN</b>

<dd>
<p>Specifies a packet-switched wireless LAN (WLAN) phone call.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Client</p>
</th>
<td width="70%">
<p>Windows 10 Mobile</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt169883">KSTELEPHONY_CALLCONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt169884">KSTELEPHONY_CALLINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt169885">KSTELEPHONY_PROVIDERCHANGE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20TELEPHONY_CALLTYPE enumeration%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
