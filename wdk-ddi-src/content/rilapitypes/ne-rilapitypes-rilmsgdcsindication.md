---
UID : NE:rilapitypes.RILMSGDCSINDICATION
title : RILMSGDCSINDICATION
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgdcsindication_2.htm
old-project : netvista
ms.assetid : 292f54d6-0555-47d0-97b9-b76e9e08bf78
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILMSGDCSINDICATION enumeration [Network Drivers Starting with Windows Vista], RIL_DCSINDICATION_MAX, RIL_DCSINDICATION_FAX, RIL_DCSINDICATION_EMAIL, rilapitypes/RIL_DCSINDICATION_FAX, rilapitypes/RIL_DCSINDICATION_OTHER, RILMSGDCSINDICATION, RIL_DCSINDICATION_OTHER, rilapitypes/RIL_DCSINDICATION_MAX, netvista.rilmsgdcsindication_2, rilapitypes/RILMSGDCSINDICATION, rilapitypes/RIL_DCSINDICATION_EMAIL
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
req.typenames : RILMSGDCSINDICATION
req.product : Windows 10 or later.
---

# RILMSGDCSINDICATION Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGDCSINDICATION { 
  RIL_DCSINDICATION_FAX,
  RIL_DCSINDICATION_EMAIL,
  RIL_DCSINDICATION_OTHER,
  RIL_DCSINDICATION_MAX
} RILMSGDCSINDICATION;
````

## Constants

<table>

<tr>
<td>RIL_DCSINDICATION_EMAIL</td>
<td></td>
</tr>

<tr>
<td>RIL_DCSINDICATION_FAX</td>
<td></td>
</tr>

<tr>
<td>RIL_DCSINDICATION_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_DCSINDICATION_OTHER</td>
<td></td>
</tr>

<tr>
<td>RIL_DCSINDICATION_VOICEMAIL</td>
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