---
UID: NF:sdplib.SdpCreateNodeSequence
title: SdpCreateNodeSequence function
author: windows-driver-content
description: The Bluetooth SdpCreateNodeSequence function is used to create an empty sequence SDP node.
old-location: bltooth\sdpcreatenodesequence.htm
old-project: bltooth
ms.assetid: 9e02f32b-cd39-4953-9698-a1800bedf0e2
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: SdpCreateNodeSequence, SdpCreateNodeSequence function [Bluetooth Devices], bltooth.sdpcreatenodesequence, bth_funcs_646168a7-522f-425c-99b7-706b84e02e20.xml, sdplib/SdpCreateNodeSequence
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: sdplib.h
req.include-header: BthSdpddi.h
req.target-type: Desktop
req.target-min-winverclnt: Versions:\_Supported in Windows Vista, and later.
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
req.irql: "<= PASSIVE_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	sdplib.h
api_name:
-	SdpCreateNodeSequence
product: Windows
targetos: Windows
req.typenames: SDCMD_DESCRIPTOR, *PSDCMD_DESCRIPTOR
req.product: Windows 10 or later.
---


# SdpCreateNodeSequence function
The Bluetooth 
  <b>SdpCreateNodeSequence</b> function is used to create an empty sequence SDP node.

## Syntax

````
PSDP_NODE SdpCreateNodeSequence(
  _In_ ULONG tag
);
````

## Parameters

`tag`

A profile driver defined tag to associate with the node.


## Return Value

If successful, this function returns a pointer to the newly allocated 
     <a href="..\sdpnode\ns-sdpnode-_sdp_node.md">SDP_NODE</a> structure. If not successful, this
     function returns <b>NULL</b>.

## Remarks

After a sequence node is created by calling the 
    <b>SdpCreateNodeSequence</b> function, Bluetooth drivers can call the 
    <a href="..\sdplib\nf-sdplib-sdpappendnodetocontainernode.md">
    SdpAppendNodeToContainerNode</a> function to insert other nodes into the sequence node or to add the
    new sequence node to another sequence node.

A sequence node can be added as a top-level attribute of an SDP record by calling the 
    <a href="..\sdplib\nf-sdplib-sdpaddattributetotree.md">SdpAddAttributeToTree</a> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Versions:\_Supported in Windows Vista, and later.  |
| **Target Platform** | Desktop |
| **Header** | sdplib.h (include BthSdpddi.h) |
| **IRQL** | "<= PASSIVE_LEVEL" |

## See Also

<a href="..\sdpnode\ns-sdpnode-_sdp_node.md">SDP_NODE</a>



<a href="..\sdplib\nf-sdplib-sdpappendnodetocontainernode.md">SdpAppendNodeToContainerNode</a>



<a href="..\sdplib\nf-sdplib-sdpaddattributetotree.md">SdpAddAttributeToTree</a>