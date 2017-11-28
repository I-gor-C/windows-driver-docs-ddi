---
UID: NF.dbgeng.IDebugControl4.GetExtensionByPathWide
title: IDebugControl4::GetExtensionByPathWide
author: windows-driver-content
description: The GetExtensionByPathWide method returns the handle for an already loaded extension library.
old-location: debugger\getextensionbypathwide.htm
old-project: debugger
ms.assetid: 85257190-2b39-487d-ada6-4c8cd0b1450f
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl4, GetExtensionByPathWide, IDebugControl4::GetExtensionByPathWide
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
req.alt-api: IDebugControl4.GetExtensionByPathWide
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

# IDebugControl4::GetExtensionByPathWide method



## -description
<p>The <b>GetExtensionByPathWide</b>  method returns the handle for an already loaded extension library.</p>


## -syntax

````
HRESULT GetExtensionByPathWide(
  [in]  PCWSTR   Path,
  [out] PULONG64 Handle
);
````


## -parameters
<dl>

### -param <i>Path</i> [in]

<dd>
<p>Specifies the fully qualified path and file name of the extension library.</p>
</dd>

### -param <i>Handle</i> [out]

<dd>
<p>Receives the handle of the extension library.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>Extension libraries are loaded into the <a href="debugger.debugging_session_and_execution_model#host_engine#host_engine">host engine</a>, which is where this method looks for the requested extension library.  <i>Path</i> is a path and file name for the host engine.</p>

<p>For more information on using extension libraries, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539033">Calling Extensions and Extension Functions</a>.</p>

<p>Extension libraries are loaded into the <a href="debugger.debugging_session_and_execution_model#host_engine#host_engine">host engine</a>, which is where this method looks for the requested extension library.  <i>Path</i> is a path and file name for the host engine.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537892">AddExtension</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl4::GetExtensionByPathWide method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
