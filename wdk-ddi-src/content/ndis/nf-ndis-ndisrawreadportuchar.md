---
UID: NF.ndis.NdisRawReadPortUchar
title: NdisRawReadPortUchar
author: windows-driver-content
description: NdisRawReadPortUchar reads a byte from a given I/O port on the NIC.
old-location: netvista\ndisrawreadportuchar.htm
old-project: netvista
ms.assetid: 5bda6d10-dd68-4385-b71c-8319e6ed0d4a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisRawReadPortUchar
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisRawReadPortUchar (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisRawReadPortUchar (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisRawReadPortUchar
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

# NdisRawReadPortUchar function



## -description
<p><b>NdisRawReadPortUchar</b> reads a byte from a given I/O port on the NIC.</p>


## -syntax

````
VOID NdisRawReadPortUchar(
  _In_  ULONG_PTR Port,
  _Out_ PUCHAR    Data
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
<p>Pointer to a caller-supplied variable in which this function returns a byte read in from the
     port.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisRawReadPortUchar</b> runs fast
    because it need not map a bus-relative I/O port address onto a host-dependent logical port address at
    every call.</p>

<p><b>NdisRawReadPortUchar</b> runs fast
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
   <a href="https://msdn.microsoft.com/3ee06ee2-76b3-4654-824e-7bf661b771e4">NdisRawReadPortUchar (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisRawReadPortUchar (NDIS
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563782">NdisRawReadPortBufferUchar</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563801">NdisRawReadPortUlong</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563808">NdisRawReadPortUshort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563829">NdisRawWritePortUchar</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisRawReadPortUchar function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
