---
UID : NF:ks.KsGetNodeIdFromIrp
title : KsGetNodeIdFromIrp function
author : windows-driver-content
description : The KsGetNodeIdFromIrp function returns the node ID of the node to which Irp was submitted.
old-location : stream\ksgetnodeidfromirp.htm
old-project : stream
ms.assetid : 3bb115eb-074d-4983-97e4-fa38aaa8a81b
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : avfunc_dbc2812f-8011-40e6-8847-f7c3fc35b4b5.xml, ks/KsGetNodeIdFromIrp, KsGetNodeIdFromIrp function [Streaming Media Devices], stream.ksgetnodeidfromirp, KsGetNodeIdFromIrp
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ks.h
req.include-header : Ks.h
req.target-type : Universal
req.target-min-winverclnt : Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ks.lib
req.dll : 
req.irql : Any level
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : 
---


# KsGetNodeIdFromIrp function
The<b> KsGetNodeIdFromIrp </b>function returns the node ID of the node to which <i>Irp</i> was submitted.

## Syntax

````
ULONG KsGetNodeIdFromIrp(
  _In_ PIRP Irp
);
````

## Parameters

`Irp`

A pointer to the <a href="..\wdm\ns-wdm-_irp.md">IRP</a> structure for which to determine the associated node ID. This IRP must have been sent to a file object corresponding to a filter, pin, or node.


## Return Value

<b>KsGetNodeIdFromIrp </b>returns the ID of the node to which <i>Irp </i>was submitted. If <i>Irp</i> was instead submitted directly to the filter, it returns KSFILTER_NODE.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions. Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions. |
| **Target Platform** | Universal |
| **Header** | ks.h (include Ks.h) |
| **Library** | Ks.lib |
| **IRQL** | Any level |

## See Also

<a href="..\ks\nf-ks-ksforwardirp.md">KsForwardIrp</a>

<a href="..\ks\nf-ks-ksdispatchirp.md">KsDispatchIrp</a>

<a href="..\ks\nf-ks-ksaddirptocancelablequeue.md">KsAddIrpToCancelableQueue</a>

<a href="..\wdm\ns-wdm-_irp.md">IRP</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGetNodeIdFromIrp function%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>