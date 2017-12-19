---
UID: NF.ndis.NdisRawWritePortBufferUchar
title: NdisRawWritePortBufferUchar macro
author: windows-driver-content
description: NdisRawWritePortBufferUchar writes a specified number of bytes from a caller-supplied buffer to a given I/O port.
old-location: netvista\ndisrawwriteportbufferuchar.htm
old-project: NetVista
ms.assetid: 2e802f1c-1d27-43cb-a69d-023519806fc2
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NdisRawWritePortBufferUchar
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisRawWritePortBufferUchar   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisRawWritePortBufferUchar   (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisRawWritePortBufferUchar
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

# NdisRawWritePortBufferUchar macro



## -description
<b>NdisRawWritePortBufferUchar</b> writes a specified number of bytes from a caller-supplied buffer to a
  given I/O port.



## -syntax

````
VOID NdisRawWritePortBufferUchar(
  [in] ULONG_PTR Port,
  [in] PUCHAR    Buffer,
  [in] ULONG     Length
);
````


## -parameters

### -param Port [in]

Specifies the I/O port. This address falls in a range that was mapped during initialization with 
     <a href="netvista.ndismregisterioportrange">
     NdisMRegisterIoPortRange</a>.


### -param Buffer [in]

Pointer to a caller-allocated resident buffer containing the bytes to be written.


### -param Length [in]

Specifies the number of bytes to write to the I/O port.


## -remarks
A miniport driver calls 
    <b>NdisRawWritePortBufferUchar</b> to transfer a sequence of bytes, one at a time, to a NIC.

<b>NdisRawWritePortBufferUchar</b> runs fast because it need not map a bus-relative port address onto a
    host-dependent logical port address at every call.


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
   <a href="https://msdn.microsoft.com/e4a58fba-3496-412c-b318-09f3bbffdf24">NdisRawWritePortBufferUchar
   (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisRawWritePortBufferUchar
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
<a href="netvista.ndisrawwriteportbufferulong">NdisRawWritePortBufferUlong</a>
</dt>
<dt>
<a href="netvista.ndisrawwriteportbufferushort">NdisRawWritePortBufferUshort</a>
</dt>
<dt>
<a href="netvista.ndisrawwriteportuchar">NdisRawWritePortUchar</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NdisRawWritePortBufferUchar macro%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

