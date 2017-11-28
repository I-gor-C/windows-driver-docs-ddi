---
UID: NS.ntifs._FILE_ALLOCATION_INFORMATION
title: FILE_ALLOCATION_INFORMATION
author: windows-driver-content
description: The FILE_ALLOCATION_INFORMATION structure is used to set the allocation size for a file.
old-location: ifsk\file_allocation_information.htm
old-project: ifsk
ms.assetid: 52c62e52-3bf7-40eb-80ff-df14c50c86e1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILE_ALLOCATION_INFORMATION, FILE_ALLOCATION_INFORMATION, *PFILE_ALLOCATION_INFORMATION
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
req.alt-api: FILE_ALLOCATION_INFORMATION
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

# FILE_ALLOCATION_INFORMATION structure



## -description
<p>The FILE_ALLOCATION_INFORMATION structure is used to set the allocation size for a file. </p>


## -syntax

````
typedef struct _FILE_ALLOCATION_INFORMATION {
  LARGE_INTEGER AllocationSize;
} FILE_ALLOCATION_INFORMATION, *PFILE_ALLOCATION_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>AllocationSize</b>

<dd>
<p>File allocation size, in bytes. Usually this value is a multiple of the sector or cluster size of the underlying physical device. </p>
</dd>
</dl>

## -remarks
<p>This operation can be performed in either of the following ways: </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>, passing FileAllocationInformation as the value of <i>FileInformationClass</i> and passing a caller-allocated, FILE_ALLOCATION_INFORMATION-structured buffer as the value of <i>FileInformation</i>. The <i>FileHandle</i> parameter specifies the file whose allocation size is to be set. </p>

<p>Create an IRP with major function code IRP_MJ_SET_INFORMATION. </p>

<p>This operation is valid only for files. It is undefined for directories. </p>

<p>File system minifilters must use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a>, not <a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>, to set the allocation size for a file. </p>

<p>FILE_WRITE_DATA access is required to set this information. </p>

<p>A file's allocation size and end-of-file position are independent of each other, with the following exception: The end-of-file position must always be less than or equal to the allocation size. If the allocation size is set to a value that is less than the end-of-file position, the end-of-file position is automatically adjusted to match the allocation size. </p>

<p>The size of the <i>FileInformation</i> buffer passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a> must be &gt;= <b>sizeof</b>(FILE_ALLOCATION_INFORMATION). </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545780">FILE_END_OF_FILE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549366">IRP_MJ_SET_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_ALLOCATION_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
