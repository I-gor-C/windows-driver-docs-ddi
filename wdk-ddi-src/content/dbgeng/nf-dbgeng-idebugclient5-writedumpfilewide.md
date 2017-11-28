---
UID: NF.dbgeng.IDebugClient5.WriteDumpFileWide
title: IDebugClient5::WriteDumpFileWide
author: windows-driver-content
description: The WriteDumpFileWide method creates a user-mode or kernel-modecrash dump file.
old-location: debugger\writedumpfilewide.htm
old-project: debugger
ms.assetid: b089499f-4f15-400e-bf88-53d0507200b9
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugClient5, WriteDumpFileWide, IDebugClient5::WriteDumpFileWide
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
req.alt-api: IDebugClient4.WriteDumpFileWide,IDebugClient5.WriteDumpFileWide
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
req.iface: IDebugClient5
---

# IDebugClient5::WriteDumpFileWide method



## -description
<p>The <b>WriteDumpFileWide</b> method creates a user-mode or kernel-modecrash dump file.</p>


## -syntax

````
HRESULT WriteDumpFileWide(
  [in, optional] PCWSTR  FileName,
  [in]           ULONG64 FileHandle,
  [in]           ULONG   Qualifier,
  [in]           ULONG   FormatFlags,
  [in, optional] PCWSTR  Comment
);
````


## -parameters
<dl>

### -param <i>FileName</i> [in, optional]

<dd>
<p>Specifies the name of the dump file to create.  <i>FileName</i> must include the file name extension. <i>FileName</i> can include a relative or absolute path; relative paths are relative to the directory in which the debugger was started.  If <i>FileHandle</i> is not <b>NULL</b>, <i>FileName</i> is ignored (except when writing status messages to the debugger console).</p>
</dd>

### -param <i>FileHandle</i> [in]

<dd>
<p>Specifies the file handle of the file to write the crash dump to.  If <i>FileHandle</i> is <b>NULL</b>, the file specified in <i>FileName</i> is used instead.</p>
</dd>

### -param <i>Qualifier</i> [in]

<dd>
<p>Specifies the type of dump to create.  For possible values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541472">DEBUG_DUMP_XXX</a>.</p>
</dd>

### -param <i>FormatFlags</i> [in]

<dd>
<p>Specifies flags that determine the format of the dump file and--for user-mode minidumps--what information to include in the file.  For details, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541497">DEBUG_FORMAT_XXX</a>.</p>
</dd>

### -param <i>Comment</i> [in, optional]

<dd>
<p>Specifies a comment string to be included in the crash dump file.  This string is displayed in the debugger console when the dump file is loaded.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information about crash dump files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542783">Dump-File Targets</a>.</p>

<p>For more information about crash dump files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542783">Dump-File Targets</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550494">IDebugClient4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550497">IDebugClient5</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561382">WriteDumpFile2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562428">.dump (Create Dump File)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient4::WriteDumpFileWide method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
