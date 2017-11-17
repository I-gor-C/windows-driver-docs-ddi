---
UID: NF.ks.KsDeviceRegisterAdapterObject
title: KsDeviceRegisterAdapterObject
author: windows-driver-content
description: The KsDeviceRegisterAdapterObject function registers a DMA adapter object with AVStream for performing scatter/gather DMA on the specified device. All drivers compiled for Win64 should use IKsDeviceFunctions::RegisterAdapterObjectEx instead.
old-location: stream\ksdeviceregisteradapterobject.htm
ms.assetid: 6e3c33fe-eb28-4985-98f3-cafa85543d68
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsDeviceRegisterAdapterObject
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: KsDeviceRegisterAdapterObject
req.iface: 
---

# KsDeviceRegisterAdapterObject function



## -description
<p>The<b> KsDeviceRegisterAdapterObject</b> function registers a DMA adapter object with AVStream for performing scatter/gather DMA on the specified device. All drivers compiled for Win64 should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff559852">IKsDeviceFunctions::RegisterAdapterObjectEx</a> instead.</p>


## -syntax

````
void KsDeviceRegisterAdapterObject(
  _In_ PKSDEVICE       Device,
  _In_ PADAPTER_OBJECT AdapterObject,
  _In_ ULONG           MaxMappingByteCount,
  _In_ ULONG           MappingTableStride
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a> structure representing the AVStream device for which to register an adapter object.</p>
</dd>

### -param <i>AdapterObject</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544062">DMA_ADAPTER</a> structure returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff549220">IoGetDmaAdapter</a> that represents the DMA controller..</p>
</dd>

### -param <i>MaxMappingByteCount</i> [in]

<dd>
<p>This parameter specifies the maximum number of bytes that the device can handle for a single mapping. Allows AVStream to automatically break up large chunks of contiguous physical memory into multiple scatter/gather elements for devices that impose a size limit on individual mappings in DMA transfers. <i>Breaks are not guaranteed to occur on page boundaries.</i></p>
</dd>

### -param <i>MappingTableStride</i> [in]

<dd>
<p>This parameter specifies how many bytes each entry in the mapping table requires. This must be at least <b>sizeof</b> (<a href="https://msdn.microsoft.com/library/windows/hardware/ff563394">KSMAPPING</a>) and can be as large as necessary.</p>
<p>Additional space can be used by the minidriver as context information.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A minidriver that calls <b>KsDeviceRegisterAdapterObject</b> is responsible for previously acquiring the adapter object through <a href="https://msdn.microsoft.com/library/windows/hardware/ff549220">IoGetDmaAdapter</a>. </p>

<p>Also note that if the minidriver specifies the KSPIN_FLAG_GENERATE_MAPPINGS flag for any pin on any filter on the device, the minidriver must call <b>KsDeviceRegisterAdapterObject</b> before processing any data. More information about this flag can be found in the reference page for <a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a>. Also see <a href="NULL">AVStream DMA Services</a>.</p><p class="note">In addition, as noted in the member description above, setting <i>MaxMappingsByteCount</i> does not guarantee that breaks will occur on page boundaries. If you require breaks on page boundaries, consider not specifying a limit on mapping sizes; instead, break the returned scatter/gather mappings into page-aligned chunks manually.</p>

<p>Also see <a href="NULL">Supporting DMA in 64-Bit AVStream Drivers</a>.</p>

<p>A minidriver that calls <b>KsDeviceRegisterAdapterObject</b> is responsible for previously acquiring the adapter object through <a href="https://msdn.microsoft.com/library/windows/hardware/ff549220">IoGetDmaAdapter</a>. </p>

<p>Also note that if the minidriver specifies the KSPIN_FLAG_GENERATE_MAPPINGS flag for any pin on any filter on the device, the minidriver must call <b>KsDeviceRegisterAdapterObject</b> before processing any data. More information about this flag can be found in the reference page for <a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a>. Also see <a href="NULL">AVStream DMA Services</a>.</p><p class="note">In addition, as noted in the member description above, setting <i>MaxMappingsByteCount</i> does not guarantee that breaks will occur on page boundaries. If you require breaks on page boundaries, consider not specifying a limit on mapping sizes; instead, break the returned scatter/gather mappings into page-aligned chunks manually.</p>

<p>Also see <a href="NULL">Supporting DMA in 64-Bit AVStream Drivers</a>.</p>

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
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562553">KSFILTER_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563394">KSMAPPING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549220">IoGetDmaAdapter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsDeviceRegisterAdapterObject function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
