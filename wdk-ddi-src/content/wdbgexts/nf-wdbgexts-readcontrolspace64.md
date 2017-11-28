---
UID: NF.wdbgexts.ReadControlSpace64
title: ReadControlSpace64
author: windows-driver-content
description: The ReadControlSpace64 function reads the processor-specific control space into the array pointed to by buf.
old-location: debugger\readcontrolspace64.htm
old-project: debugger
ms.assetid: 4fa3d51a-d2f5-4b5f-abc0-515bf7211b87
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ReadControlSpace64
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ReadControlSpace64
req.alt-loc: wdbgexts.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# ReadControlSpace64 function



## -description
<p>The <b>ReadControlSpace64</b> function reads the processor-specific control space into the array pointed to by <i>buf</i>.</p>


## -syntax

````
__inline VOID ReadControlSpace64(
   USHORT  processor,
   ULONG64 address,
   PVOID   buf,
   ULONG   size
);
````


## -parameters
<dl>

### -param <i>processor</i> 

<dd>
<p>Specifies the number of the processor whose control space is to be read.</p>
</dd>

### -param <i>address</i> 

<dd>
<p>Specifies the address of the control space.</p>
</dd>

### -param <i>buf</i> 

<dd>
<p>Specifies the address of an array of bytes to hold the control space data.</p>
</dd>

### -param <i>size</i> 

<dd>
<p>Specifies the number of bytes in the array pointed to by <i>buf</i>.</p>
</dd>
</dl>

## -returns
<p>None</p>

<p>This macro does not return a value.

</p>

<p>The parameters provided to this macro are the same as those provided to the <b>ReadControlSpace64</b> function except that instead of providing a pointer to a structure and its size, the structure can be provided directly.</p>

<p>The <b>ReadTypedControlSpace64</b> macro is a thin wrapper around the <b>ReadControlSpace64</b> function.  It is provided as a convenience for reading processor-specific control space into a structure.</p><dl>
<dd>
<p><i>_Proc</i></p>
<p>Specifies the number of the processor whose control space is to be read.</p>
</dd>
<dd>
<p><i>_Addr</i></p>
<p>Specifies the address of the control space.</p>
</dd>
<dd>
<p><i>_Buf</i></p>
<p>Specifies the object into which the control space data is read.</p>
</dd>
<dd>
<p><b>Return value</b></p>
<p>This macro does not return a value.

</p>
</dd>
</dl><p><i>_Proc</i></p>

<p>Specifies the number of the processor whose control space is to be read.</p>

<p><i>_Addr</i></p>

<p>Specifies the address of the control space.</p>

<p><i>_Buf</i></p>

<p>Specifies the object into which the control space data is read.</p>

<p><b>Return value</b></p>

<p>This macro does not return a value.

</p>

<p>The parameters provided to this macro are the same as those provided to the <b>ReadControlSpace64</b> function except that instead of providing a pointer to a structure and its size, the structure can be provided directly.</p>

<p>This macro does not return a value.

</p>

<p>The parameters provided to this macro are the same as those provided to the <b>ReadControlSpace64</b> function except that instead of providing a pointer to a structure and its size, the structure can be provided directly.</p>

<p>The <b>ReadTypedControlSpace64</b> macro is a thin wrapper around the <b>ReadControlSpace64</b> function.  It is provided as a convenience for reading processor-specific control space into a structure.</p><dl>
<dd>
<p><i>_Proc</i></p>
<p>Specifies the number of the processor whose control space is to be read.</p>
</dd>
<dd>
<p><i>_Addr</i></p>
<p>Specifies the address of the control space.</p>
</dd>
<dd>
<p><i>_Buf</i></p>
<p>Specifies the object into which the control space data is read.</p>
</dd>
<dd>
<p><b>Return value</b></p>
<p>This macro does not return a value.

</p>
</dd>
</dl><p><i>_Proc</i></p>

<p>Specifies the number of the processor whose control space is to be read.</p>

<p><i>_Addr</i></p>

<p>Specifies the address of the control space.</p>

<p><i>_Buf</i></p>

<p>Specifies the object into which the control space data is read.</p>

<p><b>Return value</b></p>

<p>This macro does not return a value.

</p>

<p>The parameters provided to this macro are the same as those provided to the <b>ReadControlSpace64</b> function except that instead of providing a pointer to a structure and its size, the structure can be provided directly.</p>

## -remarks
<p>If you are writing 32-bit code, you should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff553527">ReadControlSpace</a> instead. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537780">32-Bit Pointers and 64-Bit Pointers</a> for details.</p>

<p>If you are writing a WdbgExts extension, include <b>wdbgexts.h</b>. If you are writing a DbgEng extension that calls this function, include <b>wdbgexts.h</b> before <b>dbgeng.h</b> (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details).
</p>

<p>The <b>ReadTypedControlSpace32</b> macro is a thin wrapper around the <b>ReadControlSpace64</b> function.  It is provided as a convenience for reading processor-specific control space into a structure.</p><dl>
<dd>
<p><i>_Proc</i></p>
<p>Specifies the number of the processor whose control space is to be read.</p>
</dd>
<dd>
<p><i>_Addr</i></p>
<p>Specifies the address of the control space.</p>
</dd>
<dd>
<p><i>_Buf</i></p>
<p>Specifies the object into which the control space data is read.</p>
</dd>
<dd>
<p><b>Return value</b></p>
<p>This macro does not return a value.

</p>
</dd>
</dl><p><i>_Proc</i></p>

<p>Specifies the number of the processor whose control space is to be read.</p>

<p><i>_Addr</i></p>

<p>Specifies the address of the control space.</p>

<p><i>_Buf</i></p>

<p>Specifies the object into which the control space data is read.</p>

<p><b>Return value</b></p>

<p>If you are writing 32-bit code, you should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff553527">ReadControlSpace</a> instead. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537780">32-Bit Pointers and 64-Bit Pointers</a> for details.</p>

<p>If you are writing a WdbgExts extension, include <b>wdbgexts.h</b>. If you are writing a DbgEng extension that calls this function, include <b>wdbgexts.h</b> before <b>dbgeng.h</b> (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details).
</p>

<p>The <b>ReadTypedControlSpace32</b> macro is a thin wrapper around the <b>ReadControlSpace64</b> function.  It is provided as a convenience for reading processor-specific control space into a structure.</p><dl>
<dd>
<p><i>_Proc</i></p>
<p>Specifies the number of the processor whose control space is to be read.</p>
</dd>
<dd>
<p><i>_Addr</i></p>
<p>Specifies the address of the control space.</p>
</dd>
<dd>
<p><i>_Buf</i></p>
<p>Specifies the object into which the control space data is read.</p>
</dd>
<dd>
<p><b>Return value</b></p>
<p>This macro does not return a value.

</p>
</dd>
</dl><p><i>_Proc</i></p>

<p>Specifies the number of the processor whose control space is to be read.</p>

<p><i>_Addr</i></p>

<p>Specifies the address of the control space.</p>

<p><i>_Buf</i></p>

<p>Specifies the object into which the control space data is read.</p>

<p><b>Return value</b></p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdbgexts.h (include Wdbgexts.h, Wdbgexts.h, or Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>