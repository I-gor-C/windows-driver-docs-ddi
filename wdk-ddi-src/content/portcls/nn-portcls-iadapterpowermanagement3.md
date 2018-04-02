---
UID: NN:portcls.IAdapterPowerManagement3
title: IAdapterPowerManagement3
author: windows-driver-content
description: The IAdapterPowerManagement3 interface inherits from IUnknown, and it is used for receiving power management messages.
old-location: audio\iadapterpowermanagement3.htm
old-project: audio
ms.assetid: 5F0729DB-C991-4745-9550-9D25D6836A1F
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: IAdapterPowerManagement3, IAdapterPowerManagement3 interface [Audio Devices], IAdapterPowerManagement3 interface [Audio Devices], described, audio.iadapterpowermanagement3, portcls/IAdapterPowerManagement3
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	Portcls.h
api_name:
-	IAdapterPowerManagement3
product: Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IAdapterPowerManagement3 interface

The IAdapterPowerManagement3 interface inherits from <b>IUnknown</b>, and it is used for receiving power management messages.

To register this interface with PortCls, the adapter driver must call  <a href="https://msdn.microsoft.com/library/windows/hardware/ff537724">PcRegisterAdapterPowerManagement</a>.
<div class="alert"><b>Note</b>  If you want to fill the <a href="http://go.microsoft.com/fwlink/p/?linkid=143127">caps structure</a> for your device, your adapter driver can call <b>PcRegisterAdapterPowerManagement</b> from within the <a href="http://msdn.microsoft.com/en-us/library/windows/hardware/ff540521(v=vs.85).aspx">AddDevice</a> routine, or before your driver calls <b>AddDevice.</b></div><div> </div>

## Methods

<p>The <b>IAdapterPowerManagement3</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IAdapterPowerManagement3::D3ExitLatencyChanged](nf-portcls-iadapterpowermanagement3-d3exitlatencychanged.md) | PortCls calls the D3ExitLatencyChanged method while the device is in sleep (D3) power state, to provide a new exit latency value. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | portcls.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff536486">IAdapterPowerManagement2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff537724">PcRegisterAdapterPowerManagement</a>