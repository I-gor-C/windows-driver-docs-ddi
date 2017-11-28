---
UID: NF.dbgeng.IDebugSymbols3.GetFunctionEntryByOffset
title: IDebugSymbols3::GetFunctionEntryByOffset
author: windows-driver-content
description: The GetFunctionEntryByOffset method returns the function entry information for a function.
old-location: debugger\getfunctionentrybyoffset.htm
old-project: debugger
ms.assetid: 6b1fa9fc-f033-4d93-a2ec-f31159d6a69d
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbols3, GetFunctionEntryByOffset, IDebugSymbols3::GetFunctionEntryByOffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h, Winnt.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbols3.GetFunctionEntryByOffset
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
req.iface: IDebugSymbols3
---

# IDebugSymbols3::GetFunctionEntryByOffset method



## -description
<p>The <b>GetFunctionEntryByOffset</b> method returns the function entry information for a function.</p>


## -syntax

````
HRESULT GetFunctionEntryByOffset(
  [in]            ULONG64 Offset,
  [in]            ULONG   Flags,
  [out, optional] PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  BufferNeeded
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies a location in the current process's virtual address space of the function's implementation.  This is the value returned in the <i>Offset</i> parameter of <a href="https://msdn.microsoft.com/library/windows/hardware/ff547856">GetNextSymbolMatch</a> and <a href="debugger.getsymboloffset">IDebugSymbolGroup::GetSymbolOffset</a>, and the value of the <b>Offset</b> field in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541662">DEBUG_SYMBOL_ENTRY</a> structure.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies a bit-flag which alters the behavior of this method.  If the bit DEBUG_GETFNENT_RAW_ENTRY_ONLY is not set, the engine will provide artificial entries for well known cases.  If this bit is set the artificial entries are not used.</p>
</dd>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>Receives the function entry information.  If the effective processor is an x86, this is the FPO_DATA structure for the function.  For all other architectures, this is the IMAGE_FUNCTION_ENTRY structure for that architecture.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size of the buffer <i>Buffer</i>.</p>
</dd>

### -param <i>BufferNeeded</i> [out, optional]

<dd>
<p>Specifies the size of the function entry information.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful, but the buffer was not large enough to hold the function entry information and so the information was truncated to fit.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>No function entry information was found for the location <i>Offset</i>.</p>

<p> </p>

## -remarks
<p>The structures FPO_DATA and IMAGE_FUNCTION_ENTRY are documented in "Image Help Library" which is included in Debugging Tools For Windows in the DbgHelp.chm file. </p>

<p>For more information about symbols, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.</p>

<p>The structures FPO_DATA and IMAGE_FUNCTION_ENTRY are documented in "Image Help Library" which is included in Debugging Tools For Windows in the DbgHelp.chm file. </p>

<p>For more information about symbols, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.</p>

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
<dt>Dbgeng.h (include Dbgeng.h or Winnt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550870">IDebugSymbols3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547856">GetNextSymbolMatch</a>
</dt>
<dt>
<a href="debugger.getsymboloffset">IDebugSymbolGroup::GetSymbolOffset</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541662">DEBUG_SYMBOL_ENTRY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetFunctionEntryByOffset method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
