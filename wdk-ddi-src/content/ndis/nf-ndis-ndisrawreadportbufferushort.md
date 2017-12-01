---
UID: NF.ndis.NdisRawReadPortBufferUshort
title: NdisRawReadPortBufferUshort
author: windows-driver-content
description: NdisRawReadPortBufferUshort reads a specified number of USHORTs into a caller-supplied buffer.
old-location: netvista\ndisrawreadportbufferushort.htm
old-project: netvista
ms.assetid: c100aad1-2fb9-49e0-b68e-20b165a69701
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisRawReadPortBufferUshort
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisRawReadPortBufferUshort   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisRawReadPortBufferUshort   (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisRawReadPortBufferUshort
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: 
---

# NdisRawReadPortBufferUshort function



## -description
<p><b>NdisRawReadPortBufferUshort</b> reads a specified number of USHORTs into a caller-supplied buffer.</p>


## -syntax

````
VOID NdisRawReadPortBufferUshort(
  _In_  ULONG_PTR Port,
  _Out_ PUSHORT   Buffer,
  _In_  ULONG     Length
);
````


## -parameters
<dl>

### -param <i>Port</i> [in]

<dd>
<p>Specifies the I/O port. This address falls in a range that was mapped during initialization with 
     <a href="..\ndis\nf-ndis-ndismregisterioportrange.md">
     NdisMRegisterIoPortRange</a>.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer, in resident memory, into which the USHORTs will be
     transferred from the NIC. The caller must allocate a buffer at least (<b>sizeof</b>(USHORT)
     *
     <i>Length</i> ).</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies how many USHORTs to transfer from the NIC.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisRawReadPortBufferUshort</b> reads each USHORT value, one at a time, from the given I/O port into
    the given buffer.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/6a413abb-0e01-4dba-9f80-609cf58d168c">NdisRawReadPortBufferUshort
   (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisRawReadPortBufferUshort
   (NDIS 5.1)</b>) in Windows XP.</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismregisterioportrange.md">NdisMRegisterIoPortRange</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisrawreadportbufferuchar.md">NdisRawReadPortBufferUchar</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisrawreadportbufferulong.md">NdisRawReadPortBufferUlong</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisrawreadportushort.md">NdisRawReadPortUshort</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisrawwriteportbufferushort.md">NdisRawWritePortBufferUshort</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisRawReadPortBufferUshort function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
