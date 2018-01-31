---
UID : NF:ks.KsAcquireControl
title : KsAcquireControl function
author : windows-driver-content
description : The KsAcquireControl function acquires the filter control mutex for Object.
old-location : stream\ksacquirecontrol.htm
old-project : stream
ms.assetid : c316382c-8416-43c2-b5fd-2d52d01e1419
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KsAcquireControl, stream.ksacquirecontrol, ks/KsAcquireControl, avfunc_a3c1eb2c-db95-463f-98f5-a158dd1e14f5.xml, KsAcquireControl function [Streaming Media Devices]
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


# KsAcquireControl function
The <b>KsAcquireControl</b> function acquires the filter control mutex for <i>Object</i>.

## Syntax

````
void KsAcquireControl(
  _In_ PVOID Object
);
````

## Parameters

`Object`

A pointer to the object for which to acquire the filter control mutex. This should be a pointer to either a <a href="..\ks\ns-ks-_ksfilter.md">KSFILTER</a> or a <a href="..\ks\ns-ks-_kspin.md">KSPIN</a>, cast to PVOID.


## Return Value

None

## Remarks

Minidrivers typically do not call this function directly, but instead call either <a href="..\ks\nf-ks-ksfilteracquirecontrol.md">KsFilterAcquireControl</a> or <a href="..\ks\nf-ks-kspinacquirecontrol.md">KsPinAcquireControl</a>. These functions provide the necessary typecasting to PVOID automatically.

For more information, see <a href="https://msdn.microsoft.com/011edaaa-7449-41c3-8cfb-0d319901af8b">Mutexes in AVStream</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |

## See Also

<a href="..\ks\ns-ks-_kspin.md">KSPIN</a>

<a href="..\ks\nf-ks-ksreleasecontrol.md">KsReleaseControl</a>

<a href="..\ks\nf-ks-kspinacquirecontrol.md">KsPinAcquireControl</a>

<a href="..\ks\ns-ks-_ksfilter.md">KSFILTER</a>

<a href="..\ks\nf-ks-ksfilteracquirecontrol.md">KsFilterAcquireControl</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsAcquireControl function%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>