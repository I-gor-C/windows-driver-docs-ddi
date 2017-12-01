---
UID: NE.wwan._WWAN_CONTEXT_TYPE
title: WWAN_CONTEXT_TYPE
author: windows-driver-content
description: The WWAN_CONTEXT_TYPE enumeration lists the different types of connection contexts that are supported by the MB device.
old-location: netvista\wwan_context_type.htm
old-project: netvista
ms.assetid: 73a18050-fc89-41df-82ce-0f29c5716496
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_CONTEXT_TYPE
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
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_CONTEXT_TYPE enumeration



## -description
<p>The WWAN_CONTEXT_TYPE enumeration lists the different types of connection contexts that are supported
  by the MB device.</p>


## -syntax

````
typedef enum _WWAN_CONTEXT_TYPE { 
  WwanContextTypeNone        = 0,
  WwanContextTypeInternet,
  WwanContextTypeVpn,
  WwanContextTypeVoice,
  WwanContextTypeVideoShare,
  WwanContextTypeCustom,
  WwanContextTypePurchase,
  WwanContextTypeMax
} WWAN_CONTEXT_TYPE, *PWWAN_CONTEXT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WwanContextTypeNone"></a><a id="wwancontexttypenone"></a><a id="WWANCONTEXTTYPENONE"></a><b>WwanContextTypeNone</b>

<dd>
<p>The context is not yet provisioned.</p>
</dd>

### -field <a id="WwanContextTypeInternet"></a><a id="wwancontexttypeinternet"></a><a id="WWANCONTEXTTYPEINTERNET"></a><b>WwanContextTypeInternet</b>

<dd>
<p>The context represents a connection to the Internet.</p>
</dd>

### -field <a id="WwanContextTypeVpn"></a><a id="wwancontexttypevpn"></a><a id="WWANCONTEXTTYPEVPN"></a><b>WwanContextTypeVpn</b>

<dd>
<p>The context represents a connection to virtual private network (VPN to a corporate
     network).</p>
</dd>

### -field <a id="WwanContextTypeVoice"></a><a id="wwancontexttypevoice"></a><a id="WWANCONTEXTTYPEVOICE"></a><b>WwanContextTypeVoice</b>

<dd>
<p>The context represents a connection to a Voice-over-IP (VOIP) service.</p>
</dd>

### -field <a id="WwanContextTypeVideoShare"></a><a id="wwancontexttypevideoshare"></a><a id="WWANCONTEXTTYPEVIDEOSHARE"></a><b>WwanContextTypeVideoShare</b>

<dd>
<p>The context represents a connection to a video sharing service.</p>
</dd>

### -field <a id="WwanContextTypeCustom"></a><a id="wwancontexttypecustom"></a><a id="WWANCONTEXTTYPECUSTOM"></a><b>WwanContextTypeCustom</b>

<dd>
<p>The context represents a connection to a custom service.</p>
</dd>

### -field <a id="WwanContextTypePurchase"></a><a id="wwancontexttypepurchase"></a><a id="WWANCONTEXTTYPEPURCHASE"></a><b>WwanContextTypePurchase</b>

<dd>
<p>Purchase a connection. For example, a walled garden, hot-lining or captive portal.</p>
</dd>

### -field <a id="WwanContextTypeMax"></a><a id="wwancontexttypemax"></a><a id="WWANCONTEXTTYPEMAX"></a><b>WwanContextTypeMax</b>

<dd>
<p>The total number of supported context types.</p>
</dd>
</dl>

## -remarks
<p>This enumeration indicates the usage of the provisioned context. For example, whether the context is
    used to connect to the Internet, or to a VPN into a corporate network. Miniport driver should specify 
    <b>WwanContextTypeNone</b> for empty (unprovisioned) context slots.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 8 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wwan\ns-wwan--wwan-context.md">WWAN_CONTEXT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_CONTEXT_TYPE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
