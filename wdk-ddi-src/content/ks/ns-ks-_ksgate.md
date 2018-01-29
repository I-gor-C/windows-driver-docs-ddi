---
UID : NS:ks._KSGATE
title : _KSGATE
author : windows-driver-content
description : The KSGATE structure describes an AVStream gate object.
old-location : stream\ksgate.htm
old-project : stream
ms.assetid : f6b5169e-2ff1-43da-a207-0c15c75e1367
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ks/KSGATE, PKSGATE structure pointer [Streaming Media Devices], _KSGATE, avstruct_b232aae6-2b0a-44f9-beaf-29fe4b7f8b86.xml, KSGATE structure [Streaming Media Devices], stream.ksgate, PKSGATE, *PKSGATE, ks/PKSGATE, KSGATE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ks.h
req.include-header : Ks.h
req.target-type : Windows
req.target-min-winverclnt : Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.
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
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : KSGATE, *PKSGATE
---

# _KSGATE structure
The KSGATE structure describes an AVStream gate object.

## Syntax
````
typedef struct _KSGATE {
  LONG    Count;
  PKSGATE NextGate;
} KSGATE, *PKSGATE;
````

## Members


## Remarks
Conceptually, flow control gates are logical AND and OR gates; in AVStream, they are used as a processing-control mechanism. For more information, see <a href="https://msdn.microsoft.com/c5592f92-a432-44e3-afe0-60fcf917a443">Flow Control Gates in AVStream</a>.

All of the manipulations of <b>Count</b> are done using interlocked functions to provide synchronous state changes. There is no distinction as to whether a given KSGATE represents an AND gate or an OR gate. Thus, clients should be careful not to transition a gate into an invalid state by using <b>KSGATE</b><i>Xxx</i><b>And</b> functions on an OR gate or <b>KSGATE</b><i>Xxx</i><b>Or</b> functions on an AND gate or by using <b>KsGateTurnInput</b><i>Xxx</i> functions invalidly.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="..\ks\nf-ks-ksgateinitializeor.md">KsGateInitializeOr</a>

<a href="..\ks\ns-ks-_ksgate.md">KSGATE</a>

<a href="..\ks\nf-ks-ksgateinitializeand.md">KsGateInitializeAnd</a>

<a href="..\ks\nf-ks-ksgateinitialize.md">KsGateInitialize</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSGATE structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>