---
UID: NF.dbgeng.IDebugClient5.OpenDumpFileWide
title: IDebugClient5::OpenDumpFileWide
author: windows-driver-content
description: The OpenDumpFileWide method opens a dump file as a debugger target.
old-location: debugger\opendumpfilewide.htm
old-project: debugger
ms.assetid: 56efc94f-ef1e-41f9-ab99-57f0be34a770
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugClient5, OpenDumpFileWide, IDebugClient5::OpenDumpFileWide
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
req.alt-api: IDebugClient4.OpenDumpFileWide,IDebugClient5.OpenDumpFileWide
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

# IDebugClient5::OpenDumpFileWide method



## -description
<p>The <b>OpenDumpFileWide</b> method opens a dump file as a debugger target.</p>


## -syntax

````
HRESULT OpenDumpFileWide(
  [in, optional] PCWSTR  FileName,
  [in]           ULONG64 FileHandle
);
````


## -parameters
<dl>

### -param <i>FileName</i> [in, optional]

<dd>
<p>Specifies the name of the dump file to open -- unless <i>FileHandle</i> is not zero, in which case <i>FileName</i> is used only when the engine is queried for the name of the dump file.  <i>FileName</i> must include the file name extension.  <i>FileName</i> can include a relative or absolute path; relative paths are relative to the directory in which the debugger was started.  <i>FileName</i> can also be in the form of a file URL, starting with "file://".  If <i>FileName</i> specifies a cabinet (.cab) file, the cabinet file is searched for the first file with extension .kdmp, then .hdmp, then .mdmp, and finally .dmp.</p>
</dd>

### -param <i>FileHandle</i> [in]

<dd>
<p>Specifies the file handle of the dump file to open.  If <i>FileHandle</i> is zero, <i>FileName</i> is used to open the dump file.  Otherwise, if <i>FileName</i> is not <b>NULL</b>, the engine returns it when queried for the name of the dump file.  If <i>FileHandle</i> is not zero and <i>FileName</i> is <b>NULL</b>, the engine will return <b>&lt;HandleOnly&gt;</b> for the file name.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The ASCII version of this method is <a href="debugger.opendumpfile">OpenDumpFile</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugclient4.md">IDebugClient4</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
<dt>
<a href="debugger.opendumpfile">OpenDumpFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564611">.opendump (Open Dump File)</a>
</dt>
<dt>
<a href="debugger.adddumpinformationfile">AddDumpInformationFile</a>
</dt>
<dt>
<a href="debugger.adddumpinformationfilewide">AddDumpInformationFileWide</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient4::OpenDumpFileWide method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
