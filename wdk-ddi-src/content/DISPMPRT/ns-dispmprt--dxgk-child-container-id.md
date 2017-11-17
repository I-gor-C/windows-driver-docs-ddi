---
UID: NS.dispmprt._DXGK_CHILD_CONTAINER_ID
title: DXGK_CHILD_CONTAINER_ID
author: windows-driver-content
description: Contains the container ID for a child device that is connected to a display adapter.
old-location: display\dxgk_child_container_id.htm
ms.assetid: 9573f6e9-80a6-4390-b2ab-4543e3b1f5f4
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_CHILD_CONTAINER_ID
req.alt-loc: Dispmprt.h
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
ms.keywords: DXGK_CHILD_CONTAINER_ID, DXGK_CHILD_CONTAINER_ID, *PDXGK_CHILD_CONTAINER_ID
req.iface: 
---

# DXGK_CHILD_CONTAINER_ID structure



## -description
<p>Contains the container ID for a child device that is connected to a display adapter.</p>


## -syntax

````
typedef struct _DXGK_CHILD_CONTAINER_ID {
  GUID ContainerId;
  struct {
    ULONG64 PortId;
    USHORT  ManufacturerName;
    USHORT  ProductCode;
  } EldInfo;
} DXGK_CHILD_CONTAINER_ID, *PDXGK_CHILD_CONTAINER_ID;
````


## -struct-fields
<dl>

### -field <b>ContainerId</b>

<dd>
<p>The container ID for the child device. For more information, see the Remarks section.</p>
</dd>

### -field <b>EldInfo</b>

<dd>
<p>This structure contains the information that the operating system used to generate the container ID for the child device.</p>
<dl>

### -field <b>PortId</b>

<dd>
<p>A ULONG64 value that contains the port ID for the child device. The operating system created this ID based on the name of the child device.</p>
</dd>

### -field <b>ManufacturerName</b>

<dd>
<p>A USHORT value that contains the manufacturer's name. The operating system obtains this data from the child device's descriptor.</p>
</dd>

### -field <b>ProductCode</b>

<dd>
<p>A USHORT value that contains the manufacturer's product code for the child device. The operating system obtains this data from the child device's descriptor.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The operating system calls the display miniport driver's <a href="https://msdn.microsoft.com/eb1a0df0-6239-4d82-8477-7dd015f80b6e">DxgkDdiQueryChildRelations</a> function to enumerate the child devices of the display adapter. The operating system then calls the display miniport driver's <a href="https://msdn.microsoft.com/0dfcc012-9fff-40b6-b71f-da2ca229896c">DxgkDdiQueryDeviceDescriptor</a> function for each child device to obtain the  Extended Display Information Data (EDID) for the device. For more information on this procedure, see <a href="https://msdn.microsoft.com/3bec2117-aef4-41fc-b88a-0081c7c9fe3d">Enumerating Child Devices of a Display Adapter</a>.</p>

<p>Based on the device's EDID data, the operating system generates a default container ID for the child device. Then, the operating system calls the display miniport driver's <a href="https://msdn.microsoft.com/e7073fb3-0cb7-425e-9ffb-d7eaa963a70f">DxgkDdiGetChildContainerId</a> function and passes a pointer to a <b>DXGK_CHILD_CONTAINER_ID</b> structure through the <i>ContainerId</i> parameter. The <b>ContainerId</b> member of this structure contains the default container ID for the child display device.</p>

<p>The display miniport driver can either accept the default container ID because the display hardware has no container ID coded into the firmware, or it can set the <b>ContainerId</b> member to a unique identifier obtained from the display hardware device before it returns from the call to <a href="https://msdn.microsoft.com/e7073fb3-0cb7-425e-9ffb-d7eaa963a70f">DxgkDdiGetChildContainerId</a>.</p>

<p>For more information about Container IDs, see <a href="devinst.container_ids">Container IDs</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
<a href="https://msdn.microsoft.com/e7073fb3-0cb7-425e-9ffb-d7eaa963a70f">DxgkDdiGetChildContainerId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/eb1a0df0-6239-4d82-8477-7dd015f80b6e">DxgkDdiQueryChildRelations</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/0dfcc012-9fff-40b6-b71f-da2ca229896c">DxgkDdiQueryDeviceDescriptor</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_CHILD_CONTAINER_ID structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
