---
UID: NS.NTIFS._FILE_LEVEL_TRIM_OUTPUT
title: _FILE_LEVEL_TRIM_OUTPUT
author: windows-driver-content
description: The FILE_LEVEL_TRIM_OUTPUT structure contains the results of a trim operation performed by an FSCTL_FILE_LEVEL_TRIM request.
old-location: ifsk\file_level_trim_output.htm
old-project: ifsk
ms.assetid: 28CCE967-E752-4E0E-94D9-3A4243266684
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: _FILE_LEVEL_TRIM_OUTPUT, *PFILE_LEVEL_TRIM_OUTPUT, FILE_LEVEL_TRIM_OUTPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_LEVEL_TRIM_RANGE_OUTPUT
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
---

# _FILE_LEVEL_TRIM_OUTPUT structure



## -description
The <b>FILE_LEVEL_TRIM_OUTPUT</b> structure contains the results of a trim operation performed by an <a href="ifsk.fsctl_file_level_trim">FSCTL_FILE_LEVEL_TRIM</a> request.



## -syntax

````
typedef struct _FILE_LEVEL_TRIM_OUTPUT {
  ULONG NumRangesProcessed;
} FILE_LEVEL_TRIM_RANGE_OUTPUT, *PFILE_LEVEL_TRIM_RANGE_OUTPUT;
````


## -struct-fields

### -field NumRangesProcessed

The number or trim ranges processed.


## -remarks
This structure is optionally included as the output buffer for an <a href="ifsk.fsctl_file_level_trim">FSCTL_FILE_LEVEL_TRIM</a> request. <b>NumRangesProcessed</b> indicates how many ranges of the in the array given in <a href="ifsk.file_level_trim">FILE_LEVEL_TRIM</a> were processed.

All trim ranges in the array in <a href="ifsk.file_level_trim">FILE_LEVEL_TRIM</a> were successfully processed if  <b>NumRangesProcessed</b> is equivalent to the <b>NumRanges</b> member of <b>FILE_LEVEL_TRIM</b>. Otherwise, the value in <b>NumRangesProcessed</b> is the starting index of the trim ranges that were not processed.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows 8 and later versions of Windows.

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
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fsctl_file_level_trim">FSCTL_FILE_LEVEL_TRIM</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_LEVEL_TRIM_OUTPUT structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

