---
UID : NE:d3dkmddi._DXGK_POWER_COMPONENT_TYPE
title : _DXGK_POWER_COMPONENT_TYPE
author : windows-driver-content
description : Indicates the power component type that is reported by the display miniport driver to the Microsoft DirectX graphics kernel subsystem.
old-location : display\dxgk_power_component_type.htm
old-project : display
ms.assetid : fe732082-5aa1-4265-a76a-bd2e5b733557
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_POWER_COMPONENT_TYPE, DXGK_POWER_COMPONENT_TYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dkmddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXGK_POWER_COMPONENT_TYPE
req.alt-loc : D3dkmddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : DXGK_POWER_COMPONENT_TYPE
---

# _DXGK_POWER_COMPONENT_TYPE Enumeration
Indicates the power component type that is reported by the display miniport driver to the Microsoft DirectX graphics kernel subsystem.

## Syntax
````
typedef enum _DXGK_POWER_COMPONENT_TYPE { 
  DXGK_POWER_COMPONENT_ENGINE           = 0,
  DXGK_POWER_COMPONENT_MONITOR          = 1,
  DXGK_POWER_COMPONENT_MONITOR_REFRESH  = 2,
  DXGK_POWER_COMPONENT_OTHER            = 5,
  DXGK_POWER_COMPONENT_MAX              = 6
} DXGK_POWER_COMPONENT_TYPE;
````

## Constants

<table>

<tr>
<td>DXGK_POWER_COMPONENT_ENGINE</td>
<td>Indicates that the component is a  GPU engine.

<div class="alert"><b>Note</b>  An engine can have only one power component assigned.</div>
<div> </div></td>
</tr>

<tr>
<td>DXGK_POWER_COMPONENT_MAX</td>
<td>A maximum value that is used for testing purposes.</td>
</tr>

<tr>
<td>DXGK_POWER_COMPONENT_MONITOR</td>
<td>Indicates a monitor that is connected to a VidPN target and can have its power managed. A typical component of this type is an LCD panel backlight.</td>
</tr>

<tr>
<td>DXGK_POWER_COMPONENT_MONITOR_REFRESH</td>
<td>Indicates hardware that scans out from a VidPN source and generates a signal for a VidPN target.

A typical component of this type is a self-refreshing monitor, which can display the last frame even if the frame buffer stops sending data to the monitor. The display miniport driver should report this component type only if all monitors that can be driven from the VidPN source are self-refreshing.</td>
</tr>

<tr>
<td>DXGK_POWER_COMPONENT_OTHER</td>
<td>Indicates a component for which the idle state is managed entirely by the display miniport driver. The DirectX graphics kernel subsystem passes this information to the <a href="https://msdn.microsoft.com/9F2D8ACD-44D5-46E0-9FC7-1B38B99450FF">Power Management Framework</a>.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h |