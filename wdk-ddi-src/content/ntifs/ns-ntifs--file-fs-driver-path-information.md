---
UID: NS.ntifs._FILE_FS_DRIVER_PATH_INFORMATION
title: FILE_FS_DRIVER_PATH_INFORMATION
author: windows-driver-content
description: The FILE_FS_DRIVER_PATH_INFORMATION structure is used to query whether a given driver is in the I/O path for a file system volume.
old-location: ifsk\file_fs_driver_path_information.htm
old-project: ifsk
ms.assetid: 6149765b-cd2c-44f5-aa72-f4755e0b034c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILE_FS_DRIVER_PATH_INFORMATION, FILE_FS_DRIVER_PATH_INFORMATION, *PFILE_FS_DRIVER_PATH_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_FS_DRIVER_PATH_INFORMATION
req.alt-loc: ntifs.h
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
req.iface: 
---

# FILE_FS_DRIVER_PATH_INFORMATION structure



## -description
<p>The FILE_FS_DRIVER_PATH_INFORMATION structure is used to query whether a given driver is in the I/O path for a file system volume. </p>


## -syntax

````
typedef struct _FILE_FS_DRIVER_PATH_INFORMATION {
  BOOLEAN DriverInPath;
  ULONG   DriverNameLength;
  WCHAR   DriverName[1];
} FILE_FS_DRIVER_PATH_INFORMATION, *PFILE_FS_DRIVER_PATH_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>DriverInPath</b>

<dd>
<p>Receives <b>TRUE</b> if the driver is in the I/O path for the file system volume, <b>FALSE</b> otherwise. </p>
</dd>

### -field <b>DriverNameLength</b>

<dd>
<p>Caller-supplied length of the driver name string. </p>
</dd>

### -field <b>DriverName</b>

<dd>
<p>Caller-supplied Unicode string containing the name of the driver. </p>
</dd>
</dl>

## -remarks
<p>To perform this query, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567070">ZwQueryVolumeInformationFile</a>, passing FileFsDriverPathInformation as the value of <i>FileInformationClass</i> and passing a caller-allocated, FILE_FS_DRIVER_PATH_INFORMATION-structured buffer as the value of <i>FileInformation</i>. </p>

<p>This information is file system-independent. Thus the call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567070">ZwQueryVolumeInformationFile</a> does not cause an IRP to be sent to the file system. </p>

<p>No specific access rights are required to query this information. Thus this information is available as long as the volume is accessed through an open handle to the volume itself, or to a file or directory on the volume. </p>

<p>The size of the buffer passed in the <i>FileInformation</i> parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567070">ZwQueryVolumeInformationFile</a> must be at least <b>sizeof</b> (FILE_FS_DRIVER_PATH_INFORMATION). </p>

<p>This structure must be aligned on a LONGLONG (8-byte) boundary. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567070">ZwQueryVolumeInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_FS_DRIVER_PATH_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
