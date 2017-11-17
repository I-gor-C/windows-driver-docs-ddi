---
UID: NS.ntpoapi._SYSTEM_POWER_POLICY
title: SYSTEM_POWER_POLICY
author: windows-driver-content
description: 
ms.assetid: 5e950c44-0fa4-4148-b64e-89505c993387
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SYSTEM_POWER_POLICY, SYSTEM_POWER_POLICY, *PSYSTEM_POWER_POLICY
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

# SYSTEM_POWER_POLICY structure

## -description



## -struct-fields

### -field ULONG Revision			
 	
### -field POWER_ACTION_POLICY PowerButton			
 	
### -field POWER_ACTION_POLICY SleepButton			
 	
### -field POWER_ACTION_POLICY LidClose			
 	
### -field SYSTEM_POWER_STATE LidOpenWake			
 	
### -field ULONG Reserved			
 	
### -field POWER_ACTION_POLICY Idle			
 	
### -field ULONG IdleTimeout			
 	
### -field UCHAR IdleSensitivity			
 	
### -field UCHAR DynamicThrottle			
 	
### -field UCHAR [2] Spare2			
 	
### -field SYSTEM_POWER_STATE MinSleep			
 	
### -field SYSTEM_POWER_STATE MaxSleep			
 	
### -field SYSTEM_POWER_STATE ReducedLatencySleep			
 	
### -field ULONG WinLogonFlags			
 	
### -field ULONG Spare3			
 	
### -field ULONG DozeS4Timeout			
 	
### -field ULONG BroadcastCapacityResolution			
 	
### -field SYSTEM_POWER_LEVEL [NUM_DISCHARGE_POLICIES] DischargePolicy			
 	
### -field ULONG VideoTimeout			
 	
### -field BOOLEAN VideoDimDisplay			
 	
### -field ULONG [3] VideoReserved			
 	
### -field ULONG SpindownTimeout			
 	
### -field BOOLEAN OptimizeForPower			
 	
### -field UCHAR FanThrottleTolerance			
 	
### -field UCHAR ForcedThrottle			
 	
### -field UCHAR MinThrottle			
 	
### -field POWER_ACTION_POLICY OverThrottled			
 	
## -remarks

## -see-also