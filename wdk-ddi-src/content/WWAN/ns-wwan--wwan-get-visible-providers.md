---
UID: NS.wwan._WWAN_GET_VISIBLE_PROVIDERS
title: WWAN_GET_VISIBLE_PROVIDERS
author: windows-driver-content
description: The WWAN_GET_VISIBLE_PROVIDERS structure provides information about the type of visible providers to return.
old-location: netvista\wwan_get_visible_providers.htm
ms.assetid: 62516178-11F9-43F3-A70D-42C8FDDAE2DB
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_GET_VISIBLE_PROVIDERS
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
ms.keywords: WWAN_GET_VISIBLE_PROVIDERS, WWAN_GET_VISIBLE_PROVIDERS, *PWWAN_GET_VISIBLE_PROVIDERS
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_GET_VISIBLE_PROVIDERS structure



## -description
<p>The WWAN_GET_VISIBLE_PROVIDERS structure provides information about the type of visible providers to return.</p>


## -syntax

````
typedef struct _WWAN_GET_VISIBLE_PROVIDERS {
  ULONG Action;
} WWAN_GET_VISIBLE_PROVIDERS, *PWWAN_GET_VISIBLE_PROVIDERS;
````


## -struct-fields
<dl>

### -field <b>Action</b>

<dd>
<p>Provides information about the type of visible providers to return. The following values are defined:</p>
<table></table>
<p> </p>
<table>
<tr>
<td>
<p><b>Value</b></p>
</td>
<td>
<p><b>Meaning</b></p>
</td>
</tr>
<tr>
<td>
<p>WWAN_GET_VISIBLE_PROVIDERS_ALL</p>
</td>
<td>
<p>All providers that are currently visible should be returned.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_GET_VISIBLE_PROVIDERS_MULTICARRIER</p>
</td>
<td>
<p>Only providers that are currently visible and that can be set as home provider should be returned.</p>
</td>
</tr>
</table>
<p> </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh831863">NDIS_WWAN_GET_VISIBLE_PROVIDERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_GET_VISIBLE_PROVIDERS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
