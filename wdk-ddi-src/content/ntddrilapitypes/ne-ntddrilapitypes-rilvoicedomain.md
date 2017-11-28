---
UID: NE.ntddrilapitypes.RILVOICEDOMAIN
title: RILVOICEDOMAIN
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilvoicedomain.htm
old-project: netvista
ms.assetid: a7154c32-bca6-482d-b1f9-7c090a7ce432
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILVOICEDOMAIN
req.alt-loc: ntddrilapitypes.h
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
---

# RILVOICEDOMAIN enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILVOICEDOMAIN { 
  RIL_VOICE_DOMAIN_3GPP,
  RIL_VOICE_DOMAIN_3GPP2,
  RIL_VOICE_DOMAIN_IMS,
  RIL_VOICE_DOMAIN_MAX
} RILVOICEDOMAIN;
````


## -enum-fields
<dl>

### -field <a id="RIL_VOICE_DOMAIN_3GPP"></a><a id="ril_voice_domain_3gpp"></a><b>RIL_VOICE_DOMAIN_3GPP</b>

<dd></dd>

### -field <a id="RIL_VOICE_DOMAIN_3GPP2"></a><a id="ril_voice_domain_3gpp2"></a><b>RIL_VOICE_DOMAIN_3GPP2</b>

<dd></dd>

### -field <a id="RIL_VOICE_DOMAIN_IMS"></a><a id="ril_voice_domain_ims"></a><b>RIL_VOICE_DOMAIN_IMS</b>

<dd></dd>

### -field <a id="RIL_VOICE_DOMAIN_MAX"></a><a id="ril_voice_domain_max"></a><b>RIL_VOICE_DOMAIN_MAX</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>