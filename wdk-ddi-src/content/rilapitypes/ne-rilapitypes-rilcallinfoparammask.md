---
UID: NE.rilapitypes.RILCALLINFOPARAMMASK
title: RILCALLINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallinfoparammask_2.htm
old-project: netvista
ms.assetid: 8e5935d9-382f-409d-a9ed-9381613b5d9c
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: RILCALLINFOPARAMMASK
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

# RILCALLINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCALLINFOPARAMMASK { 
  RIL_PARAM_CI_ID,
  RIL_PARAM_CI_DIRECTION,
  RIL_PARAM_CI_STATUS,
  RIL_PARAM_CI_TYPE,
  RIL_PARAM_CI_MULTIPARTY,
  RIL_PARAM_CI_ADDRESS,
  RIL_PARAM_CI_SUBADDRESS,
  RIL_PARAM_CI_DESCRIPTION,
  RIL_PARAM_CI_NUM_PRES_IND,
  RIL_PARAM_CI_NAME_PRES_IND,
  RIL_PARAM_CI_FLAGS,
  RIL_PARAM_CI_DISCONNECTINITIATOR,
  RIL_PARAM_CI_DISCONNECTREASON,
  RIL_PARAM_CI_DISCONNECTDETAILS,
  RIL_PARAM_CI_OFFERANSWER,
  RIL_PARAM_CI_HANDOVERSTATE,
  RIL_PARAM_CI_CALLMODIFICATIONCAUSE,
  RIL_PARAM_CI_RTTMODETYPE,
  RIL_PARAM_CI_RTTCAPINFO,
  RIL_PARAM_CI_RTTACTION,
  RIL_PARAM_CI_ALL
} RILCALLINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field RIL_PARAM_CI_ID

<dd></dd>

### -field RIL_PARAM_CI_DIRECTION

<dd></dd>

### -field RIL_PARAM_CI_STATUS

<dd></dd>

### -field RIL_PARAM_CI_TYPE

<dd></dd>

### -field RIL_PARAM_CI_MULTIPARTY

<dd></dd>

### -field RIL_PARAM_CI_ADDRESS

<dd></dd>

### -field RIL_PARAM_CI_SUBADDRESS

<dd></dd>

### -field RIL_PARAM_CI_DESCRIPTION

<dd></dd>

### -field RIL_PARAM_CI_NUM_PRES_IND

<dd></dd>

### -field RIL_PARAM_CI_NAME_PRES_IND

<dd></dd>

### -field RIL_PARAM_CI_FLAGS

<dd></dd>

### -field RIL_PARAM_CI_DISCONNECTINITIATOR

<dd></dd>

### -field RIL_PARAM_CI_DISCONNECTREASON

<dd></dd>

### -field RIL_PARAM_CI_DISCONNECTDETAILS

<dd></dd>

### -field RIL_PARAM_CI_OFFERANSWER

<dd></dd>

### -field RIL_PARAM_CI_HANDOVERSTATE

<dd></dd>

### -field RIL_PARAM_CI_CALLMODIFICATIONCAUSE

<dd></dd>

### -field RIL_PARAM_CI_RTTMODETYPE

<dd></dd>

### -field RIL_PARAM_CI_RTTCAPINFO

<dd></dd>

### -field RIL_PARAM_CI_RTTACTION

<dd></dd>

### -field RIL_PARAM_CI_ALL

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