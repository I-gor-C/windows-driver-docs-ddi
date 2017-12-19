---
UID: NF.ndis.NdisRawWritePortBufferUshort
title: NdisRawWritePortBufferUshort macro
author: windows-driver-content
description: NdisRawWritePortBufferUshort writes a specified number of USHORT values from a caller-supplied buffer to a given I/O port.
old-location: netvista\ndisrawwriteportbufferushort.htm
old-project: NetVista
ms.assetid: 457b13e5-5917-4aa2-b471-bc9fde14f950
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NdisRawWritePortBufferUshort
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisRawWritePortBufferUshort   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisRawWritePortBufferUshort   (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisRawWritePortBufferUshort
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

# NdisRawWritePortBufferUshort macro



## -description
<b>NdisRawWritePortBufferUshort</b> writes a specified number of USHORT values from a caller-supplied buffer
  to a given I/O port.



## -syntax

````
VOID NdisRawWritePortBufferUshort(
  [in] ULONG_PTR Port,
  [in] PUSHORT   Buffer,
  [in] ULONG     Length
);
````


## -parameters

### -param Port [in]

Specifies the I/O port. This address falls in a range that was mapped during initialization with 
     <a href="netvista.ndismregisterioportrange">
     NdisMRegisterIoPortRange</a>.


### -param Buffer [in]

Pointer to a caller-allocated resident buffer containing the USHORTs to be written.


### -param Length [in]

Specifies the number of USHORTs to write to the I/O port.


## -remarks
A miniport driver calls 
    <b>NdisRawWritePortBufferUshort</b> to transfer a sequence of USHORTs, one at a time, to a NIC.

<b>NdisRawWritePortBufferUshort</b> runs fast because it need not map a bus-relative port address onto a
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
   <a href="https://msdn.microsoft.com/820a5659-3762-4c1a-ba74-b06399851eb4">NdisRawWritePortBufferUshort
   (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisRawWritePortBufferUshort
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
<a href="netvista.ndisrawreadportbufferushort">NdisRawReadPortBufferUshort</a>
</dt>
<dt>
<a href="netvista.ndisrawwriteportbufferuchar">NdisRawWritePortBufferUchar</a>
</dt>
<dt>
<a href="netvista.ndisrawwriteportbufferulong">NdisRawWritePortBufferUlong</a>
</dt>
<dt>
<a href="netvista.ndisrawwriteportushort">NdisRawWritePortUshort</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NdisRawWritePortBufferUshort macro%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

