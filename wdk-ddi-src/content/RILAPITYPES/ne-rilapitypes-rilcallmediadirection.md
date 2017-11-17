---
UID: NE.rilapitypes.RILCALLMEDIADIRECTION
title: RILCALLMEDIADIRECTION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmediadirection_2.htm
ms.assetid: fcb5f1a4-8673-412e-95ac-5f3ca781411b
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
req.alt-api: RILCALLMEDIADIRECTION
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

# RILCALLMEDIADIRECTION enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCALLMEDIADIRECTION { 
  RIL_CALLMEDIADIRECTION_RX,
  RIL_CALLMEDIADIRECTION_TX,
  RIL_CALLMEDIADIRECTION_RXTX,
  RIL_CALLMEDIADIRECTION_MAX
} RILCALLMEDIADIRECTION;
````


## -enum-fields
<dl>

### -field <a id="RIL_CALLMEDIADIRECTION_RX"></a><a id="ril_callmediadirection_rx"></a><b>RIL_CALLMEDIADIRECTION_RX</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIADIRECTION_TX"></a><a id="ril_callmediadirection_tx"></a><b>RIL_CALLMEDIADIRECTION_TX</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIADIRECTION_RXTX"></a><a id="ril_callmediadirection_rxtx"></a><b>RIL_CALLMEDIADIRECTION_RXTX</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIADIRECTION_MAX"></a><a id="ril_callmediadirection_max"></a><b>RIL_CALLMEDIADIRECTION_MAX</b>

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