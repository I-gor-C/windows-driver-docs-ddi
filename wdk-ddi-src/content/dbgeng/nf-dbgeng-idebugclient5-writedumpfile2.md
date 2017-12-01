---
UID: NF.dbgeng.IDebugClient5.WriteDumpFile2
title: IDebugClient5::WriteDumpFile2
author: windows-driver-content
description: The WriteDumpFile2 method creates a user-mode or kernel-modecrash dump file.
old-location: debugger\writedumpfile2.htm
old-project: debugger
ms.assetid: a6cdefc2-8670-485d-979a-8a270dad1c0b
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugClient5, WriteDumpFile2, IDebugClient5::WriteDumpFile2
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
req.alt-api: IDebugClient2.WriteDumpFile2,IDebugClient3.WriteDumpFile2,IDebugClient4.WriteDumpFile2,IDebugClient5.WriteDumpFile2
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

# IDebugClient5::WriteDumpFile2 method



## -description
<p>The <b>WriteDumpFile2</b> method creates a user-mode or kernel-modecrash dump file.</p>


## -syntax

````
HRESULT WriteDumpFile2(
  [in]           PCSTR DumpFile,
  [in]           ULONG Qualifier,
  [in]           ULONG FormatFlags,
  [in, optional] PCSTR Comment
);
````


## -parameters
<dl>

### -param <i>DumpFile</i> [in]

<dd>
<p>Specifies the name of the dump file to create.  <i>DumpFile</i> must include the file name extension.  <i>DumpFile</i> can include a relative or absolute path; relative paths are relative to the directory in which the debugger was started.</p>
</dd>

### -param <i>Qualifier</i> [in]

<dd>
<p>Specifies the type of dump file to create.  For possible values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541472">DEBUG_DUMP_XXX</a>.</p>
</dd>

### -param <i>FormatFlags</i> [in]

<dd>
<p>Specifies flags that determine the format of the dump file and--for user-mode minidumps--what information to include in the file.  For details, see Remarks.</p>
</dd>

### -param <i>Comment</i> [in, optional]

<dd>
<p>Specifies a comment string to be included in the crash dump file.  This string is displayed in the debugger console when the dump file is loaded.  Some dump file formats do not support the storing of comment strings.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The DEBUG_FORMAT_<i>XXX</i> bit-flags are used by <b>WriteDumpFile2</b> and <a href="debugger.writedumpfilewide">WriteDumpFileWide</a> to determine the format of a crash dump file and, for user-mode Minidumps, what information to include in the file.</p>

<p>The following bit-flags apply to all crash dump files.</p>

<p>DEBUG_FORMAT_WRITE_CAB</p>

<p>Package the crash dump file in a CAB file.  The supplied file name or file handle is used for the CAB file; the crash dump is first created in a temporary file before being moved into the CAB file.</p>

<p>DEBUG_FORMAT_CAB_SECONDARY_FILES</p>

<p>
<dl>
<dt>Include the current symbols and mapped images in the CAB file.</dt>
<dt>If DEBUG_FORMAT_WRITE_CAB is not set, this flag is ignored.</dt>
</dl>
</p>

<p>DEBUG_FORMAT_NO_OVERWRITE</p>

<p>Do not overwrite existing files.</p>

<p>The following bit-flags can also be included for user-mode Minidumps.</p>

<p>DEBUG_FORMAT_USER_SMALL_FULL_MEMORY</p>

<p>Add full memory data.  All accessible committed pages owned by the target application will be included.</p>

<p>DEBUG_FORMAT_USER_SMALL_HANDLE_DATA</p>

<p>Add data about the handles that are associated with the target application.</p>

<p>DEBUG_FORMAT_USER_SMALL_UNLOADED_MODULES</p>

<p>Add unloaded module information.  This information is available only in Windows Server 2003 and later versions of Windows.</p>

<p>DEBUG_FORMAT_USER_SMALL_INDIRECT_MEMORY</p>

<p>Add indirect memory.  A small region of memory that surrounds any address that is referenced by a pointer on the stack or backing store is included.</p>

<p>DEBUG_FORMAT_USER_SMALL_DATA_SEGMENTS</p>

<p>Add all data segments within the executable images.</p>

<p>DEBUG_FORMAT_USER_SMALL_FILTER_MEMORY</p>

<p>Set to zero all of the memory on the stack and in the backing store that is not useful for recreating the stack trace.  This can make compression of the Minidump more efficient and increase privacy by removing unnecessary information.</p>

<p>DEBUG_FORMAT_USER_SMALL_FILTER_PATHS</p>

<p>Remove the module paths, leaving only the module names.  This is useful for protecting privacy by hiding the directory structure (which may contain the user's name).</p>

<p>DEBUG_FORMAT_USER_SMALL_PROCESS_THREAD_DATA</p>

<p>Add the process environment block (PEB) and thread environment block (TEB).  This flag can be used to provide Windows system information for threads and processes.</p>

<p>DEBUG_FORMAT_USER_SMALL_PRIVATE_READ_WRITE_MEMORY</p>

<p>Add all committed private read-write memory pages.</p>

<p>DEBUG_FORMAT_USER_SMALL_NO_OPTIONAL_DATA</p>

<p>
<dl>
<dt>Prevent privacy-sensitive data from being included in the Minidump.  Currently, this flag excludes from the Minidump data that would have been added due to the following flags being set:</dt>
<dt>DEBUG_FORMAT_USER_SMALL_PROCESS_THREAD_DATA,</dt>
<dt>DEBUG_FORMAT_USER_SMALL_FULL_MEMORY,</dt>
<dt>DEBUG_FORMAT_USER_SMALL_INDIRECT_MEMORY,</dt>
<dt>DEBUG_FORMAT_USER_SMALL_PRIVATE_READ_WRITE_MEMORY.</dt>
</dl>
</p>

<p>DEBUG_FORMAT_USER_SMALL_FULL_MEMORY_INFO</p>

<p>Add all basic memory information.  This is the information returned by the <a href="debugger.queryvirtual">QueryVirtual</a> method.  The information for all memory is included, not just valid memory, which allows the debugger to reconstruct the complete virtual memory layout from the Minidump.</p>

<p>DEBUG_FORMAT_USER_SMALL_THREAD_INFO</p>

<p>Add additional thread information, which includes execution time, start time, exit time, start address, and exit status.</p>

<p>DEBUG_FORMAT_USER_SMALL_CODE_SEGMENTS</p>

<p>Add all code segments with the executable images.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugclient2.md">IDebugClient2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient3.md">IDebugClient3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient4.md">IDebugClient4</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
<dt>
<a href="debugger.writedumpfilewide">WriteDumpFileWide</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562428">.dump (Create Dump File)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient2::WriteDumpFile2 method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
