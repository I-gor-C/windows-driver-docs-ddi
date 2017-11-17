---
UID: NS.ntddk._FILE_DISPOSITION_INFORMATION
title: FILE_DISPOSITION_INFORMATION
author: windows-driver-content
description: The FILE_DISPOSITION_INFORMATION structure is used as an argument to the ZwSetInformationFile routine.
old-location: kernel\file_disposition_information.htm
ms.assetid: a13b5411-a0dd-4a54-98a8-419e2f0e95b8
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_DISPOSITION_INFORMATION
req.alt-loc: Ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: FILE_DISPOSITION_INFORMATION, FILE_DISPOSITION_INFORMATION, *PFILE_DISPOSITION_INFORMATION
req.iface: 
---

# FILE_DISPOSITION_INFORMATION structure



## -description
<p>The <b>FILE_DISPOSITION_INFORMATION</b> structure is used as an argument to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a> routine.</p>


## -syntax

````
typedef struct _FILE_DISPOSITION_INFORMATION {
  BOOLEAN DeleteFile;
} FILE_DISPOSITION_INFORMATION, *PFILE_DISPOSITION_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>DeleteFile</b>

<dd>
<p>Indicates whether the operating system file should delete the file when the file is closed. Set this member to <b>TRUE</b> to delete the file when it is closed. Otherwise, set to <b>FALSE</b>. Setting this member to <b>FALSE</b> has no effect if the handle was opened with FILE_FLAG_DELETE_ON_CLOSE.</p>
</dd>
</dl>

## -remarks
<p>The caller must have DELETE access to a given file in order to call <b>ZwSetInformationFile</b> with <b>DeleteFile</b> set to <b>TRUE</b> in this structure. Subsequently, the only legal operation by such a caller is to close the open file handle. </p>

<p>A file marked for deletion is not actually deleted until all open handles for the file object have been closed and the link count for the file is zero.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20FILE_DISPOSITION_INFORMATION structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
