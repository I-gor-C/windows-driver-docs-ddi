---
UID: NE.d3dkmddi._DXGK_POWER_COMPONENT_TYPE
title: DXGK_POWER_COMPONENT_TYPE
author: windows-driver-content
description: Indicates the power component type that is reported by the display miniport driver to the Microsoft DirectX graphics kernel subsystem.
old-location: display\dxgk_power_component_type.htm
old-project: display
ms.assetid: fe732082-5aa1-4265-a76a-bd2e5b733557
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_POWER_COMPONENT_TYPE
req.alt-loc: D3dkmddi.h
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

# DXGK_POWER_COMPONENT_TYPE enumeration



## -description
<p>Indicates the power component type that is reported by the display miniport driver to the Microsoft DirectX graphics kernel subsystem.</p>


## -syntax

````
typedef enum _DXGK_POWER_COMPONENT_TYPE { 
  DXGK_POWER_COMPONENT_ENGINE           = 0,
  DXGK_POWER_COMPONENT_MONITOR          = 1,
  DXGK_POWER_COMPONENT_MONITOR_REFRESH  = 2,
  DXGK_POWER_COMPONENT_OTHER            = 5,
  DXGK_POWER_COMPONENT_MAX              = 6
} DXGK_POWER_COMPONENT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="DXGK_POWER_COMPONENT_ENGINE"></a><a id="dxgk_power_component_engine"></a><b>DXGK_POWER_COMPONENT_ENGINE</b>

<dd>
<p>Indicates that the component is a  GPU engine.</p>
<div class="alert"><b>Note</b>  An engine can have only one power component assigned.</div>
<div> </div>
</dd>

### -field <a id="DXGK_POWER_COMPONENT_MONITOR"></a><a id="dxgk_power_component_monitor"></a><b>DXGK_POWER_COMPONENT_MONITOR</b>

<dd>
<p>Indicates a monitor that is connected to a VidPN target and can have its power managed. A typical component of this type is an LCD panel backlight.</p>
</dd>

### -field <a id="DXGK_POWER_COMPONENT_MONITOR_REFRESH"></a><a id="dxgk_power_component_monitor_refresh"></a><b>DXGK_POWER_COMPONENT_MONITOR_REFRESH</b>

<dd>
<p>Indicates hardware that scans out from a VidPN source and generates a signal for a VidPN target.</p>
<p>A typical component of this type is a self-refreshing monitor, which can display the last frame even if the frame buffer stops sending data to the monitor. The display miniport driver should report this component type only if all monitors that can be driven from the VidPN source are self-refreshing.</p>
</dd>

### -field <a id="DXGK_POWER_COMPONENT_OTHER"></a><a id="dxgk_power_component_other"></a><b>DXGK_POWER_COMPONENT_OTHER</b>

<dd>
<p>Indicates a component for which the idle state is managed entirely by the display miniport driver. The DirectX graphics kernel subsystem passes this information to the <a href="https://msdn.microsoft.com/9F2D8ACD-44D5-46E0-9FC7-1B38B99450FF">Power Management Framework</a>.</p>
</dd>

### -field <a id="DXGK_POWER_COMPONENT_MAX"></a><a id="dxgk_power_component_max"></a><b>DXGK_POWER_COMPONENT_MAX</b>

<dd>
<p>A maximum value that is used for testing purposes.</p>
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
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>