---
UID: NS.storport._SRBEX_DATA_IO_INFO
title: SRBEX_DATA_IO_INFO
author: windows-driver-content
description: The SRBEX_DATA_IO_INFO structure contains additional information related to a read or write request in an extended SRB.
old-location: storage\srbex_data_io_info.htm
old-project: storage
ms.assetid: D4B99D6F-0A0C-49CE-A8E2-19C1A835EDA6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SRBEX_DATA_IO_INFO, SRBEX_DATA_IO_INFO, *PSRBEX_DATA_IO_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: storport.h
req.include-header: Storport.h, Srb.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SRBEX_DATA_IO_INFO
req.alt-loc: Storport.h
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
req.product: Windows 10 or later.
---

# SRBEX_DATA_IO_INFO structure



## -description
<p>The <b>SRBEX_DATA_IO_INFO</b> structure contains additional information related to a read or write request in an extended SRB.</p>


## -syntax

````
typedef struct _SRBEX_DATA_IO_INFO {
  SRBEXDATATYPE Type;
  ULONG         Length;
  ULONG         Flags;
  ULONG         Key;
  ULONG         RWLength;
  BOOLEAN       IsWriteRequest;
  UCHAR         CachePriority;
  UCHAR         Reserved[2];
  ULONG         Reserved1[3];
} SRBEX_DATA_IO_INFO, *PSRBEX_DATA_IO_INFO;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>Data type indicator for the bidirectional extended SRB data structure. Set to <b>SrbExDataTypeIoInfo</b>.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>Length of the data in this structure, in bytes, starting with the <b>Flags</b> member. Set to SRBEX_DATA_IO_INFO_LENGTH.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Flags set for handling the request. May be a combination of these values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="REQUEST_INFO_NO_CACHE_FLAG"></a><a id="request_info_no_cache_flag"></a><dl>

### -field <b>REQUEST_INFO_NO_CACHE_FLAG</b>

</dl>
</td>
<td width="60%">
<p>Non-cached writes are specified for this request.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="REQUEST_INFO_PAGING_IO_FLAG"></a><a id="request_info_paging_io_flag"></a><dl>

### -field <b>REQUEST_INFO_PAGING_IO_FLAG</b>

</dl>
</td>
<td width="60%">
<p>Paging IO is specified for this request.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="REQUEST_INFO_SEQUENTIAL_IO_FLAG"></a><a id="request_info_sequential_io_flag"></a><dl>

### -field <b>REQUEST_INFO_SEQUENTIAL_IO_FLAG</b>

</dl>
</td>
<td width="60%">
<p>Reads or writes are sequential.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="REQUEST_INFO_TEMPORARY_FLAG"></a><a id="request_info_temporary_flag"></a><dl>

### -field <b>REQUEST_INFO_TEMPORARY_FLAG</b>

</dl>
</td>
<td width="60%">
<p>The file for this request is temporary.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="REQUEST_INFO_WRITE_THROUGH_FLAG"></a><a id="request_info_write_through_flag"></a><dl>

### -field <b>REQUEST_INFO_WRITE_THROUGH_FLAG</b>

</dl>
</td>
<td width="60%">
<p>No system buffering for the request.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="REQUEST_INFO_HYBRID_WRITE_THROUGH_FLAG"></a><a id="request_info_hybrid_write_through_flag"></a><dl>

### -field <b>REQUEST_INFO_HYBRID_WRITE_THROUGH_FLAG</b>

</dl>
</td>
<td width="60%">
<p>Perform a hybrid cache write through to disk</p>
<p>This flag is available starting with Windows 8.1 Update.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="REQUEST_INFO_VALID_CACHEPRIORITY_FLAG"></a><a id="request_info_valid_cachepriority_flag"></a><dl>

### -field <b>REQUEST_INFO_VALID_CACHEPRIORITY_FLAG</b>

</dl>
</td>
<td width="60%">
<p>The hybrid cache priority level is valid for this I/O.</p>
<p>This flag is available starting with Windows 8.1 Update.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Key</b>

<dd>
<p>A tag value to identify a block of data transferred.</p>
</dd>

### -field <b>RWLength</b>

<dd>
<p>The length, in bytes of the data to transfer.</p>
</dd>

### -field <b>IsWriteRequest</b>

<dd>
<p>TRUE if the I/O operation in the SRB is a write request. Otherwise, FALSE; the I/O operation is a read request.</p>
</dd>

### -field <b>CachePriority</b>

<dd>
<p>Priority level for a hybrid cache read or write.</p>
<p>This member is valid starting with Windows 8.1 Update.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved. Set to 0.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>This member is reserved. Set to 0.</p>
<p>This member is present starting with Windows 8.1 Update.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h or Srb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\srb\ns-srb--storage-request-block.md">STORAGE_REQUEST_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SRBEX_DATA_IO_INFO structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
