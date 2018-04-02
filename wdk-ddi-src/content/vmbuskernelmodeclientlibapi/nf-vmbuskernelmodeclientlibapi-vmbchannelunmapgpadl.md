---
UID: NF:vmbuskernelmodeclientlibapi.VmbChannelUnmapGpadl
title: VmbChannelUnmapGpadl function
author: windows-driver-content
description: The VmbChannelUnmapGpadl function unmaps a Guest Physical Address Descriptor List (GPADL) mapped using by the VmbChannelMapGpadl function. The buffer must no longer be in use by the server before this function is called.
old-location: netvista\vmbchannelunmapgpadl.htm
old-project: netvista
ms.assetid: EE300158-D7D8-4353-B205-362232A22568
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: VmbChannelUnmapGpadl, VmbChannelUnmapGpadl function [Network Drivers Starting with Windows Vista], netvista.vmbchannelunmapgpadl, vmbuskernelmodeclientlibapi/VmbChannelUnmapGpadl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: vmbuskernelmodeclientlibapi.h
req.include-header: VmbusKernelModeClientLibApi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 1.13
req.umdf-ver: 2.0
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
-	HeaderDef
api_location:
-	VmbusKernelModeClientLibApi.h
api_name:
-	VmbChannelUnmapGpadl
product: Windows
targetos: Windows
req.typenames: VIDEO_PORT_AGP_SERVICES, *PVIDEO_PORT_AGP_SERVICES
req.product: Windows 10 or later.
---


# VmbChannelUnmapGpadl function
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

The <b>VmbChannelUnmapGpadl</b> function unmaps a Guest Physical Address Descriptor List (GPADL) mapped using by the <a href="https://msdn.microsoft.com/A7801EE9-BFDB-4F77-9DA4-A6612F63AD48">VmbChannelMapGpadl</a> function. The buffer must no longer be in
use by the server before this function is called.

## Syntax

```
void VmbChannelUnmapGpadl(
  VMBCHANNEL Channel,
  UINT32     GpadlHandle
);
```

## Parameters

`Channel`

A handle for a channel.

`GpadlHandle`

The handle of the GPADL to unmap.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows Server 2012 R2 |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.13 |
| **Minimum UMDF version** | 2.0 |
| **Header** | vmbuskernelmodeclientlibapi.h (include VmbusKernelModeClientLibApi.h) |

## See Also

<a href="https://msdn.microsoft.com/A7801EE9-BFDB-4F77-9DA4-A6612F63AD48">VmbChannelMapGpadl</a>