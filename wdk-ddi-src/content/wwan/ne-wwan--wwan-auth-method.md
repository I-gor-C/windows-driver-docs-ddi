---
UID: NE.wwan._WWAN_AUTH_METHOD
title: WWAN_AUTH_METHOD
author: windows-driver-content
description: The WWAN_AUTH_METHOD enumeration lists supported authentication methods.
old-location: netvista\wwan_auth_method.htm
old-project: netvista
ms.assetid: D24D8C90-8F65-42BC-8FBC-308ECC4A73C9
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_AUTH_METHOD
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

# WWAN_AUTH_METHOD enumeration



## -description
<p>The WWAN_AUTH_METHOD enumeration lists supported authentication methods.</p>


## -syntax

````
typedef enum _WWAN_AUTH_METHOD { 
  WwanAuthSim        = 0,
  WwanAuthAka,
  WwanAuthAkaPrime,
  WwanAuthMethodMax
} WWAN_AUTH_METHOD;
````


## -enum-fields
<dl>

### -field <a id="WwanAuthSim"></a><a id="wwanauthsim"></a><a id="WWANAUTHSIM"></a><b>WwanAuthSim</b>

<dd>
<p>Authenticate using the SIM method.</p>
</dd>

### -field <a id="WwanAuthAka"></a><a id="wwanauthaka"></a><a id="WWANAUTHAKA"></a><b>WwanAuthAka</b>

<dd>
<p>Authenticate using the AKA method.</p>
</dd>

### -field <a id="WwanAuthAkaPrime"></a><a id="wwanauthakaprime"></a><a id="WWANAUTHAKAPRIME"></a><b>WwanAuthAkaPrime</b>

<dd>
<p>Authenticate using the AKA' (AKA Prime) method.</p>
</dd>

### -field <a id="WwanAuthMethodMax"></a><a id="wwanauthmethodmax"></a><a id="WWANAUTHMETHODMAX"></a><b>WwanAuthMethodMax</b>

<dd>
<p>This value is reserved. Do not use.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh464127">WWAN_AUTH_CHALLENGE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh464129">WWAN_AUTH_RESPONSE</a> structures use this enumeration.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh464127">WWAN_AUTH_CHALLENGE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh464129">WWAN_AUTH_RESPONSE</a> structures use this enumeration.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh464127">WWAN_AUTH_CHALLENGE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh464129">WWAN_AUTH_RESPONSE</a> structures use this enumeration.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with  Windows 8.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464127">WWAN_AUTH_CHALLENGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464129">WWAN_AUTH_RESPONSE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_AUTH_METHOD enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
