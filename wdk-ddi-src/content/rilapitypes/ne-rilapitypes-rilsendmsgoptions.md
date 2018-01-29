---
UID : NE:rilapitypes.RILSENDMSGOPTIONS
title : RILSENDMSGOPTIONS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsendmsgoptions_2.htm
old-project : netvista
ms.assetid : 84d13b43-06c4-4454-9853-80b1fe65d29d
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.rilsendmsgoptions_2, rilapitypes/RIL_SENDOPT_PERSISTLINK, rilapitypes/RILSENDMSGOPTIONS, RIL_SENDOPT_PERSISTLINK, rilapitypes/RIL_SENDOPT_IMS, RIL_SENDOPT_IMS, RILSENDMSGOPTIONS, RILSENDMSGOPTIONS enumeration [Network Drivers Starting with Windows Vista]
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
req.typenames : RILSENDMSGOPTIONS
req.product : Windows 10 or later.
---

# RILSENDMSGOPTIONS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSENDMSGOPTIONS { 
  RIL_SENDOPT_PERSISTLINK,
  RIL_SENDOPT_IMS
} RILSENDMSGOPTIONS;
````

## Constants

<table>

<tr>
<td>RIL_SENDOPT_IMS</td>
<td></td>
</tr>

<tr>
<td>RIL_SENDOPT_NONE</td>
<td></td>
</tr>

<tr>
<td>RIL_SENDOPT_PERSISTLINK</td>
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