---
UID: NF.ndis.NdisMGetDeviceProperty
title: NdisMGetDeviceProperty
author: windows-driver-content
description: The NdisMGetDeviceProperty function retrieves device objects required to set up communication with a miniport driver through a bus driver.
old-location: netvista\ndismgetdeviceproperty.htm
ms.assetid: caef96b6-1b94-475d-9f78-66ae6d6ac979
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 5.1, and NDIS 6.0 and later. For NDIS 5.1 drivers, see 
   NdisMGetDeviceProperty (NDIS
   5.1).
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMGetDeviceProperty
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miniport_Driver_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: NdisMGetDeviceProperty
req.iface: 
---

# NdisMGetDeviceProperty function



## -description
<p>The
  <b>NdisMGetDeviceProperty</b> function retrieves device objects required to set up communication with a
  miniport driver through a bus driver.</p>


## -syntax

````
VOID NdisMGetDeviceProperty(
  _In_      NDIS_HANDLE       MiniportAdapterHandle,
  _Out_opt_ PDEVICE_OBJECT    *PhysicalDeviceObject,
  _Out_opt_ PDEVICE_OBJECT    *FunctionalDeviceObject,
  _Out_opt_ PDEVICE_OBJECT    *NextDeviceObject,
  _Out_opt_ PCM_RESOURCE_LIST *AllocatedResources,
  _Out_opt_ PCM_RESOURCE_LIST *AllocatedResourcesTranslated
);
````


## -parameters
<dl>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>The NDIS handle that identifies the miniport adapter. This handle was originally passed to the 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">
     MiniportInitializeEx</a> function.</p>
</dd>

### -param <i>PhysicalDeviceObject</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated buffer. The buffer receives a pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure that represents the
     physical device for the miniport adapter. This pointer is optional.</p>
</dd>

### -param <i>FunctionalDeviceObject</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated buffer. The buffer receives a pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure. 
     <b>DEVICE_OBJECT</b> represents the functional device object that NDIS creates for the physical device.
     This pointer is optional.</p>
</dd>

### -param <i>NextDeviceObject</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated buffer. The buffer receives a pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure that represents the next device object. This next device object is
     preceded in the chain by the functional device object that belongs to the miniport driver. NDIS creates
     this functional device object for the physical device. For example, the next device object could be the
     object that is associated with a bus driver or HAL This pointer is optional.</p>
</dd>

### -param <i>AllocatedResources</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated buffer that receives a pointer to a 
     CM_RESOURCE_LIST structure. 
     CM_RESOURCE_LIST describes a list of hardware resources that the PnP manager assigns to the
     physical device. This list contains the resources in raw form, that is, not translated by HAL. This
     pointer is optional.</p>
</dd>

### -param <i>AllocatedResourcesTranslated</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated buffer that receives a pointer to a 
     CM_RESOURCE_LIST structure. 
     CM_RESOURCE_LIST describes a list of hardware resources that the PnP manager assigns to the
     physical device. This list contains the resources in translated form, that is, translated by HAL. This
     pointer is optional.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Miniport drivers must retrieve specific information to set up their communications. Miniport drivers
    for miniport instances that communicate through bus drivers use 
    <b>NdisMGetDeviceProperty</b> to retrieve this information. For example, miniport driver instances that
    attach to Universal Serial Bus (USB) or IEEE 1394 buses require miniport drivers that expose a standard
    NDIS miniport driver interface at their upper edge, and use the class interface for the particular bus at
    their lower edge. To use the USB or 1394 class interface, a miniport driver creates and submits I/O
    Request Packets (IRPs). The miniport driver uses the physical and next-device objects that 
    <b>NdisMGetDeviceProperty</b> retrieves to submit IRPs to the class interface for a particular bus. To
    locate more information about creating and submitting IRPs to bus drivers, see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff546847">Handling IRPs</a>.</p>

<p>Pointers to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> for the physical, functional, and next device objects that 
    <b>NdisMGetDeviceProperty</b> retrieves are simply handles that are opaque to the miniport driver.</p>

<p>Miniport drivers can call 
    <b>NdisMGetDeviceProperty</b> to retrieve pointers to "raw" or "translated" resources. Raw resources have
    not been translated by HAL; translated resources have been. To locate more information about raw and
    translated resources, see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562374">Plug and Play</a>.</p>

<p>Miniport drivers must retrieve specific information to set up their communications. Miniport drivers
    for miniport instances that communicate through bus drivers use 
    <b>NdisMGetDeviceProperty</b> to retrieve this information. For example, miniport driver instances that
    attach to Universal Serial Bus (USB) or IEEE 1394 buses require miniport drivers that expose a standard
    NDIS miniport driver interface at their upper edge, and use the class interface for the particular bus at
    their lower edge. To use the USB or 1394 class interface, a miniport driver creates and submits I/O
    Request Packets (IRPs). The miniport driver uses the physical and next-device objects that 
    <b>NdisMGetDeviceProperty</b> retrieves to submit IRPs to the class interface for a particular bus. To
    locate more information about creating and submitting IRPs to bus drivers, see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff546847">Handling IRPs</a>.</p>

<p>Pointers to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> for the physical, functional, and next device objects that 
    <b>NdisMGetDeviceProperty</b> retrieves are simply handles that are opaque to the miniport driver.</p>

<p>Miniport drivers can call 
    <b>NdisMGetDeviceProperty</b> to retrieve pointers to "raw" or "translated" resources. Raw resources have
    not been translated by HAL; translated resources have been. To locate more information about raw and
    translated resources, see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562374">Plug and Play</a>.</p>

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
<p>Supported in NDIS 5.1, and NDIS 6.0 and later. For NDIS 5.1 drivers, see 
   <a href="https://msdn.microsoft.com/65f3f766-8b04-466b-9e92-1bd8f1c4fbcc">NdisMGetDeviceProperty (NDIS
   5.1)</a>.</p>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547979">Irql_Miniport_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMGetDeviceProperty function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
