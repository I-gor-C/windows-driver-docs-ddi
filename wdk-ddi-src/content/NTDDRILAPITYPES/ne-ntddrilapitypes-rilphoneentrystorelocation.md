---
UID: NE.ntddrilapitypes.RILPHONEENTRYSTORELOCATION
title: RILPHONEENTRYSTORELOCATION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphoneentrystorelocation.htm
ms.assetid: 2a20e9c8-a8f2-4519-a22b-2444c46ba13a
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILPHONEENTRYSTORELOCATION
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
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
req.iface: 
---

# RILPHONEENTRYSTORELOCATION enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILPHONEENTRYSTORELOCATION { 
  RIL_PBLOC_UICCFIXDIALING,
  RIL_PBLOC_OWNNUMBERS,
  RIL_PBLOC_UICCPHONEBOOK,
  RIL_PBLOC_UICCSERVICEDIALING,
  RIL_PBLOC_ALL
} RILPHONEENTRYSTORELOCATION;
````


## -enum-fields
<dl>

### -field <a id="RIL_PBLOC_UICCFIXDIALING"></a><a id="ril_pbloc_uiccfixdialing"></a><b>RIL_PBLOC_UICCFIXDIALING</b>

<dd></dd>

### -field <a id="RIL_PBLOC_OWNNUMBERS"></a><a id="ril_pbloc_ownnumbers"></a><b>RIL_PBLOC_OWNNUMBERS</b>

<dd></dd>

### -field <a id="RIL_PBLOC_UICCPHONEBOOK"></a><a id="ril_pbloc_uiccphonebook"></a><b>RIL_PBLOC_UICCPHONEBOOK</b>

<dd></dd>

### -field <a id="RIL_PBLOC_UICCSERVICEDIALING"></a><a id="ril_pbloc_uiccservicedialing"></a><b>RIL_PBLOC_UICCSERVICEDIALING</b>

<dd></dd>

### -field <a id="RIL_PBLOC_ALL"></a><a id="ril_pbloc_all"></a><b>RIL_PBLOC_ALL</b>

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