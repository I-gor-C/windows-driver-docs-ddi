---
UID : NN:ks.IKsReferenceClock
title : IKsReferenceClock
author : windows-driver-content
description : The IKsReferenceClock interface is a COM-style interface that is provided by AVStream on all pins. The pin passes the request onto the master clock.
old-location : stream\iksreferenceclock.htm
old-project : stream
ms.assetid : 92a84bf3-34bf-4ee7-97c0-f5e6427c0464
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _KsEdit
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : ks.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IKsReferenceClock
req.alt-loc : ks.h
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
req.typenames : 
---

# IKsReferenceClock interface

The <b>IKsReferenceClock</b> interface is a COM-style interface that is provided by AVStream on all pins. The pin passes the request onto the master clock.

## Methods

<p>The <b>IKsReferenceClock</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ks.IKsReferenceClock.GetCorrelatedPhysicalTime](nf-ks-iksreferenceclock-getcorrelatedphysicaltime.md) | The IKsReferenceClock::GetCorrelatedPhysicalTime method queries the associated reference clock for the current physical time and retrieves the correlated system time. |
| [ks.IKsReferenceClock.GetCorrelatedTime](nf-ks-iksreferenceclock-getcorrelatedtime.md) | The IKsReferenceClock::GetCorrelatedTime method queries the associated reference clock for current stream time and acquires the correlated system time. |
| [ks.IKsReferenceClock.GetPhysicalTime](nf-ks-iksreferenceclock-getphysicaltime.md) | The IKsReferenceClock::GetPhysicalTime method queries the associated reference clock for the current physical time. |
| [ks.IKsReferenceClock.GetResolution](nf-ks-iksreferenceclock-getresolution.md) | The IKsReferenceClock::GetResolution method queries the associated reference clock for its resolution. |
| [ks.IKsReferenceClock.GetState](nf-ks-iksreferenceclock-getstate.md) | The IKsReferenceClock::GetState method queries the associated reference clock for its current streaming state. |
| [ks.IKsReferenceClock.GetTime](nf-ks-iksreferenceclock-gettime.md) | The IKsReferenceClock::GetTime method queries the associated reference clock for the current time. |

## Remarks

The minidriver can acquire an <b>IKsReferenceClock</b> interface by calling <a href="..\ks\nf-ks-kspingetreferenceclockinterface.md">KsPinGetReferenceClockInterface</a>. Because this is a COM-style interface, <b>KsPinGetReferenceClockInterface</b> calls <b>QueryInterface</b>, which in turn invokes <b>AddRef</b> to increment the interface pointer. This means that when the minidriver is finished with the <b>IKsReferenceClock</b> interface, the minidriver must release it by calling <b>Release</b>.

Clients that are written in C will see the <b>IKsReferenceClock</b> interface as a structure that contains a pointer to a table of functions instead of a C++ abstract base class. A client that is written in C++ might do the following:

However, a client that is written in C would do the following instead :

For more information, see <a href="https://msdn.microsoft.com/305039fe-0a00-4f3e-ae1a-61c50a2f2fb3">AVStream Overview</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | ks.h |
| **DLL** |  |

    ## See Also

        <dl>
<dt>
<a href="..\ks\nf-ks-kspingetconnectedpininterface.md">KsPinGetConnectedPinInterface</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspingetconnectedfilterinterface.md">KsPinGetConnectedFilterInterface</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspingetreferenceclockinterface.md">KsPinGetReferenceClockInterface</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsReferenceClock interface%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>