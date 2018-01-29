---
UID : NF:ks.IKsReferenceClock.GetState
title : IKsReferenceClock::GetState method
author : windows-driver-content
description : The IKsReferenceClock::GetState method queries the associated reference clock for its current streaming state.
old-location : stream\iksreferenceclock_getstate.htm
old-project : stream
ms.assetid : 5a77a8bc-b477-41b3-bc4e-07c6c14291a1
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : GetState method [Streaming Media Devices], GetState, IKsReferenceClock interface [Streaming Media Devices], GetState method, IKsReferenceClock::GetState, avintfc_e2017894-2e83-4091-84b7-5ea793076b29.xml, IKsReferenceClock, GetState method [Streaming Media Devices], IKsReferenceClock interface, ks/IKsReferenceClock::GetState, stream.iksreferenceclock_getstate
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : ks.h
req.include-header : Ks.h
req.target-type : Universal
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
req.lib : ks.h
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


# GetState method
The <b>IKsReferenceClock::GetState</b> method queries the associated reference clock for its current streaming state.

## Syntax

````
NTSTATUS GetState(
  [out] PKSSTATE State
);
````

## Parameters

`State`

Points to a <a href="..\ks\ne-ks-pksstate.md">KSSTATE</a> structure that indicates the streaming state of the underlying clock.


## Return Value

The <b>IKsReferenceClock::GetState</b> method returns STATUS_SUCCESS or  the error code that the relevant clock returned from its <b>GetState</b> property. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff565093">KSPROPERTY_CLOCK_STATE</a>.  May return STATUS_DEVICE_NOT_READY if no clock is assigned.

## Remarks

For more information, see <a href="https://msdn.microsoft.com/fc1d5bca-72e3-48e2-b46f-09a13bba83b4">AVStream Clocks</a>.

AVStream uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565093">KSPROPERTY_CLOCK_STATE</a> property to retrieve the correlated time.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\ks\nf-ks-kspingetreferenceclockinterface.md">KsPinGetReferenceClockInterface</a>

<a href="..\ks\ne-ks-pksstate.md">KSSTATE</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsReferenceClock::GetState method%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>