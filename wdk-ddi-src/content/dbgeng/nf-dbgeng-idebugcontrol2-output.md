---
UID: NF.dbgeng.IDebugControl2.Output
title: IDebugControl2::Output
author: windows-driver-content
description: The Output method formats a string and send the result to output callbacks that have been registered with the engine's clients.
old-location: debugger\output.htm
old-project: debugger
ms.assetid: 2c748325-3718-4fcc-98a3-3318d361ba6e
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl2, Output, IDebugControl2::Output
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl.Output,IDebugControl2.Output,IDebugControl3.Output
req.alt-loc: dbgeng.h
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
req.iface: IDebugControl2
---

# IDebugControl2::Output method



## -description
<p>The <b>Output</b>  method formats a string and send the result to output callbacks that have been registered with the engine's clients.</p>


## -syntax

````
HRESULT Output(
  [in] ULONG Mask,
  [in] PCSTR Format,
             ...
);
````


## -parameters
<dl>

### -param <i>Mask</i> [in]

<dd>
<p>Specifies the output-type bit field.  See <a href="debugger.debug_output_xxx">DEBUG_OUTPUT_XXX</a> for possible values.</p>
</dd>

### -param <i>Format</i> [in]

<dd>
<p>Specifies the format string, as in <b>printf</b>.  In general, conversion characters work exactly as in C. For the floating-point conversion characters the 64-bit argument is interpreted as a 32-bit floating-point number unless the <b>l</b>  modifier is used.</p>
<p>The <b>%p</b> conversion character is supported, but it represents a pointer in a target's address space.  It cannot have any modifiers and it uses the debugger's internal address formatting.  The following additional conversion characters are supported.</p>
<table>
<tr>
<th>Character</th>
<th>Argument type</th>
<th>Argument</th>
<th>Text printed</th>
</tr>
<tr>
<td>
<p><b>%p</b></p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Pointer in an address space</p>
</td>
<td>
<p>The value of the pointer. </p>
</td>
</tr>
<tr>
<td>
<p><b>%N</b></p>
</td>
<td>
<p>DWORD_PTR (32 or 64 bits, depending on the host's architecture) </p>
</td>
<td>
<p>Pointer in the host's virtual address space</p>
</td>
<td>
<p>The value of the pointer.  (This is equivalent to the standard C <b>%p</b> character.) </p>
</td>
</tr>
<tr>
<td>
<p><b>%I</b></p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Any 64-bit value</p>
</td>
<td>
<p>The specified value.  If this is greater than 0xFFFFFFFF, it is printed as a 64-bit value. Otherwise, it is printed as a 32-bit value.</p>
</td>
</tr>
<tr>
<td>
<p><b>%ma</b></p>
</td>
<td>
<p>ULONG64 </p>
</td>
<td>
<p>Address of a NULL-terminated ASCII string in the process's virtual address space</p>
</td>
<td>
<p>The specified string.</p>
</td>
</tr>
<tr>
<td>
<p><b>%mu</b></p>
</td>
<td>
<p>ULONG64 </p>
</td>
<td>
<p>Address of a NULL-terminated Unicode string in the process's virtual address space</p>
</td>
<td>
<p>The specified string.</p>
</td>
</tr>
<tr>
<td>
<p><b>%msa</b></p>
</td>
<td>
<p>ULONG64 </p>
</td>
<td>
<p>Address of an ANSI_STRING structure in the process's virtual address space</p>
</td>
<td>
<p>The specified string.</p>
</td>
</tr>
<tr>
<td>
<p><b>%msu</b></p>
</td>
<td>
<p>ULONG64 </p>
</td>
<td>
<p>Address of a UNICODE_STRING structure in the process's virtual address space</p>
</td>
<td>
<p>The specified string.</p>
</td>
</tr>
<tr>
<td>
<p><b>%y</b></p>
</td>
<td>
<p>ULONG64 </p>
</td>
<td>
<p>Address in the process's virtual address space of an item with symbol information</p>
</td>
<td>
<p>String that contains the name of the specified symbol (and displacement, if any). </p>
</td>
</tr>
<tr>
<td>
<p><b>%ly</b></p>
</td>
<td>
<p>ULONG64 </p>
</td>
<td>
<p>Address in the process's virtual address space of an item with symbol information</p>
</td>
<td>
<p>String that contains the name of the specified symbol (and displacement, if any), as well as any available source line information. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>...</i> 

<dd>
<p>Specifies additional parameters that contain values to be inserted into the output during formatting.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>When generating very large output strings, it is possible to reach the limits of the debugger engine or of the operating system.  For example, some versions of the debugger engine have a 16K character limit for a single output.  If you find that very large output is getting truncated, you might need to split your output into multiple requests.</p>

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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol2.md">IDebugControl2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="debugger.dprintf">dprintf</a>
</dt>
<dt>
<a href="debugger.controlledoutput">ControlledOutput</a>
</dt>
<dt>
<a href="debugger.outputvalist">OutputVaList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564716">.printf</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::Output method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
