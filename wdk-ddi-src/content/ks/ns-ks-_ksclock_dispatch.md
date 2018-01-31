---
UID : NS:ks._KSCLOCK_DISPATCH
title : "_KSCLOCK_DISPATCH"
author : windows-driver-content
description : The KSCLOCK_DISPATCH structure contains the callbacks required for a pin to implement a clock object.
old-location : stream\ksclock_dispatch.htm
old-project : stream
ms.assetid : cc9b7049-7b43-4c66-9d08-93af22d92540
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : PKSCLOCK_DISPATCH, stream.ksclock_dispatch, _KSCLOCK_DISPATCH, *PKSCLOCK_DISPATCH, KSCLOCK_DISPATCH structure [Streaming Media Devices], KSCLOCK_DISPATCH, PKSCLOCK_DISPATCH structure pointer [Streaming Media Devices], ks/KSCLOCK_DISPATCH, ks/PKSCLOCK_DISPATCH, avstruct_5015e5e6-b0c5-4eb9-9e04-8631e732f8be.xml
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
req.typenames : "*PKSCLOCK_DISPATCH, KSCLOCK_DISPATCH"
---

# _KSCLOCK_DISPATCH structure
The KSCLOCK_DISPATCH structure contains the callbacks required for a pin to implement a clock object.

## Syntax
````
typedef struct _KSCLOCK_DISPATCH {
  PFNKSPINSETTIMER       SetTimer;
  PFNKSPINCANCELTIMER    CancelTimer;
  PFNKSPINCORRELATEDTIME CorrelatedTime;
  PFNKSPINRESOLUTION     Resolution;
} KSCLOCK_DISPATCH, *PKSCLOCK_DISPATCH;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="..\ks\ns-ks-_kspin.md">KSPIN</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551882">KDPC</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff565092">KSPROPERTY_CLOCK_RESOLUTION</a>

<a href="..\ks\ns-ks-_kspin_dispatch.md">KSPIN_DISPATCH</a>

<a href="..\wdm\nf-wdm-kesettimerex.md">KeSetTimerEx</a>

<a href="..\ks\ns-ks-ksresolution.md">KSRESOLUTION</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSCLOCK_DISPATCH structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>