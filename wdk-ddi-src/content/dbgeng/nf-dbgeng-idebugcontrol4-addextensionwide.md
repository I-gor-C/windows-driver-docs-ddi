---
UID: NF.dbgeng.IDebugControl4.AddExtensionWide
title: IDebugControl4::AddExtensionWide
author: windows-driver-content
description: The AddExtensionWide method loads an extension library into the debugger engine.
old-location: debugger\addextensionwide.htm
old-project: debugger
ms.assetid: 5c918f44-1ee7-4666-b83a-e13ce02e26db
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl4, AddExtensionWide, IDebugControl4::AddExtensionWide
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
req.alt-api: IDebugControl4.AddExtensionWide
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
req.iface: IDebugControl4
---

# IDebugControl4::AddExtensionWide method



## -description
<p>The <b>AddExtensionWide</b>  method loads an extension library into the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a>.</p>


## -syntax

````
HRESULT AddExtensionWide(
  [in]  PCSTR    Path,
  [in]  ULONG    Flags,
  [out] PULONG64 Handle
);
````


## -parameters
<dl>

### -param <i>Path</i> [in]

<dd>
<p>Specifies the fully qualified path and file name of the extension library to load.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Set to zero.</p>
</dd>

### -param <i>Handle</i> [out]

<dd>
<p>Receives the handle of the loaded extension library.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>If the extension library has already been loaded, the handle to already loaded library is returned.  The extension library is not loaded again.</p>

<p>The extension library is loaded into the host engine and <i>Path</i> contains a path and file name for this instance of the debugger engine.</p>

<p>For more information on using extension libraries, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539033">Calling Extensions and Extension Functions</a>.</p>

<p>If the extension library has already been loaded, the handle to already loaded library is returned.  The extension library is not loaded again.</p>

<p>The extension library is loaded into the host engine and <i>Path</i> contains a path and file name for this instance of the debugger engine.</p>

<p>For more information on using extension libraries, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539033">Calling Extensions and Extension Functions</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550526">IDebugControl4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554497">RemoveExtension</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546717">GetExtensionByPath</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl4::AddExtensionWide method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
