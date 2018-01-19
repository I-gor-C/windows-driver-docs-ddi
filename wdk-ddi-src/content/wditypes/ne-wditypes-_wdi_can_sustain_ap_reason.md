---
UID : NE:wditypes._WDI_CAN_SUSTAIN_AP_REASON
title : _WDI_CAN_SUSTAIN_AP_REASON
author : windows-driver-content
description : The WDI_CAN_SUSTAIN_AP_REASON enumeration defines the reasons the port is ready to receive a OID_WDI_TASK_START_AP request.
old-location : netvista\wdi_can_sustain_ap_reason.htm
old-project : netvista
ms.assetid : 9AAE4B3F-7C5C-457D-9388-63E6E6AB8A2E
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _WDI_CAN_SUSTAIN_AP_REASON, WDI_CAN_SUSTAIN_AP_REASON
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : wditypes.hpp
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : WDI_CAN_SUSTAIN_AP_REASON
req.alt-loc : wditypes.hpp
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : WDI_CAN_SUSTAIN_AP_REASON
req.product : Windows 10 or later.
---

# _WDI_CAN_SUSTAIN_AP_REASON Enumeration
The WDI_CAN_SUSTAIN_AP_REASON enumeration defines the reasons the port is ready to receive a <a href="https://msdn.microsoft.com/library/windows/hardware/dn925964">OID_WDI_TASK_START_AP</a> request.

## Syntax
````
typedef enum _WDI_CAN_SUSTAIN_AP_REASON { 
  WDI_CAN_SUSTAIN_AP_REASON_IHV_START  = 0xFF000000,
  WDI_CAN_SUSTAIN_AP_REASON_IHV_END    = 0xFFFFFFFF
} WDI_CAN_SUSTAIN_AP_REASON;
````

## Constants

<table>

<tr>
<td>WDI_CAN_SUSTAIN_AP_REASON_IHV_END</td>
<td>The end value of possible IHV-specified reasons.</td>
</tr>

<tr>
<td>WDI_CAN_SUSTAIN_AP_REASON_IHV_START</td>
<td>The start value of possible IHV-specified reasons.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wditypes.hpp |