---
UID: NN:portcls.IMiniportWaveRTStreamNotification
title: IMiniportWaveRTStreamNotification
author: windows-driver-content
description: The IMiniportWaveRTStreamNotification interface is supported in Windows Vista and later Windows operating systems, and it augments the IMiniportWaveRTStream interface, providing additional methods to facilitate DMA driver event notifications.
old-location: audio\iminiportwavertstreamnotification.htm
old-project: audio
ms.assetid: e009c459-77f7-43ee-9e95-8408324b0a9b
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: audio.iminiportwavertstreamnotification, IMiniportWaveRTStreamNotification interface [Audio Devices], IMiniportWaveRTStreamNotification interface [Audio Devices], described, IMiniportWaveRTStreamNotification, portcls/IMiniportWaveRTStreamNotification, audmp-routines_a49bf74b-367b-44f4-b8de-a3adf6240b36.xml
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	portcls.h
apiname:
-	IMiniportWaveRTStreamNotification
product: Windows
targetos: Windows
req.typenames: "*PPC_EXIT_LATENCY, PC_EXIT_LATENCY"
---

# IMiniportWaveRTStreamNotification interface

The <code>IMiniportWaveRTStreamNotification</code> interface is supported in Windows Vista and later Windows operating systems, and it augments the <a href="..\portcls\nn-portcls-iminiportwavertstream.md">IMiniportWaveRTStream</a> interface, providing additional methods to facilitate DMA driver event notifications. 

To access the <code>IMiniportWaveRTStreamNotification</code> interface, the <a href="https://msdn.microsoft.com/d25e37e2-2e29-4bf9-8150-221ebef88c87">WaveRT port driver</a> calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536762">IMiniportWaveRT::NewStream</a> method and receives an <a href="..\portcls\nn-portcls-iminiportwavertstream.md">IMiniportWaveRTStream</a> interface. The WaveRT port driver then queries the <b>IMiniportWaveRTStream</b> interface, uisng QueryInterface, and receives the <code>IMiniportWaveRTStreamNotification</code> interface. 

<code>IMiniportWaveRTStreamNotification</code> inherits from the <b>IUnknown</b> interface.

## Methods

<p>The <b>IMiniportWaveRTStreamNotification</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [portcls.IMiniportWaveRTStreamNotification.AllocateBufferWithNotification](nf-portcls-iminiportwavertstreamnotification-allocatebufferwithnotification.md) | The AllocateAudioBufferWithNotification method allocates a cyclic buffer for audio data when you want to implement DMA-driven event notification. If you do not want event notification, you must use IMiniportWaveRTStream::AllocateAudioBuffer. |
| [portcls.IMiniportWaveRTStreamNotification.FreeBufferWithNotification](nf-portcls-iminiportwavertstreamnotification-freebufferwithnotification.md) | The FreeBufferWithNotification method is used to free an audio buffer previously allocated with a call to IMiniportWaveRTStreamNotification::AllocateBufferWithNotification. |
| [portcls.IMiniportWaveRTStreamNotification.RegisterNotificationEvent](nf-portcls-iminiportwavertstreamnotification-registernotificationevent.md) | The RegisterNotificationEvent method registers an event to be notified for DMA-driven event notification. |
| [portcls.IMiniportWaveRTStreamNotification.UnregisterNotificationEvent](nf-portcls-iminiportwavertstreamnotification-unregisternotificationevent.md) | The UnregisterNotificationEvent method unregisters an event from DMA driven event notification. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | portcls.h |