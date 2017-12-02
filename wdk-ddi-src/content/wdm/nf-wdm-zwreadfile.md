---
UID: NF.wdm.ZwReadFile
title: ZwReadFile
author: windows-driver-content
description: The ZwReadFile routine reads data from an open file.
old-location: kernel\zwreadfile.htm
old-project: kernel
ms.assetid: 0f1ec015-bda6-45fe-973d-be414aece918
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ZwReadFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwReadFile,NtReadFile
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, BufAfterReqCompletedIntIoctlA, BufAfterReqCompletedIoctlA, BufAfterReqCompletedReadA, BufAfterReqCompletedWriteA, HwStorPortProhibitedDDIs
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
req.product: Windows 10 or later.
---

# ZwReadFile function



## -description
<p>The <b>ZwReadFile</b> routine reads data from an open file. </p>


## -syntax

````
NTSTATUS ZwReadFile(
  _In_     HANDLE           FileHandle,
  _In_opt_ HANDLE           Event,
  _In_opt_ PIO_APC_ROUTINE  ApcRoutine,
  _In_opt_ PVOID            ApcContext,
  _Out_    PIO_STATUS_BLOCK IoStatusBlock,
  _Out_    PVOID            Buffer,
  _In_     ULONG            Length,
  _In_opt_ PLARGE_INTEGER   ByteOffset,
  _In_opt_ PULONG           Key
);
````


## -parameters
<dl>

### -param FileHandle [in]

<dd>
<p>Handle to the file object. This handle is created by a successful call to <a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a> or <a href="..\wdm\nf-wdm-zwopenfile.md">ZwOpenFile</a>. </p>
</dd>

### -param Event [in, optional]

<dd>
<p>Optionally, a handle to an event object to set to the signaled state after the read operation completes. Device and intermediate drivers should set this parameter to <b>NULL</b>.</p>
</dd>

### -param ApcRoutine [in, optional]

<dd>
<p>This parameter is reserved. Device and intermediate drivers should set this pointer to <b>NULL</b>.</p>
</dd>

### -param ApcContext [in, optional]

<dd>
<p>This parameter is reserved. Device and intermediate drivers should set this pointer to <b>NULL</b>.</p>
</dd>

### -param IoStatusBlock [out]

<dd>
<p>Pointer to an <a href="..\wdm\ns-wdm--io-status-block.md">IO_STATUS_BLOCK</a> structure that receives the final completion status and information about the requested read operation. The <b>Information</b> member receives the number of bytes actually read from the file.</p>
</dd>

### -param Buffer [out]

<dd>
<p>Pointer to a caller-allocated buffer that receives the data read from the file.</p>
</dd>

### -param Length [in]

<dd>
<p>The size, in bytes, of the buffer pointed to by <i>Buffer</i>.</p>
</dd>

### -param ByteOffset [in, optional]

<dd>
<p>Pointer to a variable that specifies the starting byte offset in the file where the read operation will begin. If an attempt is made to read beyond the end of the file, <b>ZwReadFile</b> returns an error.</p>
<p>If the call to <a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a> set either of the <b>CreateOptions</b> flags FILE_SYNCHRONOUS_IO_ALERT or FILE_SYNCHRONOUS_IO_NONALERT, the I/O Manager maintains the current file position. If so, the caller of <b>ZwReadFile</b> can specify that the current file position offset be used instead of an explicit <b>ByteOffset</b> value. This specification can be made by using one of the following methods:</p>
<ul>
<li>
<p>Specify a pointer to a LARGE_INTEGER value with the <b>HighPart</b> member set to -1 and the <b>LowPart</b> member set to the system-defined value FILE_USE_FILE_POINTER_POSITION.</p>
</li>
<li>
<p>Pass a <b>NULL</b> pointer for <i>ByteOffset</i>.</p>
</li>
</ul>
<p><b>ZwReadFile</b> updates the current file position by adding the number of bytes read when it completes the read operation, if it is using the current file position maintained by the I/O Manager.</p>
<p>Even when the I/O Manager is maintaining the current file position, the caller can reset this position by passing an explicit <i>ByteOffset</i> value to <b>ZwReadFile</b>. Doing this automatically changes the current file position to that <i>ByteOffset</i> value, performs the read operation, and then updates the position according to the number of bytes actually read. This technique gives the caller atomic seek-and-read service.</p>
</dd>

### -param Key [in, optional]

<dd>
<p>Device and intermediate drivers should set this pointer to <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>ZwReadFile</b> returns either STATUS_SUCCESS or the appropriate NTSTATUS error code.</p>

## -remarks
<p>Callers of <b>ZwReadFile</b> must have already called <a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a> with the FILE_READ_DATA or GENERIC_READ value set in the <i>DesiredAccess</i> parameter.</p>

<p>If the preceding call to <a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a> set the FILE_NO_INTERMEDIATE_BUFFERING flag in the <i>CreateOptions</i> parameter to <b>ZwCreateFile</b>, the <i>Length</i> and <i>ByteOffset</i> parameters to <b>ZwReadFile</b> must be multiples of the sector size. For more information, see <b>ZwCreateFile</b>.</p>

<p><b>ZwReadFile</b> begins reading from the given <i>ByteOffset</i> or the current file position into the given <i>Buffer</i>. It terminates the read operation under one of the following conditions:</p>

<p>The buffer is full because the number of bytes specified by the <i>Length</i> parameter has been read. Therefore, no more data can be placed into the buffer without an overflow.</p>

<p>The end of file is reached during the read operation, so there is no more data in the file to be transferred into the buffer.</p>

<p>If the caller opened the file with the SYNCHRONIZE flag set in <i>DesiredAccess</i>, the calling thread can synchronize to the completion of the read operation by waiting on the file handle, <i>FileHandle</i>. The handle is signaled each time that an I/O operation that was issued on the handle completes. However, the caller must not wait on a handle that was opened for synchronous file access (FILE_SYNCHRONOUS_IO_NONALERT or FILE_SYNCHRONOUS_IO_ALERT). In this case, <b>ZwReadFile</b> waits on behalf of the caller and does not return until the read operation is complete. The caller can safely wait on the file handle only if all three of the following conditions are met:</p>

<p>The handle was opened for asynchronous access (that is, neither FILE_SYNCHRONOUS_IO_<b>XXX</b> flag was specified). </p>

<p>The handle is being used for only one I/O operation at a time. </p>

<p><b>ZwReadFile</b> returned STATUS_PENDING. </p>

<p>A driver should call <b>ZwReadFile</b> in the context of the system process if any of the following conditions exist:</p>

<p>The driver created the file handle that it passes to <b>ZwReadFile</b>.</p>

<p><b>ZwReadFile</b> will notify the driver of I/O completion by means of an event that the driver created.</p>

<p><b>ZwReadFile</b> will notify the driver of I/O completion by means of  an APC callback routine that the driver passes to <b>ZwReadFile</b>. </p>

<p>File and event handles are valid only in the process context where the handles are created. Therefore, to avoid security holes, the driver should create any file or event handle that it passes to <b>ZwReadFile</b> in the context of the system process rather than the context of the process that the driver is in.</p>

<p>Likewise, <b>ZwReadFile</b> should be called in the context of the system process if it notifies the driver of I/O completion by means of an APC, because APCs are always fired in the context of the thread that issues the I/O request. If the driver calls <b>ZwReadFile</b> in the context of a process other than the system one, the APC could be delayed indefinitely, or it might not fire at all.</p>

<p>For more information about working with files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565384">Using Files in a Driver</a>.</p>

<p>Callers of <b>ZwReadFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.kmdf_bufafterreqcompletedintioctla">BufAfterReqCompletedIntIoctlA</a>, <a href="devtest.kmdf_bufafterreqcompletedioctla">BufAfterReqCompletedIoctlA</a>, <a href="devtest.kmdf_bufafterreqcompletedreada">BufAfterReqCompletedReadA</a>, <a href="devtest.kmdf_bufafterreqcompletedwritea">BufAfterReqCompletedWriteA</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-keinitializeevent.md">KeInitializeEvent</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwwritefile.md">ZwWriteFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwReadFile routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
