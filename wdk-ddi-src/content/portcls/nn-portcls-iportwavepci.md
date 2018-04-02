---
UID: NN:portcls.IPortWavePci
title: IPortWavePci
author: windows-driver-content
description: The IPortWavePci interface is the WavePci port driver's primary interface.
old-location: audio\iportwavepci.htm
old-project: audio
ms.assetid: a3489a6a-e993-4f89-9242-714323ec64ec
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: IPortWavePci, IPortWavePci interface [Audio Devices], IPortWavePci interface [Audio Devices], described, audio.iportwavepci, audmp-routines_4948783a-44c9-42c3-ba67-c3c66a0a2951.xml, portcls/IPortWavePci
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
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
-	portcls.h
api_name:
-	IPortWavePci
product:
- Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IPortWavePci interface

The <code>IPortWavePci</code> interface is the WavePci port driver's primary interface. The PortCls system driver implements this interface and exposes it to the adapter driver that implements the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536724">IMiniportWavePci</a> object. The <code>IPortWavePci</code> interface provides notification and DMA services to the miniport object. An adapter driver creates an <code>IPortWavePci</code> object by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff537715">PcNewPort</a> and specifying REFIID <b>IID_IPortWavePci</b>. <code>IPortWavePci</code> inherits from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536842">IPort</a> interface.

An adapter driver forms a miniport/port driver pair by binding an <b>IMiniportWavePci</b> object to an <code>IPortWavePci</code> object. The PortCls system driver registers this pair with the system as a <a href="https://msdn.microsoft.com/9e364c8f-55c3-4ec9-a9ce-9ee0f6a0746b">wave filter</a>.

## Methods

<p>The <b>IPortWavePci</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPortWavePci::NewMasterDmaChannel](nf-portcls-iportwavepci-newmasterdmachannel.md) | The NewMasterDmaChannel method creates a new instance of a bus-master DMA channel. |
| [IPortWavePci::Notify](nf-portcls-iportwavepci-notify.md) | The Notify method notifies the port driver that an interrupt indicating the progress of the DMA pointer has occurred. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | portcls.h |