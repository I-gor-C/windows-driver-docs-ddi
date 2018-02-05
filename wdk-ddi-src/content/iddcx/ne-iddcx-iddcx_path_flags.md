---
UID : NE:iddcx.IDDCX_PATH_FLAGS
title : IDDCX_PATH_FLAGS
author : windows-driver-content
description : Indicates the state of the path.
old-location : display\iddcx_path_flags.htm
old-project : display
ms.assetid : f7a9b20a-753c-487d-a2d5-3e1c08317519
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : iddcx/IDDCX_PATH_FLAGS_ACTIVE, IDDCX_PATH_FLAGS_ACTIVE, IDDCX_PATH_FLAGS enumeration [Display Devices], iddcx/IDDCX_PATH_FLAGS, IDDCX_PATH_FLAGS_NONE, IDDCX_PATH_FLAGS, display.iddcx_path_flags, iddcx/IDDCX_PATH_FLAGS_NONE, iddcx/IDDCX_PATH_FLAGS_CHANGED, IDDCX_PATH_FLAGS_CHANGED
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : iddcx.h
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
req.irql : "_requires_same_"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : 
---

# IDDCX_PATH_FLAGS Enumeration
Indicates the state of the path.

## Syntax
````
typedef enum _IDDCX_PATH_FLAGS { 
  IDDCX_PATH_FLAGS_NONE     = 0,
  IDDCX_PATH_FLAGS_CHANGED  = 1,
  IDDCX_PATH_FLAGS_ACTIVE   = 2
} IDDCX_PATH_FLAGS;
````

## Constants

<table>

<tr>
<td>IDDCX_PATH_FLAGS_ACTIVE</td>
<td>Indicates if this path is active</td>
</tr>

<tr>
<td>IDDCX_PATH_FLAGS_CHANGED</td>
<td>Indicates if this path has changed</td>
</tr>

<tr>
<td>IDDCX_PATH_FLAGS_NONE</td>
<td>Indicates that the path is not active and has not changed.</td>
</tr>

<tr>
<td>UINT</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | iddcx.h |