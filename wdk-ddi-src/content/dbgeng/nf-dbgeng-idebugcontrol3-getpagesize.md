---
UID : NF:dbgeng.IDebugControl3.GetPageSize
title : IDebugControl3::GetPageSize method
author : windows-driver-content
description : The GetPageSize method returns the page size for the effective processor mode.
old-location : debugger\getpagesize.htm
old-project : debugger
ms.assetid : 26f11dfb-3fc3-4804-a294-2dfc674b4a73
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugControl3, IDebugControl3::GetPageSize, GetPageSize
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : dbgeng.h
req.include-header : Dbgeng.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IDebugControl.GetPageSize,IDebugControl2.GetPageSize,IDebugControl3.GetPageSize
req.alt-loc : dbgeng.h
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
req.typenames : "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---


# GetPageSize method
The <b>GetPageSize</b> method returns the page size for the effective processor mode.

## Syntax

````
HRESULT GetPageSize(
  [out] PULONG Size
);
````

## Parameters

`Size`

Receives the page size.


## Return Value

This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |