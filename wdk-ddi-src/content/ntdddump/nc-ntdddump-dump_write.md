---
UID: NC.ntdddump.DUMP_WRITE
title: DUMP_WRITE
author: windows-driver-content
description: The Dump_Write callback routine is called before the write to the dump port driver. The filter driver can access the dump data at this time.
old-location: storage\dump_write.htm
old-project: storage
ms.assetid: c7eda6a7-a1ce-43a3-b0e4-41f5afc61be6
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _VERIFY_INFORMATION, *PVERIFY_INFORMATION, VERIFY_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ntdddump.h
req.include-header: Ntdddump.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows Vista and Windows Server 2008.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dump_Write
req.alt-loc: ntdddump.h
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

# DUMP_WRITE callback



## -description
The <i>Dump_Write</i> callback routine is called before the write to the dump port driver. The filter driver can access the dump data at this time.



## -prototype

````
PDUMP_WRITE Dump_Write;

NTSTATUS Dump_Write(
  _In_    PFILTER_EXTENSION FilterExtension,
  _Inout_ PLARGE_INTEGER    DiskByteOffset,
  _Inout_ PMDL              Mdl
)
{ ... }
````


## -parameters

### -param FilterExtension [in]

A pointer to a <a href="storage.filter_extension">FILTER_EXTENSION</a> structure.


### -param DiskByteOffset [in, out]

The value, in bytes, relative to the destination partition for the crash dump or hibernation. Filter drivers should not modify this field.


### -param Mdl [in, out]

A pointer to an <a href="kernel.mdl">MDL</a> structure that describes the data buffer. If the <b>MDL</b> is modified, the size of the write operation cannot change.


## -returns
If the routine succeeds, it must return STATUS_SUCCESS. Otherwise, it must return one of the error status values defined in <i>Ntstatus.h</i>.


## -remarks
Filter drivers can read the data that needs to be written. However, filter drivers cannot write to the buffer, as this could change the contents of the code or data that is being used by the crash dump process. Also, filter drivers are not allowed to change the size of the data.

To safely modify the data for the dump write, a filter driver should allocate a secondary buffer. The buffer's size will be the value of the <b>MaxPagesPerWrite</b> member of <a href="storage.filter_initialization_data">FILTER_INITIALIZATION_DATA</a> multiplied by <b>PAGE_SIZE</b>. The data for the current buffer described by <i>Mdl</i> is copied into the secondary buffer and processed. After the filter is finished handling the dump data in the secondary buffer, the  <a href="kernel.mdl">MDL</a> pointed to by <i>Mdl</i> is updated with the address of the secondary buffer. The starting address of the secondary buffer set in the <b>MDL</b> must be page aligned.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows Vista and Windows Server 2008.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntdddump.h (include Ntdddump.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntdddump\nc-ntdddump-dump_read.md">Dump_Read</a>
</dt>
<dt>
<a href="storage.filter_extension">FILTER_EXTENSION</a>
</dt>
<dt>
<a href="storage.filter_initialization_data">FILTER_INITIALIZATION_DATA</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20Dump_Write routine%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

