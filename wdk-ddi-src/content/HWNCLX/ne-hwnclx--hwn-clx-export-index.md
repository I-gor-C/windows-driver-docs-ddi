---
UID: NE.hwnclx._HWN_CLX_EXPORT_INDEX
title: HWN_CLX_EXPORT_INDEX
author: windows-driver-content
description: Defines the position for each of the Hardware Notification exports in the export table.
old-location: gpiobtn\_hwn_clx_export_index.htm
ms.assetid: fcbbd188-438a-4eaa-8034-67ca52d1fb56
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: gpiobtn
req.header: hwnclx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HWN_CLX_EXPORT_INDEX
req.alt-loc: Hwnclx.h
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
ms.keywords: HIDD_ATTRIBUTES, HIDD_ATTRIBUTES, *PHIDD_ATTRIBUTES
req.iface: 
---

# HWN_CLX_EXPORT_INDEX enumeration



## -description
<p>Defines the position for each of the Hardware Notification exports in the export table.
</p>


## -syntax

````
typedef enum _HWN_CLX_EXPORT_INDEX { 
  RegisterClientIndex             = 0x0,
  UnregisterClientIndex,
  AddDevicePreDeviceCreateIndex,
  AddDevicePostDeviceCreateIndex,
  HwNExportLastExportIndex
} HWN_CLX_EXPORT_INDEX;
````


## -enum-fields
<dl>

### -field <a id="RegisterClientIndex"></a><a id="registerclientindex"></a><a id="REGISTERCLIENTINDEX"></a><b>RegisterClientIndex</b>

<dd>
<p>Position of the <a href="https://msdn.microsoft.com/69de1551-e41f-4d18-89db-28d190676922">HwNRegisterClient</a> hardware notification in the export table.
</p>
</dd>

### -field <a id="UnregisterClientIndex"></a><a id="unregisterclientindex"></a><a id="UNREGISTERCLIENTINDEX"></a><b>UnregisterClientIndex</b>

<dd>
<p>Position of the <a href="https://msdn.microsoft.com/94e5153a-3ce5-400c-b53a-5323b34a6c34">HwNUnregisterClient</a> hardware notification in the export table.
</p>
</dd>

### -field <a id="AddDevicePreDeviceCreateIndex"></a><a id="adddevicepredevicecreateindex"></a><a id="ADDDEVICEPREDEVICECREATEINDEX"></a><b>AddDevicePreDeviceCreateIndex</b>

<dd>
<p>Position of the <a href="https://msdn.microsoft.com/c7bbba08-e9d0-4f78-93d8-e451e4dc2573">HwNProcessAddDevicePreDeviceCreate</a> hardware notification in the export table.
</p>
</dd>

### -field <a id="AddDevicePostDeviceCreateIndex"></a><a id="adddevicepostdevicecreateindex"></a><a id="ADDDEVICEPOSTDEVICECREATEINDEX"></a><b>AddDevicePostDeviceCreateIndex</b>

<dd>
<p>Position of the <a href="https://msdn.microsoft.com/907cdeac-e2f0-48fa-bbf0-082c0fce6401">HwNProcessAddDevicePostDeviceCreate</a> hardware notification in the export table.
</p>
</dd>

### -field <a id="HwNExportLastExportIndex"></a><a id="hwnexportlastexportindex"></a><a id="HWNEXPORTLASTEXPORTINDEX"></a><b>HwNExportLastExportIndex</b>

<dd>
<p>Position of the last hardware notification in the export table.
</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hwnclx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><a href="https://msdn.microsoft.com/en-us/library/windows/hardware/dn789335">Hardware notifications support</a></dt>
<dt>
<a href="https://msdn.microsoft.com/405ff6db-9bc0-42f3-a740-49dd3967a8b3">Hardware notifications reference</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [gpiobtn\gpiobtn]:%20HWN_CLX_EXPORT_INDEX enumeration%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
