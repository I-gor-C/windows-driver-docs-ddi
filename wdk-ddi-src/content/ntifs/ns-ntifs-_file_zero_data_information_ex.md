---
UID: NS.NTIFS._FILE_ZERO_DATA_INFORMATION_EX
title: _FILE_ZERO_DATA_INFORMATION_EX
author: windows-driver-content
description: Contains a range of a file to set to zeros.
old-location: ifsk\file_zero_data_information_ex.htm
old-project: ifsk
ms.assetid: 429C644C-C784-4C0E-96C3-EC82698F6624
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _FILE_ZERO_DATA_INFORMATION_EX, PFILE_ZERO_DATA_INFORMATION_EX, *PFILE_ZERO_DATA_INFORMATION_EX, FILE_ZERO_DATA_INFORMATION_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_ZERO_DATA_INFORMATION_EX
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

# _FILE_ZERO_DATA_INFORMATION_EX structure



## -description
Contains a range of a file to set to zeros. This structure is used by the 
<a href="ifsk.fsctl_set_zero_data">FSCTL_SET_ZERO_DATA</a> control code. It's similar to <a href="ifsk.file_zero_data_information">FILE_ZERO_DATA_INFORMATION</a>, but contains an additional <b>Flags</b> member. 



## -syntax

````
typedef struct _FILE_ZERO_DATA_INFORMATION_EX {
  LARGE_INTEGER FileOffset;
  LARGE_INTEGER BeyondFinalZero;
  ULONG         Flags;
} FILE_ZERO_DATA_INFORMATION_EX, *PFILE_ZERO_DATA_INFORMATION_EX;
````


## -struct-fields

### -field FileOffset

The file offset of the start of the range to set to zeros, in bytes.


### -field BeyondFinalZero

The byte offset of the first byte beyond the last zeroed byte.


### -field Flags

The following flags are supported:

<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td><b>FILE_ZERO_DATA_INFORMATION_FLAG_PRESERVE_CACHED_DATA</b></td>
<td>Indicates not to purge the contents of the cache corresponding to this range of the file. Only drivers can set this flag.</td>
</tr>
</table>
 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

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
<a href="ifsk.fltfscontrolfile">FltFsControlFile</a>
</dt>
<dt>
<a href="ifsk.fsctl_set_zero_data">FSCTL_SET_ZERO_DATA</a>
</dt>
<dt>
<a href="ifsk.file_zero_data_information">FILE_ZERO_DATA_INFORMATION</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_ZERO_DATA_INFORMATION_EX structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

