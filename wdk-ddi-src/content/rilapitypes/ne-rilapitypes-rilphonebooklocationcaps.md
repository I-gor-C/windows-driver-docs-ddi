---
UID: NE.rilapitypes.RILPHONEBOOKLOCATIONCAPS
title: RILPHONEBOOKLOCATIONCAPS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebooklocationcaps_2.htm
old-project: netvista
ms.assetid: 6fe1077d-3b12-4cb6-b2ed-675b19b034c4
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
req.alt-api: RILPHONEBOOKLOCATIONCAPS
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

# RILPHONEBOOKLOCATIONCAPS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>