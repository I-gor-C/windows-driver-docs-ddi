---
UID: NF.ks.IKsDeviceFunctions.RegisterAdapterObjectEx
title: IKsDeviceFunctions::RegisterAdapterObjectEx
author: windows-driver-content
description: The IKsDeviceFunctions::RegisterAdapterObjectEx method registers a DMA adapter object with AVStream. All drivers compiled for Win64 platforms should use this method instead of KsDeviceRegisterAdapterObject.
old-location: stream\iksdevicefunctions_registeradapterobjectex.htm
old-project: stream
ms.assetid: e5dc54a6-e26a-455b-9990-92f5cfece923
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IKsDeviceFunctions, RegisterAdapterObjectEx, IKsDeviceFunctions::RegisterAdapterObjectEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows Server 2003 with Service Pack 1 (SP1) and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsDeviceFunctions.RegisterAdapterObjectEx
req.alt-loc: ks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: IKsDeviceFunctions
---

# IKsDeviceFunctions::RegisterAdapterObjectEx method



## -description
<p>The <b>IKsDeviceFunctions::RegisterAdapterObjectEx</b> method registers a DMA adapter object with AVStream. All drivers compiled for Win64 platforms should use this method instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561687">KsDeviceRegisterAdapterObject</a>.</p>


## -syntax

````
NTSTATUS RegisterAdapterObjectEx(
  [in] PADAPTER_OBJECT     AdapterObject,
  [in] PDEVICE_DESCRIPTION DeviceDescription,
  [in] ULONG               NumberOfMapRegisters,
  [in] ULONG               MaxMappingsByteCount,
  [in] ULONG               MappingTableStride
);
````


## -parameters
<dl>

### -param <i>AdapterObject</i> [in]

<dd>
<p>Pointer to the ADAPTER_OBJECT for the device. Must be acquired through <a href="https://msdn.microsoft.com/library/windows/hardware/ff549220">IoGetDmaAdapter</a> before calling <b>RegisterAdapterObjectEx</b>.</p>
</dd>

### -param <i>DeviceDescription</i> [in]

<dd>
<p>Pointer to a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff543107">DEVICE_DESCRIPTION</a> that describes the attributes of the physical device for which the caller is registering a DMA object.</p>
</dd>

### -param <i>NumberOfMapRegisters</i> [in]

<dd>
<p>Specifies the number of map registers returned from the minidriver's call to <b>IoGetDmaAdapter</b>.</p>
</dd>

### -param <i>MaxMappingsByteCount</i> [in]

<dd>
<p>Specifies the maximum number of bytes that the device can handle for a single mapping. Enables AVStream to automatically break up large chunks of contiguous physical memory into multiple scatter/gather elements for devices that impose a size limit on individual mappings in DMA transfers. See important additional information about <b>MaxMappingsByteCount</b> on the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561687">KsDeviceRegisterAdapterObject</a> reference page.</p>
</dd>

### -param <i>MappingTableStride</i> [in]

<dd>
<p>Specifies how many bytes each entry in the mapping table requires. This value must be at least <b>sizeof</b> (<a href="https://msdn.microsoft.com/library/windows/hardware/ff563394">KSMAPPING</a>) and can be as large as necessary.</p>
<p>Additional space can be used by the minidriver as context information.</p>
</dd>
</dl>

## -returns
<p><b>RegisterAdapterObjectEx</b> returns STATUS_SUCCESS if the DMA object was successfully registered. The method returns STATUS_INSUFFICIENT_RESOURCES if sufficient memory is not available.</p>

## -remarks
<p>Also see <a href="NULL">Supporting DMA in 64-Bit AVStream Drivers</a>.</p>

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
<p>Available in Microsoft Windows Server 2003 with Service Pack 1 (SP1) and later versions of Windows.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561687">KsDeviceRegisterAdapterObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsDeviceFunctions::RegisterAdapterObjectEx method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
