---
UID: NF.dbgeng.IDebugSymbols3.GetFunctionEntryByOffset
title: IDebugSymbols3::GetFunctionEntryByOffset method
author: windows-driver-content
description: The GetFunctionEntryByOffset method returns the function entry information for a function.
old-location: debugger\getfunctionentrybyoffset.htm
old-project: Debugger
ms.assetid: 6b1fa9fc-f033-4d93-a2ec-f31159d6a69d
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IDebugSymbols3, IDebugSymbols3::GetFunctionEntryByOffset, GetFunctionEntryByOffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
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
---

# IDebugSymbols3::GetFunctionEntryByOffset method



## -description
The <b>GetFunctionEntryByOffset</b> method returns the function entry information for a function.



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

### -param Offset [in]

Specifies a location in the current process's virtual address space of the function's implementation.  This is the value returned in the <i>Offset</i> parameter of <a href="debugger.getnextsymbolmatch">GetNextSymbolMatch</a> and <a href="debugger.getsymboloffset">IDebugSymbolGroup::GetSymbolOffset</a>, and the value of the <b>Offset</b> field in the <a href="debugger.debug_symbol_entry">DEBUG_SYMBOL_ENTRY</a> structure.


### -param Flags [in]

Specifies a bit-flag which alters the behavior of this method.  If the bit DEBUG_GETFNENT_RAW_ENTRY_ONLY is not set, the engine will provide artificial entries for well known cases.  If this bit is set the artificial entries are not used.


### -param Buffer [out, optional]

Receives the function entry information.  If the effective processor is an x86, this is the FPO_DATA structure for the function.  For all other architectures, this is the IMAGE_FUNCTION_ENTRY structure for that architecture.


### -param BufferSize [in]

Specifies the size of the buffer <i>Buffer</i>.


### -param BufferNeeded [out, optional]

Specifies the size of the function entry information.


## -returns
This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.
<dl>
<dt><b>S_FALSE</b></dt>
</dl>The method was successful, but the buffer was not large enough to hold the function entry information and so the information was truncated to fit.
<dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl>No function entry information was found for the location <i>Offset</i>.

 


## -remarks
The structures FPO_DATA and IMAGE_FUNCTION_ENTRY are documented in "Image Help Library" which is included in Debugging Tools For Windows in the DbgHelp.chm file. 

For more information about symbols, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>
</dt>
<dt>
<a href="debugger.getnextsymbolmatch">GetNextSymbolMatch</a>
</dt>
<dt>
<a href="debugger.getsymboloffset">IDebugSymbolGroup::GetSymbolOffset</a>
</dt>
<dt>
<a href="debugger.debug_symbol_entry">DEBUG_SYMBOL_ENTRY</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugSymbols3::GetFunctionEntryByOffset method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

