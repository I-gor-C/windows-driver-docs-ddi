---
UID: NS.dispmprt._DXGK_DEVICE_INFO
title: DXGK_DEVICE_INFO
author: windows-driver-content
description: The DXGK_DEVICE_INFO structure holds information that describes a display adapter.
old-location: display\dxgk_device_info.htm
old-project: display
ms.assetid: dcdae08f-69a6-496b-8391-d2b505fb86d9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_DEVICE_INFO, DXGK_DEVICE_INFO, *PDXGK_DEVICE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_DEVICE_INFO
req.alt-loc: dispmprt.h
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
req.iface: 
---

# DXGK_DEVICE_INFO structure



## -description
<p>The DXGK_DEVICE_INFO structure holds information that describes a display adapter.</p>


## -syntax

````
typedef struct _DXGK_DEVICE_INFO {
  PVOID             MiniportDeviceContext;
  PDEVICE_OBJECT    PhysicalDeviceObject;
  UNICODE_STRING    DeviceRegistryPath;
  PCM_RESOURCE_LIST TranslatedResourceList;
  LARGE_INTEGER     SystemMemorySize;
  PHYSICAL_ADDRESS  HighestPhysicalAddress;
  PHYSICAL_ADDRESS  AgpApertureBase;
  SIZE_T            AgpApertureSize;
  DOCKING_STATE     DockingState;
} DXGK_DEVICE_INFO, *PDXGK_DEVICE_INFO;
````


## -struct-fields
<dl>

### -field <b>MiniportDeviceContext</b>

<dd>
<p>A handle to a context block (created and maintained by the display miniport driver) associated with a display adapter.</p>
</dd>

### -field <b>PhysicalDeviceObject</b>

<dd>
<p>A pointer to the physical device object (PDO) that represents the display adapter.</p>
</dd>

### -field <b>DeviceRegistryPath</b>

<dd>
<p>A Unicode string that holds the registry path of the software key for the display adapter. Registry data should be written only to this path.</p>
</dd>

### -field <b>TranslatedResourceList</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541994">CM_RESOURCE_LIST</a> structure that holds the translated resources assigned to the display adapter.</p>
</dd>

### -field <b>SystemMemorySize</b>

<dd>
<p>The size, in bytes, of system memory.</p>
</dd>

### -field <b>HighestPhysicalAddress</b>

<dd>
<p>The highest physical address of system memory (RAM).</p>
</dd>

### -field <b>AgpApertureBase</b>

<dd>
<p>The base physical address of the AGP aperture. If 0, the display adapter is not an AGP adapter, or AGP resources were not found.</p>
</dd>

### -field <b>AgpApertureSize</b>

<dd>
<p>The size, in bytes, of the AGP aperture. If 0, the display adapter is not an AGP adapter, or AGP resources were not found.</p>
</dd>

### -field <b>DockingState</b>

<dd>
<p>The state of a portable computer that can be attached to a docking station.</p>
</dd>
</dl>

## -remarks
<p>The display miniport driver's <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a> function allocates a DXGK_DEVICE_INFO structure and calls <a href="..\dispmprt\nc-dispmprt-dxgkcb-get-device-information.md">DxgkCbGetDeviceInformation</a> to get that structure filled in with information about a display adapter. Five of the structure members (<b>Version</b>, <b>SystemMemorySize</b>, <b>HighestPhysicalAddress</b>, <b>AgpApertureBase</b>, and <b>AgpApertureSize</b>) hold general information and are not associated with a particular display adapter. Those members are included in the DXGK_DEVICE_INFO structure because they provide information that <i>DxgkDdiStartDevice</i> requires to initialize the driver and display adapter hardware.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541994">CM_RESOURCE_LIST</a>
</dt>
<dt>
<a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkcb-get-device-information.md">DxgkCbGetDeviceInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_DEVICE_INFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
