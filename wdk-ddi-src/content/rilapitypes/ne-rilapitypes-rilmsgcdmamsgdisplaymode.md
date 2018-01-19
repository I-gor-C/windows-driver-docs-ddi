---
UID : NE:rilapitypes.RILMSGCDMAMSGDISPLAYMODE
title : RILMSGCDMAMSGDISPLAYMODE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgcdmamsgdisplaymode_2.htm
old-project : netvista
ms.assetid : 6ec37cf6-0d07-445b-9a5b-8d560069c612
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILMSGCDMAMSGDISPLAYMODE, RILMSGCDMAMSGDISPLAYMODE
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
req.alt-api : RILMSGCDMAMSGDISPLAYMODE
req.alt-loc : rilapitypes.h
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
req.typenames : RILMSGCDMAMSGDISPLAYMODE
req.product : Windows 10 or later.
---

# RILMSGCDMAMSGDISPLAYMODE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGCDMAMSGDISPLAYMODE { 
  RIL_MSGDISPLAYMODE_MOBILEDEFAULT,
  RIL_MSGDISPLAYMODE_USERDEFAULT,
  RIL_MSGDISPLAYMODE_MAX
} RILMSGCDMAMSGDISPLAYMODE;
````

## Constants

<table>

<tr>
<td>RIL_MSGDISPLAYMODE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGDISPLAYMODE_MOBILEDEFAULT</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGDISPLAYMODE_USERDEFAULT</td>
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