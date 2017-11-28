---
UID: NS.wwan._WWAN_AUTH_CHALLENGE
title: WWAN_AUTH_CHALLENGE
author: windows-driver-content
description: The WWAN_AUTH_CHALLENGE structure represents an authentication challenge for a specific method.
old-location: netvista\wwan_auth_challenge.htm
old-project: netvista
ms.assetid: A31B9E91-B5F9-4EF3-AD9E-A5E26CBD4B35
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WWAN_AUTH_CHALLENGE, WWAN_AUTH_CHALLENGE, *PWWAN_AUTH_CHALLENGE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_AUTH_CHALLENGE
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

# WWAN_AUTH_CHALLENGE structure



## -description
<p>The WWAN_AUTH_CHALLENGE structure represents an authentication challenge for a specific method.</p>


## -syntax

````
typedef struct _WWAN_AUTH_CHALLENGE {
  WWAN_AUTH_METHOD AuthMethod;
  union {
    WWAN_AUTH_SIM_CHALLENGE  AuthSim;
    WWAN_AUTH_AKA_CHALLENGE  AuthAka;
    WWAN_AUTH_AKAP_CHALLENGE AuthAkap;
  } u;
} WWAN_AUTH_CHALLENGE, *PWWAN_AUTH_CHALLENGE;
````


## -struct-fields
<dl>

### -field <b>AuthMethod</b>

<dd>
<p>The authentication challenge method.</p>
</dd>

### -field <b>u</b>

<dd>
<p>The container union for the different authentication challenge methods.</p>
<dl>

### -field <b>AuthSim</b>

<dd>
<p>The challenge that uses the SIM authentication method. If <b>AuthMethod</b> is set to <i>WwanAuthSim</i>, use this member.</p>
</dd>

### -field <b>AuthAka</b>

<dd>
<p>The challenge that uses the AKA authentication method.  If <b>AuthMethod</b> is set to <i>WwanAuthAka</i>, use this member.</p>
</dd>

### -field <b>AuthAkap</b>

<dd>
<p>The challenge that uses the AKA' authentication method. If <b>AuthMethod</b> is set to <i>WwanAuthAkap,</i> use this member.</p>
</dd>
</dl>
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
<p>Supported starting with  Windows 8.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464128">WWAN_AUTH_METHOD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464130">WWAN_AUTH_SIM_CHALLENGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh440304">WWAN_AUTH_AKA_CHALLENGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh440302">WWAN_AUTH_AKAP_CHALLENGE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_AUTH_CHALLENGE structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
