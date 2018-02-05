---
UID : NN:portcls.IPortClsRuntimePower
title : IPortClsRuntimePower
author : windows-driver-content
description : IPortClsRuntimePower is the interface that the port class driver (PortCls) uses for accessing the runtime power management capabilities of the audio adapter.
old-location : audio\iportclsruntimepower.htm
old-project : audio
ms.assetid : 8D03B2A0-6C8C-4EBE-86F4-70C8DE179947
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : audio.iportclsruntimepower, IPortClsRuntimePower interface [Audio Devices], IPortClsRuntimePower interface [Audio Devices], described, IPortClsRuntimePower, portcls/IPortClsRuntimePower
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : portcls.h
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
req.lib : Portcls.lib
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PPC_EXIT_LATENCY, PC_EXIT_LATENCY"
---

# IPortClsRuntimePower interface

IPortClsRuntimePower is the interface that the port class driver (PortCls)  uses for accessing the runtime power management capabilities of the audio adapter.

## Methods

<p>The <b>IPortClsRuntimePower</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [portcls.IPortClsRuntimePower.RegisterPowerControlCallback](nf-portcls-iportclsruntimepower-registerpowercontrolcallback.md) | The port class driver (PortCls) uses the RegisterPowerControlCallback method to register a power control callback. |
| [portcls.IPortClsRuntimePower.SendPowerControl](nf-portcls-iportclsruntimepower-sendpowercontrol.md) | The port class driver (PortCls) uses the SendPowerControl method to send power control codes to the audio adapter. |
| [portcls.IPortClsRuntimePower.UnregisterPowerControlCallback](nf-portcls-iportclsruntimepower-unregisterpowercontrolcallback.md) | The port class driver (PortCls) uses the UnregisterPowerControlCallback method to unregister a power control callback. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | portcls.h |