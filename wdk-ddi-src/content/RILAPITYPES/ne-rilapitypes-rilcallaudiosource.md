---
UID: NE.rilapitypes.RILCALLAUDIOSOURCE
title: RILCALLAUDIOSOURCE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallaudiosource_2.htm
ms.assetid: 9da5508a-7397-4260-b5d8-16b0d624b98b
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCALLAUDIOSOURCE
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
ms.keywords: RIL_WritePhonebookEntry
req.iface: 
req.product: Windows 10 or later.
---

# RILCALLAUDIOSOURCE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCALLAUDIOSOURCE { 
  RIL_CALLAUDIOSOURCE_PKT_MODEM,
  RIL_CALLAUDIOSOURCE_PKT_APP,
  RIL_CALLAUDIOSOURCE_MAX
} RILCALLAUDIOSOURCE;
````


## -enum-fields
<dl>

### -field <a id="RIL_CALLAUDIOSOURCE_PKT_MODEM"></a><a id="ril_callaudiosource_pkt_modem"></a><b>RIL_CALLAUDIOSOURCE_PKT_MODEM</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOSOURCE_PKT_APP"></a><a id="ril_callaudiosource_pkt_app"></a><b>RIL_CALLAUDIOSOURCE_PKT_APP</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOSOURCE_MAX"></a><a id="ril_callaudiosource_max"></a><b>RIL_CALLAUDIOSOURCE_MAX</b>

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