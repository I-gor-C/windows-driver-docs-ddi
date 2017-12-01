---
UID: NE.rilapitypes.RILCALLBARRINGSTATUSPARAMSTYPE
title: RILCALLBARRINGSTATUSPARAMSTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallbarringstatusparamstype_2.htm
old-project: netvista
ms.assetid: ed54bc8d-0cf2-4d6a-935c-b5b2a539eea0
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: RILCALLBARRINGSTATUSPARAMSTYPE
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

# RILCALLBARRINGSTATUSPARAMSTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCALLBARRINGSTATUSPARAMSTYPE { 
  RIL_BARRTYPE_OUTGOINGINT,
  RIL_BARRTYPE_OUTGOINGINTEXTOHOME,
  RIL_BARRTYPE_ALLINCOMING,
  RIL_BARRTYPE_INCOMINGROAMING,
  RIL_BARRTYPE_INCOMINGNOTINUICC,
  RIL_BARRTYPE_ALLBARRING,
  RIL_BARRTYPE_ALLOUTGOINGBARRING,
  RIL_BARRTYPE_ALLINCOMINGBARRING,
  RIL_BARRTYPE_ALL
} RILCALLBARRINGSTATUSPARAMSTYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_BARRTYPE_OUTGOINGINT"></a><a id="ril_barrtype_outgoingint"></a><b>RIL_BARRTYPE_OUTGOINGINT</b>

<dd></dd>

### -field <a id="RIL_BARRTYPE_OUTGOINGINTEXTOHOME"></a><a id="ril_barrtype_outgoingintextohome"></a><b>RIL_BARRTYPE_OUTGOINGINTEXTOHOME</b>

<dd></dd>

### -field <a id="RIL_BARRTYPE_ALLINCOMING"></a><a id="ril_barrtype_allincoming"></a><b>RIL_BARRTYPE_ALLINCOMING</b>

<dd></dd>

### -field <a id="RIL_BARRTYPE_INCOMINGROAMING"></a><a id="ril_barrtype_incomingroaming"></a><b>RIL_BARRTYPE_INCOMINGROAMING</b>

<dd></dd>

### -field <a id="RIL_BARRTYPE_INCOMINGNOTINUICC"></a><a id="ril_barrtype_incomingnotinuicc"></a><b>RIL_BARRTYPE_INCOMINGNOTINUICC</b>

<dd></dd>

### -field <a id="RIL_BARRTYPE_ALLBARRING"></a><a id="ril_barrtype_allbarring"></a><b>RIL_BARRTYPE_ALLBARRING</b>

<dd></dd>

### -field <a id="RIL_BARRTYPE_ALLOUTGOINGBARRING"></a><a id="ril_barrtype_alloutgoingbarring"></a><b>RIL_BARRTYPE_ALLOUTGOINGBARRING</b>

<dd></dd>

### -field <a id="RIL_BARRTYPE_ALLINCOMINGBARRING"></a><a id="ril_barrtype_allincomingbarring"></a><b>RIL_BARRTYPE_ALLINCOMINGBARRING</b>

<dd></dd>

### -field <a id="RIL_BARRTYPE_ALL"></a><a id="ril_barrtype_all"></a><b>RIL_BARRTYPE_ALL</b>

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