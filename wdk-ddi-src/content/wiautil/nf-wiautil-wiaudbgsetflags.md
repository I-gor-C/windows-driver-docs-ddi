---
UID: NF.wiautil.wiauDbgSetFlags
title: wiauDbgSetFlags
author: windows-driver-content
description: The wiauDbgSetFlags function sets debugging flags.
old-location: image\wiaudbgsetflags.htm
old-project: image
ms.assetid: e3b944ef-daa5-412c-ac11-7b08d2b9333b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: wiauDbgSetFlags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiautil.h
req.include-header: Wiautil.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiauDbgSetFlags
req.alt-loc: wiautil.h
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
req.iface: 
req.product: Windows 10 or later.
---

# wiauDbgSetFlags function



## -description
<p>The <b>wiauDbgSetFlags</b> function sets debugging flags.</p>


## -syntax

````
inline DWORD __stdcall wiauDbgSetFlags(
   DWORD flags
);
````


## -parameters
<dl>

### -param <i>flags</i> 

<dd>
<p>Is a set of flags that control message logging. This parameter can be set to a combination of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WIAUDBG_BREAK_ON_ERRORS</p>
</td>
<td>
<p>Call <b>DebugBreak</b> (described in the Microsoft Windows SDK documentation) when an error occurs.</p>
</td>
</tr>
<tr>
<td>
<p>WIAUDBG_DONT_LOG</p>
</td>
<td>
<p>Do not log to either log file or debugger.</p>
</td>
</tr>
<tr>
<td>
<p>WIAUDBG_DONT_LOG_TO_DEBUGGER</p>
</td>
<td>
<p>Do not log to debugger.</p>
</td>
</tr>
<tr>
<td>
<p>WIAUDBG_DONT_LOG_TO_FILE</p>
</td>
<td>
<p>Do not log to log file.</p>
</td>
</tr>
<tr>
<td>
<p>WIAUDBG_DUMP</p>
</td>
<td>
<p>Log data.</p>
</td>
</tr>
<tr>
<td>
<p>WIAUDBG_ERRORS</p>
</td>
<td>
<p>Log error messages.</p>
</td>
</tr>
<tr>
<td>
<p>WIAUDBG_FNS</p>
</td>
<td>
<p>Log function entries and exits.</p>
</td>
</tr>
<tr>
<td>
<p>WIAUDBG_PRINT_INFO</p>
</td>
<td>
<p>Log thread, file, and line number.</p>
</td>
</tr>
<tr>
<td>
<p>WIAUDBG_PRINT_TIME</p>
</td>
<td>
<p>Log current time.</p>
</td>
</tr>
<tr>
<td>
<p>WIAUDBG_TRACES</p>
</td>
<td>
<p>Log trace messages.</p>
</td>
</tr>
<tr>
<td>
<p>WIAUDBG_WARNINGS</p>
</td>
<td>
<p>Log warning messages.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>The <b>wiauDbgSetFlags</b> function returns a value containing the flags that were in effect before the call to this function.</p>

## -remarks


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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiautil.h (include Wiautil.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549643">wiauDbgFlags</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiauDbgSetFlags function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
