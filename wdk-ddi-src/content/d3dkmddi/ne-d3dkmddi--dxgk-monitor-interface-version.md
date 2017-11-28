---
UID: NE.d3dkmddi._DXGK_MONITOR_INTERFACE_VERSION
title: DXGK_MONITOR_INTERFACE_VERSION
author: windows-driver-content
description: Indicates a particular version of the Monitor interface.
old-location: display\dxgk_monitor_interface_version.htm
old-project: display
ms.assetid: 76af0d70-f9bb-4768-9bfd-f2aaeb212db0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MONITOR_INTERFACE_VERSION
req.alt-loc: d3dkmddi.h
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

# DXGK_MONITOR_INTERFACE_VERSION enumeration



## -description
<p>The <b>DXGK_MONITOR_INTERFACE_VERSION</b> enumeration indicates a particular version of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568433">Monitor interface</a>.</p>


## -syntax

````
typedef enum _DXGK_MONITOR_INTERFACE_VERSION { 
  DXGK_MONITOR_INTERFACE_VERSION_UNINITIALIZED  = 0,
  DXGK_MONITOR_INTERFACE_VERSION_V1             = 1,
  DXGK_MONITOR_INTERFACE_VERSION_V2             = 2
} DXGK_MONITOR_INTERFACE_VERSION;
````


## -enum-fields
<dl>

### -field <a id="DXGK_MONITOR_INTERFACE_VERSION_UNINITIALIZED"></a><a id="dxgk_monitor_interface_version_uninitialized"></a><b>DXGK_MONITOR_INTERFACE_VERSION_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type DXGK_MONITOR_INTERFACE_VERSION has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="DXGK_MONITOR_INTERFACE_VERSION_V1"></a><a id="dxgk_monitor_interface_version_v1"></a><b>DXGK_MONITOR_INTERFACE_VERSION_V1</b>

<dd>
<p>Indicates version 1, available in Windows Vista and later versions of the Windows operating systems.</p>
</dd>

### -field <a id="DXGK_MONITOR_INTERFACE_VERSION_V2"></a><a id="dxgk_monitor_interface_version_v2"></a><b>DXGK_MONITOR_INTERFACE_VERSION_V2</b>

<dd>
<p>
      Indicates version 2, available in Windows 7 and later versions of the Windows operating systems.
     </p>
</dd>
</dl>

## -remarks
<p>The <b>Version</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561949">DXGK_MONITOR_INTERFACE</a> structure is a value from the <b>DXGK_MONITOR_INTERFACE_VERSION</b> enumeration.</p>

<p>The <b>Version</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561949">DXGK_MONITOR_INTERFACE</a> structure is a value from the <b>DXGK_MONITOR_INTERFACE_VERSION</b> enumeration.</p>

<p>The <b>Version</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561949">DXGK_MONITOR_INTERFACE</a> structure is a value from the <b>DXGK_MONITOR_INTERFACE_VERSION</b> enumeration.</p>

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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>