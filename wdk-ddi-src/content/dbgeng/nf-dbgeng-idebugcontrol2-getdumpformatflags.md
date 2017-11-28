---
UID: NF.dbgeng.IDebugControl2.GetDumpFormatFlags
title: IDebugControl2::GetDumpFormatFlags
author: windows-driver-content
description: The GetDumpFormatFlags method returns the flags that describe what information is available in a dump file target.
old-location: debugger\getdumpformatflags.htm
old-project: debugger
ms.assetid: 86070c36-6702-42c8-b4fe-b3ef15ba418f
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl2, GetDumpFormatFlags, IDebugControl2::GetDumpFormatFlags
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
req.alt-api: IDebugControl2.GetDumpFormatFlags,IDebugControl3.GetDumpFormatFlags
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
req.iface: IDebugControl2
---

# IDebugControl2::GetDumpFormatFlags method



## -description
<p>The <b>GetDumpFormatFlags</b> method returns the flags that describe what information is available in a dump file target.</p>


## -syntax

````
HRESULT GetDumpFormatFlags(
  [out] PULONG FormatFlags
);
````


## -parameters
<dl>

### -param <i>FormatFlags</i> [out]

<dd>
<p>Receives the flags that describe the information included in a dump file.  Different dump files support different sets of format information.  For example, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541497">DEBUG_FORMAT_XXX</a> for a description of the flags used for user-mode Minidump files.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>This method is only available when debugging crash dump files.  If the crash dump file is in a default format or does not have variable formats, zero will be returned to <i>FormatFlags</i>.</p>

<p>This method is only available when debugging crash dump files.  If the crash dump file is in a default format or does not have variable formats, zero will be returned to <i>FormatFlags</i>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561382">WriteDumpFile2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561389">WriteDumpFileWide</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl2::GetDumpFormatFlags method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
