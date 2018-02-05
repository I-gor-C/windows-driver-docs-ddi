---
UID : NF:ks.KsFilterCreatePinFactory
title : KsFilterCreatePinFactory function
author : windows-driver-content
description : The KsFilterCreatePinFactory function creates a new pin factory on the specified filter.
old-location : stream\ksfiltercreatepinfactory.htm
old-project : stream
ms.assetid : f4c8de23-dc92-41b0-82ee-2622d3942c0e
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : avfunc_845b66c4-755e-43db-afdc-db929b6bd1c6.xml, ks/KsFilterCreatePinFactory, KsFilterCreatePinFactory, stream.ksfiltercreatepinfactory, KsFilterCreatePinFactory function [Streaming Media Devices]
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
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : 
---


# KsFilterCreatePinFactory function
The<b> KsFilterCreatePinFactory</b> function creates a new pin factory on the specified filter.

## Syntax

````
NTSTATUS KsFilterCreatePinFactory(
  _In_        PKSFILTER           Filter,
  _In_  const KSPIN_DESCRIPTOR_EX *PinDescriptor,
  _Out_       PULONG              PinID
);
````

## Parameters

`Filter`

A pointer to a <a href="..\ks\ns-ks-_ksfilter.md">KSFILTER</a> structure for which to create a new pin factory.

`PinDescriptor`

A pointer to a <a href="..\ks\ns-ks-_kspin_descriptor_ex.md">KSPIN_DESCRIPTOR_EX</a> structure that describes the pins this factory will create.

`PinID`

A pointer to the location containing the ID of the new factory.


## Return Value

<b>KsFilterCreatePinFactory</b> returns the success or failure of the attempt to create the pin factory. Failure may occur due to invalid parameters or low memory.

## Remarks

Note that the filter control mutex must be held before calling this function. For more information, see <a href="https://msdn.microsoft.com/011edaaa-7449-41c3-8cfb-0d319901af8b">Mutexes in AVStream</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions. Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions. |
| **Target Platform** | Universal |
| **Header** | ks.h (include Ks.h) |
| **Library** | Ks.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\ks\nf-ks-ksfiltercreatenode.md">KsFilterCreateNode</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterCreatePinFactory function%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>