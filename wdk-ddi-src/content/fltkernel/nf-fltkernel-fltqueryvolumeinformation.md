---
UID: NF.fltkernel.FltQueryVolumeInformation
title: FltQueryVolumeInformation
author: windows-driver-content
description: The FltQueryVolumeInformation routine retrieves information about the volume that the given instance is attached to.
old-location: ifsk\fltqueryvolumeinformation.htm
old-project: ifsk
ms.assetid: 57b65e87-7f2d-44fc-84b9-e029c8075be3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltQueryVolumeInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available and supported in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP with Service Pack 2 (SP2), Windows Server 2003 SP1 and later  Windows operating systems. Not available or supported in Windows 2000 SP4 and earlier Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltQueryVolumeInformation
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FltQueryVolumeInformation function



## -description
<p>The <b>FltQueryVolumeInformation</b> routine retrieves information about the volume that the given instance is attached to. </p>


## -syntax

````
NTSTATUS FltQueryVolumeInformation(
  _In_  PFLT_INSTANCE        Instance,
  _Out_ PIO_STATUS_BLOCK     Iosb,
  _Out_ PVOID                FsInformation,
  _In_  ULONG                Length,
  _In_  FS_INFORMATION_CLASS FsInformationClass
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>An opaque instance pointer for a minifilter driver instance that is attached to the volume. </p>
</dd>

### -param <i>Iosb</i> [out]

<dd>
<p>A pointer to caller-allocated IO_STATUS_BLOCK structure that receives the final completion status and information about the query operation. For successful calls that return data, the number of bytes written to the <i>FsInformation</i> buffer is returned in the structure's <b>Information</b> member. </p>
</dd>

### -param <i>FsInformation</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer that receives the desired information about the volume. The structure of the information returned in the buffer is defined by the <i>FsInformationClass</i> parameter. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The size in bytes of the buffer that <i>FsInformation</i> points to. The caller should set this parameter according to the given <i>FsInformationClass</i>. For example, if the value of <i>FsInformationClass</i> is FileFsControlInformation, <i>Length</i> must be at least <b>sizeof</b>(FILE_FS_CONTROL_INFORMATION). </p>
</dd>

### -param <i>FsInformationClass</i> [in]

<dd>
<p>The type of information requested. One of the following value. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="FileFsAttributeInformation"></a><a id="filefsattributeinformation"></a><a id="FILEFSATTRIBUTEINFORMATION"></a><dl>

### -param <b>FileFsAttributeInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540251">FILE_FS_ATTRIBUTE_INFORMATION</a> structure containing attribute information about the file system responsible for the volume. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsControlInformation"></a><a id="filefscontrolinformation"></a><a id="FILEFSCONTROLINFORMATION"></a><dl>

### -param <b>FileFsControlInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540258">FILE_FS_CONTROL_INFORMATION</a> structure containing file system control information about the volume. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsDeviceInformation"></a><a id="filefsdeviceinformation"></a><a id="FILEFSDEVICEINFORMATION"></a><dl>

### -param <b>FileFsDeviceInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545788">FILE_FS_DEVICE_INFORMATION</a> structure containing device information for the volume. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsDriverPathInformation"></a><a id="filefsdriverpathinformation"></a><a id="FILEFSDRIVERPATHINFORMATION"></a><dl>

### -param <b>FileFsDriverPathInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540262">FILE_FS_DRIVER_PATH_INFORMATION</a> structure containing information about whether a specified driver is in the I/O path for the volume. The caller must store the name of the driver into the <b>FILE_FS_DRIVER_PATH_INFORMATION</b> structure before calling <b>FltQueryVolumeInformation</b>. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsFullSizeInformation"></a><a id="filefsfullsizeinformation"></a><a id="FILEFSFULLSIZEINFORMATION"></a><dl>

### -param <b>FileFsFullSizeInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540267">FILE_FS_FULL_SIZE_INFORMATION</a> structure containing information about the total amount of space available on the volume. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsObjectIdInformation"></a><a id="filefsobjectidinformation"></a><a id="FILEFSOBJECTIDINFORMATION"></a><dl>

### -param <b>FileFsObjectIdInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540274">FILE_FS_OBJECTID_INFORMATION</a> structure containing file system-specific object ID information for the volume. Be aware that this is not the same as the (GUID-based) unique volume name assigned by the operating system. <div class="alert"><b>Note</b>  This value is not valid for snapshot volumes.</div>
<div> </div>
</p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsSizeInformation"></a><a id="filefssizeinformation"></a><a id="FILEFSSIZEINFORMATION"></a><dl>

### -param <b>FileFsSizeInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540282">FILE_FS_SIZE_INFORMATION</a> structure containing information about the amount of space on the volume that is available to the user associated with the calling thread. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsVolumeInformation"></a><a id="filefsvolumeinformation"></a><a id="FILEFSVOLUMEINFORMATION"></a><dl>

### -param <b>FileFsVolumeInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540287">FILE_FS_VOLUME_INFORMATION</a> containing information about the volume such as the volume label, serial number, and creation time. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FileFsSectorSizeInformation"></a><a id="filefssectorsizeinformation"></a><a id="FILEFSSECTORSIZEINFORMATION"></a><dl>

### -param <b>FileFsSectorSizeInformation</b>

</dl>
</td>
<td width="60%">
<p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406395">FILE_FS_SECTOR_SIZE_INFORMATION</a> structure that contains information about the physical and logical sector sizes of a volume.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>The <b>FltQueryVolumeInformation</b> routine returns <b>STATUS_SUCCESS</b> or an appropriate <b>NTSTATUS</b> value such as one of the following: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a> encountered a pool allocation failure. This is an error code. </p><dl>
<dt><b>STATUS_INVALID_INFO_CLASS</b></dt>
</dl><p>An invalid value was specified for <i>FsInformationClass</i>. This is an error code. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>Instance</i> is attached to a network volume. <a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a> cannot be used to query network volume information. This is an error code. </p>

<p> </p>

## -remarks
<p>Fields in the FILE_<i>XXX</i>_INFORMATION structure that are not supported by the underlying file system are set to zero. </p>

<p>To change information about a volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544564">FltSetVolumeInformation</a>. </p>

<p>To get volume property information for the given volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543254">FltGetVolumeProperties</a>. </p>

<p>To get the volume name for a given volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543249">FltGetVolumeName</a>. </p>

<p>To get the volume GUID name for a given volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543230">FltGetVolumeGuidName</a>. </p>

<p>Fields in the FILE_<i>XXX</i>_INFORMATION structure that are not supported by the underlying file system are set to zero. </p>

<p>To change information about a volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544564">FltSetVolumeInformation</a>. </p>

<p>To get volume property information for the given volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543254">FltGetVolumeProperties</a>. </p>

<p>To get the volume name for a given volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543249">FltGetVolumeName</a>. </p>

<p>To get the volume GUID name for a given volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543230">FltGetVolumeGuidName</a>. </p>

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
<p>Available and supported in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP with Service Pack 2 (SP2), Windows Server 2003 SP1 and later  Windows operating systems. Not available or supported in Windows 2000 SP4 and earlier Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include FltKernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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
<dt><b>FILE_FS_SECTOR_SIZE_INFORMATION</b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540282">FILE_FS_SIZE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540287">FILE_FS_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543230">FltGetVolumeGuidName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543249">FltGetVolumeName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543254">FltGetVolumeProperties</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544564">FltSetVolumeInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltQueryVolumeInformation routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
