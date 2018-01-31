---
UID : NE:ntddrilapitypes.RILPHONEBOOKENTRYPARAMMASK
title : RILPHONEBOOKENTRYPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilphonebookentryparammask.htm
old-project : netvista
ms.assetid : 6c3f8053-1cb7-44e8-be17-47678b224fa9
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddrilapitypes/RIL_PARAM_PBE_ADDITIONALNUMSIZE, ntddrilapitypes/RIL_PARAM_PBE_TEXT, ntddrilapitypes/RIL_PARAM_PBE_EMAILOFFSET, ntddrilapitypes/RIL_PARAM_PBE_SECONDNAME, RIL_PARAM_PBE_ALL, ntddrilapitypes/RIL_PARAM_PBE_GROUPIDCOUNT, RIL_PARAM_PBE_ADDITIONALNUMCOUNT, RIL_PARAM_PBE_SECONDNAME, RIL_PARAM_PBE_ADDRESS, ntddrilapitypes/RIL_PARAM_PBE_ADDITIONALNUMOFFSET, RIL_PARAM_PBE_EMAILCOUNT, RIL_PARAM_PBE_ADDITIONALNUMOFFSET, ntddrilapitypes/RIL_PARAM_PBE_GROUPID, ntddrilapitypes/RIL_PARAM_PBE_ADDITIONALNUMCOUNT, RILPHONEBOOKENTRYPARAMMASK, RILPHONEBOOKENTRYPARAMMASK enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_PARAM_PBE_EMAILCOUNT, ntddrilapitypes/RIL_PARAM_PBE_ADDRESS, RIL_PARAM_PBE_EMAILSIZE, netvista.rilphonebookentryparammask, ntddrilapitypes/RILPHONEBOOKENTRYPARAMMASK, RIL_PARAM_PBE_GROUPID, RIL_PARAM_PBE_TEXT, ntddrilapitypes/RIL_PARAM_PBE_EMAILSIZE, RIL_PARAM_PBE_EMAILOFFSET, ntddrilapitypes/RIL_PARAM_PBE_ALL, RIL_PARAM_PBE_ADDITIONALNUMSIZE, RIL_PARAM_PBE_GROUPIDCOUNT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddrilapitypes.h
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
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : RILPHONEBOOKENTRYPARAMMASK
---

# RILPHONEBOOKENTRYPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPHONEBOOKENTRYPARAMMASK { 
  RIL_PARAM_PBE_ADDRESS,
  RIL_PARAM_PBE_TEXT,
  RIL_PARAM_PBE_SECONDNAME,
  RIL_PARAM_PBE_GROUPIDCOUNT,
  RIL_PARAM_PBE_GROUPID,
  RIL_PARAM_PBE_ADDITIONALNUMCOUNT,
  RIL_PARAM_PBE_ADDITIONALNUMSIZE,
  RIL_PARAM_PBE_ADDITIONALNUMOFFSET,
  RIL_PARAM_PBE_EMAILCOUNT,
  RIL_PARAM_PBE_EMAILSIZE,
  RIL_PARAM_PBE_EMAILOFFSET,
  RIL_PARAM_PBE_ALL
} RILPHONEBOOKENTRYPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_PBE_ADDITIONALNUMCOUNT</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBE_ADDITIONALNUMOFFSET</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBE_ADDITIONALNUMSIZE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBE_ADDRESS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBE_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBE_EMAILCOUNT</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBE_EMAILOFFSET</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBE_EMAILSIZE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBE_GROUPID</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBE_GROUPIDCOUNT</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBE_INDEX</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBE_SECONDNAME</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBE_TEXT</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |