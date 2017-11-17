---
UID: NF.portcls.IPortClsStreamResourceManager2.AddStreamResource2
title: IPortClsStreamResourceManager2::AddStreamResource2
author: windows-driver-content
description: AddStreamResource2 adds a stream resource. Two type of stream resources are supported: interrupts and driver-owned threads. The AddStreamResource2 method can only be used by audio waveRT miniport drivers.
old-location: audio\iportclsstreamresourcemanager2_addstreamresource2.htm
ms.assetid: C140D11C-41D6-4812-AD95-990CBFA06FE8
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 10, version 1511 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPortClsStreamResourceManager2.AddStreamResource2
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: IPortClsStreamResourceManager2, AddStreamResource2, IPortClsStreamResourceManager2::AddStreamResource2
req.iface: IPortClsStreamResourceManager2
---

# IPortClsStreamResourceManager2::AddStreamResource2 method



## -description
<p>AddStreamResource2 adds a stream resource. 
Two type of stream resources are supported: interrupts and driver-owned threads. The AddStreamResource2 method can only be used by audio waveRT miniport drivers.</p>


## -syntax

````
NTSTATUS  AddStreamResource2(
  [in]  PDEVICE_OBJECT               PhysicalDeviceObject,
  [in]  PVOID                        ResourceSet,
  [in]  PPCSTREAMRESOURCE_DESCRIPTOR ResourceDescriptor,
  [out] PCSTREAMRESOURCE*            ResourceHandle
);
````


## -parameters
<dl>

### -param <i>PhysicalDeviceObject</i> [in]

<dd>
<p>Pointer to the device object. The device object is a system structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a>.</p>
</dd>

### -param <i>ResourceSet</i> [in]

<dd>
<p>PVOID - Reserved for future use, set to NULL. Only device-scoped resources are supported at this time.</p>
</dd>

### -param <i>ResourceDescriptor</i> [in]

<dd>
<p>PPCSTREAMRESOURCE_DESCRIPTOR - The resource to add. For more information see, <a href="https://msdn.microsoft.com/library/windows/hardware/mt298191">PCSTREAMRESOURCE_DESCRIPTOR</a>. 
</p>
</dd>

### -param <i>ResourceHandle</i> [out]

<dd>
<p>PCSTREAMRESOURCE* - The location that will hold the resource handle. For more information, see <a href="https://msdn.microsoft.com/35A90B3C-27D7-4BBA-A754-098D191A3201">RemoveStreamResource</a>.  </p>
</dd>
</dl>

## -returns
<p>STATUS_SUCCESS – The driver was able to register the resource of the specified PDO. 

 </p>

<p>STATUS_INVALID_PARAMETER – The driver returns this error if it finds any other parameter invalid, aside from the specific cases for other error status instances. 

</p>

<p>Additional standard status codes may be returned.</p>

## -remarks


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
<p>Available in Windows 10, version 1511 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
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
<a href="https://msdn.microsoft.com/35A90B3C-27D7-4BBA-A754-098D191A3201">RemoveStreamResource</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt298191">PCSTREAMRESOURCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt270106">IPortClsStreamResourceManager</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt604862">IPortClsStreamResourceManager2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortClsStreamResourceManager2::AddStreamResource2 method%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
