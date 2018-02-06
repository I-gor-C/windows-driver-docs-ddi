---
UID: NS:1394._IRB_REQ_ISOCH_SET_CHANNEL_BANDWIDTH
title: "_IRB_REQ_ISOCH_SET_CHANNEL_BANDWIDTH"
author: windows-driver-content
description: This structure contains the fields necessary for the Bus driver to carry out an IsochSetChannelBandwidth request.
old-location: ieee\irb_req_isoch_set_channel_bandwidth.htm
old-project: IEEE
ms.assetid: CBEB68C2-549F-4EB6-9AF4-4DCA6749F75D
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IEEE.irb_req_isoch_set_channel_bandwidth, IRB_REQ_ISOCH_SET_CHANNEL_BANDWIDTH structure [Buses], IRB_REQ_ISOCH_SET_CHANNEL_BANDWIDTH, _IRB_REQ_ISOCH_SET_CHANNEL_BANDWIDTH, 1394/IRB_REQ_ISOCH_SET_CHANNEL_BANDWIDTH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 1394.h
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
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	1394.h
apiname:
-	IRB_REQ_ISOCH_SET_CHANNEL_BANDWIDTH
product: Windows
targetos: Windows
req.typenames: IRB_REQ_ISOCH_SET_CHANNEL_BANDWIDTH
---

# _IRB_REQ_ISOCH_SET_CHANNEL_BANDWIDTH structure
This structure contains the fields necessary for the Bus driver to carry out an <b>IsochSetChannelBandwidth</b> request.

## Syntax
````
typedef struct _IRB_REQ_ISOCH_SET_CHANNEL_BANDWIDTH {
  HANDLE hBandwidth;
  ULONG  nMaxBytesPerFrame;
  ULONG  nBandwidthUnitsRequired;
} IRB_REQ_ISOCH_SET_CHANNEL_BANDWIDTH;
````

## Members


`hBandwidth`

Bandwidth handle to reset.

`nBandwidthUnitsRequired`

Specifies a pre-calculated value.

`nMaxBytesPerFrame`

Specifies the new bandwidth for <b>hBandwidth</b>.

## Remarks
This request does not require the caller to know the bandwidth that was allocated when a handle was generated. REQUEST_ISOCH_SET_CHANNEL_BANDWIDTH can be used to readjust the bandwidth on a bandwidth handle whose bytes per frame setting is unknown. Despite its name, this request does not involve isochronous channels in any way.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | 1394.h |