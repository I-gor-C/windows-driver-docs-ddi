---
UID : NE:ntddrilapitypes.RILSUBADDRESSTYPE
title : RILSUBADDRESSTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsubaddresstype.htm
old-project : netvista
ms.assetid : 18c4f26a-6463-4157-bd81-6bbb2100eff2
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddrilapitypes/RILSUBADDRESSTYPE, ntddrilapitypes/RIL_SUBADDRTYPE_MAX, netvista.rilsubaddresstype, ntddrilapitypes/RIL_SUBADDRTYPE_USER, RILSUBADDRESSTYPE, RIL_SUBADDRTYPE_USER, RILSUBADDRESSTYPE enumeration [Network Drivers Starting with Windows Vista], RIL_SUBADDRTYPE_MAX
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
req.typenames : RILSUBADDRESSTYPE
---

# RILSUBADDRESSTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSUBADDRESSTYPE { 
  RIL_SUBADDRTYPE_USER,
  RIL_SUBADDRTYPE_MAX
} RILSUBADDRESSTYPE;
````

## Constants

<table>

<tr>
<td>RIL_SUBADDRTYPE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_SUBADDRTYPE_NSAP</td>
<td></td>
</tr>

<tr>
<td>RIL_SUBADDRTYPE_USER</td>
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