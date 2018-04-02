---
UID: NN:wdtfsimulatedbatterysystemaction.IWDTFSimulatedBatterySystemAction
title: IWDTFSimulatedBatterySystemAction
author: windows-driver-content
description: IWDTFSimulatedBatterySystemAction Interface
old-location: dtf\iwdtfsimulatedbatterysystemaction.htm
old-project: dtf
ms.assetid: 38df72bd-5206-4655-846c-ae925ed648eb
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IWDTFSimulatedBatterySystemAction, IWDTFSimulatedBatterySystemAction interface [Windows Device Testing Framework], IWDTFSimulatedBatterySystemAction interface [Windows Device Testing Framework], described, dtf.iwdtfsimulatedbatterysystemaction, wdtfsimulatedbatterysystemaction/IWDTFSimulatedBatterySystemAction
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtfsimulatedbatterysystemaction.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFSimulatedBatterySystemAction.idl
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	wdtfsimulatedbatterysystemaction.h
api_name:
-	IWDTFSimulatedBatterySystemAction
product:
- Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFSimulatedBatterySystemAction interface

IWDTFSimulatedBatterySystemAction Interface

## Methods

<p>The <b>IWDTFSimulatedBatterySystemAction</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFSimulatedBatterySystemAction::DisableRealBatteries](nf-wdtfsimulatedbatterysystemaction-iwdtfsimulatedbatterysystemaction-disablerealbatteries.md) | Disables real batteries if they are present in the system. |
| [IWDTFSimulatedBatterySystemAction::DisableSimulatedBattery](nf-wdtfsimulatedbatterysystemaction-iwdtfsimulatedbatterysystemaction-disablesimulatedbattery.md) | Disables the simulated battery. |
| [IWDTFSimulatedBatterySystemAction::EnableRealBatteries](nf-wdtfsimulatedbatterysystemaction-iwdtfsimulatedbatterysystemaction-enablerealbatteries.md) | Enables real batteries if they are present in the system. |
| [IWDTFSimulatedBatterySystemAction::EnableSimulatedBattery](nf-wdtfsimulatedbatterysystemaction-iwdtfsimulatedbatterysystemaction-enablesimulatedbattery.md) | Enables the simulated battery. |
| [IWDTFSimulatedBatterySystemAction::SetSimulatedBatteryChargePercentage](nf-wdtfsimulatedbatterysystemaction-iwdtfsimulatedbatterysystemaction-setsimulatedbatterychargepercentage.md) | Sets the charge percentage reported to the OS by the simulated battery. |
| [IWDTFSimulatedBatterySystemAction::SetSimulatedBatteryToAC](nf-wdtfsimulatedbatterysystemaction-iwdtfsimulatedbatterysystemaction-setsimulatedbatterytoac.md) | Sets the simulated battery status to AC power. |
| [IWDTFSimulatedBatterySystemAction::SetSimulatedBatteryToDC](nf-wdtfsimulatedbatterysystemaction-iwdtfsimulatedbatterysystemaction-setsimulatedbatterytodc.md) | Sets the simulated battery status to DC power. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Target Platform** | Windows |
| **Header** | wdtfsimulatedbatterysystemaction.h |