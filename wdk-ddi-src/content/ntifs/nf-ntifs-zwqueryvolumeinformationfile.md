---
UID: NF.ntifs.ZwQueryVolumeInformationFile
title: ZwQueryVolumeInformationFile
author: windows-driver-content
description: The ZwQueryVolumeInformationFile routine retrieves information about the volume associated with a given file, directory, storage device, or volume.
old-location: kernel\zwqueryvolumeinformationfile.htm
old-project: kernel
ms.assetid: f83b7171-e250-4c2c-b3cc-2924f58e406e
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ZwQueryVolumeInformationFile
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
req.alt-api: ZwQueryVolumeInformationFile,NtQueryVolumeInformationFile
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

# ZwQueryVolumeInformationFile function



## -description
<p>The <b>ZwQueryVolumeInformationFile</b> routine retrieves information about the volume associated with a given file, directory, storage device, or volume.</p>


## -syntax

````
NTSTATUS ZwQueryVolumeInformationFile(
  _In_  HANDLE               FileHandle,
  _Out_ PIO_STATUS_BLOCK     IoStatusBlock,
  _Out_ PVOID                FsInformation,
  _In_  ULONG                Length,
  _In_  FS_INFORMATION_CLASS FsInformationClass
);
````


## -parameters
<dl>

### -param <i>FileHandle</i> [in]

<dd>
<p>A handle to a file object returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567011">ZwOpenFile</a> for an open file, directory, storage device, or volume for which volume information is being requested.</p>
</dd>

### -param <i>IoStatusBlock</i> [out]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure that receives the final completion status and information about the query operation. For successful calls that return data, the number of bytes written to the <i>FsInformation</i> buffer is returned in the structure's <b>Information</b> member.</p>
</dd>

### -param <i>FsInformation</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer that receives the desired information about the volume. The structure of the information returned in the buffer is defined by the <i>FsInformationClass</i> parameter.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Size in bytes of the buffer pointed to by <i>FsInformation</i>. The caller should set this parameter according to the given <i>FsInformationClass</i>.</p>
</dd>

### -param <i>FsInformationClass</i> [in]

<dd>
<p>Type of information to be returned about the volume. Set this member to one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/hh439282">FS_INFORMATION_CLASS</a> enumeration values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>FileFsAttributeInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540251">FILE_FS_ATTRIBUTE_INFORMATION</a> structure containing attribute information about the file system responsible for the volume.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileFsControlInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540258">FILE_FS_CONTROL_INFORMATION</a> structure containing file system control information about the volume.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileFsDeviceInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545788">FILE_FS_DEVICE_INFORMATION</a> structure containing device information for the volume.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileFsDriverPathInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540262">FILE_FS_DRIVER_PATH_INFORMATION</a> structure containing information about whether a specified driver is in the I/O path for the volume. The caller must store the name of the driver into the <b>FILE_FS_DRIVER_PATH_INFORMATION</b> structure before calling <b>ZwQueryVolumeInformationFile</b>.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileFsFullSizeInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540267">FILE_FS_FULL_SIZE_INFORMATION</a> structure containing information about the total amount of space available on the volume.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileFsObjectIdInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540274">FILE_FS_OBJECTID_INFORMATION</a> structure containing file system-specific object ID information for the volume. Note that this is not the same as the (GUID-based) unique volume name assigned by the operating system.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileFsSizeInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540282">FILE_FS_SIZE_INFORMATION</a> structure containing information about the amount of space on the volume that is available to the user associated with the calling thread.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileFsVolumeInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540287">FILE_FS_VOLUME_INFORMATION</a> containing information about the volume such as the volume label, serial number, and creation time.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileFsSectorSizeInformation</b></p>
</td>
<td>
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406395">FILE_FS_SECTOR_SIZE_INFORMATION</a> structure that contains information about the physical and logical sector sizes of a volume.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>ZwQueryVolumeInformationFile</b> returns STATUS_SUCCESS or an appropriate error status.</p>

## -remarks
<p><b>ZwQueryVolumeInformationFile</b> retrieves information about the volume associated with a given file, directory, storage device, or volume.</p>

<p>If the <i>FileHandle</i> represents a direct device open, only <i>FileFsDeviceInformation</i> can be specified as the value of <i>FsInformationClass</i>.</p>

<p><b>ZwQueryVolumeInformationFile</b> returns zero in any member of a <b>FILE_<i>XXX</i>_INFORMATION</b> structure that is not supported by the file system.</p>

<p>For information about other file information query routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545843">File Objects</a>.</p>

<p>Minifilters should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff543446">FltQueryVolumeInformationFile</a> instead of <b>ZwQueryVolumeInformationFile</b>.</p>

<p>Callers of <b>ZwQueryVolumeInformationFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p><b>ZwQueryVolumeInformationFile</b> retrieves information about the volume associated with a given file, directory, storage device, or volume.</p>

<p>If the <i>FileHandle</i> represents a direct device open, only <i>FileFsDeviceInformation</i> can be specified as the value of <i>FsInformationClass</i>.</p>

<p><b>ZwQueryVolumeInformationFile</b> returns zero in any member of a <b>FILE_<i>XXX</i>_INFORMATION</b> structure that is not supported by the file system.</p>

<p>For information about other file information query routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545843">File Objects</a>.</p>

<p>Minifilters should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff543446">FltQueryVolumeInformationFile</a> instead of <b>ZwQueryVolumeInformationFile</b>.</p>

<p>Callers of <b>ZwQueryVolumeInformationFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540251">FILE_FS_ATTRIBUTE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540258">FILE_FS_CONTROL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545788">FILE_FS_DEVICE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540262">FILE_FS_DRIVER_PATH_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540267">FILE_FS_FULL_SIZE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540274">FILE_FS_OBJECTID_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540282">FILE_FS_SIZE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540287">FILE_FS_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543446">FltQueryVolumeInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549318">IRP_MJ_QUERY_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549415">IRP_MJ_SET_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567011">ZwOpenFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567047">ZwQueryDirectoryFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567112">ZwSetVolumeInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwQueryVolumeInformationFile routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
