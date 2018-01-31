---
UID : NF:dbgeng.IDebugControl3.GetPageSize
title : IDebugControl3::GetPageSize method
author : windows-driver-content
description : The GetPageSize method returns the page size for the effective processor mode.
old-location : debugger\getpagesize.htm
old-project : debugger
ms.assetid : 26f11dfb-3fc3-4804-a294-2dfc674b4a73
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : IDebugControl3, GetPageSize method [Windows Debugging], IDebugControl interface, GetPageSize method [Windows Debugging], IDebugControl2 interface, GetPageSize method [Windows Debugging], IDebugControl2 interface [Windows Debugging], GetPageSize method, dbgeng/IDebugControl::GetPageSize, IDebugControl::GetPageSize, IDebugControl2::GetPageSize, IDebugControl3 interface [Windows Debugging], GetPageSize method, GetPageSize, IDebugControl_b38e4c0a-5992-4afe-b684-2eb65b3a0271.xml, debugger.getpagesize, IDebugControl3::GetPageSize, IDebugControl interface [Windows Debugging], GetPageSize method, dbgeng/IDebugControl3::GetPageSize, GetPageSize method [Windows Debugging], IDebugControl3 interface, dbgeng/IDebugControl2::GetPageSize
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : dbgeng.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DOT4_ACTIVITY, *PDOT4_ACTIVITY
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
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>S_OK</b></dt>
</dl>
</td>
<td width="60%">
The method was successful.

</td>
</tr>
</table>


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