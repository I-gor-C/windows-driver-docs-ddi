---
UID: NS.rilapitypes.RILPOSITIONINFO_V1
title: RILPOSITIONINFO_V1
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfo_v1_2.htm
ms.assetid: ff622111-e4c3-47eb-9509-dbe86d0d5acf
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILPOSITIONINFO_V1
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
ms.keywords: RILPOSITIONINFO_V1, RILPOSITIONINFO_V1
req.iface: 
req.product: Windows 10 or later.
---

# RILPOSITIONINFO_V1 structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILPOSITIONINFO_V1 {
  DWORD                                   cbSize;
  DWORD                                   dwSystemType;
  RILPOSITIONINFOGSM                      stGSMServingCellInfo;
  RILPOSITIONINFOUMTS                     stUMTSServingCellInfo;
  RILPOSITIONINFOLTE                      stLTEServingCellInfo;
  DWORD                                   dwCntGSMNMR;
  RILGSMNMR [MAX_GSMPOS_COUNT_OF_NMR]     rgNMR;
  DWORD                                   dwCntUMTSMRL;
  RILUMTSMRL [MAX_UMTSPOS_COUNT_OF_MRL]   ruMRL;
  DWORD                                   dwCntEUTRAMRL;
  RILEUTRAMRL [MAX_EUTRAPOS_COUNT_OF_MRL] reMRL;
  DWORD                                   dwCntC2KMRL;
  RILC2KMRL [MAX_C2KPOS_COUNT_OF_MRL]     rc2kMRL;
} RILPOSITIONINFO_V1, RILPOSITIONINFO_V1;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwSystemType</b>

<dd></dd>

### -field <b>stGSMServingCellInfo</b>

<dd></dd>

### -field <b>stUMTSServingCellInfo</b>

<dd></dd>

### -field <b>stLTEServingCellInfo</b>

<dd></dd>

### -field <b>dwCntGSMNMR</b>

<dd></dd>

### -field <b>rgNMR</b>

<dd></dd>

### -field <b>dwCntUMTSMRL</b>

<dd></dd>

### -field <b>ruMRL</b>

<dd></dd>

### -field <b>dwCntEUTRAMRL</b>

<dd></dd>

### -field <b>reMRL</b>

<dd></dd>

### -field <b>dwCntC2KMRL</b>

<dd></dd>

### -field <b>rc2kMRL</b>

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