---
UID : NE:rilapitypes.RILIMSNWENABLEDFLAGS
title : RILIMSNWENABLEDFLAGS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilimsnwenabledflags_2.htm
old-project : netvista
ms.assetid : 3295b0f0-a498-47fb-9744-06ea74626bb5
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RILIMSNWENABLEDFLAGS, rilapitypes/RIL_IMS_NW_ENABLED_FLAG_PROVISION, RILIMSNWENABLEDFLAGS enumeration [Network Drivers Starting with Windows Vista], RIL_IMS_NW_ENABLED_FLAG_EAB, RIL_IMS_NW_ENABLED_FLAG_ALL, rilapitypes/RIL_IMS_NW_ENABLED_FLAG_VOICE, rilapitypes/RIL_IMS_NW_ENABLED_FLAG_ALL, rilapitypes/RIL_IMS_NW_ENABLED_FLAG_VIDEO, RILIMSNWENABLEDFLAGS, RIL_IMS_NW_ENABLED_FLAG_PROVISION, rilapitypes/RIL_IMS_NW_ENABLED_FLAG_EAB, RIL_IMS_NW_ENABLED_FLAG_VOICE, RIL_IMS_NW_ENABLED_FLAG_VIDEO, netvista.rilimsnwenabledflags_2
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
req.typenames : RILIMSNWENABLEDFLAGS
req.product : Windows 10 or later.
---

# RILIMSNWENABLEDFLAGS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILIMSNWENABLEDFLAGS { 
  RIL_IMS_NW_ENABLED_FLAG_PROVISION,
  RIL_IMS_NW_ENABLED_FLAG_VOICE,
  RIL_IMS_NW_ENABLED_FLAG_VIDEO,
  RIL_IMS_NW_ENABLED_FLAG_EAB,
  RIL_IMS_NW_ENABLED_FLAG_ALL
} RILIMSNWENABLEDFLAGS;
````

## Constants

<table>

<tr>
<td>RIL_IMS_NW_ENABLED_FLAG_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_IMS_NW_ENABLED_FLAG_EAB</td>
<td></td>
</tr>

<tr>
<td>RIL_IMS_NW_ENABLED_FLAG_NONE</td>
<td></td>
</tr>

<tr>
<td>RIL_IMS_NW_ENABLED_FLAG_PROVISION</td>
<td></td>
</tr>

<tr>
<td>RIL_IMS_NW_ENABLED_FLAG_VIDEO</td>
<td></td>
</tr>

<tr>
<td>RIL_IMS_NW_ENABLED_FLAG_VOICE</td>
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