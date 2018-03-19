---
UID: NC:vmbuskernelmodeclientlibapi.EVT_VMB_CHANNEL_PNP_FAILURE
title: EVT_VMB_CHANNEL_PNP_FAILURE
author: windows-driver-content
description: The EvtChannelPnpFailure callback function is invoked if the client endpoint in the guest virtual machine asynchronously fails to connect even though a PnP device was located.
old-location: netvista\evt_vmb_channel_pnp_failure.htm
old-project: netvista
ms.assetid: 3331C043-CFB2-434C-8475-2F5F094F2460
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: EVT_VMB_CHANNEL_PNP_FAILURE, EvtChannelPnpFailure, EvtChannelPnpFailure callback function [Network Drivers Starting with Windows Vista], PFN_VMB_CHANNEL_PNP_FAILURE, PFN_VMB_CHANNEL_PNP_FAILURE callback function pointer [Network Drivers Starting with Windows Vista], netvista.evt_vmb_channel_pnp_failure, vmbuskernelmodeclientlibapi/EvtChannelPnpFailure
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
-	PFN_VMB_CHANNEL_PNP_FAILURE
product: Windows
targetos: Windows
req.typenames: VIDEO_PORT_AGP_SERVICES, *PVIDEO_PORT_AGP_SERVICES
req.product: Windows 10 or later.
---


# EVT_VMB_CHANNEL_PNP_FAILURE callback function
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

The <i>EvtChannelPnpFailure</i> callback function is invoked if the client endpoint in the
guest virtual machine asynchronously fails to connect even though a
PnP device was located.

## Syntax

```
EVT_VMB_CHANNEL_PNP_FAILURE EvtVmbChannelPnpFailure;

void EvtVmbChannelPnpFailure(
  VMBCHANNEL Channel,
  NTSTATUS FailureStatus
)
{...}
```

## Parameters

`Channel`

The channel of the client endpoint.

`FailureStatus`

A failure code.


## Return Value

This callback function does not return a value.

## Remarks

The <a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbclientchannelinitsettargetpnp.md">VmbClientChannelInitSetTargetPnp</a> function registers <i>EvtChannelPnpFailure</i> code to run in the event  of this kind of failure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | vmbuskernelmodeclientlibapi.h (include VmbusKernelModeClientLibApi.h) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbclientchannelinitsettargetpnp.md">VmbClientChannelInitSetTargetPnp</a>