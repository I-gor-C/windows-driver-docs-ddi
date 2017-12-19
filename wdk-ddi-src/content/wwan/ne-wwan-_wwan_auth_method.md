---
UID: NE.wwan._WWAN_AUTH_METHOD
title: _WWAN_AUTH_METHOD
author: windows-driver-content
description: The WWAN_AUTH_METHOD enumeration lists supported authentication methods.
old-location: netvista\wwan_auth_method.htm
old-project: NetVista
ms.assetid: D24D8C90-8F65-42BC-8FBC-308ECC4A73C9
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _WWAN_AUTH_METHOD, *PWWAN_AUTH_METHOD, PWWAN_AUTH_METHOD, WWAN_AUTH_METHOD
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
req.product: Windows 10 or later.
---

# _WWAN_AUTH_METHOD enumeration



## -description
The WWAN_AUTH_METHOD enumeration lists supported authentication methods.



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

### -field WwanAuthSim

Authenticate using the SIM method.


### -field WwanAuthAka

Authenticate using the AKA method.


### -field WwanAuthAkaPrime

Authenticate using the AKA' (AKA Prime) method.


### -field WwanAuthMethodMax

This value is reserved. Do not use.


## -remarks
The <a href="netvista.wwan_auth_challenge">WWAN_AUTH_CHALLENGE</a> and <a href="netvista.wwan_auth_response">WWAN_AUTH_RESPONSE</a> structures use this enumeration.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported starting with  Windows 8.

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="netvista.wwan_auth_challenge">WWAN_AUTH_CHALLENGE</a>
</dt>
<dt>
<a href="netvista.wwan_auth_response">WWAN_AUTH_RESPONSE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20WWAN_AUTH_METHOD enumeration%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

