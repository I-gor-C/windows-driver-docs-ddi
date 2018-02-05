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
ms.keywords : POEMPTOPTS, prcomoem/OEMPTOPTS, prcomoem/OEMPT_NOSHAPSHOT, tagOEMPTOPTS, OEMPT_DEFAULT, prcomoem/OEMPT_DEFAULT, *POEMPTOPTS, prcomoem/POEMPTOPTS, POEMPTOPTS enumeration pointer [Print Devices], OEMPTOPTS, OEMPTOPTS enumeration [Print Devices], print.oemptopts, OEMPT_NOSHAPSHOT
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
| **Header** | prcomoem.h |