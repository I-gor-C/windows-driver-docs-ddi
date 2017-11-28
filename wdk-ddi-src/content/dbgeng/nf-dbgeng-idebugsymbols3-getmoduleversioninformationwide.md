---
UID: NF.dbgeng.IDebugSymbols3.GetModuleVersionInformationWide
title: IDebugSymbols3::GetModuleVersionInformationWide
author: windows-driver-content
description: The GetModuleVersionInformationWide method returns version information for the specified module.
old-location: debugger\getmoduleversioninformationwide.htm
old-project: debugger
ms.assetid: 60bb493c-81a2-45d7-8c2c-939afeda8a14
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbols3, GetModuleVersionInformationWide, IDebugSymbols3::GetModuleVersionInformationWide
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
req.alt-api: IDebugSymbols3.GetModuleVersionInformationWide
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

# IDebugSymbols3::GetModuleVersionInformationWide method



## -description
<p>The <b>GetModuleVersionInformationWide</b>  method returns version information for the specified module.</p>


## -syntax

````
HRESULT GetModuleVersionInformationWide(
  [in]            ULONG   Index,
  [in]            ULONG64 Base,
  [in]            PCWSTR  Item,
  [out, optional] PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  VerInfoSize
);
````


## -parameters
<dl>

### -param <i>Index</i> [in]

<dd>
<p>Specifies the index of the module.  If it is set to DEBUG_ANY_ID, the <i>Base</i> parameter is used to specify the location of the module instead.</p>
</dd>

### -param <i>Base</i> [in]

<dd>
<p>If <i>Index</i> is DEBUG_ANY_ID, specifies the location in the target's memory address space of the base of the module.  Otherwise it is ignored.</p>
</dd>

### -param <i>Item</i> [in]

<dd>
<p>Specifies the version information being requested.  This string corresponds to the <i>lpSubBlock</i> parameter of the function <b>VerQueryValue</b>.  For details on the <b>VerQueryValue</b> function, see the Platform SDK.</p>
</dd>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>Receives the requested version information.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in characters of the buffer <i>Buffer</i>.</p>
</dd>

### -param <i>VerInfoSize</i> [out, optional]

<dd>
<p>Receives the size in characters of the version information.  If <i>VerInfoSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The size of the buffer was smaller than the size of the version information.  In this case the buffer is filled with the truncated version information.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>The specified module was not found.</p>

<p> </p>

## -remarks
<p>Module version information is available only for loaded modules and may not be available in all sessions.</p>

<p>For more information about modules, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552231">Modules</a>.</p>

<p>Module version information is available only for loaded modules and may not be available in all sessions.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547138">GetModuleByOffset2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547080">GetModuleByIndex</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547927">GetNumberModules</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetModuleVersionInformationWide method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
