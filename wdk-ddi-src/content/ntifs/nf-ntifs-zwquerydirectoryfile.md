---
UID: NF.ntifs.ZwQueryDirectoryFile
title: ZwQueryDirectoryFile
author: windows-driver-content
description: The ZwQueryDirectoryFile routine returns various kinds of information about files in the directory specified by a given file handle.
old-location: kernel\zwquerydirectoryfile.htm
old-project: kernel
ms.assetid: 47e88095-fab3-4fa2-814e-db04ce864e7e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ZwQueryDirectoryFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwQueryDirectoryFile,NtQueryDirectoryFile
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
---

# ZwQueryDirectoryFile function



## -description
<p>The <b>ZwQueryDirectoryFile</b> routine returns various kinds of information about files in the directory specified by a given file handle.</p>


## -syntax

````
NTSTATUS ZwQueryDirectoryFile(
  _In_     HANDLE                 FileHandle,
  _In_opt_ HANDLE                 Event,
  _In_opt_ PIO_APC_ROUTINE        ApcRoutine,
  _In_opt_ PVOID                  ApcContext,
  _Out_    PIO_STATUS_BLOCK       IoStatusBlock,
  _Out_    PVOID                  FileInformation,
  _In_     ULONG                  Length,
  _In_     FILE_INFORMATION_CLASS FileInformationClass,
  _In_     BOOLEAN                ReturnSingleEntry,
  _In_opt_ PUNICODE_STRING        FileName,
  _In_     BOOLEAN                RestartScan
);
````


## -parameters
<dl>

### -param FileHandle [in]

<dd>
<p>A handle returned by <a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a> or <a href="..\wdm\nf-wdm-zwopenfile.md">ZwOpenFile</a> for the file object that represents the directory for which information is being requested. The file object must have been opened for asynchronous I/O if the caller specifies a non-<b>NULL</b> value for <i>Event</i> or <i>ApcRoutine</i>.</p>
</dd>

### -param Event [in, optional]

<dd>
<p>An optional handle for a caller-created event. If this parameter is supplied, the caller will be put into a wait state until the requested operation is completed and the given event is set to the Signaled state. This parameter is optional and can be <b>NULL</b>. It must be <b>NULL</b> if the caller will wait for the <i>FileHandle</i> to be set to the Signaled state.</p>
</dd>

### -param ApcRoutine [in, optional]

<dd>
<p>An address of an optional, caller-supplied APC routine to be called when the requested operation completes. This parameter is optional and can be <b>NULL</b>. If there is an I/O completion object associated with the file object, this parameter must be <b>NULL</b>.</p>
</dd>

### -param ApcContext [in, optional]

<dd>
<p>An optional pointer to a caller-determined context area if the caller supplies an APC or if an I/O completion object is associated with the file object. When the operation completes, this context is passed to the APC, if one was specified, or is included as part of the completion message that the I/O Manager posts to the associated I/O completion object. </p>
<p>This parameter is optional and can be <b>NULL</b>. It must be <b>NULL</b> if <i>ApcRoutine</i> is <b>NULL</b> and there is no I/O completion object associated with the file object.</p>
</dd>

### -param IoStatusBlock [out]

<dd>
<p>A pointer to an <a href="..\wdm\ns-wdm--io-status-block.md">IO_STATUS_BLOCK</a> structure that receives the final completion status and information about the operation. For successful calls that return data, the number of bytes written to the <i>FileInformation</i> buffer is returned in the structure's <b>Information</b> member.</p>
</dd>

### -param FileInformation [out]

<dd>
<p>A pointer to a buffer that receives the desired information about the file. The structure of the information returned in the buffer is defined by the <i>FileInformationClass</i> parameter.</p>
</dd>

### -param Length [in]

<dd>
<p>The size, in bytes, of the buffer pointed to by <i>FileInformation</i>. The caller should set this parameter according to the given <i>FileInformationClass</i>.</p>
</dd>

### -param FileInformationClass [in]

<dd>
<p>The type of information to be returned about files in the directory. One of the following. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>FileBothDirectoryInformation</b></p>
</td>
<td>
<p>Return a <a href="..\ntifs\ns-ntifs--file-both-dir-information.md">FILE_BOTH_DIR_INFORMATION</a> structure for each file.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileDirectoryInformation</b></p>
</td>
<td>
<p>Return a <a href="..\ntifs\ns-ntifs--file-directory-information.md">FILE_DIRECTORY_INFORMATION</a> structure for each file.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileFullDirectoryInformation</b></p>
</td>
<td>
<p>Return a <a href="..\ntifs\ns-ntifs--file-full-dir-information.md">FILE_FULL_DIR_INFORMATION</a> structure for each file.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileIdBothDirectoryInformation</b></p>
</td>
<td>
<p>Return a <a href="..\ntifs\ns-ntifs--file-id-both-dir-information.md">FILE_ID_BOTH_DIR_INFORMATION</a> structure for each file.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileIdFullDirectoryInformation</b></p>
</td>
<td>
<p>Return a <a href="..\ntifs\ns-ntifs--file-id-full-dir-information.md">FILE_ID_FULL_DIR_INFORMATION</a> structure for each file.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileNamesInformation</b></p>
</td>
<td>
<p>Return a <a href="..\ntifs\ns-ntifs--file-names-information.md">FILE_NAMES_INFORMATION</a> structure for each file.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileObjectIdInformation</b></p>
</td>
<td>
<p>Return a <a href="..\ntifs\ns-ntifs--file-objectid-information.md">FILE_OBJECTID_INFORMATION</a> structure for each file. This information class is valid only for NTFS volumes on Windows 2000 and later versions of Windows.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileReparsePointInformation</b></p>
</td>
<td>
<p>Return a single <a href="..\ntifs\ns-ntifs--file-reparse-point-information.md">FILE_REPARSE_POINT_INFORMATION</a> structure for the directory.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param ReturnSingleEntry [in]

<dd>
<p>Set to <b>TRUE</b> if only a single entry should be returned, <b>FALSE</b> otherwise. If this parameter is <b>TRUE</b>, <b>ZwQueryDirectoryFile</b> returns only the first entry that is found.</p>
</dd>

### -param FileName [in, optional]

<dd>
<p>An optional pointer to a caller-allocated Unicode string containing the name of a file (or multiple files, if wildcards are used) within the directory specified by <i>FileHandle</i>. This parameter is optional and can be <b>NULL</b>. </p>
<p>If <i>FileName</i> is not <b>NULL</b>, only files whose names match the <i>FileName</i> string are included in the directory scan. If <i>FileName</i> is <b>NULL</b>, all files are included. </p>
<p>The <i>FileName</i> is used as a search expression and is captured on the very first call to <b>ZwQueryDirectoryFile</b> for a given handle. Subsequent calls to <b>ZwQueryDirectoryFile</b> will use the search expression set in the first call. The <i>FileName</i> parameter passed to subsequent calls will be ignored. </p>
</dd>

### -param RestartScan [in]

<dd>
<p>Set to <b>TRUE</b> if the scan is to start at the first entry in the directory. Set to <b>FALSE</b> if resuming the scan from a previous call.</p>
<p>When the <b>ZwQueryDirectoryFile</b> routine is called for a particular handle, the <i>RestartScan</i> parameter is treated as if it were set to <b>TRUE</b>, regardless of its value. On subsequent <b>ZwQueryDirectoryFile</b> calls, the value of the <i>RestartScan</i> parameter is honored.</p>
</dd>
</dl>

## -returns
<p>The <b>ZwQueryDirectoryFile</b>routine returns STATUS_SUCCESS or an appropriate error status. Note that the set of error status values that can be returned is file-system-specific. <b>ZwQueryDirectoryFile</b>also returns the number of bytes actually written to the given <i>FileInformation</i> buffer in the <b>Information</b> member of <i>IoStatusBlock</i>.</p>

## -remarks
<p>The <b>ZwQueryDirectoryFile</b> routine returns information about files that are contained in the directory represented by <i>FileHandle</i>.</p>

<p>If provided, the value of the <i>FileName</i> parameter determines the entries that are included in the directory scan for all subsequent calls to <b>ZwQueryDirectoryFile</b> for a given <i>FileHandle</i>.</p>

<p>If there is at least one matching entry, <b>ZwQueryDirectoryFile</b> creates a <b>FILE_<i>XXX</i>_INFORMATION</b> structure for each entry and stores them in the buffer.</p>

<p>Assuming that at least one matching directory entry is found, the number of entries for which information is returned is the <i>smallest</i> of the following:</p>

<p>One entry, if <i>ReturnSingleEntry</i> is <b>TRUE</b> and <i>FileName</i> is <b>NULL</b>.</p>

<p>The number of entries that match the <i>FileName</i> string, if <i>FileName</i> is not <b>NULL</b>. (Note that if the string contains no wildcards, there can be at most one matching entry.)</p>

<p>The number of entries whose information fits into the specified buffer.</p>

<p>The number of entries contained in the directory.</p>

<p>On the first call to <b>ZwQueryDirectoryFile</b>, if the structure created for the first entry found is too large to fit into the output buffer, the routine writes the fixed portion of the structure to the output buffer. The routine then writes to the output buffer as much of the <i>FileName</i> string as will fit. (The fixed portion of the structure consists of all fields except the final <i>FileName</i> string. On the first call, but not on subsequent calls, the I/O system ensures that the buffer is large enough to hold the fixed portion of the appropriate <b>FILE_<i>XXX</i>_INFORMATION</b> structure.) When this happens, <b>ZwQueryDirectoryFile</b> returns an appropriate status value such as STATUS_BUFFER_OVERFLOW.</p>

<p>On each call, <b>ZwQueryDirectoryFile</b> returns as many <b>FILE_<i>XXX</i>_INFORMATION</b> structures (one per directory entry) as can be contained entirely in the buffer pointed to by <i>FileInformation</i>. On the first call, <b>ZwQueryDirectoryFile</b> returns STATUS_SUCCESS only if the output buffer contains at least one complete structure. On subsequent calls, if the output buffer contains no structures, <b>ZwQueryDirectoryFile</b> returns STATUS_SUCCESS but sets <i>IoStatusBlock</i>-&gt;<b>Information</b> = 0 to notify the caller of this condition. In this case, the caller should allocate a larger buffer and call <b>ZwQueryDirectoryFile</b> again. No information about any remaining entries is reported. Thus, except in the cases listed above where only one entry is returned, <b>ZwQueryDirectoryFile</b> must be called at least twice to enumerate the contents of an entire directory.</p>

<p>When calling <b>ZwQueryDirectoryFile</b>, you may see changes made to the directory that occur in parallel with <b>ZwQueryDirectoryFile</b> calls.  This behavior is dependent on the implementation of the underlying file system.</p>

<p>The final call to <b>ZwQueryDirectoryFile</b> returns an empty output buffer and reports an appropriate status value such as STATUS_NO_MORE_FILES.</p>

<p>If <b>ZwQueryDirectoryFile</b> is called multiple times on the same directory and some other operation changes the contents of that directory, any changes may or may not be seen, depending on the timing of the operations.</p>

<p><b>ZwQueryDirectoryFile</b>returns zero in any member of a <b>FILE_<i>XXX</i>_INFORMATION</b> structure that is not supported by the file system.</p>

<p>Callers of <b>ZwQueryDirectoryFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

<p>For information about other file information query routines, see <a href="kernel.file_objects">File Objects</a>.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL (see Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\ns-ntifs--file-both-dir-information.md">FILE_BOTH_DIR_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-directory-information.md">FILE_DIRECTORY_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-full-dir-information.md">FILE_FULL_DIR_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-id-both-dir-information.md">FILE_ID_BOTH_DIR_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-id-full-dir-information.md">FILE_ID_FULL_DIR_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-names-information.md">FILE_NAMES_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-objectid-information.md">FILE_OBJECTID_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-reparse-point-information.md">FILE_REPARSE_POINT_INFORMATION</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopenfile.md">ZwOpenFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwQueryDirectoryFile routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
