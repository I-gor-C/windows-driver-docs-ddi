---
UID: NF.netdma.NetDmaGetVersion
title: NetDmaGetVersion function
author: windows-driver-content
description: Note  The NetDMA interface is not supported in Windows 8 and later. The NetDmaGetVersion function returns the version of the NetDMA interface that the local computer supports.
old-location: netvista\netdmagetversion.htm
old-project: netvista
ms.assetid: eec8ba30-0f9e-4487-ba0d-99587d97b44a
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NetDmaGetVersion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: netdma.h
req.include-header: Netdma.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NetDMA 2.0 and NetDMA 1.1 drivers in Windows Server 2008.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NetDmaGetVersion
req.alt-loc: netdma.h
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
---

# NetDmaGetVersion function



## -description

## -syntax

````
UINT NetDmaGetVersion(void);
````


## -parameters


## -returns
<b>NetDmaGetVersion</b> returns a UINT value that contains the major and minor version numbers as
     follows:
<dl>
<dt><b>High 16 bits</b></dt>
</dl>The major version number of the NetDMA interface.
<dl>
<dt><b>Low 16 bits</b></dt>
</dl>The minor version of NetDMA interface.

 

<b>NetDmaGetVersion</b> returns a UINT value that contains the major and minor version numbers as
     follows:
<dl>
<dt><b>High 16 bits</b></dt>
</dl>The major version number of the NetDMA interface.
<dl>
<dt><b>Low 16 bits</b></dt>
</dl>The minor version of NetDMA interface.

 

<b>NetDmaGetVersion</b> returns a UINT value that contains the major and minor version numbers as
     follows:
<dl>
<dt><b>High 16 bits</b></dt>
</dl>The major version number of the NetDMA interface.
<dl>
<dt><b>Low 16 bits</b></dt>
</dl>The minor version of NetDMA interface.

 

## -remarks
NetDMA provider drivers can call the 
    <b>NetDmaGetVersion</b> function to obtain the version of the NetDMA interface. A NetDMA provider must
    register as a NetDMA provider with a version equal to or lower than the NetDMA provider interface version
    that the local computer supports. The NetDMA provider driver specifies the major and minor version of the
    NetDMA provider in the 
    <b>MajorVersion</b> and 
    <b>MinorVersion</b> members of the 
    <a href="netvista.net_dma_provider_characteristics">
    NET_DMA_PROVIDER_CHARACTERISTICS</a> structure that it passes to the 
    <a href="netvista.netdmaregisterprovider">
    NetDmaRegisterProvider</a> function.

NetDMA provider drivers call 
    <b>NetDmaGetVersion</b> at IRQL = PASSIVE_LEVEL.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Supported for NetDMA 2.0 and NetDMA 1.1 drivers in Windows Server 2008.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Netdma.h (include Netdma.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndisgetroutineaddress">NdisGetRoutineAddress</a>
</dt>
<dt>
<a href="netvista.net_dma_provider_characteristics">
   NET_DMA_PROVIDER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="netvista.netdmaregisterprovider">NetDmaRegisterProvider</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NetDmaGetVersion function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>