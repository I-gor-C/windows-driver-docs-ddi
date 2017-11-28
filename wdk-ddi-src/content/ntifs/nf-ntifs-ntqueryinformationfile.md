---
UID: NF.ntifs.NtQueryInformationFile
title: NtQueryInformationFile
author: windows-driver-content
description: The ZwQueryInformationFile routine returns various kinds of information about a file object.
old-location: kernel\zwqueryinformationfile.htm
old-project: kernel
ms.assetid: 007df07e-685b-4224-b9d6-55e87cf0bd5c
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: NtQueryInformationFile
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
req.alt-api: ZwQueryInformationFile,NtQueryInformationFile
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

# NtQueryInformationFile function



## -description
<p>The <b>ZwQueryInformationFile</b> routine returns various kinds of information about a file object.</p>


## -syntax

````
NTSTATUS ZwQueryInformationFile(
  _In_  HANDLE                 FileHandle,
  _Out_ PIO_STATUS_BLOCK       IoStatusBlock,
  _Out_ PVOID                  FileInformation,
  _In_  ULONG                  Length,
  _In_  FILE_INFORMATION_CLASS FileInformationClass
);
````


## -parameters
<dl>

### -param <i>FileHandle</i> [in]

<dd>
<p>Handle to a file object. The handle is created by a successful call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567011">ZwOpenFile</a>.</p>
</dd>

### -param <i>IoStatusBlock</i> [out]

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure that receives the final completion status and information about the operation. The <b>Information</b> member receives the number of bytes that this routine actually writes to the <i>FileInformation</i> buffer.</p>
</dd>

### -param <i>FileInformation</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer into which the routine writes the requested information about the file object. The <i>FileInformationClass</i> parameter specifies the type of information that the caller requests.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The size, in bytes, of the buffer pointed to by <i>FileInformation</i>.</p>
</dd>

### -param <i>FileInformationClass</i> [in]

<dd>
<p>Specifies the type of information to be returned about the file, in the buffer that <i>FileInformation</i> points to. Device and intermediate drivers can specify any of the following <a href="https://msdn.microsoft.com/library/windows/hardware/ff728840">FILE_INFORMATION_CLASS</a> values.</p>
<table>
<tr>
<th>FILE_INFORMATION_CLASS value</th>
<th>Type of information returned</th>
</tr>
<tr>
<td>
<p><b>FileAccessInformation</b></p>
</td>
<td>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545733">FILE_ACCESS_INFORMATION</a> structure. This structure contains an access mask. For more information about access masks, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileAlignmentInformation</b></p>
</td>
<td>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545740">FILE_ALIGNMENT_INFORMATION</a> structure. The caller can query this information as long as the file is open, without any particular requirements for <i>DesiredAccess</i>. This information is useful if the file was opened with the FILE_NO_INTERMEDIATE_BUFFERING flag specified in the <i>CreateOptions</i> parameter.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileAllInformation</b></p>
</td>
<td>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545743">FILE_ALL_INFORMATION</a> structure. By combining several file-information structures into a single structure, <b>FILE_ALL_INFORMATION</b> reduces the number of queries required to obtain information about a file.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileAttributeTagInformation</b></p>
</td>
<td>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545750">FILE_ATTRIBUTE_TAG_INFORMATION</a> structure. The caller must have opened the file with the FILE_READ_ATTRIBUTES flag specified in the <i>DesiredAccess</i> parameter.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileBasicInformation</b></p>
</td>
<td>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545762">FILE_BASIC_INFORMATION</a> structure. The caller must have opened the file with the FILE_READ_ATTRIBUTES flag specified in the <i>DesiredAccess</i> parameter.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileEaInformation</b></p>
</td>
<td>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545773">FILE_EA_INFORMATION</a> structure. This structure specifies the size of the extended attributes block that is associated with the file.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileInternalInformation</b></p>
</td>
<td>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff540318">FILE_INTERNAL_INFORMATION</a> structure. This structure specifies a 64-bit file ID that uniquely identifies a file in NTFS. On other file systems, this file ID is not guaranteed to be unique.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileIoPriorityHintInformation</b></p>
</td>
<td>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545802">FILE_IO_PRIORITY_HINT_INFORMATION</a> structure. The caller must have opened the file with the FILE_READ_DATA flag specified in the <i>DesiredAccess</i> parameter.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileModeInformation</b></p>
</td>
<td>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545809">FILE_MODE_INFORMATION</a> structure. This structure contains a set of flags that specify the mode in which the file can be accessed. These flags are a subset of the options that can be specified in the <i>CreateOptions</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548418">IoCreateFile</a> routine.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileNameInformation</b></p>
</td>
<td>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a> structure. The structure can contain the file's full path or only a portion of it. The caller can query this information as long as the file is open, without any particular requirements for <i>DesiredAccess</i>.</p>
<p>For more information about the file-name syntax, see the Remarks section later in this topic.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileNetworkOpenInformation</b></p>
</td>
<td>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545822">FILE_NETWORK_OPEN_INFORMATION</a> structure. The caller must have opened the file with the FILE_READ_ATTRIBUTES flag specified in the <i>DesiredAccess</i> parameter.</p>
</td>
</tr>
<tr>
<td>
<p><b>FilePositionInformation</b></p>
</td>
<td>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545848">FILE_POSITION_INFORMATION</a> structure. The caller must have opened the file with the <i>DesiredAccess</i> FILE_READ_DATA or FILE_WRITE_DATA flag specified in the <i>DesiredAccess</i> parameter, and with the FILE_SYNCHRONOUS_IO_ALERT or FILE_SYNCHRONOUS_IO_NONALERT flag specified in the <i>CreateOptions </i>parameter.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileStandardInformation</b></p>
</td>
<td>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545855">FILE_STANDARD_INFORMATION</a> structure. The caller can query this information as long as the file is open, without any particular requirements for <i>DesiredAccess</i>.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileIsRemoteDeviceInformation</b></p>
</td>
<td>
<p>A <a href="..\wdm\ns-wdm--file-is-remote-device-information.md">FILE_IS_REMOTE_DEVICE_INFORMATION</a> structure. The caller can query this information as  long as the file is open, without any particular requirements for <i>DesiredAccess</i>.                         </p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>ZwQueryInformationFile </b>returns STATUS_SUCCESS or an appropriate NTSTATUS error code.</p>

## -remarks
<p><b>ZwQueryInformationFile</b> returns information about the specified file object. Note that it returns zero in any member of a <b>FILE_<i>XXX</i>_INFORMATION</b> structure that is not supported by a particular device or file system.</p>

<p>When <i>FileInformationClass</i> = <b>FileNameInformation</b>, the file name is returned in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a> structure. The precise syntax of the file name depends on a number of factors:</p>

<p>If you opened the file by submitting a full path to <a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>, <b>ZwQueryInformationFile</b> returns that full path.</p>

<p>If the <b>ObjectAttributes-&gt;RootDirectory</b> handle was opened by name in a call to <b>ZwCreateFile</b>, and subsequently the file was opened by <b>ZwCreateFile</b> relative to this root-directory handle, <b>ZwQueryInformationFile</b> returns the full path.</p>

<p>If the <b>ObjectAttributes-&gt;RootDirectory</b> handle was opened by file ID (using the FILE_OPEN_BY_FILE_ID flag) in a call to <b>ZwCreateFile</b>, and subsequently the file was opened by <b>ZwCreateFile</b> relative to this root-directory handle, <b>ZwQueryInformationFile</b> returns the relative path. </p>

<p>However, if the user has <b>SeChangeNotifyPrivilege</b> (described in the Microsoft Windows SDK documentation), <b>ZwQueryInformationFile</b> returns the full path in all cases.</p>

<p>If only the relative path is returned, the file name string will not begin with a backslash.</p>

<p>If the full path and file name are returned, the string will begin with a single backslash, regardless of its location. Thus the file C:\dir1\dir2\filename.ext will appear as \dir1\dir2\filename.ext, while the file \\server\share\dir1\dir2\filename.ext will appear as \server\share\dir1\dir2\filename.ext.</p>

<p>If <b>ZwQueryInformationFile</b> fails because of a buffer overflow, drivers that implement <b>FileNameInformation</b> should return as many WCHAR characters of the file name as will fit in the buffer and specify the full length that is required in the <i>FileNameLength</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a> structure. You should reissue the query by using the file name length so that you can retrieve the full file name. Drivers that do not follow this pattern might require a gradual increase in length until they retrieve the full file name. For more information about working with files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565384">Using Files in a Driver</a>.</p>

<p>Callers of <b>ZwQueryInformationFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p><b>ZwQueryInformationFile</b> returns information about the specified file object. Note that it returns zero in any member of a <b>FILE_<i>XXX</i>_INFORMATION</b> structure that is not supported by a particular device or file system.</p>

<p>When <i>FileInformationClass</i> = <b>FileNameInformation</b>, the file name is returned in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a> structure. The precise syntax of the file name depends on a number of factors:</p>

<p>If you opened the file by submitting a full path to <a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>, <b>ZwQueryInformationFile</b> returns that full path.</p>

<p>If the <b>ObjectAttributes-&gt;RootDirectory</b> handle was opened by name in a call to <b>ZwCreateFile</b>, and subsequently the file was opened by <b>ZwCreateFile</b> relative to this root-directory handle, <b>ZwQueryInformationFile</b> returns the full path.</p>

<p>If the <b>ObjectAttributes-&gt;RootDirectory</b> handle was opened by file ID (using the FILE_OPEN_BY_FILE_ID flag) in a call to <b>ZwCreateFile</b>, and subsequently the file was opened by <b>ZwCreateFile</b> relative to this root-directory handle, <b>ZwQueryInformationFile</b> returns the relative path. </p>

<p>However, if the user has <b>SeChangeNotifyPrivilege</b> (described in the Microsoft Windows SDK documentation), <b>ZwQueryInformationFile</b> returns the full path in all cases.</p>

<p>If only the relative path is returned, the file name string will not begin with a backslash.</p>

<p>If the full path and file name are returned, the string will begin with a single backslash, regardless of its location. Thus the file C:\dir1\dir2\filename.ext will appear as \dir1\dir2\filename.ext, while the file \\server\share\dir1\dir2\filename.ext will appear as \server\share\dir1\dir2\filename.ext.</p>

<p>If <b>ZwQueryInformationFile</b> fails because of a buffer overflow, drivers that implement <b>FileNameInformation</b> should return as many WCHAR characters of the file name as will fit in the buffer and specify the full length that is required in the <i>FileNameLength</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a> structure. You should reissue the query by using the file name length so that you can retrieve the full file name. Drivers that do not follow this pattern might require a gradual increase in length until they retrieve the full file name. For more information about working with files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565384">Using Files in a Driver</a>.</p>

<p>Callers of <b>ZwQueryInformationFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545733">FILE_ACCESS_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545740">FILE_ALIGNMENT_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545743">FILE_ALL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545750">FILE_ATTRIBUTE_TAG_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545762">FILE_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545773">FILE_EA_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540318">FILE_INTERNAL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545802">FILE_IO_PRIORITY_HINT_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--file-is-remote-device-information.md">FILE_IS_REMOTE_DEVICE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545809">FILE_MODE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545817">FILE_NAME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545822">FILE_NETWORK_OPEN_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545848">FILE_POSITION_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545855">FILE_STANDARD_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwQueryInformationFile routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
