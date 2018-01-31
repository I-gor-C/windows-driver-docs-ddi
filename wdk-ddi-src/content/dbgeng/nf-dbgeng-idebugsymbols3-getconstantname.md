---
UID : NF:dbgeng.IDebugSymbols3.GetConstantName
title : IDebugSymbols3::GetConstantName method
author : windows-driver-content
description : The GetConstantName method returns the name of the specified constant.
old-location : debugger\getconstantname.htm
old-project : debugger
ms.assetid : bb308ee7-e8bc-49c0-b1f9-199af7dca289
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : IDebugSymbols2 interface [Windows Debugging], GetConstantName method, IDebugSymbols2::GetConstantName, debugger.getconstantname, IDebugSymbols3::GetConstantName, dbgeng/IDebugSymbols2::GetConstantName, IDebugSymbols3 interface [Windows Debugging], GetConstantName method, dbgeng/IDebugSymbols3::GetConstantName, IDebugSymbols_438111b4-a0f4-40cc-aadc-8b1d2c67b219.xml, GetConstantName, GetConstantName method [Windows Debugging], IDebugSymbols2 interface, IDebugSymbols3, GetConstantName method [Windows Debugging], IDebugSymbols3 interface, GetConstantName method [Windows Debugging]
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


# GetConstantName method
The <b>GetConstantName</b>  method returns the name of the specified constant.

## Syntax

````
HRESULT GetConstantName(
  [in]            ULONG64 Module,
  [in]            ULONG   TypeId,
  [in]            ULONG64 Value,
  [out, optional] PSTR    NameBuffer,
  [in]            ULONG   NameBufferSize,
  [out, optional] PULONG  NameSize
);
````

## Parameters

`Module`

Specifies the base address of the module in which the constant was defined.

`TypeId`

Specifies the type ID of the constant.

`Value`

Specifies the value of the constant.

`NameBuffer`

Receives the constant's name.  If <i>NameBuffer</i> is <b>NULL</b>, this information is not returned.

`NameBufferSize`

Specifies the size in characters of the buffer <i>NameBuffer</i>.

`NameSize`

Receives the size in characters of the constant's name.


## Return Value

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
<tr>
<td width="40%">
<dl>
<dt><b>S_FALSE</b></dt>
</dl>
</td>
<td width="60%">
The method was successful. However, the buffer was not large enough for the constant's name and it was truncated.

</td>
</tr>
</table> 

This method can also return error values.  For more information, see <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a>.

## Remarks

For more information about symbols, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.

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