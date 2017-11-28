---
UID: NF.dbgeng.IDebugControl3.ControlledOutput
title: IDebugControl3::ControlledOutput
author: windows-driver-content
description: The ControlledOutput method formats a string and sends the result to output callbacks that were registered with some of the engine's clients.
old-location: debugger\controlledoutput.htm
old-project: debugger
ms.assetid: d1a4aba3-9567-4d8e-980c-f6a85f54870e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl3, ControlledOutput, IDebugControl3::ControlledOutput
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
req.alt-api: IDebugControl.ControlledOutput,IDebugControl2.ControlledOutput,IDebugControl3.ControlledOutput
req.alt-loc: Dbgeng.h
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
req.iface: IDebugControl3
---

# IDebugControl3::ControlledOutput method



## -description
<p>The <b>ControlledOutput</b>  method formats a string and sends the result to <a href="debugger.using_input_and_output#output_callbacks#output_callbacks">output callbacks</a> that were registered with some of the engine's clients.</p>


## -syntax

````
HRESULT ControlledOutput(
  [in] ULONG OutputControl,
  [in] ULONG Mask,
  [in] PCSTR Format,
             ...
);
````


## -parameters
<dl>

### -param <i>OutputControl</i> [in]

<dd>
<p>Specifies an output control that determines which of the clients' output callbacks will receive the output.  For possible values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541517">DEBUG_OUTCTL_XXX</a>.  For more information about output, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550971">Input and Output</a>.</p>
</dd>

### -param <i>Mask</i> [in]

<dd>
<p>Specifies the output-type bit field.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff541518">DEBUG_OUTPUT_XXX</a> for possible values.</p>
</dd>

### -param <i>Format</i> [in]

<dd>
<p>Specifies the format string, as in <b>printf</b>.  Typically, conversion characters work exactly as they do in C. For the floating-point conversion characters, the 64-bit argument is interpreted as a 32-bit floating-point number unless the <b>l</b>  modifier is used.</p>
<p>The <b>%p</b> conversion character is supported, but it represents a pointer in a target's address space.  It might not have any modifiers and it uses the debugger's internal address formatting.  The following additional conversion characters are supported.</p>
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
<p>Pointer in an address space.</p>
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
<p>Pointer in the host's virtual address space.</p>
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
<p>Any 64-bit value.</p>
</td>
<td>
<p>The specified value.  If this is greater than 0xFFFFFFFF, it is printed as a 64-bit value; otherwise, it is printed as a 32-bit value.</p>
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
<p>Address of a NULL-terminated ASCII string in the process's virtual address space.</p>
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
<p>Address of a NULL-terminated Unicode string in the process's virtual address space.</p>
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
<p>Address of an ANSI_STRING structure in the process's virtual address space.</p>
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
<p>Address of a UNICODE_STRING structure in the process's virtual address space.</p>
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
<p>Address in the process's virtual address space of an item with symbol information.</p>
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
<p>Address in the process's virtual address space of an item with symbol information.</p>
</td>
<td>
<p>String that contains the name of the specified symbol (and displacement, if any), as well as any available source line information. </p>
</td>
</tr>
</table>
<p> </p>
<p>The %Y format specifier can be used to support the Debugger Markup Language (DML). For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/mt613235">Customizing Debugger Output Using DML</a>.</p>
<p>The following table summarizes the use of the %Y format specifier.</p>
<table>
<tr>
<td>Character</td>
<td>Argument type</td>
<td>Argument</td>
<td>Text printed</td>
</tr>
<tr>
<td>
<p><b>%Y{t}</b></p>
</td>
<td>
<p>String</p>
</td>
<td>Text</td>
<td>	  Quoted string.  Will convert text to DML if the output format (first arg) is DML.</td>
</tr>
<tr>
<td>
<p><b>%Y{T}</b></p>
</td>
<td>
<p>String</p>
</td>
<td>Text</td>
<td>Quoted string.  Will always convert text to DML regardless of the output format.</td>
</tr>
<tr>
<td>
<p><b>%Y{s}</b></p>
</td>
<td>
<p> String</p>
</td>
<td>Text</td>
<td>  Unquoted string. Will convert text to DML if the output format (first arg) is DML.</td>
</tr>
<tr>
<td>
<p><b>%Y{S}</b></p>
</td>
<td>
<p>String</p>
</td>
<td>Text</td>
<td>	  Unquoted string. Will always convert text to DML regardless of the output format.</td>
</tr>
<tr>
<td>
<p><b>%Y{as}</b></p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>Debugger formatted pointer</td>
<td>Adds either an empty string or 9 characters of spacing for padding the high 32-bit portion of debugger formatted pointer fields. The extra space outputs 9 spaces which includes the upper 8 zeros plus the ` character.</td>
</tr>
<tr>
<td>
<p><b>%Y{ps}</b></p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>Debugger formatted pointer</td>
<td>	Adds either an empty string or 8 characters of spacing for padding the high 32-bit portion of debugger formatted pointer fields. </td>
</tr>
<tr>
<td>
<p><b>%Y{l}</b></p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>Debugger formatted pointer</td>
<td>	Address as source line information.</td>
</tr>
</table>
<p> </p>
<p>This code snippet illustrates the use of the  %Y format specifier.</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>HRESULT CALLBACK testout(_In_ PDEBUG_CLIENT pClient, _In_ PCWSTR /*pwszArgs*/)
{
    HRESULT hr = S_OK;

    ComPtr&lt;IDebugControl4&gt; spControl;
    IfFailedReturn(pClient-&gt;QueryInterface(IID_PPV_ARGS(&amp;spControl)));

    spControl-&gt;ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{t}: %Y{t}\n", L"Hello &lt;World&gt;");
    spControl-&gt;ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{T}: %Y{T}\n", L"Hello &lt;World&gt;");
    spControl-&gt;ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{s}: %Y{s}\n", L"Hello &lt;World&gt;");
    spControl-&gt;ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{S}: %Y{S}\n", L"Hello &lt;World&gt;");

    spControl-&gt;ControlledOutputWide(0, DEBUG_OUTPUT_NORMAL, L"TEXT/NORMAL Y{t}: %Y{t}\n", L"Hello &lt;World&gt;");
    spControl-&gt;ControlledOutputWide(0, DEBUG_OUTPUT_NORMAL, L"TEXT/NORMAL Y{T}: %Y{T}\n", L"Hello &lt;World&gt;");
    spControl-&gt;ControlledOutputWide(0, DEBUG_OUTPUT_NORMAL, L"TEXT/NORMAL Y{s}: %Y{s}\n", L"Hello &lt;World&gt;");
    spControl-&gt;ControlledOutputWide(0, DEBUG_OUTPUT_NORMAL, L"TEXT/NORMAL Y{S}: %Y{S}\n", L"Hello &lt;World&gt;");

    spControl-&gt;ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{a}: %Y{a}\n", (ULONG64)0x00007ffa7da163c0);
    spControl-&gt;ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{as} 64bit   : '%Y{as}'\n", (ULONG64)0x00007ffa7da163c0);
    spControl-&gt;ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{as} 32value : '%Y{as}'\n", (ULONG64)0x1);

    spControl-&gt;ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{ps} 64bit   : '%Y{ps}'\n", (ULONG64)0x00007ffa7da163c0);
    spControl-&gt;ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{ps} 32value : '%Y{ps}'\n", (ULONG64)0x1);

    spControl-&gt;ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{l}: %Y{l}\n", (ULONG64)0x00007ffa7da163c0);

    return hr;

}
</pre>
</td>
</tr>
</table></span></div>
<p>This sample code would generate the following output.</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>0:004&gt; !testout
DML/NORMAL Y{t}: "Hello &lt;World&gt;"
DML/NORMAL Y{T}: "Hello &lt;World&gt;"
DML/NORMAL Y{s}: Hello &lt;World&gt;
DML/NORMAL Y{S}: Hello &lt;World&gt;
TEXT/NORMAL Y{t}: "Hello &lt;World&gt;"
TEXT/NORMAL Y{T}: &amp;quot;Hello &amp;lt;World&amp;gt;&amp;quot;
TEXT/NORMAL Y{s}: Hello &lt;World&gt;
TEXT/NORMAL Y{S}: Hello &amp;lt;World&amp;gt;
DML/NORMAL Y{a}: 00007ffa`7da163c0
DML/NORMAL Y{as} 64bit   : '         '
DML/NORMAL Y{as} 32value : '         '
DML/NORMAL Y{ps} 64bit   : '        '
DML/NORMAL Y{ps} 32value : '        '
DML/NORMAL Y{l}: [d:\th\minkernel\kernelbase\debug.c @ 443]
</pre>
</td>
</tr>
</table></span></div>
<p></p>
</dd>

### -param <i>...</i> 

<dd>
<p>Specifies additional parameters that represent values to be inserted into the output during formatting.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>When generating very large output strings, it is possible to reach the limits of the debugger engine or of the operating system.  For example, some versions of the debugger engine have a 16K character limit for a single output.  If you find that very large output is getting truncated, you might need to split your output into multiple requests.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550508">IDebugControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539252">ControlledOutputVaList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542750">dprintf</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553183">Output</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564716">.printf</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::ControlledOutput method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
