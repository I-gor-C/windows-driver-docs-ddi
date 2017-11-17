---
UID: NS.wlanihv._DOT11_EAP_RESULT
title: DOT11_EAP_RESULT
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_eap_result.htm
ms.assetid: 90898f5c-ffc1-4e6c-a8f8-ba839f449082
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: wlanihv.h
req.include-header: Winlanihv.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_EAP_RESULT
req.alt-loc: wlanihv.h
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
ms.keywords: DOT11_EAP_RESULT, DOT11_EAP_RESULT, *PDOT11_EAP_RESULT
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_EAP_RESULT structure



## -description

## -syntax

````
typedef struct _DOT11_EAP_RESULT {
  UINT32         dwFailureReasonCode;
  EAP_ATTRIBUTES *pAttribArray;
} DOT11_EAP_RESULT, *PDOT11_EAP_RESULT;
````


## -struct-fields
<dl>

### -field <b>dwFailureReasonCode</b>

<dd>
<p>The reason code returned by the EAP method. The meaning of the code is specific to the EAP
     method.</p>
</dd>

### -field <b>pAttribArray</b>

<dd>
<p>A pointer to an EAP_ATTRIBUTES array structure that contains the EAP attributes returned by the
     authentication session. For more information about EAP_ATTRIBUTES, see the Microsoft Windows SDK
     documentation.</p>
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
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wlanihv.h (include Winlanihv.h)</dt>
</dl>
</td>
</tr>
</table>