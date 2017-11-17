---
UID: NE.ntddrilapitypes.RILPHONEBOOKLOCATIONCAPS
title: RILPHONEBOOKLOCATIONCAPS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebooklocationcaps.htm
ms.assetid: df2f059c-d1c3-4716-8254-47c71f0b4a7c
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
req.alt-api: RILPHONEBOOKLOCATIONCAPS
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

# RILPHONEBOOKLOCATIONCAPS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILPHONEBOOKLOCATIONCAPS { 
  RIL_CAPS_PBLOC_UICCFIXDIALING,
  RIL_CAPS_PBLOC_OWNNUMBERS,
  RIL_CAPS_PBLOC_UICCPHONEBOOK,
  RIL_CAPS_PBLOC_UICCSERVICEDIALING,
  RIL_CAPS_PBLOC_ALL
} RILPHONEBOOKLOCATIONCAPS;
````


## -enum-fields
<dl>

### -field <a id="RIL_CAPS_PBLOC_UICCFIXDIALING"></a><a id="ril_caps_pbloc_uiccfixdialing"></a><b>RIL_CAPS_PBLOC_UICCFIXDIALING</b>

<dd></dd>

### -field <a id="RIL_CAPS_PBLOC_OWNNUMBERS"></a><a id="ril_caps_pbloc_ownnumbers"></a><b>RIL_CAPS_PBLOC_OWNNUMBERS</b>

<dd></dd>

### -field <a id="RIL_CAPS_PBLOC_UICCPHONEBOOK"></a><a id="ril_caps_pbloc_uiccphonebook"></a><b>RIL_CAPS_PBLOC_UICCPHONEBOOK</b>

<dd></dd>

### -field <a id="RIL_CAPS_PBLOC_UICCSERVICEDIALING"></a><a id="ril_caps_pbloc_uiccservicedialing"></a><b>RIL_CAPS_PBLOC_UICCSERVICEDIALING</b>

<dd></dd>

### -field <a id="RIL_CAPS_PBLOC_ALL"></a><a id="ril_caps_pbloc_all"></a><b>RIL_CAPS_PBLOC_ALL</b>

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