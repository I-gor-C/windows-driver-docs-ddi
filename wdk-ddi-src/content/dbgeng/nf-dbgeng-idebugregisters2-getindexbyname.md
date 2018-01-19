---
UID : NF:dbgeng.IDebugRegisters2.GetIndexByName
title : IDebugRegisters2::GetIndexByName method
author : windows-driver-content
description : The GetIndexByName method returns the index of the named register.
old-location : debugger\getindexbyname.htm
old-project : debugger
ms.assetid : a012b235-ed50-4009-a7ee-01783f9e3597
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugRegisters2, IDebugRegisters2::GetIndexByName, GetIndexByName
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : dbgeng.h
req.include-header : DbgEng.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IDebugRegisters.GetIndexByName,IDebugRegisters2.GetIndexByName
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


# GetIndexByName method
The <b>GetIndexByName</b> method returns the index of the named register.

## Syntax

````
HRESULT GetIndexByName(
  [in]  PCSTR  Name,
  [out] PULONG Index
);
````

## Parameters

`Name`

Specifies the name of the register whose index is requested.

`Index`

Receives the index of the register.


## Return Value

This list does not contain all the errors that might occur.  For a list of possible errors, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff549771">HRESULT Values</a>.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.
<dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl>The register was not found.

## Remarks

For an overview of the <a href="..\dbgeng\nn-dbgeng-idebugregisters.md">IDebugRegisters</a> interface and other register-related methods, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554369">Registers</a>.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include DbgEng.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |