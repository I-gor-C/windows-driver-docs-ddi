---
UID : NF:vmbuskernelmodeclientlibapi.VmbChannelEnable
title : VmbChannelEnable function
author : windows-driver-content
description : The VmbChannelEnable function enables a channel that is in the disabled state by connecting to VMBus and offering or opening a channel, as appropriate for the endpoint type.
old-location : netvista\vmbchannelenable.htm
old-project : netvista
ms.assetid : A0256B3F-C35C-45AB-A825-0A82189F08DC
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : VmbChannelEnable
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
req.alt-api : VmbChannelEnable
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


# VmbChannelEnable function
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

The <b>VmbChannelEnable</b> function enables a channel that is in the disabled state by connecting to VMBus and
offering or opening a channel, as  appropriate for the endpoint type.

## Syntax

````
NTSTATUS
 VmbChannelEnable(
  _In_ VMBCHANNEL Channel
);
````

## Parameters

`Channel`

The handle of a channel to enable.


## Return Value

None


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