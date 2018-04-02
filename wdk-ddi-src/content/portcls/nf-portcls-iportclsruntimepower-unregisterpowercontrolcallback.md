---
UID: NF:portcls.IPortClsRuntimePower.UnregisterPowerControlCallback
title: IPortClsRuntimePower::UnregisterPowerControlCallback method
author: windows-driver-content
description: The port class driver (PortCls) uses the UnregisterPowerControlCallback method to unregister a power control callback.
old-location: audio\iportclsruntimepower_unregisterpowercontrolcallback.htm
old-project: audio
ms.assetid: F7E83587-0499-4D56-8D34-5513454FFEE2
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: IPortClsRuntimePower, IPortClsRuntimePower interface [Audio Devices], UnregisterPowerControlCallback method, IPortClsRuntimePower::UnregisterPowerControlCallback, UnregisterPowerControlCallback method [Audio Devices], UnregisterPowerControlCallback method [Audio Devices], IPortClsRuntimePower interface, UnregisterPowerControlCallback,IPortClsRuntimePower.UnregisterPowerControlCallback, audio.iportclsruntimepower_unregisterpowercontrolcallback, portcls/IPortClsRuntimePower::UnregisterPowerControlCallback
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 7
req.target-min-winversvr: Windows Server 2003
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
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
-	Portcls.h
api_name:
-	IPortClsRuntimePower.UnregisterPowerControlCallback
product: Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---


# IPortClsRuntimePower::UnregisterPowerControlCallback method
The port class driver (PortCls) uses the <code>UnregisterPowerControlCallback</code>  method to unregister a power control callback.

## Syntax

```
NTSTATUS UnregisterPowerControlCallback(
  PDEVICE_OBJECT _DeviceObject
);
```

## Parameters

`_DeviceObject`

The device object.


## Return Value

The <code>UnregisterPowerControlCallback</code> method returns STATUS_SUCCESS, if the call is successful. Otherwise, it returns the appropriate error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 7 Windows Server 2003 |
| **Target Platform** | Universal |
| **Header** | portcls.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn265125">IPortClsRuntimePower</a>