---
UID : NE:wdfcompaniontarget._WDF_TASK_SEND_OPTIONS_FLAGS
title : _WDF_TASK_SEND_OPTIONS_FLAGS
author : windows-driver-content
description : For internal use only.
old-location : wdf\wdf_task_send_options_flags.htm
old-project : wdf
ms.assetid : 8ff13908-57f2-404f-a8ea-70c798ee3d7d
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _WDF_TASK_SEND_OPTIONS_FLAGS, wdfcompaniontarget/WDF_TASK_SEND_OPTION_TIMEOUT, wdfcompaniontarget/WDF_TASK_SEND_OPTIONS_FLAGS, WDF_TASK_SEND_OPTIONS_FLAGS enumeration, WDF_TASK_SEND_OPTION_TIMEOUT, wdf.wdf_task_send_options_flags, WDF_TASK_SEND_OPTIONS_FLAGS, wdfcompaniontarget/WDF_TASK_SEND_OPTION_SYNCHRONOUS, WDF_TASK_SEND_OPTION_SYNCHRONOUS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : wdfcompaniontarget.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 1.23
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
req.typenames : WDF_TASK_SEND_OPTIONS_FLAGS
req.product : Windows 10 or later.
---

# _WDF_TASK_SEND_OPTIONS_FLAGS Enumeration
For internal use only.

## Syntax
````
typedef enum _WDF_TASK_SEND_OPTIONS_FLAGS { 
  WDF_TASK_SEND_OPTION_TIMEOUT      = 1,
  WDF_TASK_SEND_OPTION_SYNCHRONOUS  = 2
} WDF_TASK_SEND_OPTIONS_FLAGS;
````

## Constants

<table>

<tr>
<td>WDF_TASK_SEND_OPTION_SYNCHRONOUS</td>
<td></td>
</tr>

<tr>
<td>WDF_TASK_SEND_OPTION_TIMEOUT</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** | 1.23 |
| **Minimum UMDF version** |  |
| **Header** | wdfcompaniontarget.h |