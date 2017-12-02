---
UID: NE.rilapitypes.RILPERSOLOCKSUPPORTCAPS
title: RILPERSOLOCKSUPPORTCAPS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpersolocksupportcaps_2.htm
old-project: netvista
ms.assetid: 630f48cc-2236-48ec-a62a-cdafa31a3afd
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
req.alt-api: RILPERSOLOCKSUPPORTCAPS
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

# RILPERSOLOCKSUPPORTCAPS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILPERSOLOCKSUPPORTCAPS { 
  RIL_CAPS_PERSOFEATURE_3GPP_NETSUB,
  RIL_CAPS_PERSOFEATURE_3GPP_SP,
  RIL_CAPS_PERSOFEATURE_3GPP_CORP,
  RIL_CAPS_PERSOFEATURE_3GPP_USIM,
  RIL_CAPS_PERSOFEATURE_3GPP2_NETTYPE1,
  RIL_CAPS_PERSOFEATURE_3GPP2_NETTYPE2,
  RIL_CAPS_PERSOFEATURE_3GPP2_HRPD,
  RIL_CAPS_PERSOFEATURE_3GPP2_SP,
  RIL_CAPS_PERSOFEATURE_3GPP2_CORP,
  RIL_CAPS_PERSOFEATURE_3GPP2_UIM,
  RIL_CAPS_PERSOFEATURE_ALL
} RILPERSOLOCKSUPPORTCAPS;
````


## -enum-fields
<dl>

### -field RIL_CAPS_PERSOFEATURE_3GPP_NETSUB

<dd></dd>

### -field RIL_CAPS_PERSOFEATURE_3GPP_SP

<dd></dd>

### -field RIL_CAPS_PERSOFEATURE_3GPP_CORP

<dd></dd>

### -field RIL_CAPS_PERSOFEATURE_3GPP_USIM

<dd></dd>

### -field RIL_CAPS_PERSOFEATURE_3GPP2_NETTYPE1

<dd></dd>

### -field RIL_CAPS_PERSOFEATURE_3GPP2_NETTYPE2

<dd></dd>

### -field RIL_CAPS_PERSOFEATURE_3GPP2_HRPD

<dd></dd>

### -field RIL_CAPS_PERSOFEATURE_3GPP2_SP

<dd></dd>

### -field RIL_CAPS_PERSOFEATURE_3GPP2_CORP

<dd></dd>

### -field RIL_CAPS_PERSOFEATURE_3GPP2_UIM

<dd></dd>

### -field RIL_CAPS_PERSOFEATURE_ALL

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