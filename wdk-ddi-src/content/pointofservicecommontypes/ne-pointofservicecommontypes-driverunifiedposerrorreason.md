---
UID : NE:pointofservicecommontypes.DriverUnifiedPosErrorReason
title : DriverUnifiedPosErrorReason
author : windows-driver-content
description : This enumeration indicates the reason for the error.
old-location : pos\unifiedposerrorreason.htm
old-project : pos
ms.assetid : 2bbf5fcf-666e-4265-95cf-7e04670d59da
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : Offline, pointofservicecommontypes/Extended, DriverUnifiedPosErrorReason, Illegal, pointofservicecommontypes/Busy, Timeout, pointofservicecommontypes/UnknownErrorReason, NoService, pointofservicecommontypes/NoService, pos.unifiedposerrorreason, Busy, DriverUnifiedPosErrorReason enumeration, pointofservicecommontypes/Timeout, Extended, pointofservicecommontypes/Disabled, Closed, Disabled, pointofservicecommontypes/Illegal, pointofservicecommontypes/ NoHardware, Failure, NoHardware, pointofservicecommontypes/Offline, UnknownErrorReason, pointofservicecommontypes/Failure, pointofservicecommontypes/Closed, pointofservicecommontypes/DriverUnifiedPosErrorReason
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : pointofservicecommontypes.h
req.include-header : Pointofservicecommontypes.h
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
req.irql : Called at PASSIVE_LEVEL.
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DriverUnifiedPosErrorReason
---

# DriverUnifiedPosErrorReason Enumeration
This enumeration indicates the reason for the error.

## Syntax
````
typedef enum _DriverUnifiedPosErrorReason { 
  UnknownErrorReason  = 0,
  NoService           = 1,
  Disabled            = 2,
  Illegal             = 3,
   NoHardware         = 4,
  Closed              = 5,
  Offline             = 6,
  Failure             = 7,
  Timeout             = 8,
  Busy                = 9,
  Extended            = 10
} DriverUnifiedPosErrorReason;
````

## Constants

<table>

<tr>
<td>Busy</td>
<td>The device is busy and cannot complete the operation.</td>
</tr>

<tr>
<td>Closed</td>
<td>The device is closed.</td>
</tr>

<tr>
<td>Disabled</td>
<td>The device must be enabled in order to perform the operation.</td>
</tr>

<tr>
<td>Extended</td>
<td>The device returned a vendor specified error.</td>
</tr>

<tr>
<td>Failure</td>
<td>The device is connected and powered on, but it failed to perform the operation.</td>
</tr>

<tr>
<td>Illegal</td>
<td>The function is not available or is not supported on this device.</td>
</tr>

<tr>
<td>NoHardware</td>
<td>The physical device is not connected or not powered on.</td>
</tr>

<tr>
<td>NoService</td>
<td>Cannot communicate with the device due to the current configuration.</td>
</tr>

<tr>
<td>Offline</td>
<td>The device is offline.</td>
</tr>

<tr>
<td>Timeout</td>
<td>The operation timed out on the device.</td>
</tr>

<tr>
<td>UnknownErrorReason</td>
<td>The reason for the error is not known.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | pointofservicecommontypes.h (include Pointofservicecommontypes.h) |