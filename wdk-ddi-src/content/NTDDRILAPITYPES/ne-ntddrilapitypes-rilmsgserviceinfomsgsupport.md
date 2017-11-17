---
UID: NE.ntddrilapitypes.RILMSGSERVICEINFOMSGSUPPORT
title: RILMSGSERVICEINFOMSGSUPPORT
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgserviceinfomsgsupport.htm
ms.assetid: b09a5b1d-b8da-4a75-b2d5-ee07072d45aa
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILMSGSERVICEINFOMSGSUPPORT
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
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
req.iface: 
---

# RILMSGSERVICEINFOMSGSUPPORT enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGSERVICEINFOMSGSUPPORT { 
  RIL_MSI_SMS_OUTGOING,
  RIL_MSI_SMS_BROADCAST
} RILMSGSERVICEINFOMSGSUPPORT;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSI_SMS_OUTGOING"></a><a id="ril_msi_sms_outgoing"></a><b>RIL_MSI_SMS_OUTGOING</b>

<dd></dd>

### -field <a id="RIL_MSI_SMS_BROADCAST"></a><a id="ril_msi_sms_broadcast"></a><b>RIL_MSI_SMS_BROADCAST</b>

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