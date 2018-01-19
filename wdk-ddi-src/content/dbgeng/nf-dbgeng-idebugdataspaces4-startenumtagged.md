---
UID : NF:dbgeng.IDebugDataSpaces4.StartEnumTagged
title : IDebugDataSpaces4::StartEnumTagged method
author : windows-driver-content
description : The StartEnumTagged method initializes a enumeration over the tagged data associated with a debugger session.
old-location : debugger\startenumtagged.htm
old-project : debugger
ms.assetid : b79b1f09-baff-4071-a209-6fc399c9aef9
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugDataSpaces4, IDebugDataSpaces4::StartEnumTagged, StartEnumTagged
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
req.alt-api : IDebugDataSpaces3.StartEnumTagged,IDebugDataSpaces4.StartEnumTagged
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


# StartEnumTagged method
The <b>StartEnumTagged</b> method initializes a enumeration over the tagged data associated with a debugger session.

## Syntax

````
HRESULT StartEnumTagged(
  [out] PULONG64 Handle
);
````

## Parameters

`Handle`

Receives the handle identifying the enumeration.  This handle can be passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547874">GetNextTagged</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff542978">EndEnumTagged</a>.


## Return Value

This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.

## Remarks

The resources held by an enumeration created with this method can be released using <a href="https://msdn.microsoft.com/library/windows/hardware/ff542978">EndEnumTagged</a>.</p>

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