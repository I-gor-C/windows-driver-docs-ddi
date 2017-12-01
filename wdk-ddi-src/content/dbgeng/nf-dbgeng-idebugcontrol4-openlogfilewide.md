---
UID: NF.dbgeng.IDebugControl4.OpenLogFileWide
title: IDebugControl4::OpenLogFileWide
author: windows-driver-content
description: The OpenLogFileWide method opens a log file that will receive output from the client objects.
old-location: debugger\openlogfilewide.htm
old-project: debugger
ms.assetid: 1e69812e-077e-476f-a253-f0c39575eb32
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl4, OpenLogFileWide, IDebugControl4::OpenLogFileWide
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
req.alt-api: IDebugControl4.OpenLogFileWide
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

# IDebugControl4::OpenLogFileWide method



## -description
<p>The <b>OpenLogFileWide</b>  method opens a log file that will receive output from the <a href="debugger.client_objects#client_objects#client_objects">client objects</a>.</p>


## -syntax

````
HRESULT OpenLogFileWide(
  [in] PCWSTR File,
  [in] BOOL   Append
);
````


## -parameters
<dl>

### -param <i>File</i> [in]

<dd>
<p>Specifies the name of the log file.  <i>File</i> can include a relative or absolute path; relative paths are relative to the directory in which the debugger  was started.  If the file does not exist, it will be created.</p>
</dd>

### -param <i>Append</i> [in]

<dd>
<p>Specifies whether or not to append log messages to an existing log file.  If <b>TRUE</b>, log messages will be appended to the file; if <b>FALSE</b>, the contents of any existing file matching <i>File</i> are discarded.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p><b>OpenLogFile</b> and <b>OpenLogFileWide</b> behave the same way as <a href="debugger.openlogfile2">OpenLogFile2</a> and <b>OpenLogFile2Wide</b> with <i>Flags</i> set to DEBUG_LOG_APPEND if <i>Append</i> is <b>TRUE</b> and DEBUG_LOG_DEFAULT otherwise.</p>

<p>Only one log file can be open at a time.  If there is already a log file open, it will be closed.</p>

<p>For more information about log files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560116">Using Input and Output</a>.</p>

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
<a href="debugger.openlogfile2">OpenLogFile2</a>
</dt>
<dt>
<a href="debugger.getlogfile">GetLogFile</a>
</dt>
<dt>
<a href="debugger.closelogfile">CloseLogFile</a>
</dt>
<dt>
<a href="debugger.getlogmask">GetLogMask</a>
</dt>
<dt>
<a href="debugger.setlogmask">SetLogMask</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564018">.logopen (Open Log File)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563986">.logappend (Append Log File)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl4::OpenLogFileWide method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
