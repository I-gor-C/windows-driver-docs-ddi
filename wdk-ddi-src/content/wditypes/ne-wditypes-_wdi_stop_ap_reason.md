---
UID : NE:wditypes._WDI_STOP_AP_REASON
title : _WDI_STOP_AP_REASON
author : windows-driver-content
description : The WDI_STOP_AP_REASON enumeration defines the reasons an adapter cannot sustain 802.11 Access Point (AP) functionality on any of the PHYs.
old-location : netvista\wdi_stop_ap_reason.htm
old-project : netvista
ms.assetid : F0CACC25-2F7B-431A-8AAB-CBE495178CC1
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _WDI_STOP_AP_REASON, WDI_STOP_AP_REASON
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
req.alt-api : WDI_STOP_AP_REASON
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
req.typenames : WDI_STOP_AP_REASON
req.product : Windows 10 or later.
---

# _WDI_STOP_AP_REASON Enumeration
The WDI_STOP_AP_REASON enumeration defines the reasons an adapter cannot sustain 802.11 Access Point (AP) functionality on any of the PHYs.

## Syntax
````
typedef enum _WDI_STOP_AP_REASON { 
  WDI_STOP_AP_REASON_FREQUENCY_NOT_AVAILABLE  = 1,
  WDI_STOP_AP_REASON_CHANNEL_NOT_AVAILABLE    = 2,
  WDI_STOP_AP_REASON_AP_ACTIVE                = 3,
  WDI_STOP_AP_REASON_IHV_START                = 0xFF000000,
  WDI_STOP_AP_REASON_IHV_END                  = 0xFFFFFFFF
} WDI_STOP_AP_REASON;
````

## Constants

<table>

<tr>
<td>WDI_STOP_AP_REASON_AP_ACTIVE</td>
<td>The adapter determined that an AP is already active on another 802.11 MAC entity for this physical wireless LAN adapter.</td>
</tr>

<tr>
<td>WDI_STOP_AP_REASON_CHANNEL_NOT_AVAILABLE</td>
<td>The adapter determined that no operating channel is available.</td>
</tr>

<tr>
<td>WDI_STOP_AP_REASON_FREQUENCY_NOT_AVAILABLE</td>
<td>The adapter determined that no valid operating frequency is available.</td>
</tr>

<tr>
<td>WDI_STOP_AP_REASON_IHV_END</td>
<td>The end value of possible IHV-specified reasons.</td>
</tr>

<tr>
<td>WDI_STOP_AP_REASON_IHV_START</td>
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