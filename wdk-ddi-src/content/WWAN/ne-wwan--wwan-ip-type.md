---
UID: NE.wwan._WWAN_IP_TYPE
title: WWAN_IP_TYPE
author: windows-driver-content
description: The WWAN_IP_TYPE enumeration lists the different levels of supported IP.
old-location: netvista\wwan_ip_type.htm
ms.assetid: E4CE7BE7-021A-4C9A-B467-B63AACEC1266
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_IP_TYPE
req.alt-loc: wwan.h
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
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_IP_TYPE enumeration



## -description
<p>The WWAN_IP_TYPE enumeration lists the different levels of supported IP.</p>


## -syntax

````
typedef enum _WWAN_IP_TYPE { 
  WwanIPTypeDefault  = 0,
  WwanIPTypeIPv4     = ,
  WwanIPTypeIPv6     = ,
  WwanIPTypeIpv4v6   = 
} WWAN_IP_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WwanIPTypeDefault"></a><a id="wwaniptypedefault"></a><a id="WWANIPTYPEDEFAULT"></a><b>WwanIPTypeDefault</b>

<dd>
<p>Default IP.</p>
</dd>

### -field <a id="WwanIPTypeIPv4"></a><a id="wwaniptypeipv4"></a><a id="WWANIPTYPEIPV4"></a><b>WwanIPTypeIPv4</b>

<dd>
<p>IPv4.</p>
</dd>

### -field <a id="WwanIPTypeIPv6"></a><a id="wwaniptypeipv6"></a><a id="WWANIPTYPEIPV6"></a><b>WwanIPTypeIPv6</b>

<dd>
<p>IPv6</p>
</dd>

### -field <a id="WwanIPTypeIpv4v6"></a><a id="wwaniptypeipv4v6"></a><a id="WWANIPTYPEIPV4V6"></a><b>WwanIPTypeIpv4v6</b>

<dd>
<p>IPv4 with IPv6</p>
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
<p>Versions: Supported in Windows 8 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571235">WWAN_SET_CONTEXT_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571202">WWAN_CONTEXT_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_IP_TYPE enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
