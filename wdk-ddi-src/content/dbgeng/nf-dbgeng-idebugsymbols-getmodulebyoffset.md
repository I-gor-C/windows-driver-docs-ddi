---
UID: NF.dbgeng.IDebugSymbols.GetModuleByOffset
title: IDebugSymbols::GetModuleByOffset
author: windows-driver-content
description: The GetModuleByOffset method searches through the target's modules for one whose memory allocation includes the specified location.
old-location: debugger\getmodulebyoffset.htm
old-project: debugger
ms.assetid: ff51d0d1-47f1-4df6-b671-d74f791d778b
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols, GetModuleByOffset, IDebugSymbols::GetModuleByOffset
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
req.alt-api: IDebugSymbols.GetModuleByOffset,IDebugSymbols2.GetModuleByOffset,IDebugSymbols3.GetModuleByOffset
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
req.iface: IDebugSymbols
---

# IDebugSymbols::GetModuleByOffset method



## -description
<p>The <b>GetModuleByOffset</b> method searches through the target's <a href="debugger.modules#modules#modules">modules</a> for one whose memory allocation includes the specified location.</p>


## -syntax

````
HRESULT GetModuleByOffset(
  [in]            ULONG64  Offset,
  [in]            ULONG    StartIndex,
  [out, optional] PULONG   Index,
  [out, optional] PULONG64 Base
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies a location in the target's virtual address space which is inside the desired module's memory allocation -- for example, the address of a symbol belonging to the module.</p>
</dd>

### -param <i>StartIndex</i> [in]

<dd>
<p>Specifies the index to start searching from.</p>
</dd>

### -param <i>Index</i> [out, optional]

<dd>
<p>Receives the index of the module.  If <i>Index</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>Base</i> [out, optional]

<dd>
<p>Receives the location in the target's memory address space of the base of the module.  If <i>Base</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>Starting at the specified index, this method returns the first module it finds whose memory allocation address range includes the specified location.  If the target has more than one module whose memory address range includes this location, then subsequent modules can be found by repeated calls to this method with higher values of <i>StartIndex</i>.</p>

<p>For more information about modules, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552231">Modules</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugsymbols.md">IDebugSymbols</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols2.md">IDebugSymbols2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>
</dt>
<dt>
<a href="debugger.getmodulebyoffset2">GetModuleByOffset2</a>
</dt>
<dt>
<a href="debugger.getmodulebyindex">GetModuleByIndex</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols::GetModuleByOffset method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
