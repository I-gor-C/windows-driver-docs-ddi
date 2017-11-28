---
UID: NF.ndis.NdisRawReadPortUlong
title: NdisRawReadPortUlong
author: windows-driver-content
description: NdisRawReadPortUlong reads a ULONG value from a given I/O port on the NIC.
old-location: netvista\ndisrawreadportulong.htm
old-project: netvista
ms.assetid: 40ecda3a-67ff-48b6-8ee9-7527c7bd9c6c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisRawReadPortUlong
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisRawReadPortUlong (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisRawReadPortUlong (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisRawReadPortUlong
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

# NdisRawReadPortUlong function



## -description
<p><b>NdisRawReadPortUlong</b> reads a ULONG value from a given I/O port on the NIC.</p>


## -syntax

````
VOID NdisRawReadPortUlong(
  _In_  ULONG_PTR Port,
  _Out_ PULONG    Data
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

### -param <i>Data</i> [out]

<dd>
<p>Pointer to a caller-supplied variable in which this function returns a ULONG value read in from
     the port.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisRawReadPortUlong</b> runs fast
    because it need not map a bus-relative I/O port address onto a host-dependent logical port address at
    every call.</p>

<p><b>NdisRawReadPortUlong</b> runs fast
    because it need not map a bus-relative I/O port address onto a host-dependent logical port address at
    every call.</p>

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
   <a href="https://msdn.microsoft.com/f28881dc-088f-477a-b198-67325f67628d">NdisRawReadPortUlong (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisRawReadPortUlong (NDIS
   5.1)</b>) in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975121">NdisMRegisterIoPortRange</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563785">NdisRawReadPortBufferUlong</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563794">NdisRawReadPortUchar</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563808">NdisRawReadPortUshort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563832">NdisRawWritePortUlong</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisRawReadPortUlong function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
