---
UID: NS.windot11._DOT11_SUPPORTED_DSSS_CHANNEL
title: DOT11_SUPPORTED_DSSS_CHANNEL
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_supported_dsss_channel.htm
ms.assetid: a8c3fe52-2e5f-4212-9b52-10240d1abb86
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_SUPPORTED_DSSS_CHANNEL
req.alt-loc: windot11.h
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
ms.keywords: DOT11_SUPPORTED_DSSS_CHANNEL, DOT11_SUPPORTED_DSSS_CHANNEL, *PDOT11_SUPPORTED_DSSS_CHANNEL
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_SUPPORTED_DSSS_CHANNEL structure



## -description

## -syntax

````
typedef struct _DOT11_SUPPORTED_DSSS_CHANNEL {
  ULONG uChannel;
} DOT11_SUPPORTED_DSSS_CHANNEL, *PDOT11_SUPPORTED_DSSS_CHANNEL;
````


## -struct-fields
<dl>

### -field <b>uChannel</b>

<dd>
<p>A ULONG value, which represents a frequency channel that the 802.11 station can operate with.
     Valid channel numbers are as defined in 15.4.6.2 of 
     <i>IEEE Std. 802.11-1997</i> for the following PHY types:
     </p>
<ul>
<li>
<p>Direct-sequence spread spectrum (DSSS) PHY.</p>
</li>
<li>
<p>High-rate DSSS (HRDSSS) PHY.</p>
</li>
<li>
<p>Extended-rate PHY (ERP).</p>
</li>
<li>
<p>High-throughput (HT) 802.11n PHY when operating in the 2.4-GHz band.</p>
</li>
</ul>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/45941a4d-12e0-4a80-b04e-9e349126f5ff">
   DOT11_SUPPORTED_DSSS_CHANNEL_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_SUPPORTED_DSSS_CHANNEL structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
