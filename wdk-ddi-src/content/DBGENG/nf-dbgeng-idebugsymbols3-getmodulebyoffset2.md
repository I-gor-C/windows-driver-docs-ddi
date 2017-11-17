---
UID: NF.dbgeng.IDebugSymbols3.GetModuleByOffset2
title: IDebugSymbols3::GetModuleByOffset2
author: windows-driver-content
description: The GetModuleByOffset2 method searches through the process's modules for one whose memory allocation includes the specified location.
old-location: debugger\getmodulebyoffset2.htm
ms.assetid: 2bb23245-9d5c-4b9d-8f4a-ce5fe552efc2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbols3.GetModuleByOffset2
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
ms.keywords: IDebugSymbols3, GetModuleByOffset2, IDebugSymbols3::GetModuleByOffset2
req.iface: IDebugSymbols3
---

# IDebugSymbols3::GetModuleByOffset2 method



## -description
<p>The <b>GetModuleByOffset2</b> method searches through the process's <a href="debugger.modules#modules#modules">modules</a> for one whose memory allocation includes the specified location.</p>


## -syntax

````
HRESULT GetModuleByOffset2(
  [in]            ULONG64  Offset,
  [in]            ULONG    StartIndex,
  [in]            ULONG    Flags,
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

### -param <i>Flags</i> [in]

<dd>
<p>Specifies a bit-set containing options used when searching for the module with the specified location.  <i>Flags</i> may contain the following bit-flags:</p>
<table>
<tr>
<th>Flag</th>
<th>Effect</th>
</tr>
<tr>
<td>
<p>DEBUG_GETMOD_NO_LOADED_MODULES</p>
</td>
<td>
<p>Do not search the loaded modules.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_GETMOD_NO_UNLOADED_MODULES</p>
</td>
<td>
<p>Do not search the unloaded modules.</p>
</td>
</tr>
</table>
<p> </p>
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
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>Starting at the specified index, this method returns the first module it finds whose memory allocation address range includes the specified location.  If the target has more than one module whose memory address range includes this location, then subsequent modules can be found by repeated calls to this method with higher values of <i>StartIndex</i>.</p>

<p>For more information about modules, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552231">Modules</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550870">IDebugSymbols3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547132">GetModuleByOffset</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547080">GetModuleByIndex</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetModuleByOffset2 method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
