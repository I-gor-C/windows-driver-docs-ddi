---
UID: NS.minitape._SES_STATUS_DESCRIPTOR
title: SES_STATUS_DESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 8eb950b1-b739-45cc-b942-d92b8f3ed34c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SES_STATUS_DESCRIPTOR, SES_STATUS_DESCRIPTOR, *PSES_STATUS_DESCRIPTOR
req.header: minitape.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# SES_STATUS_DESCRIPTOR structure

## -description



## -struct-fields

### -field union __unnamed_union_0c03_67			
 	
### -field UCHAR  : 4 ElementStatus			
 	
### -field UCHAR  : 1 Swap			
 	
### -field UCHAR  : 1 Disabled			
 	
### -field UCHAR  : 1 PredictedFailure			
 	
### -field UCHAR  : 1 Reserved1			
 	
### -field UCHAR SlotAddress			
 	
### -field UCHAR  : 1 Report			
 	
### -field UCHAR  : 1 Identify			
 	
### -field UCHAR  : 1 Remove			
 	
### -field UCHAR  : 1 ReadyToInsert			
 	
### -field UCHAR  : 1 EnclosureBypassedB			
 	
### -field UCHAR  : 1 EnclosureBypassedA			
 	
### -field UCHAR  : 1 DoNotRemove			
 	
### -field UCHAR  : 1 AppBypassedA			
 	
### -field UCHAR  : 1 DeviceBypassedB			
 	
### -field UCHAR  : 1 DeviceBypassedA			
 	
### -field UCHAR  : 1 BypassedB			
 	
### -field UCHAR  : 1 BypassedA			
 	
### -field UCHAR  : 1 DeviceOff			
 	
### -field UCHAR  : 1 FaultRequested			
 	
### -field UCHAR  : 1 FaultSensed			
 	
### -field UCHAR  : 1 AppBypassedB			
 	
### -field UCHAR  : 7 Reserved1			
 	
### -field UCHAR  : 1 Identify			
 	
### -field UCHAR  : 1 Reserved2			
 	
### -field UCHAR  : 1 DCOverCurrent			
 	
### -field UCHAR  : 1 DCUnderVoltage			
 	
### -field UCHAR  : 1 DCOverVoltage			
 	
### -field UCHAR  : 4 Reserved3			
 	
### -field UCHAR  : 1 DCFail			
 	
### -field UCHAR  : 1 ACFail			
 	
### -field UCHAR  : 1 TemperatureWarning			
 	
### -field UCHAR  : 1 OverTemperatureFail			
 	
### -field UCHAR  : 1 Off			
 	
### -field UCHAR  : 1 RequestedOn			
 	
### -field UCHAR  : 1 Fail			
 	
### -field UCHAR  : 1 HotSwap			
 	
### -field UCHAR  : 3 ActualFanSpeedMSB			
 	
### -field UCHAR  : 4 Reserved1			
 	
### -field UCHAR  : 1 Identify			
 	
### -field UCHAR ActualFanSpeedLSB			
 	
### -field UCHAR  : 3 ActualSpeedCode			
 	
### -field UCHAR  : 1 Reserved2			
 	
### -field UCHAR  : 1 Off			
 	
### -field UCHAR  : 1 RequestedOn			
 	
### -field UCHAR  : 1 Fail			
 	
### -field UCHAR  : 1 HotSwap			
 	
### -field UCHAR  : 6 Reserved1			
 	
### -field UCHAR  : 1 Fail			
 	
### -field UCHAR  : 1 Identify			
 	
### -field UCHAR Temperature			
 	
### -field UCHAR  : 1 UnderTemperatureWarning			
 	
### -field UCHAR  : 1 UnderTemperatureFailure			
 	
### -field UCHAR  : 1 OverTemperatureWarning			
 	
### -field UCHAR  : 1 OverTemperatureFailure			
 	
### -field UCHAR  : 4 Reserved2			
 	
### -field UCHAR  : 1 CritUnder			
 	
### -field UCHAR  : 1 CritOver			
 	
### -field UCHAR  : 1 WarnUnder			
 	
### -field UCHAR  : 1 WarnOver			
 	
### -field UCHAR  : 2 Reserved1			
 	
### -field UCHAR  : 1 Fail			
 	
### -field UCHAR  : 1 Identify			
 	
### -field UCHAR VoltageMSB			
 	
### -field UCHAR VoltageLSB			
 	
### -field UCHAR  : 1 Reserved1			
 	
### -field UCHAR  : 1 CritOver			
 	
### -field UCHAR  : 1 Reserved2			
 	
### -field UCHAR  : 1 WarnOver			
 	
### -field UCHAR  : 2 Reserved3			
 	
### -field UCHAR  : 1 Fail			
 	
### -field UCHAR  : 1 Identify			
 	
### -field UCHAR CurrentMSB			
 	
### -field UCHAR CurrentLSB			
 	
### -field UCHAR  : 7 Reserved1			
 	
### -field UCHAR  : 1 Identify			
 	
### -field UCHAR  : 1 WarningIndication			
 	
### -field UCHAR  : 1 FailureIndication			
 	
### -field UCHAR  : 6 TimeUntilPowerCycle			
 	
### -field UCHAR  : 1 WarningRequested			
 	
### -field UCHAR  : 1 FailureRequested			
 	
### -field UCHAR  : 6 RequestedPowerOffTime			
 	
### -field UCHAR  : 1 RebuildAbort			
 	
### -field UCHAR  : 1 Rebuild			
 	
### -field UCHAR  : 1 InFailedArray			
 	
### -field UCHAR  : 1 InCriticalArray			
 	
### -field UCHAR  : 1 ConsistencyCheck			
 	
### -field UCHAR  : 1 HotSpare			
 	
### -field UCHAR  : 1 ReservedDevice			
 	
### -field UCHAR  : 1 OK			
 	
### -field UCHAR  : 1 Report			
 	
### -field UCHAR  : 1 Identify			
 	
### -field UCHAR  : 1 Remove			
 	
### -field UCHAR  : 1 ReadyToInsert			
 	
### -field UCHAR  : 1 EnclosureBypassedB			
 	
### -field UCHAR  : 1 EnclosureBypassedA			
 	
### -field UCHAR  : 1 DoNotRemove			
 	
### -field UCHAR  : 1 AppBypassedA			
 	
### -field UCHAR  : 1 DeviceBypassedB			
 	
### -field UCHAR  : 1 DeviceBypassedA			
 	
### -field UCHAR  : 1 BypassedB			
 	
### -field UCHAR  : 1 BypassedA			
 	
### -field UCHAR  : 1 DeviceOff			
 	
### -field UCHAR  : 1 FaultRequested			
 	
### -field UCHAR  : 1 FaultSensed			
 	
### -field UCHAR  : 1 AppBypassedB			
 	
## -remarks

## -see-also