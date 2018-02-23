---
UID: NN:ksproxy.IKsClockPropertySet
title: IKsClockPropertySet
author: windows-driver-content
description: The IKsClockPropertySet interface provides methods that let the proxy accurately reflect time.
old-location: stream\iksclockpropertyset.htm
old-project: stream
ms.assetid: bf50d4b1-782f-4d15-b6ef-23fa13da68ff
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: stream.iksclockpropertyset, IKsClockPropertySet interface [Streaming Media Devices], IKsClockPropertySet interface [Streaming Media Devices], described, IKsClockPropertySet, ksproxy/IKsClockPropertySet, ksproxy_0be3eb82-08b7-4afc-a4e5-3815f7499ad0.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: ksproxy.h
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
req.lib: Ksproxy.lib
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	Ksproxy.lib
-	Ksproxy.dll
apiname:
-	IKsClockPropertySet
product: Windows
targetos: Windows
req.typenames: PIPE_STATE
---

# IKsClockPropertySet interface

The <b>IKsClockPropertySet</b> interface provides methods that let the proxy accurately reflect time.

## Methods

<p>The <b>IKsClockPropertySet</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ksproxy.IKsClockPropertySet.KsGetCorrelatedPhysicalTime](nf-ksproxy-iksclockpropertyset-ksgetcorrelatedphysicaltime.md) | The KsGetCorrelatedPhysicalTime method retrieves the physical time and the correlated system time from the underlying clock. |
| [ksproxy.IKsClockPropertySet.KsGetCorrelatedTime](nf-ksproxy-iksclockpropertyset-ksgetcorrelatedtime.md) | The KsGetCorrelatedTime method retrieves the current time and the correlated system time from the underlying clock. |
| [ksproxy.IKsClockPropertySet.KsGetPhysicalTime](nf-ksproxy-iksclockpropertyset-ksgetphysicaltime.md) | The KsGetPhysicalTime method retrieves the physical time from the underlying clock. |
| [ksproxy.IKsClockPropertySet.KsGetResolution](nf-ksproxy-iksclockpropertyset-ksgetresolution.md) | The KsGetResolution method retrieves the clock resolution from the underlying clock. |
| [ksproxy.IKsClockPropertySet.KsGetState](nf-ksproxy-iksclockpropertyset-ksgetstate.md) | The KsGetState method retrieves the streaming state of a pin from the underlying clock. |
| [ksproxy.IKsClockPropertySet.KsGetTime](nf-ksproxy-iksclockpropertyset-ksgettime.md) | The KsGetTime method retrieves the time of the underlying clock. |
| [ksproxy.IKsClockPropertySet.KsSetCorrelatedPhysicalTime](nf-ksproxy-iksclockpropertyset-kssetcorrelatedphysicaltime.md) | The KsSetCorrelatedPhysicalTime method sets the physical time with the correlated system time on the underlying clock. |
| [ksproxy.IKsClockPropertySet.KsSetCorrelatedTime](nf-ksproxy-iksclockpropertyset-kssetcorrelatedtime.md) | The KsSetCorrelatedTime method sets the current time with the correlated system time on the underlying clock. |
| [ksproxy.IKsClockPropertySet.KsSetPhysicalTime](nf-ksproxy-iksclockpropertyset-kssetphysicaltime.md) | The KsSetPhysicalTime method sets the physical time on the underlying clock. |
| [ksproxy.IKsClockPropertySet.KsSetTime](nf-ksproxy-iksclockpropertyset-kssettime.md) | The KsSetTime method sets the current time on the underlying clock. |

## Remarks

The IID for this interface is IID_IKsClockPropertySet.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ksproxy.h |