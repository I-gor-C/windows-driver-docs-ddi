---
UID: NF.dbgeng.IDebugSymbols3.GetModuleByModuleName2
title: IDebugSymbols3::GetModuleByModuleName2
author: windows-driver-content
description: The GetModuleByModuleName2 method searches through the process's modules for one with the specified name.
old-location: debugger\getmodulebymodulename2.htm
old-project: debugger
ms.assetid: 25ebb316-e801-44fa-bb80-dffe9051db7e
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols3, GetModuleByModuleName2, IDebugSymbols3::GetModuleByModuleName2
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
req.alt-api: IDebugSymbols3.GetModuleByModuleName2
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

# IDebugSymbols3::GetModuleByModuleName2 method



## -description
<p>The <b>GetModuleByModuleName2</b>  method searches through the process's <a href="debugger.modules#modules#modules">modules</a> for one with the specified name.</p>


## -syntax

````
HRESULT GetModuleByModuleName2(
  [in]            PCSTR    Name,
  [in]            ULONG    StartIndex,
  [in]            ULONG    Flags,
  [out, optional] PULONG   Index,
  [out, optional] PULONG64 Base
);
````


## -parameters
<dl>

### -param <i>Name</i> [in]

<dd>
<p>Specifies the name of the desired module.</p>
</dd>

### -param <i>StartIndex</i> [in]

<dd>
<p>Specifies the index to start searching from.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies a bit-set containing options used when searching for the module with the specified name.  <i>Flags</i> may contain the following bit-flags:</p>
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
<p>Receives the index of the first module with the name <i>Name</i>.  If <i>Index</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>Base</i> [out, optional]

<dd>
<p>Receives the location in the target's memory address space of the base of the module.  If <i>Base</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>One of the arguments passed in was invalid.</p>

<p> </p>

## -remarks
<p>Starting at the specified index, these methods return the first module they find with the specified name.  If the target has more than one module with this name, then subsequent modules can be found by repeated calls to these methods with higher values of <i>StartIndex</i>.  </p>

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
<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>
</dt>
<dt>
<a href="debugger.getmodulebymodulename">GetModuleByModuleName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetModuleByModuleName2 method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
