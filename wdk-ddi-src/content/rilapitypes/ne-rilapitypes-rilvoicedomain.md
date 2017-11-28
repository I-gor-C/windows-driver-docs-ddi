---
UID: NE.rilapitypes.RILVOICEDOMAIN
title: RILVOICEDOMAIN
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilvoicedomain_2.htm
old-project: netvista
ms.assetid: bc0e9ba8-c790-402a-900a-7ae2b4f76060
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILVOICEDOMAIN
req.alt-loc: rilapitypes.h
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

# RILVOICEDOMAIN enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>