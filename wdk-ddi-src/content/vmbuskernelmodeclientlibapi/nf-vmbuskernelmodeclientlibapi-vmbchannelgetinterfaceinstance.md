---
UID: NF.vmbuskernelmodeclientlibapi.VmbChannelGetInterfaceInstance
title: VmbChannelGetInterfaceInstance function
author: windows-driver-content
description: The VmbChannelGetInterfaceInstance function gets the active interface instance, which is a GUID that uniquely identifies a channel.
old-location: netvista\vmbchannelgetinterfaceinstance.htm
old-project: NetVista
ms.assetid: BEE9581A-5FC4-4C5B-B428-B782E59720C3
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: VmbChannelGetInterfaceInstance
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
req.alt-api: VmbChannelGetInterfaceInstance
req.alt-loc: vmbkmcl.lib,vmbkmcl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Vmbkmcl.lib
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# VmbChannelGetInterfaceInstance function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

The <b>VmbChannelGetInterfaceInstance</b> function gets the active interface instance, which is a GUID that uniquely identifies a channel.



## -syntax

````
VOID VmbChannelGetInterfaceInstance(
  _In_  VMBCHANNEL Channel,
  _Out_ LPGUID     InterfaceInstance
);
````


## -parameters

### -param Channel [in]

The channel for which to get an instance.


### -param InterfaceInstance [out]

A pointer to a GUID, which is the interface instance
of the channel.


## -returns
This function does not return a value.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 8.1

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2012 R2

</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.13

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>VmbusKernelModeClientLibApi.h (include VmbusKernelModeClientLibApi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Vmbkmcl.lib</dt>
</dl>
</td>
</tr>
</table>