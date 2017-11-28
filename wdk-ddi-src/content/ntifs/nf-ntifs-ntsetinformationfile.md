---
UID: NF.ntifs.NtSetInformationFile
title: NtSetInformationFile
author: windows-driver-content
description: The ZwSetInformationFile routine changes various kinds of information about a file object.
old-location: kernel\zwsetinformationfile.htm
old-project: kernel
ms.assetid: a6f92495-89f0-4728-b6d8-083c55bc3206
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: NtSetInformationFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwSetInformationFile,NtSetInformationFile
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

# NtSetInformationFile function



## -description
<p>The <b>ZwSetInformationFile</b> routine changes various kinds of information about a file object.</p>


## -syntax

````
NTSTATUS ZwSetInformationFile(
  _In_  HANDLE                 FileHandle,
  _Out_ PIO_STATUS_BLOCK       IoStatusBlock,
  _In_  PVOID                  FileInformation,
  _In_  ULONG                  Length,
  _In_  FILE_INFORMATION_CLASS FileInformationClass
);
````


## -parameters
<dl>

### -param <i>FileHandle</i> [in]

<dd>
<p>Handle to the file object. This handle is created by a successful call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567011">ZwOpenFile</a>.</p>
</dd>

### -param <i>IoStatusBlock</i> [out]

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure that receives the final completion status and information about the requested operation. The <b>Information</b> member receives the number of bytes set on the file.</p>
</dd>

### -param <i>FileInformation</i> [in]

<dd>
<p>Pointer to a buffer that contains the information to set for the file. The particular structure in this buffer is determined by the <i>FileInformationClass</i> parameter. Setting any member of the structure to zero tells <b>ZwSetInformationFile</b> to leave the current information about the file for that member unchanged.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The size, in bytes, of the <i>FileInformation</i> buffer.</p>
</dd>

### -param <i>FileInformationClass</i> [in]

<dd>
<p>The type of information, supplied in the buffer pointed to by <i>FileInformation</i>, to set for the file. Device and intermediate drivers can specify any of the following <a href="https://msdn.microsoft.com/library/windows/hardware/ff728840">FILE_INFORMATION_CLASS</a> values.</p>
<table>
<tr>
<th><i>FileInformationClass</i> Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>FileBasicInformation</b></p>
</td>
<td>
<p>Change the information that is supplied in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545762">FILE_BASIC_INFORMATION</a> structure. The caller must have opened the file with the FILE_WRITE_ATTRIBUTES flag set in the <i>DesiredAccess</i> parameter.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileDispositionInformation</b></p>
</td>
<td>
<p>Usually, sets the <b>DeleteFile</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545765">FILE_DISPOSITION_INFORMATION</a> to <b>TRUE</b>, so the file can be deleted when <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a> is called to release the last open handle to the file object. The caller must have opened the file with the DELETE flag set in the <i>DesiredAccess</i> parameter.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileEndOfFileInformation</b></p>
</td>
<td>
<p>Change the current end-of-file information, supplied in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545780">FILE_END_OF_FILE_INFORMATION</a> structure. The operation can either truncate or extend the file. The caller must have opened the file with the FILE_WRITE_DATA flag set in the <i>DesiredAccess</i> parameter.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileIoPriorityHintInformation</b></p>
</td>
<td>
<p>Change the current default IRP priority hint for the file handle. The new value is supplied in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545802">FILE_IO_PRIORITY_HINT_INFORMATION</a> structure.</p>
<div class="alert"><b>Note</b>    This structure must be 8-byte aligned.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p><b>FileLinkInformation</b></p>
</td>
<td>
<p>Create a hard link to an existing file, which is specified in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540324">FILE_LINK_INFORMATION</a> structure. Not all file systems support hard links; for example NTFS does while FAT does not.</p>
</td>
</tr>
<tr>
<td>
<p><b>FilePositionInformation</b></p>
</td>
<td>
<p>Change the current file information, which is stored in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545848">FILE_POSITION_INFORMATION</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileRenameInformation</b></p>
</td>
<td>
<p>Change the current file name, which is supplied in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540344">FILE_RENAME_INFORMATION</a> structure. The caller must have DELETE access to the file.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileShortNameInformation</b></p>
</td>
<td>
<p>Change the current short file name, which is supplied in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a> structure. The file must be on an NTFS volume, and the caller must have opened the file with the <i>DesiredAccess</i> DELETE flag set in the <i>DesiredAccess</i> parameter.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileValidDataLengthInformation</b></p>
</td>
<td>
<p>Change the current valid data length for the file, which is supplied in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545873">FILE_VALID_DATA_LENGTH_INFORMATION</a> structure. The file must be on an NTFS volume, and the caller must have opened the file with the FILE_WRITE_DATA flag set in the <i>DesiredAccess</i> parameter. Non-administrators and remote users must have the <b>SeManageVolumePrivilege</b> privilege.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileReplaceCompletionInformation</b></p>
</td>
<td>
<p>Change or remove the I/O completion port for the specified file handle. The caller supplies a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn369252">FILE_COMPLETION_INFORMATION</a> structure that specifies a port handle and a completion key. If the port handle is non-NULL, this handle specifies a new I/O completion port to associate with the file handle. To remove the I/O completion port associated with the file handle, set the port handle in the structure to NULL. To get a port handle, a user-mode caller can call the <a href="fs.createiocompletionport">CreateIoCompletionPort</a> function.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>ZwSetInformationFile</b> returns STATUS_SUCCESS or an appropriate error status.</p>

## -remarks
<p><b>ZwSetInformationFile</b> changes information about a file. It ignores any member of a <b>FILE_<i>XXX</i>_INFORMATION</b> structure that is not supported by a particular device or file system.</p>

<p>If you set <i>FileInformationClass</i> to <b>FileDispositionInformation</b>, you can subsequently pass <i>FileHandle</i> to <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a> but not to any other <b>Zw<i>Xxx</i>File</b> routine. Because <b>FileDispositionInformation</b> causes the file to be marked for deletion, it is a programming error to attempt any subsequent operation on the handle other than closing it.</p>

<p>If you set <i>FileInformationClass</i> to <b>FilePositionInformation</b>, and the preceding call to <b>ZwCreateFile</b> included the FILE_NO_INTERMEDIATE_BUFFERING flag in the <i>CreateOptions</i> parameter, certain restrictions on the <b>CurrentByteOffset</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545848">FILE_POSITION_INFORMATION</a> structure are enforced. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>.</p>

<p>If you set <i>FileInformationClass</i> to <b>FileEndOfFileInformation</b>, and the <b>EndOfFile</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff545780">FILE_END_OF_FILE_INFORMATION</a> specifies an offset beyond the current end-of-file mark, <b>ZwSetInformationFile</b> extends the file and pads the extension with zeros.</p>

<p>For more information about working with files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565384">Using Files in a Driver</a>.</p>

<p>Callers of <b>ZwSetInformationFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p><b>ZwSetInformationFile</b> changes information about a file. It ignores any member of a <b>FILE_<i>XXX</i>_INFORMATION</b> structure that is not supported by a particular device or file system.</p>

<p>If you set <i>FileInformationClass</i> to <b>FileDispositionInformation</b>, you can subsequently pass <i>FileHandle</i> to <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a> but not to any other <b>Zw<i>Xxx</i>File</b> routine. Because <b>FileDispositionInformation</b> causes the file to be marked for deletion, it is a programming error to attempt any subsequent operation on the handle other than closing it.</p>

<p>If you set <i>FileInformationClass</i> to <b>FilePositionInformation</b>, and the preceding call to <b>ZwCreateFile</b> included the FILE_NO_INTERMEDIATE_BUFFERING flag in the <i>CreateOptions</i> parameter, certain restrictions on the <b>CurrentByteOffset</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545848">FILE_POSITION_INFORMATION</a> structure are enforced. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>.</p>

<p>If you set <i>FileInformationClass</i> to <b>FileEndOfFileInformation</b>, and the <b>EndOfFile</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff545780">FILE_END_OF_FILE_INFORMATION</a> specifies an offset beyond the current end-of-file mark, <b>ZwSetInformationFile</b> extends the file and pads the extension with zeros.</p>

<p>For more information about working with files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565384">Using Files in a Driver</a>.</p>

<p>Callers of <b>ZwSetInformationFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="fs.createiocompletionport">CreateIoCompletionPort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545762">FILE_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn369252">FILE_COMPLETION_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545765">FILE_DISPOSITION_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545780">FILE_END_OF_FILE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545802">FILE_IO_PRIORITY_HINT_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540324">FILE_LINK_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545848">FILE_POSITION_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540344">FILE_RENAME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545873">FILE_VALID_DATA_LENGTH_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567011">ZwOpenFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwSetInformationFile routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
