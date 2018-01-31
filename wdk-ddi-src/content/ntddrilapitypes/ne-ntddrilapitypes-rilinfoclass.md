---
UID : NE:ntddrilapitypes.RILINFOCLASS
title : RILINFOCLASS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilinfoclass.htm
old-project : netvista
ms.assetid : 2e4bd8bd-ce7e-4eb4-ac0d-68fb8890eb26
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddrilapitypes/RIL_INFOCLASS_FAX, RIL_INFOCLASS_ALL, ntddrilapitypes/RILINFOCLASS, RIL_INFOCLASS_DATA, ntddrilapitypes/RIL_INFOCLASS_SMS, ntddrilapitypes/RIL_INFOCLASS_DATACIRCUITSYNC, netvista.rilinfoclass, RIL_INFOCLASS_PADACCESS, RILINFOCLASS enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_INFOCLASS_DATA, ntddrilapitypes/RIL_INFOCLASS_PADACCESS, RIL_INFOCLASS_SMS, RIL_INFOCLASS_DATACIRCUITSYNC, RIL_INFOCLASS_FAX, RILINFOCLASS, ntddrilapitypes/RIL_INFOCLASS_PACKETACCESS, ntddrilapitypes/RIL_INFOCLASS_ALL, ntddrilapitypes/RIL_INFOCLASS_DATACIRCUITASYNC, ntddrilapitypes/RIL_INFOCLASS_VOICE, RIL_INFOCLASS_VOICE, RIL_INFOCLASS_DATACIRCUITASYNC, RIL_INFOCLASS_PACKETACCESS
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
req.typenames : RILINFOCLASS
---

# RILINFOCLASS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILINFOCLASS { 
  RIL_INFOCLASS_VOICE,
  RIL_INFOCLASS_DATA,
  RIL_INFOCLASS_FAX,
  RIL_INFOCLASS_SMS,
  RIL_INFOCLASS_DATACIRCUITSYNC,
  RIL_INFOCLASS_DATACIRCUITASYNC,
  RIL_INFOCLASS_PACKETACCESS,
  RIL_INFOCLASS_PADACCESS,
  RIL_INFOCLASS_ALL
} RILINFOCLASS;
````

## Constants

<table>

<tr>
<td>RIL_INFOCLASS_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_DATA</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_DATACIRCUITASYNC</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_DATACIRCUITSYNC</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_FAX</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_NONE</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_PACKETACCESS</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_PADACCESS</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_SMS</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_VOICE</td>
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