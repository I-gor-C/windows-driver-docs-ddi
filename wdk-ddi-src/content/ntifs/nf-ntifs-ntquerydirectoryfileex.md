---
UID: NF.ntifs.NtQueryDirectoryFileEx
title: NtQueryDirectoryFileEx
author: windows-driver-content
description: The ZwQueryDirectoryFileEx routine returns information about files in the directory specified by the FileHandle parameter.
old-location: kernel\zwquerydirectoryfileex.htm
old-project: kernel
ms.assetid: A15062C0-E7F2-4C28-84DF-A3A96C83CE13
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NtQueryDirectoryFileEx
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
req.iface: 
---

# NtQueryDirectoryFileEx function



## -description
<p>The <b>ZwQueryDirectoryFileEx</b> routine returns information about files in the directory
    specified by the <b>FileHandle</b> parameter.</p>


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
<p>An address of an optional, caller-supplied Asynchronous Procedure Call (APC) routine to be called when the requested operation completes. This parameter is optional and can be <b>NULL</b>. If there is an I/O completion object associated with the file object, this parameter must be <b>NULL</b>.</p>
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
<p>Specifies the type of information to be returned about files in the directory. The legal values are as follows:</p>
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
<p>.Return a <a href="..\ntifs\ns-ntifs--file-objectid-information.md">FILE_OBJECTID_INFORMATION</a> structure for each file on the volume. This information class is valid only for the directory \$Extend\$ObjId:$O:$INDEX_ALLOCATION on NTFS volumes on Windows 2000 and later versions of Windows.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileReparsePointInformation</b></p>
</td>
<td>
<p>Return a <a href="..\ntifs\ns-ntifs--file-reparse-point-information.md">FILE_REPARSE_POINT_INFORMATION</a> structure for each file on the volume. This information class is valid only for the directory \$Extend\$Reparse:$R:$INDEX_ALLOCATION on NTFS volumes on Windows 2000 and later versions of Windows.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileQuotaInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540342">FILE_QUOTA_INFORMATION</a> structure for each file on the volume. This information class is valid only for the directory \$Extend\$Quota:$Q:$INDEX_ALLOCATION on NTFS volumes on Windows 2000 and later versions of Windows.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileIdGlobalTxDirectoryInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff728839">FILE_ID_GLOBAL_TX_DIR_INFORMATION</a> structure for each file.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileIdExtdDirectoryInformation</b></p>
</td>
<td>
<p>Return a <a href="ifsk.FILE_ID_EXTD_DIR_INFORMATION">FILE_ID_EXTD_DIR_INFORMATION</a> structure for each file.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileIdExtdBothDirectoryInformation</b></p>
</td>
<td>
<p>Return a <a href="ifsk.FILE_ID_EXTD_BOTH_DIR_INFORMATION ">FILE_ID_EXTD_BOTH_DIR_INFORMATION </a> structure for each file.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param QueryFlags [in]

<dd>
<p> One or more of the flags contained in SL_QUERY_DIRECTORY_MASK.</p>
</dd>

### -param FileName [in, optional]

<dd>
<p>An optional pointer to a caller-allocated Unicode string containing the name of a file (or multiple files, if wildcards are used) within the directory specified by <i>FileHandle</i>. This parameter is optional and can be <b>NULL</b>. </p>
<p>If <i>FileName</i> is not <b>NULL</b>, only files whose names match the <i>FileName</i> string are included in the directory scan. If <i>FileName</i> is <b>NULL</b>, all files are included. </p>
<p>The <i>FileName</i> is used as a search expression and is captured on the very first call to <b>ZwQueryDirectoryFile</b> for a given handle. Subsequent calls to <b>ZwQueryDirectoryFile</b> will use the search expression set in the first call. The <i>FileName</i> parameter passed to subsequent calls will be ignored. </p>
</dd>
</dl>

## -returns
<p>The <b>ZwQueryDirectoryFileEx</b>routine returns <b>STATUS_SUCCESS</b>  if the query operation was properly queued
    to the I/O system.  Once the operation completes, the status of the query
    can be determined by examining the Status field of the I/O status block.</p>

## -remarks


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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwQueryDirectoryFileEx routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
