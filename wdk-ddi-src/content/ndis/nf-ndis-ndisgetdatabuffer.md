---
UID: NF.ndis.NdisGetDataBuffer
title: NdisGetDataBuffer function
author: windows-driver-content
description: Call the NdisGetDataBuffer function to gain access to a contiguous block of data from a NET_BUFFER structure.
old-location: netvista\ndisgetdatabuffer.htm
old-project: netvista
ms.assetid: 784d4c32-a517-4219-8e22-a998e0e66d69
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NdisGetDataBuffer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisGetDataBuffer
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_NetBuffer_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
---

# NdisGetDataBuffer function



## -description
Call the 
  <b>NdisGetDataBuffer</b> function to gain access to a contiguous block of data from a 
  <a href="netvista.net_buffer">NET_BUFFER</a> structure.


## -syntax

````
PVOID NdisGetDataBuffer(
  _In_     PNET_BUFFER NetBuffer,
  _In_     ULONG       BytesNeeded,
  _In_opt_ PVOID       Storage,
  _In_     UINT        AlignMultiple,
  _In_     UINT        AlignOffset
);
````


## -parameters

### -param NetBuffer [in]

A pointer to a NET_BUFFER structure.

### -param BytesNeeded [in]

The number of contiguous bytes of data requested.

### -param Storage [in, optional]

A pointer to a buffer, or <b>NULL</b> if no buffer is provided by the caller. The buffer must be greater
     than or equal in size to the number of bytes specified in 
     <i>BytesNeeded</i> . If this value is non-<b>NULL</b>, and the data requested is not contiguous, NDIS copies the
     requested data to the area indicated by 
     <i>Storage</i> .

### -param AlignMultiple [in]

The alignment multiple expressed in power of two. For example, 2, 4, 8, 16, and so forth. If 
     <i>AlignMultiple</i> is 1, then there is no alignment requirement.

### -param AlignOffset [in]

The offset, in bytes, from the alignment multiple.

## -returns
<b>NdisGetDataBuffer</b> returns a pointer to the start of the contiguous data or it returns <b>NULL</b>.

If the 
      <b>DataLength</b> member of the 
      <a href="netvista.net_buffer_data">NET_BUFFER_DATA</a> structure in the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure that the <i>NetBuffer</i>
      parameter points to is less than the value in the 
      <i>BytesNeeded</i> parameter, the return value is <b>NULL</b>.

If the requested data in the buffer is contiguous, the return value is a pointer to a location that
      NDIS provides. If the data is not contiguous, NDIS uses the 
      <i>Storage</i> parameter as follows:

The return value can also be <b>NULL</b> due to a low resource condition where a data buffer cannot be mapped. This may occur even if the data is contiguous or the <i>Storage</i> parameter is non-<b>NULL</b>.

## -remarks
Call this function to get a pointer to a network data header contained in the 
    <a href="netvista.net_buffer">NET_BUFFER</a> structure. You can easily parse the
    header stored in the contiguous data block that this function returns.

The requested alignment requirement is expressed as a power-of-two multiple plus an offset. For
    example, if 
    <i>AlignMultiple</i> is 4 and 
    <i>AlignOffset</i> is 3 then the data address should be a multiple of 4 plus 3. If necessary, NDIS will
    allocate memory to satisfy the alignment requirement.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Supported in NDIS 6.0 and later.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= DISPATCH_LEVEL
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules
</th>
<td width="70%">
<a href="devtest.ndis_irql_netbuffer_function">Irql_NetBuffer_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.net_buffer">NET_BUFFER</a>
</dt>
<dt>
<a href="netvista.net_buffer_data">NET_BUFFER_DATA</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisGetDataBuffer function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
