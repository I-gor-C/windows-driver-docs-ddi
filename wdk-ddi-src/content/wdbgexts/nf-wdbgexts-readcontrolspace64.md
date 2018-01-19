---
UID : NF:wdbgexts.ReadControlSpace64
title : ReadControlSpace64 function
author : windows-driver-content
description : The ReadControlSpace64 function reads the processor-specific control space into the array pointed to by buf.
old-location : debugger\readcontrolspace64.htm
old-project : debugger
ms.assetid : 4fa3d51a-d2f5-4b5f-abc0-515bf7211b87
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : ReadControlSpace64
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
req.alt-api : ReadControlSpace64
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


# ReadControlSpace64 function
The <b>ReadControlSpace64</b> function reads the processor-specific control space into the array pointed to by <i>buf</i>.

## Syntax

````
__inline VOID ReadControlSpace64(
   USHORT  processor,
   ULONG64 address,
   PVOID   buf,
   ULONG   size
);
````

## Parameters

`processor`

Specifies the number of the processor whose control space is to be read.

`address`

Specifies the address of the control space.

`buf`

Specifies the address of an array of bytes to hold the control space data.

`size`

Specifies the number of bytes in the array pointed to by <i>buf</i>.


## Return Value

None

This macro does not return a value.



The parameters provided to this macro are the same as those provided to the <b>ReadControlSpace64</b> function except that instead of providing a pointer to a structure and its size, the structure can be provided directly.

The <b>ReadTypedControlSpace64</b> macro is a thin wrapper around the <b>ReadControlSpace64</b> function.  It is provided as a convenience for reading processor-specific control space into a structure.
<dl>
<dd>
<i>_Proc</i>

Specifies the number of the processor whose control space is to be read.

</dd>
<dd>
<i>_Addr</i>

Specifies the address of the control space.

</dd>
<dd>
<i>_Buf</i>

Specifies the object into which the control space data is read.

</dd>
<dd>
<b>Return value</b>

This macro does not return a value.



</dd>
</dl><i>_Proc</i>

Specifies the number of the processor whose control space is to be read.

<i>_Addr</i>

Specifies the address of the control space.

<i>_Buf</i>

Specifies the object into which the control space data is read.

<b>Return value</b>

This macro does not return a value.



The parameters provided to this macro are the same as those provided to the <b>ReadControlSpace64</b> function except that instead of providing a pointer to a structure and its size, the structure can be provided directly.

This macro does not return a value.



The parameters provided to this macro are the same as those provided to the <b>ReadControlSpace64</b> function except that instead of providing a pointer to a structure and its size, the structure can be provided directly.

The <b>ReadTypedControlSpace64</b> macro is a thin wrapper around the <b>ReadControlSpace64</b> function.  It is provided as a convenience for reading processor-specific control space into a structure.
<dl>
<dd>
<i>_Proc</i>

Specifies the number of the processor whose control space is to be read.

</dd>
<dd>
<i>_Addr</i>

Specifies the address of the control space.

</dd>
<dd>
<i>_Buf</i>

Specifies the object into which the control space data is read.

</dd>
<dd>
<b>Return value</b>

This macro does not return a value.



</dd>
</dl><i>_Proc</i>

Specifies the number of the processor whose control space is to be read.

<i>_Addr</i>

Specifies the address of the control space.

<i>_Buf</i>

Specifies the object into which the control space data is read.

<b>Return value</b>

This macro does not return a value.



The parameters provided to this macro are the same as those provided to the <b>ReadControlSpace64</b> function except that instead of providing a pointer to a structure and its size, the structure can be provided directly.

## Remarks

If you are writing 32-bit code, you should use <a href="..\wdbgexts\ns-wdbgexts-_readcontrolspace.md">ReadControlSpace</a> instead. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537780">32-Bit Pointers and 64-Bit Pointers</a> for details.

If you are writing a WdbgExts extension, include <b>wdbgexts.h</b>. If you are writing a DbgEng extension that calls this function, include <b>wdbgexts.h</b> before <b>dbgeng.h</b> (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details).


The <b>ReadTypedControlSpace32</b> macro is a thin wrapper around the <b>ReadControlSpace64</b> function.  It is provided as a convenience for reading processor-specific control space into a structure.

<i>_Proc</i>

Specifies the number of the processor whose control space is to be read.

<i>_Addr</i>

Specifies the address of the control space.

<i>_Buf</i>

Specifies the object into which the control space data is read.

<b>Return value</b></p>

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