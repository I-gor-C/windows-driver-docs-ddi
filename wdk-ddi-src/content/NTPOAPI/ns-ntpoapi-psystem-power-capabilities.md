---
UID: NS.ntpoapi.PSYSTEM_POWER_CAPABILITIES
title: PSYSTEM_POWER_CAPABILITIES
author: windows-driver-content
description: 
ms.assetid: a192f4e7-8647-40f4-b756-eed37f11545a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PSYSTEM_POWER_CAPABILITIES, SYSTEM_POWER_CAPABILITIES, *PSYSTEM_POWER_CAPABILITIES
req.header: ntpoapi.h
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

# PSYSTEM_POWER_CAPABILITIES structure

## -description



## -struct-fields

### -field BOOLEAN PowerButtonPresent			
 	
### -field BOOLEAN SleepButtonPresent			
 	
### -field BOOLEAN LidPresent			
 	
### -field BOOLEAN SystemS1			
 	
### -field BOOLEAN SystemS2			
 	
### -field BOOLEAN SystemS3			
 	
### -field BOOLEAN SystemS4			
 	
### -field BOOLEAN SystemS5			
 	
### -field BOOLEAN HiberFilePresent			
 	
### -field BOOLEAN FullWake			
 	
### -field BOOLEAN VideoDimPresent			
 	
### -field BOOLEAN ApmPresent			
 	
### -field BOOLEAN UpsPresent			
 	
### -field BOOLEAN ThermalControl			
 	
### -field BOOLEAN ProcessorThrottle			
 	
### -field UCHAR ProcessorMinThrottle			
 	
### -field UCHAR ProcessorThrottleScale			
 	
### -field UCHAR [4] spare2			
 	
### -field UCHAR ProcessorMaxThrottle			
 	
### -field BOOLEAN FastSystemS4			
 	
### -field BOOLEAN Hiberboot			
 	
### -field BOOLEAN WakeAlarmPresent			
 	
### -field BOOLEAN AoAc			
 	
### -field BOOLEAN DiskSpinDown			
 	
### -field UCHAR [8] spare3			
 	
### -field UCHAR HiberFileType			
 	
### -field BOOLEAN AoAcConnectivitySupported			
 	
### -field UCHAR [6] spare3			
 	
### -field BOOLEAN SystemBatteriesPresent			
 	
### -field BOOLEAN BatteriesAreShortTerm			
 	
### -field BATTERY_REPORTING_SCALE [3] BatteryScale			
 	
### -field SYSTEM_POWER_STATE AcOnLineWake			
 	
### -field SYSTEM_POWER_STATE SoftLidWake			
 	
### -field SYSTEM_POWER_STATE RtcWake			
 	
### -field SYSTEM_POWER_STATE MinDeviceWakeState			
 	
### -field SYSTEM_POWER_STATE DefaultLowLatencyWake			
 	
## -remarks

## -see-also