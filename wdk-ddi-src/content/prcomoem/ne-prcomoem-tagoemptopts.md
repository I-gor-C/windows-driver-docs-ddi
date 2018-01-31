---
UID : NE:prcomoem.tagOEMPTOPTS
title : tagOEMPTOPTS
author : windows-driver-content
description : "."
old-location : print\oemptopts.htm
old-project : print
ms.assetid : A63C115D-7215-422A-B4F9-C88820FC8168
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : prcomoem/OEMPTOPTS, OEMPT_DEFAULT, POEMPTOPTS enumeration pointer [Print Devices], prcomoem/OEMPT_DEFAULT, OEMPT_NOSHAPSHOT, prcomoem/OEMPT_NOSHAPSHOT, *POEMPTOPTS, OEMPTOPTS, tagOEMPTOPTS, print.oemptopts, prcomoem/POEMPTOPTS, POEMPTOPTS, OEMPTOPTS enumeration [Print Devices]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : prcomoem.h
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
req.typenames : OEMPTOPTS, *POEMPTOPTS
req.product : Windows 10 or later.
---

# tagOEMPTOPTS Enumeration


## Syntax
````
typedef enum tagOEMPTOPTS { 
  OEMPT_DEFAULT     = 0,
  OEMPT_NOSHAPSHOT  = 0x1
} OEMPTOPTS, *POEMPTOPTS;
````

## Constants

<table>

<tr>
<td>OEMPT_DEFAULT</td>
<td></td>
</tr>

<tr>
<td>OEMPT_NOSNAPSHOT</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | prcomoem.h |