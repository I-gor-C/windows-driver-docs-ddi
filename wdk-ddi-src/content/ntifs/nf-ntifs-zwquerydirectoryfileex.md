---
UID: NF.ntifs.ZwQueryDirectoryFileEx
title: ZwQueryDirectoryFileEx function
author: windows-driver-content
description: The ZwQueryDirectoryFileEx routine returns information about files in the directory specified by the FileHandle parameter.
old-location: kernel\zwquerydirectoryfileex.htm
old-project: kernel
ms.assetid: A15062C0-E7F2-4C28-84DF-A3A96C83CE13
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: ZwQueryDirectoryFileEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwQueryDirectoryFileEx,NtQueryDirectoryFileEx
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: 
---

# ZwQueryDirectoryFileEx function



## -description
The <b>ZwQueryDirectoryFileEx</b> routine returns information about files in the directory
    specified by the <b>FileHandle</b> parameter.


## -syntax

````
NTSTATUS ZwQueryDirectoryFileEx(
  _In_     HANDLE                 FileHandle,
  _In_opt_ HANDLE                 Event,
  _In_opt_ PIO_APC_ROUTINE        ApcRoutine,
  _In_opt_ PVOID                  ApcContext,
  _Out_    PIO_STATUS_BLOCK       IoStatusBlock,
  _Out_    PVOID                  FileInformation,
  _In_     ULONG                  Length,
  _In_     FILE_INFORMATION_CLASS FileInformationClass,
  _In_     ULONG                  QueryFlags,
  _In_opt_ PUNICODE_STRING        FileName
);
````


## -parameters

### -param FileHandle [in]

A handle returned by <a href="kernel.zwcreatefile">ZwCreateFile</a> or <a href="kernel.zwopenfile">ZwOpenFile</a> for the file object that represents the directory for which information is being requested. The file object must have been opened for asynchronous I/O if the caller specifies a non-<b>NULL</b> value for <i>Event</i> or <i>ApcRoutine</i>.

### -param Event [in, optional]

An optional handle for a caller-created event. If this parameter is supplied, the caller will be put into a wait state until the requested operation is completed and the given event is set to the Signaled state. This parameter is optional and can be <b>NULL</b>. It must be <b>NULL</b> if the caller will wait for the <i>FileHandle</i> to be set to the Signaled state.

### -param ApcRoutine [in, optional]

An address of an optional, caller-supplied Asynchronous Procedure Call (APC) routine to be called when the requested operation completes. This parameter is optional and can be <b>NULL</b>. If there is an I/O completion object associated with the file object, this parameter must be <b>NULL</b>.

### -param ApcContext [in, optional]

An optional pointer to a caller-determined context area if the caller supplies an APC or if an I/O completion object is associated with the file object. When the operation completes, this context is passed to the APC, if one was specified, or is included as part of the completion message that the I/O Manager posts to the associated I/O completion object. 
This parameter is optional and can be <b>NULL</b>. It must be <b>NULL</b> if <i>ApcRoutine</i> is <b>NULL</b> and there is no I/O completion object associated with the file object.

### -param IoStatusBlock [out]

A pointer to an <a href="kernel.io_status_block">IO_STATUS_BLOCK</a> structure that receives the final completion status and information about the operation. For successful calls that return data, the number of bytes written to the <i>FileInformation</i> buffer is returned in the structure's <b>Information</b> member.

### -param FileInformation [out]

A pointer to a buffer that receives the desired information about the file. The structure of the information returned in the buffer is defined by the <i>FileInformationClass</i> parameter.

### -param Length [in]

The size, in bytes, of the buffer pointed to by <i>FileInformation</i>. The caller should set this parameter according to the given <i>FileInformationClass</i>.

### -param FileInformationClass [in]

Specifies the type of information to be returned about files in the directory. The legal values are as follows:
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<b>FileBothDirectoryInformation</b>
</td>
<td>
Return a <a href="ifsk.file_both_dir_information">FILE_BOTH_DIR_INFORMATION</a> structure for each file.
</td>
</tr>
<tr>
<td>
<b>FileDirectoryInformation</b>
</td>
<td>
Return a <a href="ifsk.file_directory_information">FILE_DIRECTORY_INFORMATION</a> structure for each file.
</td>
</tr>
<tr>
<td>
<b>FileFullDirectoryInformation</b>
</td>
<td>
Return a <a href="ifsk.file_full_dir_information">FILE_FULL_DIR_INFORMATION</a> structure for each file.
</td>
</tr>
<tr>
<td>
<b>FileIdBothDirectoryInformation</b>
</td>
<td>
Return a <a href="ifsk.file_id_both_dir_information">FILE_ID_BOTH_DIR_INFORMATION</a> structure for each file.
</td>
</tr>
<tr>
<td>
<b>FileIdFullDirectoryInformation</b>
</td>
<td>
Return a <a href="ifsk.file_id_full_dir_information">FILE_ID_FULL_DIR_INFORMATION</a> structure for each file.
</td>
</tr>
<tr>
<td>
<b>FileNamesInformation</b>
</td>
<td>
Return a <a href="ifsk.file_names_information">FILE_NAMES_INFORMATION</a> structure for each file.
</td>
</tr>
<tr>
<td>
<b>FileObjectIdInformation</b>
</td>
<td>
.Return a <a href="ifsk.file_objectid_information">FILE_OBJECTID_INFORMATION</a> structure for each file on the volume. This information class is valid only for the directory \$Extend\$ObjId:$O:$INDEX_ALLOCATION on NTFS volumes on Windows 2000 and later versions of Windows.
</td>
</tr>
<tr>
<td>
<b>FileReparsePointInformation</b>
</td>
<td>
Return a <a href="ifsk.file_reparse_point_information">FILE_REPARSE_POINT_INFORMATION</a> structure for each file on the volume. This information class is valid only for the directory \$Extend\$Reparse:$R:$INDEX_ALLOCATION on NTFS volumes on Windows 2000 and later versions of Windows.
</td>
</tr>
<tr>
<td>
<b>FileQuotaInformation</b>
</td>
<td>
Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540342">FILE_QUOTA_INFORMATION</a> structure for each file on the volume. This information class is valid only for the directory \$Extend\$Quota:$Q:$INDEX_ALLOCATION on NTFS volumes on Windows 2000 and later versions of Windows.
</td>
</tr>
<tr>
<td>
<b>FileIdGlobalTxDirectoryInformation</b>
</td>
<td>
Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff728839">FILE_ID_GLOBAL_TX_DIR_INFORMATION</a> structure for each file.
</td>
</tr>
<tr>
<td>
<b>FileIdExtdDirectoryInformation</b>
</td>
<td>
Return a <a href="ifsk.FILE_ID_EXTD_DIR_INFORMATION">FILE_ID_EXTD_DIR_INFORMATION</a> structure for each file.
</td>
</tr>
<tr>
<td>
<b>FileIdExtdBothDirectoryInformation</b>
</td>
<td>
Return a <a href="ifsk.FILE_ID_EXTD_BOTH_DIR_INFORMATION ">FILE_ID_EXTD_BOTH_DIR_INFORMATION </a> structure for each file.
</td>
</tr>
</table>
 

### -param QueryFlags [in]

 One or more of the flags contained in SL_QUERY_DIRECTORY_MASK.

### -param FileName [in, optional]

An optional pointer to a caller-allocated Unicode string containing the name of a file (or multiple files, if wildcards are used) within the directory specified by <i>FileHandle</i>. This parameter is optional and can be <b>NULL</b>. 
If <i>FileName</i> is not <b>NULL</b>, only files whose names match the <i>FileName</i> string are included in the directory scan. If <i>FileName</i> is <b>NULL</b>, all files are included. 
The <i>FileName</i> is used as a search expression and is captured on the very first call to <b>ZwQueryDirectoryFile</b> for a given handle. Subsequent calls to <b>ZwQueryDirectoryFile</b> will use the search expression set in the first call. The <i>FileName</i> parameter passed to subsequent calls will be ignored. 

## -returns
The <b>ZwQueryDirectoryFileEx</b>routine returns <b>STATUS_SUCCESS</b>  if the query operation was properly queued
    to the I/O system.  Once the operation completes, the status of the query
    can be determined by examining the Status field of the I/O status block.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.file_both_dir_information">FILE_BOTH_DIR_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.file_directory_information">FILE_DIRECTORY_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.file_full_dir_information">FILE_FULL_DIR_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.file_id_both_dir_information">FILE_ID_BOTH_DIR_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.file_id_full_dir_information">FILE_ID_FULL_DIR_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.file_names_information">FILE_NAMES_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.file_objectid_information">FILE_OBJECTID_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.file_reparse_point_information">FILE_REPARSE_POINT_INFORMATION</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="kernel.zwcreatefile">ZwCreateFile</a>
</dt>
<dt>
<a href="kernel.zwopenfile">ZwOpenFile</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwQueryDirectoryFileEx routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
