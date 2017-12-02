---
UID: NS.rilapitypes.RILPOSITIONINFO_V2~r3
title: RILPOSITIONINFO_V2
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfo_v2_2.htm
old-project: netvista
ms.assetid: f91d95bf-715d-484b-b44e-19bd2250d304
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILPOSITIONINFO_V2,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILPOSITIONINFO_V2
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

# RILPOSITIONINFO_V2 structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILPOSITIONINFO_V2 {
  DWORD                                       cbSize;
  DWORD                                       dwSystemType;
  RILPOSITIONINFOGSM                          stGSMServingCellInfo;
  RILPOSITIONINFOUMTS                         stUMTSServingCellInfo;
  RILPOSITIONINFOTDSCDMA                      stTDSCDMAServingCellInfo;
  RILPOSITIONINFOLTE                          stLTEServingCellInfo;
  DWORD                                       dwCntGSMNMR;
  RILGSMNMR [MAX_GSMPOS_COUNT_OF_NMR]         rgNMR;
  DWORD                                       dwCntUMTSMRL;
  RILUMTSMRL [MAX_UMTSPOS_COUNT_OF_MRL]       ruMRL;
  DWORD                                       dwCntTDSCDMAMRL;
  RILTDSCDMAMRL [MAX_TDSCDMAPOS_COUNT_OF_MRL] rtMRL;
  DWORD                                       dwCntEUTRAMRL;
  RILEUTRAMRL [MAX_EUTRAPOS_COUNT_OF_MRL]     reMRL;
  DWORD                                       dwCntC2KMRL;
  RILC2KMRL [MAX_C2KPOS_COUNT_OF_MRL]         rc2kMRL;
} RILPOSITIONINFO_V2, RILPOSITIONINFO_V2;
````


## -struct-fields
<dl>

### -field cbSize

<dd></dd>

### -field dwSystemType

<dd></dd>

### -field stGSMServingCellInfo

<dd></dd>

### -field stUMTSServingCellInfo

<dd></dd>

### -field stTDSCDMAServingCellInfo

<dd></dd>

### -field stLTEServingCellInfo

<dd></dd>

### -field dwCntGSMNMR

<dd></dd>

### -field rgNMR

<dd></dd>

### -field dwCntUMTSMRL

<dd></dd>

### -field ruMRL

<dd></dd>

### -field dwCntTDSCDMAMRL

<dd></dd>

### -field rtMRL

<dd></dd>

### -field dwCntEUTRAMRL

<dd></dd>

### -field reMRL

<dd></dd>

### -field dwCntC2KMRL

<dd></dd>

### -field rc2kMRL

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