---
UID: NE.rilapitypes.RILUMTSKIND
title: RILUMTSKIND
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilumtskind_2.htm
old-project: netvista
ms.assetid: 66322f97-e249-4337-b228-826ab4728220
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
req.alt-api: RILUMTSKIND
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

# RILUMTSKIND enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILUMTSKIND { 
  RIL_UMTSKIND_HSDPA,
  RIL_UMTSKIND_HSUPA,
  RIL_UMTSKIND_HSPAPLUS,
  RIL_UMTSKIND_DC_HSPAPLUS,
  RIL_UMTSKIND_HSPAPLUS_64QAM,
  RIL_UMTSKIND_MAX
} RILUMTSKIND;
````


## -enum-fields
<dl>

### -field <a id="RIL_UMTSKIND_HSDPA"></a><a id="ril_umtskind_hsdpa"></a><b>RIL_UMTSKIND_HSDPA</b>

<dd></dd>

### -field <a id="RIL_UMTSKIND_HSUPA"></a><a id="ril_umtskind_hsupa"></a><b>RIL_UMTSKIND_HSUPA</b>

<dd></dd>

### -field <a id="RIL_UMTSKIND_HSPAPLUS"></a><a id="ril_umtskind_hspaplus"></a><b>RIL_UMTSKIND_HSPAPLUS</b>

<dd></dd>

### -field <a id="RIL_UMTSKIND_DC_HSPAPLUS"></a><a id="ril_umtskind_dc_hspaplus"></a><b>RIL_UMTSKIND_DC_HSPAPLUS</b>

<dd></dd>

### -field <a id="RIL_UMTSKIND_HSPAPLUS_64QAM"></a><a id="ril_umtskind_hspaplus_64qam"></a><b>RIL_UMTSKIND_HSPAPLUS_64QAM</b>

<dd></dd>

### -field <a id="RIL_UMTSKIND_MAX"></a><a id="ril_umtskind_max"></a><b>RIL_UMTSKIND_MAX</b>

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