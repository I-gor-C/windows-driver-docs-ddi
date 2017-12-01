---
UID: NE.wwan._WWAN_AUTH_PROTOCOL
title: WWAN_AUTH_PROTOCOL
author: windows-driver-content
description: The WWAN_AUTH_PROTOCOL enumeration lists the different types of authentication protocols that are supported by the MB device.
old-location: netvista\wwan_auth_protocol.htm
old-project: netvista
ms.assetid: 33c9523e-3195-456f-8e17-b9539475bc67
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_AUTH_PROTOCOL
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

# WWAN_AUTH_PROTOCOL enumeration



## -description
<p>The WWAN_AUTH_PROTOCOL enumeration lists the different types of authentication protocols that are
  supported by the MB device.</p>


## -syntax

````
typedef enum _WWAN_AUTH_PROTOCOL { 
  WwanAuthProtocolNone      = 0,
  WwanAuthProtocolPap,
  WwanAuthProtocolChap,
  WwanAuthProtocolMsChapV2,
  WwanAuthProtocolMax
} WWAN_AUTH_PROTOCOL, *PWWAN_AUTH_PROTOCOL;
````


## -enum-fields
<dl>

### -field <a id="WwanAuthProtocolNone"></a><a id="wwanauthprotocolnone"></a><a id="WWANAUTHPROTOCOLNONE"></a><b>WwanAuthProtocolNone</b>

<dd>
<p>No authentication protocol.</p>
</dd>

### -field <a id="WwanAuthProtocolPap"></a><a id="wwanauthprotocolpap"></a><a id="WWANAUTHPROTOCOLPAP"></a><b>WwanAuthProtocolPap</b>

<dd>
<p>Unencrypted password authentication.</p>
</dd>

### -field <a id="WwanAuthProtocolChap"></a><a id="wwanauthprotocolchap"></a><a id="WWANAUTHPROTOCOLCHAP"></a><b>WwanAuthProtocolChap</b>

<dd>
<p>Use the Challenge Handshake Authentication Protocol (CHAP).</p>
</dd>

### -field <a id="WwanAuthProtocolMsChapV2"></a><a id="wwanauthprotocolmschapv2"></a><a id="WWANAUTHPROTOCOLMSCHAPV2"></a><b>WwanAuthProtocolMsChapV2</b>

<dd>
<p>Use the Microsoft Challenge Handshake Authentication Protocol (CHAP) v2.0.</p>
</dd>

### -field <a id="WwanAuthProtocolMax"></a><a id="wwanauthprotocolmax"></a><a id="WWANAUTHPROTOCOLMAX"></a><b>WwanAuthProtocolMax</b>

<dd>
<p>The total number of supported authentication protocols.</p>
</dd>
</dl>

## -remarks
<p>This enumeration applies only to GSM devices. The MB Service specifies 
    <b>WwanAuthProtocolNone</b> as the authentication type for CDMA-based devices.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 7.</p>
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
<a href="..\wwan\ns-wwan--wwan-set-context-state.md">WWAN_SET_CONTEXT_STATE</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-context.md">WWAN_CONTEXT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_AUTH_PROTOCOL enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
