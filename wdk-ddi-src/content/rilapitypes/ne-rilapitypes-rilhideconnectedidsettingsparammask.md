---
UID : NE:rilapitypes.RILHIDECONNECTEDIDSETTINGSPARAMMASK
title : RILHIDECONNECTEDIDSETTINGSPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilhideconnectedidsettingsparammask_2.htm
old-project : netvista
ms.assetid : 7977898a-9f45-4db5-9fe3-3702f6bc9124
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RIL_PARAM_HCIDS_ALL, RILHIDECONNECTEDIDSETTINGSPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_HCIDS_PROVISIONING, rilapitypes/RIL_PARAM_HCIDS_STATUS, RIL_PARAM_HCIDS_ALL, netvista.rilhideconnectedidsettingsparammask_2, RIL_PARAM_HCIDS_STATUS, rilapitypes/RIL_PARAM_HCIDS_PROVISIONING, rilapitypes/RILHIDECONNECTEDIDSETTINGSPARAMMASK, RILHIDECONNECTEDIDSETTINGSPARAMMASK
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
req.typenames : RILHIDECONNECTEDIDSETTINGSPARAMMASK
req.product : Windows 10 or later.
---

# RILHIDECONNECTEDIDSETTINGSPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILHIDECONNECTEDIDSETTINGSPARAMMASK { 
  RIL_PARAM_HCIDS_STATUS,
  RIL_PARAM_HCIDS_PROVISIONING,
  RIL_PARAM_HCIDS_ALL
} RILHIDECONNECTEDIDSETTINGSPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_HCIDS_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_HCIDS_EXECUTOR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_HCIDS_PROVISIONING</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_HCIDS_STATUS</td>
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