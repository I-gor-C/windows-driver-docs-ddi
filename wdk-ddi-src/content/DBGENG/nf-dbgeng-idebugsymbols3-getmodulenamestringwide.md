---
UID: NF.dbgeng.IDebugSymbols3.GetModuleNameStringWide
title: IDebugSymbols3::GetModuleNameStringWide
author: windows-driver-content
description: The GetModuleNameStringWide method returns the name of the specified module.
old-location: debugger\getmodulenamestringwide.htm
ms.assetid: e1b756b9-394a-4ec4-845e-867460998086
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
req.alt-api: IDebugSymbols3.GetModuleNameStringWide
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
ms.keywords: IDebugSymbols3, GetModuleNameStringWide, IDebugSymbols3::GetModuleNameStringWide
req.iface: IDebugSymbols3
---

# IDebugSymbols3::GetModuleNameStringWide method



## -description
<p>The <b>GetModuleNameStringWide</b>  method returns the name of the specified module.</p>


## -syntax

````
HRESULT GetModuleNameStringWide(
  [in]            ULONG   Which,
  [in]            ULONG   Index,
  [in]            ULONG64 Base,
  [out, optional] PWSTR   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  NameSize
);
````


## -parameters
<dl>

### -param <i>Which</i> [in]

<dd>
<p>Specifies which of the module's names to return, possible values are:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_MODNAME_IMAGE</p>
</td>
<td>
<p>The image name.  This is the name of the executable file, including the extension. Typically, the full path is included in user mode but not in kernel mode.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_MODNAME_MODULE</p>
</td>
<td>
<p>The module name. This is usually just the file name without the extension. In a few cases, the module name differs significantly from the file name.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_MODNAME_LOADED_IMAGE</p>
</td>
<td>
<p>The loaded image name.  Unless Microsoft CodeView symbols are present, this is the same as the image name.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_MODNAME_SYMBOL_FILE</p>
</td>
<td>
<p>The symbol file name.  The path and name of the symbol file. If no symbols have been loaded, this is the name of the executable file instead.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_MODNAME_MAPPED_IMAGE</p>
</td>
<td>
<p>The mapped image name.  In most cases, this is <b>NULL</b>. If the debugger is mapping an image file (for example, during minidump debugging), this is the name of the mapped image.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Index</i> [in]

<dd>
<p>Specifies the index of the module.  If it is set to DEBUG_ANY_ID, the <i>Base</i> parameter is used to specify the location of the module instead.</p>
</dd>

### -param <i>Base</i> [in]

<dd>
<p>If <i>Index</i> is DEBUG_ANY_ID, specifies the location in the target's memory address space of the base of the module.  Otherwise it is ignored.</p>
</dd>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>Receives the name of the module.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in characters of the buffer <i>Buffer</i>.</p>
</dd>

### -param <i>NameSize</i> [out, optional]

<dd>
<p>Receives the size in characters of the module's name.  If <i>NameSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful. However, the size of the buffer was smaller than the size of the module's name so it was truncated to fit in the buffer.</p>

<p> </p>

## -remarks
<p>For more information about modules, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552231">Modules</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547146">GetModuleNames</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetModuleNameStringWide method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
