---
UID: NF.ndis.NdisCopyFromNetBufferToNetBuffer
title: NdisCopyFromNetBufferToNetBuffer
author: windows-driver-content
description: Call the NdisCopyFromNetBufferToNetBuffer function to copy data from a source NET_BUFFER structure to a destination NET_BUFFER structure.
old-location: netvista\ndiscopyfromnetbuffertonetbuffer.htm
ms.assetid: b760e176-3ef7-4495-89c7-ec6b8bb3ed30
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisCopyFromNetBufferToNetBuffer
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
ms.keywords: NdisCopyFromNetBufferToNetBuffer
req.iface: 
---

# NdisCopyFromNetBufferToNetBuffer function



## -description
<p>Call the 
  <b>NdisCopyFromNetBufferToNetBuffer</b> function to copy data from a source 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure to a destination NET_BUFFER
  structure.</p>


## -syntax

````
NDIS_STATUS NdisCopyFromNetBufferToNetBuffer(
  _In_  PNET_BUFFER Destination,
  _In_  ULONG       DestinationOffset,
  _In_  ULONG       BytesToCopy,
  _In_  PNET_BUFFER Source,
  _In_  ULONG       SourceOffset,
  _Out_ PULONG      BytesCopied
);
````


## -parameters
<dl>

### -param <i>Destination</i> [in]

<dd>
<p>A pointer to a previously allocated destination NET_BUFFER structure.</p>
</dd>

### -param <i>DestinationOffset</i> [in]

<dd>
<p>The byte offset within the destination NET_BUFFER structure at which to begin writing the copied
     data. For more information about 
     <i>DestinationOffset</i>, see the following Remarks section.</p>
</dd>

### -param <i>BytesToCopy</i> [in]

<dd>
<p>The number of bytes to copy.</p>
</dd>

### -param <i>Source</i> [in]

<dd>
<p>A pointer to a previously allocated source NET_BUFFER structure.</p>
</dd>

### -param <i>SourceOffset</i> [in]

<dd>
<p>The byte offset within the source NET_BUFFER structure at which to begin copying the data. For
     more information about 
     <i>SourceOffset</i>, see the following Remarks section.</p>
</dd>

### -param <i>BytesCopied</i> [out]

<dd>
<p>A pointer to the caller-supplied variable in which this function returns the number of bytes
     actually copied. This number can be less than the value of 
     <i>BytesToCopy</i> if the source runs out of data or the destination runs out of space.</p>
</dd>
</dl>

## -returns
<p><b>NdisCopyFromNetBufferToNetBuffer</b> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The copy operation completed successfully.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>The copy operation failed because of insufficient resources.</p>

<p> </p>

## -remarks
<p>The caller of 
    <b>NdisCopyFromNetBufferToNetBuffer</b> allocates the destination 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure and possibly the source
    NET_BUFFER structure as well. The MDLs of the destination NET_BUFFER structure should have enough space
    to receive the data.</p>

<p>If the source NET_BUFFER structure runs out of data or the destination NET_BUFFER structure runs out
    of space before the specified number of bytes has been copied, the copy operation stops. In either case, 
    <b>NdisCopyFromNetBufferToNetBuffer</b> returns the number of bytes successfully copied from the source to
    the destination NET_BUFFER structure.</p>

<p>The caller must ensure that 
    <b>CurrentMdlOffset</b> and 
    <b>CurrentMdl</b> values are correct in the source and destination 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures. NDIS does not change the
    members in the destination NET_BUFFER. The caller must update the 
    <b>DataLength</b>, 
    <b>DataOffset</b>, and 
    <b>CurrentMdlOffset</b> values in the destination NET_BUFFER after 
    <b>NdisCopyFromNetBufferToNetBuffer</b> returns.</p>

<p>NDIS uses the offsets in the 
    <i>DestionationOffset</i> and 
    <i>SourceOffset</i> parameters of 
    <b>NdisCopyFromNetBufferToNetBuffer</b> as offsets from the current data offset. For example, if the 
    <b>CurrentMdlOffset</b> value in the destination NET_BUFFER is 
    <i>x</i>, and 
    <i>DestinationOffset</i> value is 
    <i>y</i>, NDIS copies the data to the destination NET_BUFFER at an 
    <i>x</i>+ 
    <i>y</i> offset in the memory that the 
    <b>CurrentMdl</b> value describes. Similar rules apply to the 
    <b>CurrentMdlOffset</b> in the source NET_BUFFER and the 
    <i>SourceOffset</i> value.</p>

<p>The caller of 
    <b>NdisCopyFromNetBufferToNetBuffer</b> allocates the destination 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure and possibly the source
    NET_BUFFER structure as well. The MDLs of the destination NET_BUFFER structure should have enough space
    to receive the data.</p>

<p>If the source NET_BUFFER structure runs out of data or the destination NET_BUFFER structure runs out
    of space before the specified number of bytes has been copied, the copy operation stops. In either case, 
    <b>NdisCopyFromNetBufferToNetBuffer</b> returns the number of bytes successfully copied from the source to
    the destination NET_BUFFER structure.</p>

<p>The caller must ensure that 
    <b>CurrentMdlOffset</b> and 
    <b>CurrentMdl</b> values are correct in the source and destination 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures. NDIS does not change the
    members in the destination NET_BUFFER. The caller must update the 
    <b>DataLength</b>, 
    <b>DataOffset</b>, and 
    <b>CurrentMdlOffset</b> values in the destination NET_BUFFER after 
    <b>NdisCopyFromNetBufferToNetBuffer</b> returns.</p>

<p>NDIS uses the offsets in the 
    <i>DestionationOffset</i> and 
    <i>SourceOffset</i> parameters of 
    <b>NdisCopyFromNetBufferToNetBuffer</b> as offsets from the current data offset. For example, if the 
    <b>CurrentMdlOffset</b> value in the destination NET_BUFFER is 
    <i>x</i>, and 
    <i>DestinationOffset</i> value is 
    <i>y</i>, NDIS copies the data to the destination NET_BUFFER at an 
    <i>x</i>+ 
    <i>y</i> offset in the memory that the 
    <b>CurrentMdl</b> value describes. Similar rules apply to the 
    <b>CurrentMdlOffset</b> in the source NET_BUFFER and the 
    <i>SourceOffset</i> value.</p>

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
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547985">Irql_NetBuffer_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisCopyFromNetBufferToNetBuffer function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
