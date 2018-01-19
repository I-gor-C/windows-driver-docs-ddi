---
UID : NE:rilapitypes.RILPHONEBOOKLOCATIONCAPS
title : RILPHONEBOOKLOCATIONCAPS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilphonebooklocationcaps_2.htm
old-project : netvista
ms.assetid : 6fe1077d-3b12-4cb6-b2ed-675b19b034c4
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILPHONEBOOKLOCATIONCAPS, RILPHONEBOOKLOCATIONCAPS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : rilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RILPHONEBOOKLOCATIONCAPS
req.alt-loc : rilapitypes.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : RILPHONEBOOKLOCATIONCAPS
req.product : Windows 10 or later.
---

# RILPHONEBOOKLOCATIONCAPS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPHONEBOOKLOCATIONCAPS { 
  RIL_CAPS_PBLOC_UICCFIXDIALING,
  RIL_CAPS_PBLOC_OWNNUMBERS,
  RIL_CAPS_PBLOC_UICCPHONEBOOK,
  RIL_CAPS_PBLOC_UICCSERVICEDIALING,
  RIL_CAPS_PBLOC_ALL
} RILPHONEBOOKLOCATIONCAPS;
````

## Constants

<table>

<tr>
<td>RIL_CAPS_PBLOC_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_CAPS_PBLOC_OWNNUMBERS</td>
<td></td>
</tr>

<tr>
<td>RIL_CAPS_PBLOC_UICCFIXDIALING</td>
<td></td>
</tr>

<tr>
<td>RIL_CAPS_PBLOC_UICCPHONEBOOK</td>
<td></td>
</tr>

<tr>
<td>RIL_CAPS_PBLOC_UICCSERVICEDIALING</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |