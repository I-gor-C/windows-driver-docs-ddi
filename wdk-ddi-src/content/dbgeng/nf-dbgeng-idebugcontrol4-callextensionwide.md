---
UID: NF.dbgeng.IDebugControl4.CallExtensionWide
title: IDebugControl4::CallExtensionWide
author: windows-driver-content
description: The CallExtensionWide method calls a debugger extension.
old-location: debugger\callextensionwide.htm
old-project: debugger
ms.assetid: a46d7ba9-24fc-4e06-9655-3fc6531d6891
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl4, CallExtensionWide, IDebugControl4::CallExtensionWide
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
req.alt-api: IDebugControl4.CallExtensionWide
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
req.iface: IDebugControl4
---

# IDebugControl4::CallExtensionWide method



## -description
<p>The <b>CallExtensionWide</b> method calls a debugger extension.</p>


## -syntax

````
HRESULT CallExtensionWide(
  [in]           ULONG64 Handle,
  [in]           PCSTR   Function,
  [in, optional] PCSTR   Arguments
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>Specifies the handle of the extension library that contains the extension to call.  If <i>Handle</i> is zero, the engine will walk the extension library chain searching for the extension.</p>
</dd>

### -param <i>Function</i> [in]

<dd>
<p>Specifies the name of the extension to call.</p>
</dd>

### -param <i>Arguments</i> [in, optional]

<dd>
<p>Specifies the arguments to pass to the extension.  <i>Arguments</i> is a string that will be parsed by the extension, just like the extension will parse arguments passed to it when called as an extension command.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>If <i>Handle</i> is zero, the engine searches each extension library until it finds one that contains the extension; the extension will then be called.  If the extension returns DEBUG_EXTENSION_CONTINUE_SEARCH, the search will continue.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol4.md">IDebugControl4</a>
</dt>
<dt>
<a href="debugger.addextension">AddExtension</a>
</dt>
<dt>
<a href="debugger.getextensionbypath">GetExtensionByPath</a>
</dt>
<dt>
<a href="debugger.getextensionfunction">GetExtensionFunction</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl4::CallExtensionWide method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
