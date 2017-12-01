---
UID: NF.ndis.NdisMGetBusData
title: NdisMGetBusData
author: windows-driver-content
description: NDIS drivers call the NdisMGetBusData function to read the configuration space of a device.
old-location: netvista\ndismgetbusdata.htm
old-project: netvista
ms.assetid: 495191f4-a5c6-4223-8c5d-e4c0ecb0cc5d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisMGetBusData
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
req.alt-api: NdisMGetBusData
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: Any level
req.iface: 
---

# NdisMGetBusData function



## -description
<p>NDIS drivers call the 
  <b>NdisMGetBusData</b> function to read the configuration space of a device.</p>


## -syntax

````
ULONG NdisMGetBusData(
  _In_  NDIS_HANDLE MiniportAdapterHandle,
  _In_  ULONG       WhichSpace,
  _In_  ULONG       Offset,
  _Out_ PVOID       Buffer,
  _In_  ULONG       Length
);
````


## -parameters
<dl>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>The miniport adapter handle that NDIS passed to the 
     <i>MiniportAdapterHandle</i> parameter of the 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">
     MiniportInitializeEx</a> function.</p>
</dd>

### -param <i>WhichSpace</i> [in]

<dd>
<p>The type of bus data to be read. For further information, see the discussion of the 
     <i>WhichSpace</i> parameter on the reference page for 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551727">IRP_MN_READ_CONFIG</a>.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>The byte offset in the configuration space, specified by 
     <i>WhichSpace</i>, from which data is read.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>A pointer to a buffer that receives the data read from the bus. Must be at least as large as 
     <i>Length</i> .</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The length, in bytes, of the data to read.</p>
</dd>
</dl>

## -returns
<p><b>NdisMGetBusData</b> returns the number of bytes read.</p>

## -remarks
<p>This function replaces the NDIS 5.1 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff554554">NdisReadPciSlotInformation</a> function.</p>

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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551727">IRP_MN_READ_CONFIG</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismsetbusdata.md">NdisMSetBusData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMGetBusData function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
