---
UID : NF:vmbuskernelmodeclientlibapi.VmbChannelPacketFail
title : VmbChannelPacketFail function
author : windows-driver-content
description : The VmbChannelPacketFail function fails a packet during packet processing due to an unrecoverable error. This function stops the queue.
old-location : netvista\vmbchannelpacketfail.htm
old-project : netvista
ms.assetid : 177B4509-A0EC-4F71-AF21-916A7A5F06DB
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : VmbChannelPacketFail
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : vmbuskernelmodeclientlibapi.h
req.include-header : VmbusKernelModeClientLibApi.h
req.target-type : Windows
req.target-min-winverclnt : Windows 8.1
req.target-min-winversvr : Windows Server 2012 R2
req.kmdf-ver : 1.13
req.umdf-ver : 2.0
req.alt-api : VmbChannelPacketFail
req.alt-loc : vmbkmcl.lib,vmbkmcl.dll
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Vmbkmcl.lib
req.dll : 
req.irql : 
req.typenames : "*PVIDEO_PORT_AGP_SERVICES, VIDEO_PORT_AGP_SERVICES"
req.product : Windows 10 or later.
---


# VmbChannelPacketFail function
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

The <b>VmbChannelPacketFail</b>  function fails a packet during packet processing due to an unrecoverable error. This function stops the queue.

## Syntax

````
VOID VmbChannelPacketFail(
  _In_ PacketCompletionContext VMBPACKETCOMPLETION
);
````

## Parameters

`PacketCompletionContext`




## Return Value

This function does not return a value.

## Remarks

Call this function for packets presented to the server endpoint which seem malformed, to
the extent that channel processing should cease.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** | 1.13 |
| **Minimum UMDF version** | 2.0 |
| **Header** | vmbuskernelmodeclientlibapi.h (include VmbusKernelModeClientLibApi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |