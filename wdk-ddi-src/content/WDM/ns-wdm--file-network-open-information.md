---
UID: NS.wdm._FILE_NETWORK_OPEN_INFORMATION
title: FILE_NETWORK_OPEN_INFORMATION
author: windows-driver-content
description: The FILE_NETWORK_OPEN_INFORMATION structure is used as an argument to ZwQueryInformationFile.
old-location: kernel\file_network_open_information.htm
ms.assetid: 742fa221-70c8-410a-a582-aedf28872ada
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_NETWORK_OPEN_INFORMATION
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: FILE_NETWORK_OPEN_INFORMATION, FILE_NETWORK_OPEN_INFORMATION, *PFILE_NETWORK_OPEN_INFORMATION
req.iface: 
req.product: Windows 10 or later.
---

# FILE_NETWORK_OPEN_INFORMATION structure



## -description
<p>The <b>FILE_NETWORK_OPEN_INFORMATION</b> structure is used as an argument to <a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a>. </p>


## -syntax

````
typedef struct _FILE_NETWORK_OPEN_INFORMATION {
  LARGE_INTEGER CreationTime;
  LARGE_INTEGER LastAccessTime;
  LARGE_INTEGER LastWriteTime;
  LARGE_INTEGER ChangeTime;
  LARGE_INTEGER AllocationSize;
  LARGE_INTEGER EndOfFile;
  ULONG         FileAttributes;
} FILE_NETWORK_OPEN_INFORMATION, *PFILE_NETWORK_OPEN_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>CreationTime</b>

<dd>
<p>Specifies the time that the file was created.</p>
</dd>

### -field <b>LastAccessTime</b>

<dd>
<p>Specifies the time that the file was last accessed.</p>
</dd>

### -field <b>LastWriteTime</b>

<dd>
<p>Specifies he time that the file was last written to.</p>
</dd>

### -field <b>ChangeTime</b>

<dd>
<p>Specifies the time that the file was last changed.</p>
</dd>

### -field <b>AllocationSize</b>

<dd>
<p>Specifies the file allocation size, in bytes. Usually, this value is a multiple of the sector or cluster size of the underlying physical device.</p>
</dd>

### -field <b>EndOfFile</b>

<dd>
<p>Specifies the absolute end-of-file position as a byte offset from the start of the file. <b>EndOfFile</b> specifies the byte offset to the end of the file. Because this value is zero-based, it actually refers to the first free byte in the file. In other words, <b>EndOfFile</b> is the offset to the byte immediately following the last valid byte in the file.</p>
</dd>

### -field <b>FileAttributes</b>

<dd>
<p>Specifies one or more FILE_ATTRIBUTE_<i>XXX</i> flags. For descriptions of these flags, see the documentation of the <b>GetFileAttributes</b> function in the Microsoft Windows SDK.</p>
</dd>
</dl>

## -remarks
<p>FILE_READ_ATTRIBUTES access to the file is required to query this information.</p>

<p>Time values <b>CreationTime</b>, <b>LastAccessTime</b>, <b>LastWriteTime</b>, and <b>ChangeTime</b> are expressed in absolute system time format. Absolute system time is the number of 100-nanosecond intervals since the start of the year 1601 in the Gregorian calendar.</p>

<p>This structure must be aligned on a LONGLONG (8-byte) boundary.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20FILE_NETWORK_OPEN_INFORMATION structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
