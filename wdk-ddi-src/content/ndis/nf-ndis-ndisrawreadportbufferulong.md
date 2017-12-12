---
UID: NF.ndis.NdisRawReadPortBufferUlong
title: NdisRawReadPortBufferUlong macro
author: windows-driver-content
description: NdisRawReadPortBufferUlong reads a specified number of ULONGs into a caller-supplied buffer.
old-location: netvista\ndisrawreadportbufferulong.htm
old-project: netvista
ms.assetid: 86a0b7c4-ef3a-4dd9-961d-35f96182e30c
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisRawReadPortBufferUlong
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisRawReadPortBufferUlong   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisRawReadPortBufferUlong   (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisRawReadPortBufferUlong
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
---

# NdisRawReadPortBufferUlong macro



## -description
<b>NdisRawReadPortBufferUlong</b> reads a specified number of ULONGs into a caller-supplied buffer.



## -syntax

````
VOID NdisRawReadPortBufferUlong(
  [in]  ULONG_PTR Port,
  [out] PULONG    Buffer,
  [in]  ULONG     Length
);
````


## -parameters

### -param Port [in]

Specifies the I/O port. This address falls in a range that was mapped during initialization with 
     <a href="netvista.ndismregisterioportrange">
     NdisMRegisterIoPortRange</a>.


### -param Buffer [out]

Pointer to a caller-allocated buffer, in resident memory, into which the ULONGs will be
     transferred from the NIC. The caller must allocate a buffer at least (
     <b>sizeof</b>(ULONG)
     *
     <i>Length</i> ).


### -param Length [in]

Specifies how many ULONGs to transfer from the NIC.


## -remarks
<b>NdisRawReadPortBufferUlong</b> reads each ULONG value, one at a time, from the given I/O port into the
    given buffer.


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
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/110f4a7a-aebc-4a51-93b9-b63f1ce9cc7d">NdisRawReadPortBufferUlong
   (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisRawReadPortBufferUlong
   (NDIS 5.1)</b>) in Windows XP.

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
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="netvista.ndismregisterioportrange">NdisMRegisterIoPortRange</a>
</dt>
<dt>
<a href="netvista.ndisrawreadportbufferuchar">NdisRawReadPortBufferUchar</a>
</dt>
<dt>
<a href="netvista.ndisrawreadportbufferushort">NdisRawReadPortBufferUshort</a>
</dt>
<dt>
<a href="netvista.ndisrawreadportulong">NdisRawReadPortUlong</a>
</dt>
<dt>
<a href="netvista.ndisrawwriteportbufferulong">NdisRawWritePortBufferUlong</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisRawReadPortBufferUlong macro%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

