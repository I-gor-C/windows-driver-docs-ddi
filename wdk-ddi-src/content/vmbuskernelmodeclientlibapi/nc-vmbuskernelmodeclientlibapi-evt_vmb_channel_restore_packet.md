---
UID: NC:vmbuskernelmodeclientlibapi.EVT_VMB_CHANNEL_RESTORE_PACKET
title: EVT_VMB_CHANNEL_RESTORE_PACKET
author: windows-driver-content
description: The EvtVmbChannelRestorePacket callback function is invoked when the virtualization service provider (VSP) server endpoint must restore the state associated with a packet object.
old-location: netvista\evt_vmb_channel_restore_packet.htm
old-project: netvista
ms.assetid: 9C89CFCB-4B8A-40D3-B982-2F7836A636A3
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: EVT_VMB_CHANNEL_RESTORE_PACKET, EvtVmbChannelRestorePacket, EvtVmbChannelRestorePacket callback function [Network Drivers Starting with Windows Vista], PFN_VMB_CHANNEL_RESTORE_PACKET, PFN_VMB_CHANNEL_RESTORE_PACKET callback function pointer [Network Drivers Starting with Windows Vista], netvista.evt_vmb_channel_restore_packet, vmbuskernelmodeclientlibapi/EvtVmbChannelRestorePacket
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: vmbuskernelmodeclientlibapi.h
req.include-header: VmbusKernelModeClientLibApi.h
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
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	VmbusKernelModeClientLibApi.h
api_name:
-	PFN_VMB_CHANNEL_RESTORE_PACKET
product: Windows
targetos: Windows
req.typenames: VIDEO_PORT_AGP_SERVICES, *PVIDEO_PORT_AGP_SERVICES
req.product: Windows 10 or later.
---


# EVT_VMB_CHANNEL_RESTORE_PACKET callback function
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

The <i>EvtVmbChannelRestorePacket</i> callback function is invoked when the virtualization service provider (VSP) server
endpoint must restore the state associated with a packet object.

## Syntax

```
EVT_VMB_CHANNEL_RESTORE_PACKET EvtVmbChannelRestorePacket;

NTSTATUS EvtVmbChannelRestorePacket(
  VMBCHANNEL Channel,
  PVOID LibBuf,
  UINT32 LibBufSize,
  PVOID SaveBuf,
  UINT32 SaveBufSize
)
{...}
```

## Parameters

`Channel`

The channel on which the packet arrives.

`LibBuf`

Pointer to packet object state internal to the Kernel Mode Client Library (KMCL).

`LibBufSize`

Size of the <i>LibBuf</i> parameter, in bytes.

`SaveBuf`

Pointer to transaction state specific to the VSP.

`SaveBufSize`

Size of the <i>SaveBuf</i> parameter, in bytes.


## Return Value

<i>EvtVmbChannelRestorePacket</i> returns a status code.

## Remarks

The <a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbserverchannelinitsetsaverestorepacketcallbacks.md">VmbServerChannelInitSetSaveRestorePacketCallbacks</a> function sets a callback function for restoring packets for each channel.

In order
to restore an in-flight packet object, the VSP must allocate a new packet
by using the <a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbpacketallocate.md">VmbPacketAllocate</a> function. The VSP restores the packet to the previous state by passing <i>LibBuf</i> and <i>LibBufSize</i> to the <a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbpacketrestore.md">VmbPacketRestore</a> function.
If the VSP provided any internal state for the transaction in the <i>EvtVmbChannelSavePacket</i>
callback function, then this is provided in <i>SaveBuf</i>, and restored by the VSP.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | vmbuskernelmodeclientlibapi.h (include VmbusKernelModeClientLibApi.h) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbpacketrestore.md">VmbPacketRestore</a>



<a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbpacketallocate.md">VmbPacketAllocate</a>



<a href="..\vmbuskernelmodeclientlibapi\nc-vmbuskernelmodeclientlibapi-evt_vmb_channel_restore_packet.md">EvtVmbChannelSavePacket</a>



<a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbserverchannelinitsetsaverestorepacketcallbacks.md">VmbServerChannelInitSetSaveRestorePacketCallbacks</a>