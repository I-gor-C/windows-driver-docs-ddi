---
UID : NF:wdbgexts.ReadMsr
title : ReadMsr function
author : windows-driver-content
description : The ReadMsr function reads the contents of a Model-Specific Register (MSR).
old-location : debugger\readmsr.htm
old-project : debugger
ms.assetid : 1cb51f88-a943-43e6-af18-0e9e301d8382
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : ReadMsr
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdbgexts.h
req.include-header : Wdbgexts.h, Dbgeng.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : ReadMsr
req.alt-loc : wdbgexts.h
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
req.typenames : EXT_TDOP
req.product : Windows 10 or later.
---


# ReadMsr function
The <b>ReadMsr</b> function reads the contents of a Model-Specific Register (MSR).

## Syntax

````
__inline VOID ReadMsr(
   ULONG     MsrReg,
   ULONGLONG *MsrValue
);
````

## Parameters

`MsrReg`

Specifies the ID number of the MSR.

`MsrValue`

Receives the value of the MSR.


## Return Value

None

## Remarks

If you are writing a WdbgExts extension, include <b>wdbgexts.h</b>. If you are writing a DbgEng extension that calls this function, include <b>wdbgexts.h</b> before <b>dbgeng.h</b> (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details).
</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdbgexts.h (include Wdbgexts.h, Dbgeng.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |