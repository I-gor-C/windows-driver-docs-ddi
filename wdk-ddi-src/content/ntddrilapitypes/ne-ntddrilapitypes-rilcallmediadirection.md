---
UID: NE.ntddrilapitypes.RILCALLMEDIADIRECTION
title: RILCALLMEDIADIRECTION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmediadirection.htm
old-project: netvista
ms.assetid: 8c6b2329-9956-43c1-8a4d-ef9587cf0980
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
req.alt-api: RILCALLMEDIADIRECTION
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

# RILCALLMEDIADIRECTION enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>