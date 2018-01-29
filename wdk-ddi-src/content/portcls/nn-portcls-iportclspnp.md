---
UID : NN:portcls.IPortClsPnp
title : IPortClsPnp
author : windows-driver-content
description : IPortClsPnp is the PnP management interface that the port class driver (PortCls) exposes to the adapter.
old-location : audio\iportclspnp.htm
old-project : audio
ms.assetid : AC04051E-8412-4B61-B452-C05A9D8D5CD9
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : audio.iportclspnp, IPortClsPnp interface [Audio Devices], IPortClsPnp interface [Audio Devices], described, IPortClsPnp, portcls/IPortClsPnp
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
req.typenames : PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IPortClsPnp interface

<code>IPortClsPnp</code> is the PnP management interface that the port class driver (PortCls) exposes to the adapter.

For more information,  see <a href="https://msdn.microsoft.com/FCAD7F8B-AA9B-430A-BCAF-04E13FA15382">Implement PnP Rebalance for PortCls Audio Drivers</a>.

The <code>IPortClsPnp</code> interface is available in Windows 10, version 1511 and later versions of Windows.

## Methods

<p>The <b>IPortClsPnp</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [portcls.IPortClsPnp.RegisterAdapterPnpManagement](nf-portcls-iportclspnp-registeradapterpnpmanagement.md) | The RegisterAdapterPowerManagement method registers the PnP management interface of the adapter with PortCls. |
| [portcls.IPortClsPnp.UnregisterAdapterPnpManagement](nf-portcls-iportclspnp-unregisteradapterpnpmanagement.md) | The UnRegisterAdapterPowerManagement method unregisters the PnP management interface of the adapter from PortCls. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | portcls.h |
| **DLL** |  |