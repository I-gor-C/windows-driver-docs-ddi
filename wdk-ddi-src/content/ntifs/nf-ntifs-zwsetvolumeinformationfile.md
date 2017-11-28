---
UID: NF.ntifs.ZwSetVolumeInformationFile
title: ZwSetVolumeInformationFile
author: windows-driver-content
description: The ZwSetVolumeInformationFile routine modifies information about the volume associated with a given file, directory, storage device, or volume.
old-location: kernel\zwsetvolumeinformationfile.htm
old-project: kernel
ms.assetid: 6afc3e8b-0be0-4728-b00f-deea5e60d27e
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ZwSetVolumeInformationFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Server 2003 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwSetVolumeInformationFile,NtSetInformationFile
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# ZwSetVolumeInformationFile function



## -description
<p>The <b>ZwSetVolumeInformationFile</b> routine modifies information about the volume associated with a given file, directory, storage device, or volume. </p>


## -syntax

````
NTSTATUS ZwSetVolumeInformationFile(
  _In_  HANDLE               FileHandle,
  _Out_ PIO_STATUS_BLOCK     IoStatusBlock,
  _In_  PVOID                FsInformation,
  _In_  ULONG                Length,
  _In_  FS_INFORMATION_CLASS FsInformationClass
);
````


## -parameters
<dl>

### -param <i>FileHandle</i> [in]

<dd>
<p>Handle to a file object for an open file, directory, storage device, or volume whose volume information is to be modified. </p>
</dd>

### -param <i>IoStatusBlock</i> [out]

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure that receives the final completion status and information about the operation. </p>
</dd>

### -param <i>FsInformation</i> [in]

<dd>
<p>Pointer to a caller-allocated buffer containing the volume information to be modified. The structure of the information in this buffer depends on the value of <i>FsInformationClass</i>, as shown in the following table. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Size in bytes of the buffer pointed to by <i>FsInformation</i>. The caller should set this parameter according to the given <i>FsInformationClass</i>. </p>
</dd>

### -param <i>FsInformationClass</i> [in]

<dd>
<p>Type of volume information to be set. One of the following: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>FileFsControlInformation</b></p>
</td>
<td>
<p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff540258">FILE_FS_CONTROL_INFORMATION</a> for the volume. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileFsLabelInformation</b></p>
</td>
<td>
<p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff540271">FILE_FS_LABEL_INFORMATION</a> for the volume. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileFsObjectIdInformation</b></p>
</td>
<td>
<p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff540274">FILE_FS_OBJECTID_INFORMATION</a> for the volume. </p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>ZwSetVolumeInformationFile</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>An invalid value was specified for <i>Length</i>. This is an error code.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567112">ZwSetVolumeInformationFile</a> encountered a pool allocation failure. This is an error code.</p><dl>
<dt><b>STATUS_INVALID_INFO_CLASS</b></dt>
</dl><p>An invalid value was specified for <i>FsInformationClass</i>. This is an error code.</p>

<p> </p>

## -remarks
<p>To query volume information, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff567070">ZwQueryVolumeInformationFile</a>. </p>

<p>To change information about a file, call <b>ZwSetVolumeInformationFile</b>. </p>

<p>Minifilters should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a> instead of <b>ZwSetVolumeInformationFile</b>. </p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p>To query volume information, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff567070">ZwQueryVolumeInformationFile</a>. </p>

<p>To change information about a file, call <b>ZwSetVolumeInformationFile</b>. </p>

<p>Minifilters should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a> instead of <b>ZwSetVolumeInformationFile</b>. </p>

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
<p>Available in Windows Server 2003 and later versions of Windows.</p>
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
<p>PASSIVE_LEVEL</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540258">FILE_FS_CONTROL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540271">FILE_FS_LABEL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540274">FILE_FS_OBJECTID_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549415">IRP_MJ_SET_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567070">ZwQueryVolumeInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwSetVolumeInformationFile routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
