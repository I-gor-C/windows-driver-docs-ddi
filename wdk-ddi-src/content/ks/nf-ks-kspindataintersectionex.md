---
UID : NF:ks.KsPinDataIntersectionEx
title : KsPinDataIntersectionEx function
author : windows-driver-content
description : The KsPinDataIntersectionEx function handles the KSPROPERTY_PIN_DATAINTERSECTION through a callback function.
old-location : stream\kspindataintersectionex.htm
old-project : stream
ms.assetid : 4d471d91-7b2c-441d-a640-4f66ef7f1b2f
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KsPinDataIntersectionEx function [Streaming Media Devices], ksfunc_22cbace6-b96b-44d7-9c30-24580f37dd58.xml, ks/KsPinDataIntersectionEx, stream.kspindataintersectionex, KsPinDataIntersectionEx
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ks.h
req.include-header : Ks.h
req.target-type : Desktop
req.target-min-winverclnt : 
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
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : 
---


# KsPinDataIntersectionEx function
The <b>KsPinDataIntersectionEx</b> function handles the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565198">KSPROPERTY_PIN_DATAINTERSECTION</a> through a callback function.

## Syntax

````
NTSTATUS KsPinDataIntersectionEx(
  _In_           PIRP                    Irp,
  _In_           PKSP_PIN                Pin,
  _Out_          PVOID                   Data,
  _In_           ULONG                   DescriptorsCount,
  _In_     const KSPIN_DESCRIPTOR        *Descriptor,
  _In_           ULONG                   DescriptorSize,
  _In_opt_       PFNKSINTERSECTHANDLEREX IntersectHandler,
  _In_opt_       PVOID                   HandlerContext
);
````

## Parameters

`Irp`

Specifies the IRP that describes the property request.

`Pin`

Specifies the specific property that is being queried.

`Data`

Specifies the pin property-specific data.

`DescriptorsCount`

Specifies the number of descriptor structures.

`Descriptor`

Specifies the pointer to the list of pin information structures.

`DescriptorSize`

Size of the descriptor structures, in bytes.

`IntersectHandler`

Contains the optional minidriver-defined <a href="..\ks\nc-ks-pfnksintersecthandlerex.md">KStrIntersectHandlerEx</a> callback function to compare data ranges.

`HandlerContext`

Optional context that is supplied to the handler.


## Return Value

Returns STATUS_SUCCESS; otherwise, an error specific to the property that is being handled.

## Remarks

<b>KsPinDataIntersectionEx</b> is very similar to <b>KsPinDataIntersection</b>, except for some of the following slight differences:
<ul>
<li>
In <b>KsPinDataIntersectionEx</b>, the size of the descriptor is passed, a feature that allows extended descriptors.

</li>
<li>
The data intersection callback function is prototyped differently in the extended version (NTSTATUS Callback (<i>Context</i>, <i>Irp</i>, <i>Pin</i>, <i>DataRange</i>, <i>MatchingDataRange</i>, <i>DataBufferSize</i>, <i>Data</i>, <i>DataSize</i>)) versus <b>KsPinDataIntersection</b> (NTSTATUS Callback (<i>Irp</i>, <i>Pin</i>, <i>DataRange</i>, <i>Data</i>)).

</li>
<li>
The output buffer (<i>Data</i>) length is passed as a parameter to the data intersection callback function (<i>DataBufferSize</i>) rather than being extracted from the current I/O stack location.

</li>
<li>
The data intersection callback function is passed a <i>Context</i> parameter (the same <i>Context</i> parameter passed to <b>KsPinDataIntersectionEx</b>).

</li>
<li>
The size of the resultant format is passed back in <i>DataSize</i> instead of <i>Irp</i>-&gt;IoStatus.Information.

</li>
</ul>These differences excepted, <b>KsPinDataIntersection</b> and <b>KsPinDataIntersectionEx</b> operate similarly.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\ks\nc-ks-pfnksintersecthandlerex.md">KStrIntersectHandlerEx</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinDataIntersectionEx function%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>