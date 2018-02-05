---
UID : NE:rilapitypes.RILPHONEENTRYSTORELOCATION
title : RILPHONEENTRYSTORELOCATION
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilphoneentrystorelocation_2.htm
old-project : netvista
ms.assetid : f9166dfa-e895-4aca-8080-af3cfe9c143f
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_PBLOC_UICCSERVICEDIALING, RIL_PBLOC_ALL, RIL_PBLOC_UICCFIXDIALING, netvista.rilphoneentrystorelocation_2, RIL_PBLOC_OWNNUMBERS, RIL_PBLOC_UICCPHONEBOOK, rilapitypes/RIL_PBLOC_UICCPHONEBOOK, rilapitypes/RIL_PBLOC_OWNNUMBERS, rilapitypes/RIL_PBLOC_UICCFIXDIALING, rilapitypes/RIL_PBLOC_UICCSERVICEDIALING, RILPHONEENTRYSTORELOCATION enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_PBLOC_ALL, RILPHONEENTRYSTORELOCATION, rilapitypes/RILPHONEENTRYSTORELOCATION
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : RILPHONEENTRYSTORELOCATION
req.product : Windows 10 or later.
---

# RILPHONEENTRYSTORELOCATION Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPHONEENTRYSTORELOCATION { 
  RIL_PBLOC_UICCFIXDIALING,
  RIL_PBLOC_OWNNUMBERS,
  RIL_PBLOC_UICCPHONEBOOK,
  RIL_PBLOC_UICCSERVICEDIALING,
  RIL_PBLOC_ALL
} RILPHONEENTRYSTORELOCATION;
````

## Constants

<table>

<tr>
<td>RIL_PBLOC_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PBLOC_OWNNUMBERS</td>
<td></td>
</tr>

<tr>
<td>RIL_PBLOC_UICCFIXDIALING</td>
<td></td>
</tr>

<tr>
<td>RIL_PBLOC_UICCPHONEBOOK</td>
<td></td>
</tr>

<tr>
<td>RIL_PBLOC_UICCSERVICEDIALING</td>
<td></td>
</tr>

<tr>
<td>RIL_PBLOC_UNKNOWN</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |