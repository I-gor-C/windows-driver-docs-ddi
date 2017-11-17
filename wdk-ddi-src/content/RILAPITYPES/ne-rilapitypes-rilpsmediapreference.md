---
UID: NE.rilapitypes.RILPSMEDIAPREFERENCE
title: RILPSMEDIAPREFERENCE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpsmediapreference_2.htm
ms.assetid: 607c00a2-6f7e-4a68-87da-f54b8dd73b88
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
req.alt-api: RILPSMEDIAPREFERENCE
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

# RILPSMEDIAPREFERENCE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILPSMEDIAPREFERENCE { 
  RIL_PSMPREF_WIFIONLY,
  RIL_PSMPREF_WIFIPREFERRED,
  RIL_PSMPREF_CELLONLY,
  RIL_PSMPREF_CELLPREFERRED,
  RIL_PSMPREF_NUMBER_OF_VALUES
} RILPSMEDIAPREFERENCE;
````


## -enum-fields
<dl>

### -field <a id="RIL_PSMPREF_WIFIONLY"></a><a id="ril_psmpref_wifionly"></a><b>RIL_PSMPREF_WIFIONLY</b>

<dd></dd>

### -field <a id="RIL_PSMPREF_WIFIPREFERRED"></a><a id="ril_psmpref_wifipreferred"></a><b>RIL_PSMPREF_WIFIPREFERRED</b>

<dd></dd>

### -field <a id="RIL_PSMPREF_CELLONLY"></a><a id="ril_psmpref_cellonly"></a><b>RIL_PSMPREF_CELLONLY</b>

<dd></dd>

### -field <a id="RIL_PSMPREF_CELLPREFERRED"></a><a id="ril_psmpref_cellpreferred"></a><b>RIL_PSMPREF_CELLPREFERRED</b>

<dd></dd>

### -field <a id="RIL_PSMPREF_NUMBER_OF_VALUES"></a><a id="ril_psmpref_number_of_values"></a><b>RIL_PSMPREF_NUMBER_OF_VALUES</b>

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