---
UID: NN:wdtfinterfaces.IWDTFSimpleIOEx2
title: IWDTFSimpleIOEx2
author: windows-driver-content
description: Defines operations for a simple synchronous I/O functionality test.
old-location: dtf\iwdtfsimpleioex2.htm
old-project: dtf
ms.assetid: a916e6b1-692c-47e9-83cc-3aeae80fb624
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IWDTFSimpleIOEx2, IWDTFSimpleIOEx2 interface [Windows Device Testing Framework], IWDTFSimpleIOEx2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFSimpleIOEx2, dtf.iwdtfsimpleioex2, wdtfinterfaces/IWDTFSimpleIOEx2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtfinterfaces.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFInterfaces.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTFInterfaces.Interop.dll
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WDTFInterfaces.Interop.dll
api_name:
-	IWDTFSimpleIOEx2
product:
- Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFSimpleIOEx2 interface

Defines operations for a simple synchronous I/O functionality test.

## Methods

<p>The <b>IWDTFSimpleIOEx2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFSimpleIOEx2::Close](nf-wdtfinterfaces-iwdtfsimpleioex2-close.md) | Closes the device. |
| [IWDTFSimpleIOEx2::Open](nf-wdtfinterfaces-iwdtfsimpleioex2-open.md) | Opens the device. |
| [IWDTFSimpleIOEx2::PerformIO](nf-wdtfinterfaces-iwdtfsimpleioex2-performio.md) | Performs a small amount of simple I/O to the device. |

## Remarks
The <b>IWDTFSimpleIOEx2</b> action interface acts on an instance of the 
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439367">IWDTFTarget2</a> interface that is retrieved by querying the 
device depot. You can retrieve a target-specific implementation of an action interface by calling the 
<a href="https://msdn.microsoft.com/dddd631e-7ccf-4554-9236-b567c5108fe2">IWDTFTarget2::GetInterface</a> method with the 
desired WDTF <i>ProgID.</i>

For an asynchronous interface for this same underlying functionality, 
see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451157">IWDTFSimpleIOStressAction2</a>. 

The <b>IWDTFSimpleIOEx2</b> action interface is compatible with the following device 
classes:

<ul>
<li>
CD-ROM drives (class =CDROM) 

</li>
<li>
Display adapters (class = Display)

</li>
<li>
Multimedia devices (class = Media)

</li>
<li>
Network adapters (class = Net)

</li>
<li>
Storage volumes (class = Volume)

</li>
</ul>
For more information about device classes, see 
<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff552344">Device Setup Classes</a>.

To learn more about the specifics of how the <b>IWDTFSimpleIOEx2</b> action 
interface works, or to support additional device classes, try to implement a target-specific version 
of it for your device class. For more information about how to implement such a version, see 
<a href="https://msdn.microsoft.com/7e7660ec-1f17-4987-82c0-f62cca3a99b9">Windows Device Testing Framework 
Design Guide</a>.

<div class="alert"><b>Note</b>  The implementations of this interface are not thread-safe.</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtfinterfaces.h |