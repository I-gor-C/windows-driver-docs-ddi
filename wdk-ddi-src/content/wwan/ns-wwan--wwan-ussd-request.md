---
UID: NS.wwan._WWAN_USSD_REQUEST
title: WWAN_USSD_REQUEST
author: windows-driver-content
description: The WWAN_USSD_REQUEST structure describes an Unstructured Supplementary Service Data (USSD) request.
old-location: netvista\wwan_ussd_request.htm
old-project: netvista
ms.assetid: 429F5EC9-F8AA-4D5D-9CA7-D9D9AEC46842
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WWAN_USSD_REQUEST, WWAN_USSD_REQUEST, *PWWAN_USSD_REQUEST
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
req.alt-api: WWAN_USSD_REQUEST
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

# WWAN_USSD_REQUEST structure



## -description
<p>The WWAN_USSD_REQUEST structure describes an Unstructured Supplementary Service Data (USSD) request.</p>


## -syntax

````
typedef struct _WWAN_USSD_REQUEST {
  WWAN_USSD_REQUEST_TYPE RequestType;
  WWAN_USSD_STRING       UssdString;
} WWAN_USSD_REQUEST, *PWWAN_USSD_REQUEST;
````


## -struct-fields
<dl>

### -field <b>RequestType</b>

<dd>
<p>The type of USSD request.</p>
</dd>

### -field <b>UssdString</b>

<dd>
<p>The USSD string that accompanies the request.</p>
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
<a href="..\wwan\ne-wwan--wwan-ussd-request-type.md">WWAN_USSD_REQUEST_TYPE</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-ussd-string.md">WWAN_USSD_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_USSD_REQUEST structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
