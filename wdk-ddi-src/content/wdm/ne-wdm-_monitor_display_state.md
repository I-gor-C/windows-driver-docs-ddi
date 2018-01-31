---
UID : NE:wdm._MONITOR_DISPLAY_STATE
title : "_MONITOR_DISPLAY_STATE"
author : windows-driver-content
description : Indicates the power state of the monitor being displayed on.
old-location : kernel\monitor_display_state.htm
old-project : kernel
ms.assetid : 50F5C1AD-BA51-4376-8093-E8596265FDAF
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : "*PMONITOR_DISPLAY_STATE, wdm/MONITOR_DISPLAY_STATE, wdm/PowerMonitorOff, wdm/PowerMonitorDim, MONITOR_DISPLAY_STATE, kernel.monitor_display_state, PowerMonitorOn, PowerMonitorOff, PowerMonitorDim, wdm/PowerMonitorOn, _MONITOR_DISPLAY_STATE, MONITOR_DISPLAY_STATE enumeration [Kernel-Mode Driver Architecture]"
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : wdm.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PMONITOR_DISPLAY_STATE, MONITOR_DISPLAY_STATE"
req.product : Windows 10 or later.
---

# _MONITOR_DISPLAY_STATE Enumeration
Indicates the power state of the monitor being displayed on.

## Syntax
````
typedef enum _MONITOR_DISPLAY_STATE { 
  PowerMonitorOff  = 0,
  PowerMonitorOn,
  PowerMonitorDim
} MONITOR_DISPLAY_STATE;
````

## Constants

<table>

<tr>
<td>PowerMonitorDim</td>
<td>This indicates that the monitor is dim.</td>
</tr>

<tr>
<td>PowerMonitorOff</td>
<td>This indicates that the monitor is off.</td>
</tr>

<tr>
<td>PowerMonitorOn</td>
<td>This indicates that the monitor is on.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h |