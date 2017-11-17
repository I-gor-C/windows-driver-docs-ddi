---
UID: NF.dbgeng.IDebugSymbols3.RemoveSyntheticModule
title: IDebugSymbols3::RemoveSyntheticModule
author: windows-driver-content
description: The RemoveSyntheticModule method removes a synthetic module from the module list the debugger maintains for the current process.
old-location: debugger\removesyntheticmodule.htm
ms.assetid: 951b42b6-4d6a-45af-a27f-6e8056676bb0
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
req.alt-api: IDebugSymbols3.RemoveSyntheticModule
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
ms.keywords: IDebugSymbols3, RemoveSyntheticModule, IDebugSymbols3::RemoveSyntheticModule
req.iface: IDebugSymbols3
---

# IDebugSymbols3::RemoveSyntheticModule method



## -description
<p>The <b>RemoveSyntheticModule</b> method removes a synthetic module from the module list the debugger maintains for the current process.</p>


## -syntax

````
HRESULT RemoveSyntheticModule(
  [in] ULONG64 Base
);
````


## -parameters
<dl>

### -param <i>Base</i> [in]

<dd>
<p>Specifies the location in the process's virtual address space of the base of the synthetic module.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>No synthetic module was found at the specified location.  This is returned if a synthetic module at this location was previously removed or discarded.</p>

<p> </p>

<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p>

## -remarks
<p>If all the modules are reloaded - for example, by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff554379">Reload</a> with the  <i>Module</i> parameter set to the empty string - all synthetic modules will be discarded.</p>

<p>For more information about synthetic modules, see Synthetic Modules.</p>

<p>If all the modules are reloaded - for example, by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff554379">Reload</a> with the  <i>Module</i> parameter set to the empty string - all synthetic modules will be discarded.</p>

<p>For more information about synthetic modules, see Synthetic Modules.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537937">AddSyntheticModule</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554542">RemoveSyntheticSymbol</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::RemoveSyntheticModule method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
