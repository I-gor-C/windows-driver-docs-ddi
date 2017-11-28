---
UID: NF.dbgeng.IDebugClient4.AddDumpInformationFileWide
title: IDebugClient4::AddDumpInformationFileWide
author: windows-driver-content
description: The AddDumpInformationFileWide method registers additional files containing supporting information that will be used when opening a dump file. The ASCII version of this method is AddDumpInformationFile.
old-location: debugger\adddumpinformationfilewide.htm
old-project: debugger
ms.assetid: 0b6318de-4f8e-43e8-ad86-c1fc52097662
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugClient4, AddDumpInformationFileWide, IDebugClient4::AddDumpInformationFileWide
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
req.alt-api: IDebugClient4.AddDumpInformationFileWide,IDebugClient5.AddDumpInformationFileWide
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
req.iface: IDebugClient4
---

# IDebugClient4::AddDumpInformationFileWide method



## -description
<p>The <b>AddDumpInformationFileWide</b> method registers additional files containing supporting information that will be used when opening a <a href="debugger.d#dump_file#dump_file">dump file</a>.  The ASCII version of this method is <a href="https://msdn.microsoft.com/library/windows/hardware/ff537865">AddDumpInformationFile</a>.</p>


## -syntax

````
HRESULT AddDumpInformationFileWide(
  [in, optional] PCWSTR  FileName,
  [in]           ULONG64 FileHandle,
  [in]           ULONG   Type
);
````


## -parameters
<dl>

### -param <i>FileName</i> [in, optional]

<dd>
<p>Specifies the name of the file containing the supporting information.  If <i>FileHandle</i> is not zero, <i>FileName</i> is used only for informational purposes.</p>
</dd>

### -param <i>FileHandle</i> [in]

<dd>
<p>Specifies the handle of the file containing the supporting information.  If <i>FileHandle</i> is zero, the file named in <i>FileName</i> is used.</p>
</dd>

### -param <i>Type</i> [in]

<dd>
<p>Specifies the type of the file in <i>FileName</i> or <i>FileHandle</i>.  Currently, only files containing paging file information are supported, and <i>Type</i> must be set to DEBUG_DUMP_FILE_PAGE_FILE_DUMP.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>If supporting information is to be used when opening a dump file, this method or <a href="https://msdn.microsoft.com/library/windows/hardware/ff537865">AddDumpInformationFile</a> must be called before <a href="https://msdn.microsoft.com/library/windows/hardware/ff552322">OpenDumpFile</a> is called. If a session has already started, this method cannot be used.</p>

<p>For more information about crash dump files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542783">Dump-File Targets</a>.</p>

<p>If supporting information is to be used when opening a dump file, this method or <a href="https://msdn.microsoft.com/library/windows/hardware/ff537865">AddDumpInformationFile</a> must be called before <a href="https://msdn.microsoft.com/library/windows/hardware/ff552322">OpenDumpFile</a> is called. If a session has already started, this method cannot be used.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537865">AddDumpInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547887">GetNumberDumpFiles</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546586">GetDumpFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552322">OpenDumpFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552324">OpenDumpFileWide</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient4::AddDumpInformationFileWide method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
