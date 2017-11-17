---
UID: NE.rilapitypes.RILMESSAGETYPE
title: RILMESSAGETYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmessagetype_2.htm
ms.assetid: 5f167bd5-a2b8-48a1-b403-e9ac68122ae4
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
req.alt-api: RILMESSAGETYPE
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

# RILMESSAGETYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILMESSAGETYPE { 
  RIL_MSGTYPE_IN_STATUS,
  RIL_MSGTYPE_IN_IS637STATUS,
  RIL_MSGTYPE_IN_CDMADELIVER,
  RIL_MSGTYPE_OUT_SUBMIT,
  RIL_MSGTYPE_OUT_CDMASUBMIT,
  RIL_MSGTYPE_BC_GENERAL
} RILMESSAGETYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGTYPE_IN_STATUS"></a><a id="ril_msgtype_in_status"></a><b>RIL_MSGTYPE_IN_STATUS</b>

<dd></dd>

### -field <a id="RIL_MSGTYPE_IN_IS637STATUS"></a><a id="ril_msgtype_in_is637status"></a><b>RIL_MSGTYPE_IN_IS637STATUS</b>

<dd></dd>

### -field <a id="RIL_MSGTYPE_IN_CDMADELIVER"></a><a id="ril_msgtype_in_cdmadeliver"></a><b>RIL_MSGTYPE_IN_CDMADELIVER</b>

<dd></dd>

### -field <a id="RIL_MSGTYPE_OUT_SUBMIT"></a><a id="ril_msgtype_out_submit"></a><b>RIL_MSGTYPE_OUT_SUBMIT</b>

<dd></dd>

### -field <a id="RIL_MSGTYPE_OUT_CDMASUBMIT"></a><a id="ril_msgtype_out_cdmasubmit"></a><b>RIL_MSGTYPE_OUT_CDMASUBMIT</b>

<dd></dd>

### -field <a id="RIL_MSGTYPE_BC_GENERAL"></a><a id="ril_msgtype_bc_general"></a><b>RIL_MSGTYPE_BC_GENERAL</b>

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